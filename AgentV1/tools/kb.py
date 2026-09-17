"""Retrieval CLI for the DB2ADMIN knowledge base.

Installed to kb/tools/kb.py by the build.  Self-contained: needs only the
standard library and kb.sqlite sitting two directories up.

    python kb/tools/kb.py search "sales order delivery"
    python kb/tools/kb.py find-column COMPANYCODE
    python kb/tools/kb.py describe SALESORDER
    python kb/tools/kb.py neighbors SALESORDER
    python kb/tools/kb.py join-path SALESORDER CURRENCY
    python kb/tools/kb.py join-sql SALESORDER SALESORDERLINE CURRENCY
    python kb/tools/kb.py sql "SELECT ..."
"""

from __future__ import annotations

import argparse
import heapq
import json
import re
import sqlite3
import sys
from pathlib import Path

KB_DIR = Path(__file__).resolve().parent.parent
DB_PATH = KB_DIR / "kb.sqlite"
SCHEMA = "DB2ADMIN"

# Descending parent -> child changes the grain of the result and multiplies
# rows, so when two routes reach the target, prefer the one that ascends to a
# shared parent. Must match classify.GRAIN_CHANGE_COST in the build.
GRAIN_CHANGE_COST = 4

# Above this cost a waypoint is a generic reference table rather than a real
# relationship; hub_penalty is precomputed per table by the build.
HUB_BLOCK_COST = 10


def connect() -> sqlite3.Connection:
    if not DB_PATH.exists():
        sys.exit(f"kb.sqlite not found at {DB_PATH}; run kb_build/build_kb.py first")
    db = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    return db




# --------------------------------------------------------------- commands

def cmd_search(db, args):
    query = " ".join(args.query) if isinstance(args.query, list) else args.query
    terms = [t for t in re.split(r"\W+", query) if t]
    if not terms:
        sys.exit("empty query")
    filt = "" if args.all else "AND queryable = 1"
    squashed = "".join(t.upper() for t in terms)

    # Table names in this schema are unspaced concatenations (PURCHASEORDERLINE),
    # so a name-substring pass finds the intended table far more reliably than
    # full-text scoring, which is diluted by the 122k column names. Rank:
    #   1. name contains the whole query with separators removed
    #   2. name contains every term
    #   3. FTS over names + column names
    seen: dict[str, sqlite3.Row] = {}
    cols = "name, module, n_columns, n_inbound_fk, primary_key, queryable, roles"

    def take(rows):
        for r in rows:
            if r["name"] not in seen and len(seen) < args.limit:
                seen[r["name"]] = r

    take(db.execute(
        f"SELECT {cols} FROM tables WHERE name LIKE ? {filt} ORDER BY length(name), name",
        (f"%{squashed}%",),
    ))
    if len(seen) < args.limit:
        where = " AND ".join(["name LIKE ?"] * len(terms))
        take(db.execute(
            f"SELECT {cols} FROM tables WHERE {where} {filt} ORDER BY length(name), name",
            [f"%{t.upper()}%" for t in terms],
        ))
    if len(seen) < args.limit:
        # weight the name column above module/roles/notes/column_names
        try:
            take(db.execute(
                f"""SELECT {', '.join('t.' + c for c in cols.split(', '))}
                    FROM tables_fts JOIN tables t ON t.name = tables_fts.name
                    WHERE tables_fts MATCH ?
                      {filt.replace('queryable', 't.queryable')}
                    ORDER BY bm25(tables_fts, 20.0, 1.0, 1.0, 1.0, 0.3) LIMIT ?""",
                (" AND ".join(f'"{t}"*' for t in terms), args.limit),
            ))
        except sqlite3.OperationalError:
            pass
    if len(seen) < args.limit:
        try:
            take(db.execute(
                f"""SELECT {', '.join('t.' + c for c in cols.split(', '))}
                    FROM tables_fts JOIN tables t ON t.name = tables_fts.name
                    WHERE tables_fts MATCH ?
                      {filt.replace('queryable', 't.queryable')}
                    ORDER BY bm25(tables_fts, 20.0, 1.0, 1.0, 1.0, 0.3) LIMIT ?""",
                (" OR ".join(f'"{t}"*' for t in terms), args.limit),
            ))
        except sqlite3.OperationalError:
            pass

    rows = list(seen.values())
    if not rows:
        print("no matches")
        return

    print(f"{'TABLE':<44} {'MODULE':<16} {'COLS':>5} {'IN-FK':>6}  PRIMARY KEY")
    print("-" * 118)
    for r in rows:
        flag = "" if r["queryable"] else "  [NOT QUERYABLE]"
        print(
            f"{r['name']:<44} {r['module']:<16} {r['n_columns']:>5} {r['n_inbound_fk']:>6}  "
            f"{r['primary_key'] or '—'}{flag}"
        )
    print(f"\n{len(rows)} match(es). Next: describe <TABLE>")


