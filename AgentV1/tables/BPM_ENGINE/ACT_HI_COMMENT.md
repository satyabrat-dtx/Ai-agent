# DB2ADMIN.ACT_HI_COMMENT

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 9
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233607

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `TYPE_` | VARCHAR(255) |  |  |  |  |
| 2 | `TIME_` | TIMESTAMP | NOT NULL |  |  |  |
| 3 | `USER_ID_` | VARCHAR(255) |  |  |  |  |
| 4 | `TASK_ID_` | VARCHAR(64) |  |  |  |  |
| 5 | `PROC_INST_ID_` | VARCHAR(64) |  |  |  |  |
| 6 | `ACTION_` | VARCHAR(255) |  |  |  |  |
| 7 | `MESSAGE_` | VARCHAR(4000) |  |  |  |  |
| 8 | `FULL_MSG_` | BLOB(1048576) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID_,
       t.TYPE_,
       t.TIME_,
       t.USER_ID_,
       t.TASK_ID_,
       t.PROC_INST_ID_,
       t.ACTION_,
       t.MESSAGE_,
       t.FULL_MSG_
FROM   DB2ADMIN.ACT_HI_COMMENT t
FETCH FIRST 100 ROWS ONLY;
```
