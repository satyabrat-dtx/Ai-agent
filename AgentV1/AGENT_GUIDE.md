# DB2ADMIN query knowledge base — agent guide

Read this file first. It is the contract for generating correct SQL against the
`DB2ADMIN` schema of database **NOW7** (IBM Db2 12.1).

The schema has **3,762 tables**, **122,450 columns** and
**11,001 foreign keys**. Do not attempt to load it all. Retrieve the
few tables a question needs, then generate SQL.

---

## 1. Retrieval protocol

Work in this order. Stop as soon as you have the tables you need.

1. **Find candidate tables** — full-text search over table and column names:
   ```bash
   python kb/tools/kb.py search "sales order delivery"
   python kb/tools/kb.py find-column CUSTOMERSUPPLIERCODE
   ```
2. **Read the table card** for each candidate — the authoritative per-table
   reference (columns, keys, every inbound and outbound FK with a ready-made
   JOIN predicate):
   ```bash
   python kb/tools/kb.py describe SALESORDER
   # or read kb/tables/<MODULE>/<TABLE>.md directly
   ```
3. **Resolve the joins** — never invent a join condition:
   ```bash
   python kb/tools/kb.py join-path SALESORDER LOGICALWAREHOUSE
   ```
4. **Generate SQL** using the emitted predicates verbatim, then apply the rules
   in §3 and the traps in §4.

`kb/kb.sqlite` carries the same content for direct SQL access, including the
`tables_fts` / `columns_fts` full-text indexes. Its shape is documented in
[`SQLITE_SCHEMA.md`](SQLITE_SCHEMA.md).

---

## 2. What is and is not authoritative

| Layer | Source | Trust |
|---|---|---|
| Tables, columns, types, nullability | declared in DDL | **authoritative** |
| Primary keys, unique, check constraints | declared in DDL | **authoritative** |
| Foreign keys and their JOIN predicates | declared in DDL | **authoritative** |
| Indexes | declared in DDL | **authoritative** |
| `FATHERID` parent links | **inferred from naming** | check `confidence` |
| Module grouping | **inferred from name prefixes** | navigational hint only |
| Table roles (`staging_mirror`, `hub`, …) | **inferred from structure** | reliable, rule-based |
| Column meanings in the glossary | **inferred from naming** | hint only |

**The source DDL contains zero `COMMENT ON` statements** — there are no
database-authored descriptions of any table or column. Every business meaning
in this KB was derived from naming conventions and FK structure. Never present
an inferred label to a user as the system's official terminology.

---

## 3. SQL generation rules

1. **Always schema-qualify**: `DB2ADMIN.TABLENAME`.
2. **Always constrain `COMPANYCODE`** when the table has it (1934
   tables do). It is the company/legal-entity discriminator and the leading PK
   column on most tables. Omitting it silently mixes legal entities.
3. **Carry `COMPANYCODE` into the join**, not just the `WHERE` clause. The
   generated predicates already do this wherever the FK is composite — use them
   as given.
4. **Composite keys are the norm.** Most joins need 2–4 column pairs. Never join
   on a single column because it "looks like" the key.
5. **Prefer `*DATETIMEUTC` over `*DATETIME`** for time comparisons and ranges;
   the non-UTC twin is local to the company.
6. **Use `FETCH FIRST n ROWS ONLY`**, not `LIMIT` — this is Db2.
7. **`CHAR` columns are blank-padded.** Compare with `TRIM(col) = 'X'` or a
   correctly padded literal; `RTRIM` before concatenating.
8. Db2 has no `TOP`, no `IIF`, no `ISNULL` — use `FETCH FIRST`, `CASE`, `COALESCE`.
9. **Never emit DDL or DML.** This KB describes a read model; generate `SELECT`
   only unless the user explicitly asked otherwise.

---

## 4. Traps — the things that silently produce wrong answers

### 4.1 `*BEAN` tables are staging mirrors, not data
319 tables are integration staging mirrors. They are
identified by a `BEAN` suffix and/or an `IMPORTAUTOCOUNTER` column, and 262 of
them shadow a real table with the same name minus `BEAN`:

```
DB2ADMIN.USAOPENBALANCE       <- authoritative, NOT NULL key columns
DB2ADMIN.USAOPENBALANCEBEAN   <- inbound staging rows, keys nullable
```

They hold in-flight inbound rows with relaxed constraints. **Querying one for
business reporting gives incomplete and unvalidated data.** Every card for these
tables opens with a `DO NOT QUERY` banner, and `tables.queryable = 0` in SQLite.
Strip the `BEAN` suffix and use the twin.