def cmd_find_column(db, args):
    col = args.column.upper()
    rows = db.execute(
        """SELECT c.table_name, c.sql_type, c.in_primary_key, c.is_foreign_key,
                  c.meaning, t.module, t.queryable
           FROM columns c JOIN tables t ON t.name = c.table_name
           WHERE c.name = ? ORDER BY t.queryable DESC, c.in_primary_key DESC, c.table_name""",
        (col,),
    ).fetchall()
    if not rows:
        like = db.execute(
            "SELECT DISTINCT name FROM columns WHERE name LIKE ? LIMIT 25",
            (f"%{col}%",),
        ).fetchall()
        if like:
            print(f"no column named exactly {col}. Similar names:")
            for r in like:
                print("  ", r["name"])
        else:
            print(f"no column matching {col}")
        return
    if rows[0]["meaning"]:
        print(f"{col}: {rows[0]['meaning']}\n")
    print(f"{col} appears on {len(rows)} table(s)")
    print(f"\n{'TABLE':<44} {'MODULE':<16} {'TYPE':<16} KEY")
    print("-" * 100)
    shown = rows if args.all else rows[: args.limit]
    for r in shown:
        key = ("PK " if r["in_primary_key"] else "") + ("FK" if r["is_foreign_key"] else "")
        flag = "" if r["queryable"] else "  [NOT QUERYABLE]"
        print(f"{r['table_name']:<44} {r['module']:<16} {r['sql_type']:<16} {key}{flag}")
    if len(rows) > len(shown):
        print(f"... {len(rows) - len(shown)} more (use --all)")


def cmd_describe(db, args):
    name = args.table.upper()
    t = db.execute("SELECT * FROM tables WHERE name = ?", (name,)).fetchone()
    if not t:
        alt = db.execute(
            "SELECT name FROM tables WHERE name LIKE ? LIMIT 10", (f"%{name}%",)
        ).fetchall()
        print(f"no table named {name}." + (" Did you mean:" if alt else ""))
        for a in alt:
            print("  ", a["name"])
        return

    card = KB_DIR / "tables" / t["module"] / f"{name}.md"
    if card.exists() and not args.terse:
        print(card.read_text(encoding="utf-8"))
        return

    print(f"# {SCHEMA}.{name}")
    print(f"module={t['module']} roles={t['roles']} queryable={bool(t['queryable'])}")
    if not t["queryable"]:
        print(f"!! DO NOT QUERY FOR BUSINESS DATA: {t['notes']}")
    print(f"primary key: {t['primary_key'] or '(none)'}")
    print(f"{t['n_columns']} columns, referenced by {t['n_inbound_fk']}, references {t['n_outbound_fk']}\n")
    for c in db.execute(
        "SELECT * FROM columns WHERE table_name = ? ORDER BY position", (name,)
    ):
        key = ("PK" if c["in_primary_key"] else "  ") + ("FK" if c["is_foreign_key"] else "  ")
        nn = "NOT NULL" if not c["nullable"] else ""
        print(f"  {key} {c['name']:<36} {c['sql_type']:<16} {nn:<9} {c['tags'] or ''}")


