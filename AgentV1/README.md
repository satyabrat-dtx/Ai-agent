# DB2ADMIN knowledge base

Query knowledge base for the `DB2ADMIN` schema of Db2 database **NOW7**, built
from `DB2ADMIN_DDL.sql` (a DB2LOOK 12.1 dump, 15,271,573 bytes).

**AI agents: start with [`AGENT_GUIDE.md`](AGENT_GUIDE.md).**

## Contents

| | |
|---|---|
| Tables | 3,762 |
| Columns | 122,450 (25,869 distinct names) |
| Foreign keys | 11,001 |
| Indexes | 3,281 |
| Views | 424 |
| Routines | 40 |
| Tables with a primary key | 3,733 |
| Tables without a primary key | 29 |
| Tables safe to query for business data | 3,364 |
| Staging mirrors (excluded) | 319 |
| BPM engine internals (excluded) | 79 |
| Inferred `FATHERID` parent links | 541 |
| `COMMENT ON` statements in the source | **0** |

Because the source has no comments, all business meaning in this KB is inferred
from naming conventions and foreign-key structure, and is labelled with a
confidence level wherever it is used.

## Quick start

```bash
python kb/tools/kb.py search "purchase order line"
python kb/tools/kb.py describe PURCHASEORDERLINE
python kb/tools/kb.py join-path PURCHASEORDERLINE CURRENCY
python kb/tools/kb.py sql "SELECT name FROM tables WHERE module='FINANCE' LIMIT 5"
```

## Docs

- [`AGENT_GUIDE.md`](AGENT_GUIDE.md) — retrieval protocol, SQL rules, traps
- [`CONVENTIONS.md`](CONVENTIONS.md) — naming conventions decoded
- [`GLOSSARY.md`](GLOSSARY.md) — column meanings
- [`SQLITE_SCHEMA.md`](SQLITE_SCHEMA.md) — `kb.sqlite` reference

## Rebuilding

```bash
python kb_build/build_kb.py      # regenerate kb/ from the DDL
python kb_build/validate_kb.py   # verify it against the DDL
```

`kb/` is derived output and can be deleted at any time. The build is
deterministic. `validate_kb.py` re-derives every count directly from the raw
DDL text and exits non-zero if the KB has drifted from its source, so run it
after any rebuild.

Build sources in `kb_build/`:

| File | Role |
|---|---|
| `parse_ddl.py` | DB2LOOK DDL → structured catalog |
| `classify.py` | all naming-based inference and join-routing constants |
| `build_kb.py` | emits every artefact under `kb/` |
| `kb_cli.py` | source of `kb/tools/kb.py` |
| `validate_kb.py` | post-build integrity checks |
