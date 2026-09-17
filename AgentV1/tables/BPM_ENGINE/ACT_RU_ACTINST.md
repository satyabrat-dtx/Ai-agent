# DB2ADMIN.ACT_RU_ACTINST

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 17
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233258

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `PROC_DEF_ID_` | VARCHAR(64) | NOT NULL |  |  |  |
| 3 | `PROC_INST_ID_` | VARCHAR(64) | NOT NULL |  |  |  |
| 4 | `EXECUTION_ID_` | VARCHAR(64) | NOT NULL |  |  |  |
| 5 | `ACT_ID_` | VARCHAR(255) | NOT NULL |  |  |  |
| 6 | `TASK_ID_` | VARCHAR(64) |  |  |  |  |
| 7 | `CALL_PROC_INST_ID_` | VARCHAR(64) |  |  |  |  |
| 8 | `ACT_NAME_` | VARCHAR(255) |  |  |  |  |
| 9 | `ACT_TYPE_` | VARCHAR(255) | NOT NULL |  |  |  |
| 10 | `ASSIGNEE_` | VARCHAR(255) |  |  |  |  |
| 11 | `START_TIME_` | TIMESTAMP | NOT NULL |  |  |  |
| 12 | `END_TIME_` | TIMESTAMP |  |  |  |  |
| 13 | `DURATION_` | BIGINT |  |  |  |  |
| 14 | `TRANSACTION_ORDER_` | INTEGER |  |  |  |  |
| 15 | `DELETE_REASON_` | VARCHAR(4000) |  |  |  |  |
| 16 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_RU_ACTI_START` (START_TIME_)
- `ACT_IDX_RU_ACTI_END` (END_TIME_)
- `ACT_IDX_RU_ACTI_PROC` (PROC_INST_ID_)
- `ACT_IDX_RU_ACTI_PROC_ACT` (PROC_INST_ID_, ACT_ID_)
- `ACT_IDX_RU_ACTI_EXEC` (EXECUTION_ID_)
- `ACT_IDX_RU_ACTI_EXEC_ACT` (EXECUTION_ID_, ACT_ID_)
- `ACT_IDX_RU_ACTI_TASK` (TASK_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.PROC_DEF_ID_,
       t.PROC_INST_ID_,
       t.EXECUTION_ID_,
       t.ACT_ID_,
       t.TASK_ID_,
       t.CALL_PROC_INST_ID_,
       t.ACT_NAME_,
       t.ACT_TYPE_,
       t.ASSIGNEE_,
       t.START_TIME_
FROM   DB2ADMIN.ACT_RU_ACTINST t
FETCH FIRST 100 ROWS ONLY;
```