def cmd_neighbors(db, args):
    name = args.table.upper()
    if not db.execute("SELECT 1 FROM tables WHERE name = ?", (name,)).fetchone():
        sys.exit(f"unknown table {name}")
    rows = db.execute(
        """SELECT j.b, j.direction, j.cardinality, j.on_clause, t.module, t.queryable, t.n_inbound_fk
           FROM join_edges j JOIN tables t ON t.name = j.b
           WHERE j.a = ? ORDER BY j.direction, j.b""",
        (name,),
    ).fetchall()
    parents = [r for r in rows if r["direction"] == "to_parent"]
    children = [r for r in rows if r["direction"] == "to_child"]

    print(f"# {name}: {len(parents)} parent(s), {len(children)} child(ren)\n")
    print("## Parents (many-to-one; safe, does not fan out rows)")
    for r in parents:
        print(f"  -> {r['b']:<42} {r['on_clause']}")
    print("\n## Children (one-to-many; FANS OUT rows — aggregate or expect duplicates)")
    for r in children[: args.limit]:
        print(f"  <- {r['b']:<42} {r['on_clause']}")
    if len(children) > args.limit:
        print(f"  ... {len(children) - args.limit} more (use --limit)")

    impl = db.execute(
        """SELECT * FROM implicit_links
           WHERE child_table = ? OR parent_table = ?""", (name, name)
    ).fetchall()
    if impl:
        print("\n## Implicit links (inferred, not declared in the DDL)")
        for r in impl:
            if r["parent_table"] is None:
                print(f"  ?? {r['child_table']}.FATHERID -> parent NOT DERIVABLE ({r['basis']})")
            else:
                print(f"  ~~ {r['on_clause']}   [{r['confidence']} confidence]")


def _graph(db):
    adj: dict[str, list[tuple[str, sqlite3.Row]]] = {}
    for r in db.execute("SELECT a, b, fk_id, direction, cardinality, on_clause FROM join_edges"):
        adj.setdefault(r["a"], []).append((r["b"], r))
    pen = {
        r["name"]: r["hub_penalty"]
        for r in db.execute("SELECT name, hub_penalty FROM tables")
    }
    return adj, pen


def _shortest(db, src, dst, allow_hubs: bool, max_hops: int = 3):
    adj, pen = _graph(db)
    # Dijkstra: cost of entering a node = 1 + hub penalty of that node,
    # so a path that detours through COMPANY loses to any genuine route.
    # The counter is a tiebreaker -- without it heapq falls through to comparing
    # the payload, and sqlite3.Row is not orderable.
    seen: set[str] = set()
    counter = 0
    pq = [(0, counter, [src], [])]
    while pq:
        cost, _, path, via = heapq.heappop(pq)
        node = path[-1]
        if node == dst:
            return cost, path, via
        if node in seen:
            continue
        seen.add(node)
        # Beyond a few hops an FK chain stops expressing a business
        # relationship: any two tables in a schema this connected can be linked
        # eventually, via waypoints that mean nothing together.
        if len(path) > max_hops:
            continue
        for nxt, edge in adj.get(node, []):
            if nxt in seen:
                continue
            p = pen.get(nxt, 0)
            # The destination itself may be a hub -- the caller asked for it.
            # Only *passing through* one is suppressed.
            if not allow_hubs and p >= HUB_BLOCK_COST and nxt != dst:
                continue
            step = 1 + p
            if edge["cardinality"] == "one_to_many":
                step += GRAIN_CHANGE_COST
            counter += 1
            heapq.heappush(pq, (cost + step, counter, path + [nxt], via + [edge]))
    return None, None, None


def cmd_join_path(db, args):
    a, b = args.a.upper(), args.b.upper()
    for t in (a, b):
        if not db.execute("SELECT 1 FROM tables WHERE name = ?", (t,)).fetchone():
            sys.exit(f"unknown table {t}")

    cost, path, via = _shortest(db, a, b, allow_hubs=args.allow_hubs, max_hops=args.max_hops)
    if path is None:
        _, path2, _ = _shortest(db, a, b, allow_hubs=True, max_hops=args.max_hops)
        _, path3, _ = _shortest(db, a, b, allow_hubs=True, max_hops=12)
        print(f"No join path between {a} and {b} within {args.max_hops} hop(s).\n")
        if path2:
            print(
                f"A route exists but passes through a generic reference table:\n"
                f"  {' -> '.join(path2)}\n"
                f"Re-run with --allow-hubs if that is genuinely what you want."
            )
        elif path3:
            print(
                f"The shortest route is {len(path3) - 1} hops:\n"
                f"  {' -> '.join(path3)}\n"
                f"A chain this long does not express a business relationship. These two\n"
                f"tables are almost certainly unrelated -- do NOT join them. Re-run with\n"
                f"--max-hops {len(path3) - 1} only if you have independent reason to believe\n"
                f"the connection is real."
            )
        else:
            print(f"There is no foreign-key route between them at all.")
        print(
            "\nIf the question really does span both tables, they are probably linked\n"
            "through application logic rather than the schema. Ask the user."
        )
        print(_implicit_hint(db, a, b))
        return

    mods = [
        db.execute("SELECT module FROM tables WHERE name = ?", (n,)).fetchone()["module"]
        for n in path
    ]
    print(f"# {a} -> {b}   ({len(path) - 1} hop(s))\n")
    print(" -> ".join(f"{n} [{m}]" for n, m in zip(path, mods)) + "\n")
    print("```sql")
    print(f"SELECT *")
    print(f"FROM   {SCHEMA}.{path[0]} {path[0]}")
    for i, edge in enumerate(via):
        nxt = path[i + 1]
        fan = "  -- one-to-many: fans out rows" if edge["cardinality"] == "one_to_many" else ""
        print(f"JOIN   {SCHEMA}.{nxt} {nxt}")
        print(f"       ON {edge['on_clause']}{fan}")
    print("```")
    if any(e["cardinality"] == "one_to_many" for e in via):
        print("\n! This path traverses a one-to-many edge: parent columns will be duplicated.")
        print("  Aggregate the child side or use EXISTS instead of a join.")
    _role_alternatives(db, via, path)
    distinct = [m for i, m in enumerate(mods) if i == 0 or m != mods[i - 1]]
    if len(set(distinct)) > 2:
        print(
            f"\n! The path crosses {len(set(distinct))} modules "
            f"({' -> '.join(distinct)}).\n"
            f"  Verify this relationship is real before using it; a path that wanders\n"
            f"  across unrelated domains is usually an artefact of shared reference data."
        )
    print(_implicit_hint(db, a, b))