### 4.2 `ACT_*` tables belong to the process engine
79 tables are Activiti/Flowable BPM engine internals
(runtime, history, identity). They are not application business data and their
schema is owned by the engine, not this application.

### 4.3 `FATHERID` is a real relationship that no foreign key declares
541 tables have a `FATHERID` column that points at the
parent row's `ABSUNIQUEID`. **Zero foreign keys in this schema reference
`ABSUNIQUEID`**, so a pure FK join graph is blind to every one of these
header→detail relationships.

```sql
-- the shape of a FATHERID join
SELECT c.*
FROM   DB2ADMIN.<PARENT> p
JOIN   DB2ADMIN.<CHILD>  c ON c.FATHERID = p.ABSUNIQUEID
```

`graph/implicit_links.json` records each one with a confidence level. For
357 of them the parent is **not derivable from the schema** — the link is
polymorphic and resolved by the application. For those, ask the user or infer the
parent from the question; do not guess silently.

### 4.4 Do not route joins through reference hubs
`COMPANY` is referenced by 1244 constraints. A shortest-path
search over raw FK edges will happily connect two unrelated tables through it:

```
SALESORDER -> COMPANY -> SOMEUNRELATEDTABLE     -- structurally valid, semantically meaningless
```

`join-path` penalises hub traversal by default. If the only available path runs
through a hub, the tool says so — treat that as "these tables are not directly
related" rather than emitting the join.

Top hubs:

| Table | Inbound FKs | Module |
|---|---|---|
| `COMPANY` | 1244 | CORE_MASTER |
| `UNITOFMEASURE` | 804 | CORE_MASTER |
| `ITEMTYPE` | 414 | CORE_MASTER |
| `USERGENERICGROUP` | 343 | CORE_MASTER |
| `DIVISION` | 336 | CORE_MASTER |
| `ICSENTITY` | 322 | CORE_MASTER |
| `ORDERPARTNER` | 286 | CORE_MASTER |
| `CURRENCY` | 276 | CORE_MASTER |
| `GLMASTER` | 211 | CORE_MASTER |
| `COUNTER` | 192 | CORE_MASTER |
| `LOGICALWAREHOUSE` | 188 | WAREHOUSE |
| `PLANT` | 160 | CORE_MASTER |
| `EMPLOYEE` | 153 | HR |
| `CUSTOMERSUPPLIERDATA` | 133 | CORE_MASTER |
| `USERGENERICGROUPTYPE` | 129 | CORE_MASTER |
| `STANDARDORDERGROUP` | 125 | CORE_MASTER |
| `COUNTRY` | 113 | CORE_MASTER |
| `STOCKTRANSACTIONTEMPLATE` | 100 | INVENTORY |
| `LOGREASON` | 97 | LOGISTICS |
| `AGENT` | 91 | CORE_MASTER |
| `COSTCENTER` | 90 | COSTING |
| `DIVISIONVSFACTORYVSDEPARTMENT` | 80 | CORE_MASTER |
| `RULES` | 77 | CORE_MASTER |
| `STATISTICALGROUP` | 76 | CORE_MASTER |
| `PAYMENTMETHOD` | 75 | CORE_MASTER |

### 4.5 The same two tables are often joinable several different ways
1,157 table pairs are connected by more than one foreign key
(4,064 FKs — 36% of all of
them). These are *role-qualified* references, and the constraint name carries the
role:

```
SALESORDER -> CUSTOMERSUPPLIERDATA
  CUSTOMERSUPPLIERDATA_FIRSTCARRIER    (COMPANYCODE, FIRSTCARRIERTYPE,  FIRSTCARRIERCODE)
  CUSTOMERSUPPLIERDATA_SECONDCARRIER   (COMPANYCODE, SECONDCARRIERTYPE, SECONDCARRIERCODE)
  CUSTOMERSUPPLIERDATA_THIRDCARRIER    (COMPANYCODE, THIRDCARRIERTYPE,  THIRDCARRIERCODE)
```

Picking the wrong one produces SQL that **runs fine and answers a different
question**. `join-path` prints every alternative whenever a hop is ambiguous —
choose by reading the constraint name, and if the question does not determine the
role, ask the user rather than defaulting.

Note the example above: `SALESORDER` has **no** direct FK to the customer master,
only carrier roles. The absence of an obvious relationship is itself information —
do not force a join that the schema does not offer.

