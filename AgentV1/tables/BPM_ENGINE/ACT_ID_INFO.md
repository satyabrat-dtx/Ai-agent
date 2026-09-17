# DB2ADMIN.ACT_ID_INFO

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 8
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233783

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `USER_ID_` | VARCHAR(64) |  |  |  |  |
| 3 | `TYPE_` | VARCHAR(64) |  |  |  |  |
| 4 | `KEY_` | VARCHAR(255) |  |  |  |  |
| 5 | `VALUE_` | VARCHAR(255) |  |  |  |  |
| 6 | `PASSWORD_` | BLOB(1048576) |  |  |  |  |
| 7 | `PARENT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.USER_ID_,
       t.TYPE_,
       t.KEY_,
       t.VALUE_,
       t.PASSWORD_,
       t.PARENT_ID_
FROM   DB2ADMIN.ACT_ID_INFO t
FETCH FIRST 100 ROWS ONLY;
```