def _role_alternatives(db, via, path) -> None:
    """Warn where a hop had several role-qualified FKs to choose between.

    Over a third of this schema's foreign keys sit on table pairs joined by more
    than one constraint (three carrier roles, three address roles, ...). Picking
    one by shortest path is a coin flip, and the wrong role yields SQL that runs
    and answers the wrong question -- so the choice has to be handed back.
    """
    warned = False
    for i, edge in enumerate(via):
        a, b = path[i], path[i + 1]
        child, parent = (a, b) if edge["direction"] == "to_parent" else (b, a)
        alts = db.execute(
            """SELECT constraint_name, child_columns, on_clause FROM foreign_keys
               WHERE child = ? AND parent = ? ORDER BY constraint_name""",
            (child, parent),
        ).fetchall()
        if len(alts) < 2:
            continue
        if not warned:
            print(
                "\n! AMBIGUOUS JOIN: this table pair is connected by several "
                "role-qualified\n  foreign keys. The predicate above is only one of them. "
                "Pick the role the\n  question actually means -- the constraint name says which:"
            )
            warned = True
        print(f"\n  {child} -> {parent}:")
        for r in alts:
            mark = "  <-- used above" if r["on_clause"] == edge["on_clause"] else ""
            print(f"    {r['constraint_name']:<44} ({r['child_columns']}){mark}")


def _implicit_hint(db, *tables) -> str:
    out = []
    for t in tables:
        r = db.execute(
            "SELECT * FROM implicit_links WHERE child_table = ?", (t,)
        ).fetchone()
        if r:
            if r["parent_table"]:
                out.append(f"  {t}.FATHERID -> {r['parent_table']}.ABSUNIQUEID [{r['confidence']}]")
            else:
                out.append(f"  {t}.FATHERID -> parent not derivable from the schema")
    if out:
        return "\nImplicit (non-FK) parent links involving these tables:\n" + "\n".join(out)
    return ""


