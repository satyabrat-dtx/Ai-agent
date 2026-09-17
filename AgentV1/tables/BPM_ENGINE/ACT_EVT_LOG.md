# DB2ADMIN.ACT_EVT_LOG

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 12
- **Primary key**: `LOG_NR_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233180

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LOG_NR_` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `TYPE_` | VARCHAR(64) |  |  |  |  |
| 2 | `PROC_DEF_ID_` | VARCHAR(64) |  |  |  |  |
| 3 | `PROC_INST_ID_` | VARCHAR(64) |  |  |  |  |
| 4 | `EXECUTION_ID_` | VARCHAR(64) |  |  |  |  |
| 5 | `TASK_ID_` | VARCHAR(64) |  |  |  |  |
| 6 | `TIME_STAMP_` | TIMESTAMP | NOT NULL |  |  |  |
| 7 | `USER_ID_` | VARCHAR(255) |  |  |  |  |
| 8 | `DATA_` | BLOB(1048576) |  |  |  |  |
| 9 | `LOCK_OWNER_` | VARCHAR(255) |  |  |  |  |
| 10 | `LOCK_TIME_` | TIMESTAMP |  |  |  |  |
| 11 | `IS_PROCESSED_` | INTEGER |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.LOG_NR_,
       t.TYPE_,
       t.PROC_DEF_ID_,
       t.PROC_INST_ID_,
       t.EXECUTION_ID_,
       t.TASK_ID_,
       t.TIME_STAMP_,
       t.USER_ID_,
       t.DATA_,
       t.LOCK_OWNER_,
       t.LOCK_TIME_,
       t.IS_PROCESSED_
FROM   DB2ADMIN.ACT_EVT_LOG t
FETCH FIRST 100 ROWS ONLY;
```
