# DB2ADMIN.ACT_RU_DEADLETTER_JOB

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 24
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 232582

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `CATEGORY_` | VARCHAR(255) |  |  |  |  |
| 3 | `TYPE_` | VARCHAR(255) | NOT NULL |  |  |  |
| 4 | `EXCLUSIVE_` | SMALLINT |  |  |  |  |
| 5 | `EXECUTION_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 6 | `PROCESS_INSTANCE_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 7 | `PROC_DEF_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 8 | `ELEMENT_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `ELEMENT_NAME_` | VARCHAR(255) |  |  |  |  |
| 10 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 11 | `SUB_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 12 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 13 | `SCOPE_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |
| 14 | `CORRELATION_ID_` | VARCHAR(255) |  |  |  |  |
| 15 | `EXCEPTION_STACK_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 16 | `EXCEPTION_MSG_` | VARCHAR(4000) |  |  |  |  |
| 17 | `DUEDATE_` | TIMESTAMP |  |  |  |  |
| 18 | `REPEAT_` | VARCHAR(255) |  |  |  |  |
| 19 | `HANDLER_TYPE_` | VARCHAR(255) |  |  |  |  |
| 20 | `HANDLER_CFG_` | VARCHAR(4000) |  |  |  |  |
| 21 | `CUSTOM_VALUES_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 22 | `CREATE_TIME_` | TIMESTAMP |  |  |  |  |
| 23 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_DEADLETTER_JOB_EXECUTION` | `EXECUTION_ID_` | [`ACT_RU_EXECUTION`](../BPM_ENGINE/ACT_RU_EXECUTION.md) | `ID_` | NO ACTION | `ACT_RU_DEADLETTER_JOB.EXECUTION_ID_ = ACT_RU_EXECUTION.ID_` |
| `ACT_FK_DEADLETTER_JOB_PROCESS_INSTANCE` | `PROCESS_INSTANCE_ID_` | [`ACT_RU_EXECUTION`](../BPM_ENGINE/ACT_RU_EXECUTION.md) | `ID_` | NO ACTION | `ACT_RU_DEADLETTER_JOB.PROCESS_INSTANCE_ID_ = ACT_RU_EXECUTION.ID_` |
| `ACT_FK_DEADLETTER_JOB_PROC_DEF` | `PROC_DEF_ID_` | [`ACT_RE_PROCDEF`](../BPM_ENGINE/ACT_RE_PROCDEF.md) | `ID_` | NO ACTION | `ACT_RU_DEADLETTER_JOB.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |
| `ACT_FK_DJOB_CUSTOM_VAL` | `CUSTOM_VALUES_ID_` | [`ACT_GE_BYTEARRAY`](../BPM_ENGINE/ACT_GE_BYTEARRAY.md) | `ID_` | NO ACTION | `ACT_RU_DEADLETTER_JOB.CUSTOM_VALUES_ID_ = ACT_GE_BYTEARRAY.ID_` |
| `ACT_FK_DJOB_EXCEPTION` | `EXCEPTION_STACK_ID_` | [`ACT_GE_BYTEARRAY`](../BPM_ENGINE/ACT_GE_BYTEARRAY.md) | `ID_` | NO ACTION | `ACT_RU_DEADLETTER_JOB.EXCEPTION_STACK_ID_ = ACT_GE_BYTEARRAY.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_DJOB_EXCEPTION_ID` (EXCEPTION_STACK_ID_)
- `ACT_IDX_DJOB_CUSTOM_VAL_ID` (CUSTOM_VALUES_ID_)
- `ACT_IDX_DJOB_CORRELATION_ID` (CORRELATION_ID_)
- `ACT_IDX_DJOB_SCOPE` (SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_DJOB_SUB_SCOPE` (SUB_SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_DJOB_SCOPE_DEF` (SCOPE_DEFINITION_ID_, SCOPE_TYPE_)
- `ACT_IDX_DEADLETTER_JOB_EXECUTION_ID` (EXECUTION_ID_)
- `ACT_IDX_DEADLETTER_JOB_PROCESS_INSTANCE_ID` (PROCESS_INSTANCE_ID_)
- `ACT_IDX_DEADLETTER_JOB_PROC_DEF_ID` (PROC_DEF_ID_)

## Check constraints

- `SQL250408061219800`: `EXCLUSIVE_ in (1,0)`

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.CATEGORY_,
       t.TYPE_,
       t.EXCLUSIVE_,
       t.EXECUTION_ID_,
       t.PROCESS_INSTANCE_ID_,
       t.PROC_DEF_ID_,
       t.ELEMENT_ID_,
       t.ELEMENT_NAME_,
       t.SCOPE_ID_,
       t.SUB_SCOPE_ID_
FROM   DB2ADMIN.ACT_RU_DEADLETTER_JOB t
FETCH FIRST 100 ROWS ONLY;
```