def cmd_join_sql(db, args):
    names = [t.upper() for t in args.tables]
    for t in names:
        if not db.execute("SELECT 1 FROM tables WHERE name = ?", (t,)).fetchone():
            sys.exit(f"unknown table {t}")
    root, rest = names[0], names[1:]
    lines = [f"FROM   {SCHEMA}.{root} {root}"]
    joined = {root}
    unreachable = []
    hops: list[tuple[list, list]] = []
    for target in rest:
        best = None
        for anchor in list(joined):
            cost, path, via = _shortest(
                db, anchor, target, allow_hubs=args.allow_hubs, max_hops=args.max_hops
            )
            if path and (best is None or cost < best[0]):
                best = (cost, path, via)
        if best is None:
            unreachable.append(target)
            continue
        _, path, via = best
        hops.append((via, path))
        for i, edge in enumerate(via):
            nxt = path[i + 1]
            if nxt in joined:
                continue
            fan = "  -- fans out" if edge["cardinality"] == "one_to_many" else ""
            lines.append(f"JOIN   {SCHEMA}.{nxt} {nxt}")
            lines.append(f"       ON {edge['on_clause']}{fan}")
            joined.add(nxt)

    cc = {
        r["table_name"]
        for r in db.execute(
            "SELECT DISTINCT table_name FROM columns WHERE name='COMPANYCODE' AND table_name IN ({})".format(
                ",".join("?" * len(joined))
            ),
            tuple(joined),
        )
    }
    # anchor the tenant filter on a table the caller actually asked for
    cc = [n for n in names if n in cc] + sorted(cc - set(names))
    print("```sql")
    print("SELECT *")
    print("\n".join(lines))
    if cc:
        print(f"WHERE  {cc[0]}.COMPANYCODE = ?   -- tenant key: always constrain")
    print("FETCH FIRST 100 ROWS ONLY;")
    print("```")
    for via, path in hops:
        _role_alternatives(db, via, path)
    extra = sorted(joined - set(names))
    if extra:
        print(f"\nBridge tables added to connect the requested set: {', '.join(extra)}")
    if unreachable:
        print(f"\n! No hub-free FK path to: {', '.join(unreachable)}")
        print("  These are not directly related to the others. Do not invent a join.")
    if len(cc) > 1:
        print(f"\n! {len(cc)} joined tables carry COMPANYCODE. Verify the composite FK")
        print("  predicates already equate them; if not, add the equality explicitly.")


def cmd_sql(db, args):
    try:
        rows = db.execute(args.query).fetchall()
    except sqlite3.Error as e:
        sys.exit(f"error: {e}")
    if not rows:
        print("(no rows)")
        return
    cols = rows[0].keys()
    print(" | ".join(cols))
    print("-+-".join("-" * len(c) for c in cols))
    for r in rows[: args.limit]:
        print(" | ".join("" if r[c] is None else str(r[c]) for c in cols))
    if len(rows) > args.limit:
        print(f"... {len(rows) - args.limit} more rows")


def cmd_stats(db, args):
    meta = {r["key"]: json.loads(r["value"]) for r in db.execute("SELECT * FROM meta")}
    print(json.dumps(meta, indent=2))


# --------------------------------------------------------------- entry

def main() -> None:
    p = argparse.ArgumentParser(
        prog="kb.py", description="Retrieval CLI for the DB2ADMIN knowledge base"
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="full-text search over table and column names")
    s.add_argument("query", nargs="+", help="search terms; quoting is optional")
    s.add_argument("--limit", type=int, default=20)
    s.add_argument("--all", action="store_true", help="include non-queryable tables")
    s.set_defaults(fn=cmd_search)

    s = sub.add_parser("find-column", help="which tables contain a column")
    s.add_argument("column")
    s.add_argument("--limit", type=int, default=30)
    s.add_argument("--all", action="store_true")
    s.set_defaults(fn=cmd_find_column)

    s = sub.add_parser("describe", help="full card for one table")
    s.add_argument("table")
    s.add_argument("--terse", action="store_true", help="compact output instead of the card")
    s.set_defaults(fn=cmd_describe)

    s = sub.add_parser("neighbors", help="everything joinable in one hop")
    s.add_argument("table")
    s.add_argument("--limit", type=int, default=40)
    s.set_defaults(fn=cmd_neighbors)

    s = sub.add_parser("join-path", help="shortest meaningful join path between two tables")
    s.add_argument("a")
    s.add_argument("b")
    s.add_argument("--allow-hubs", action="store_true", help="permit routing through reference hubs")
    s.add_argument("--max-hops", type=int, default=3,
                   help="reject paths longer than this (default 3)")
    s.set_defaults(fn=cmd_join_path)

    s = sub.add_parser("join-sql", help="build a FROM/JOIN clause spanning several tables")
    s.add_argument("tables", nargs="+")
    s.add_argument("--allow-hubs", action="store_true")
    s.add_argument("--max-hops", type=int, default=3)
    s.set_defaults(fn=cmd_join_sql)

    s = sub.add_parser("sql", help="run read-only SQL against kb.sqlite")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=50)
    s.set_defaults(fn=cmd_sql)

    s = sub.add_parser("stats", help="schema summary and provenance")
    s.set_defaults(fn=cmd_stats)

    args = p.parse_args()
    with connect() as db:
        args.fn(db, args)


if __name__ == "__main__":
    main()