### 4.6 29 tables have no primary key
Rows in them are not uniquely addressable by the schema. Expect duplicates and
do not assume a join to one is many-to-one.

### 4.7 `ABSUNIQUEID` is not the primary key
It is a framework surrogate id present on 2,896 tables. The real key is the
declared composite business key. Do not join on `ABSUNIQUEID` except for the
`FATHERID` pattern in §4.3.

---

## 5. Cardinality

Every FK edge is `many_to_one` from child to parent, so:

- child → parent (`direction: to_parent`) does **not** fan out rows;
- parent → child (`direction: to_child`) **does** fan out — aggregate, or expect
  duplicated parent columns.

When a query joins two or more children of the same parent, the row counts
multiply. Aggregate each child separately in a subquery instead.

---

## 6. Modules

Groupings inferred from table-name prefixes. Navigational only.

| Module | Tables | Label reliability |
|---|---|---|
| [`OTHER`](modules/OTHER.md) | 751 | low |
| [`WORK_DOCUMENTS`](modules/WORK_DOCUMENTS.md) | 346 | derived-from-naming |
| [`LOGISTICS`](modules/LOGISTICS.md) | 339 | derived-from-naming |
| [`HR`](modules/HR.md) | 277 | derived-from-naming |
| [`FINANCE`](modules/FINANCE.md) | 249 | derived-from-naming |
| [`SALES`](modules/SALES.md) | 246 | derived-from-naming |
| [`PLATFORM`](modules/PLATFORM.md) | 183 | derived-from-naming |
| [`SCHEDULING`](modules/SCHEDULING.md) | 180 | derived-from-naming |
| [`PRODUCTION`](modules/PRODUCTION.md) | 172 | derived-from-naming |
| [`PURCHASING`](modules/PURCHASING.md) | 131 | derived-from-naming |
| [`CORE_MASTER`](modules/CORE_MASTER.md) | 122 | derived-from-naming |
| [`ITEM_MASTER`](modules/ITEM_MASTER.md) | 114 | derived-from-naming |
| [`LOCALIZATION`](modules/LOCALIZATION.md) | 92 | low |
| [`QUALITY`](modules/QUALITY.md) | 82 | derived-from-naming |
| [`BPM_ENGINE`](modules/BPM_ENGINE.md) | 79 | derived-from-naming |
| [`COSTING`](modules/COSTING.md) | 68 | derived-from-naming |
| [`INTERNAL_ORDERS`](modules/INTERNAL_ORDERS.md) | 56 | derived-from-naming |
| [`WAREHOUSE`](modules/WAREHOUSE.md) | 56 | derived-from-naming |
| [`SUBCONTRACTING`](modules/SUBCONTRACTING.md) | 45 | derived-from-naming |
| [`TNA`](modules/TNA.md) | 42 | low |
| [`PDM`](modules/PDM.md) | 34 | low |
| [`INVENTORY`](modules/INVENTORY.md) | 32 | derived-from-naming |
| [`EINVOICING`](modules/EINVOICING.md) | 28 | derived-from-naming |
| [`SPECIFICATIONS`](modules/SPECIFICATIONS.md) | 22 | derived-from-naming |
| [`INTRASTAT`](modules/INTRASTAT.md) | 16 | derived-from-naming |

---

## 7. Files

```
kb/
  AGENT_GUIDE.md          <- this file, read first
  CONVENTIONS.md          <- naming conventions decoded
  GLOSSARY.md             <- column-name meanings (inferred)
  SQLITE_SCHEMA.md        <- kb.sqlite table reference
  kb.sqlite               <- queryable index + FTS
  tools/kb.py             <- retrieval CLI (search/describe/join-path/…)
  catalog/
    schema_summary.json   <- counts and provenance
    tables_index.json     <- light index: every table, its key, module, card path
    tables/<MODULE>.json  <- full column and key detail, split by module
    foreign_keys.json     <- all 11,001 FKs with JOIN predicates
    column_index.json     <- column name -> tables containing it
    modules.json          views.json   routines.json
  graph/
    join_graph.json       <- nodes (with hub penalties) + edges
    adjacency.json        <- per-table adjacency with JOIN predicates
    hubs.json             <- tables to avoid routing through
    implicit_links.json   <- inferred FATHERID links with confidence
  tables/<MODULE>/<TABLE>.md
  modules/<MODULE>.md
```

Regenerate everything with `python kb_build/build_kb.py`, then verify with
`python kb_build/validate_kb.py` (re-derives all counts straight from the DDL
and fails if the KB and the source have drifted apart).
Satya