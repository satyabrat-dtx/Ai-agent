# DB2ADMIN.ACT_ID_PROPERTY

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 3
- **Primary key**: `NAME_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233665

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NAME_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `VALUE_` | VARCHAR(300) |  |  |  |  |
| 2 | `REV_` | INTEGER |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.NAME_,
       t.VALUE_,
       t.REV_
FROM   DB2ADMIN.ACT_ID_PROPERTY t
FETCH FIRST 100 ROWS ONLY;
```
