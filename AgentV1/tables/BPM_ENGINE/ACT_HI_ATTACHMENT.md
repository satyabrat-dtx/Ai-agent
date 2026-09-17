# DB2ADMIN.ACT_HI_ATTACHMENT

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 11
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233635

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `USER_ID_` | VARCHAR(255) |  |  |  |  |
| 3 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 4 | `DESCRIPTION_` | VARCHAR(4000) |  |  |  |  |
| 5 | `TYPE_` | VARCHAR(255) |  |  |  |  |
| 6 | `TASK_ID_` | VARCHAR(64) |  |  |  |  |
| 7 | `PROC_INST_ID_` | VARCHAR(64) |  |  |  |  |
| 8 | `URL_` | VARCHAR(4000) |  |  |  |  |
| 9 | `CONTENT_ID_` | VARCHAR(64) |  |  |  |  |
| 10 | `TIME_` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.USER_ID_,
       t.NAME_,
       t.DESCRIPTION_,
       t.TYPE_,
       t.TASK_ID_,
       t.PROC_INST_ID_,
       t.URL_,
       t.CONTENT_ID_,
       t.TIME_
FROM   DB2ADMIN.ACT_HI_ATTACHMENT t
FETCH FIRST 100 ROWS ONLY;
```
