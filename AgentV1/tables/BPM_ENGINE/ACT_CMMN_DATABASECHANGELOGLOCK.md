# DB2ADMIN.ACT_CMMN_DATABASECHANGELOGLOCK

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 4
- **Primary key**: `ID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234419

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `LOCKED` | BOOLEAN | NOT NULL |  |  |  |
| 2 | `LOCKGRANTED` | TIMESTAMP |  |  |  |  |
| 3 | `LOCKEDBY` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID,
       t.LOCKED,
       t.LOCKGRANTED,
       t.LOCKEDBY
FROM   DB2ADMIN.ACT_CMMN_DATABASECHANGELOGLOCK t
FETCH FIRST 100 ROWS ONLY;
```
