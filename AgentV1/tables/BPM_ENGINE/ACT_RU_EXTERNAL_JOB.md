# DB2ADMIN.ACT_RU_EXTERNAL_JOB

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 27
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 232751

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `CATEGORY_` | VARCHAR(255) |  |  |  |  |
| 3 | `TYPE_` | VARCHAR(255) | NOT NULL |  |  |  |
| 4 | `LOCK_EXP_TIME_` | TIMESTAMP |  |  |  |  |
| 5 | `LOCK_OWNER_` | VARCHAR(255) |  |  |  |  |
| 6 | `EXCLUSIVE_` | SMALLINT |  |  |  |  |
| 7 | `EXECUTION_ID_` | VARCHAR(64) |  |  |  |  |
| 8 | `PROCESS_INSTANCE_ID_` | VARCHAR(64) |  |  |  |  |
| 9 | `PROC_DEF_ID_` | VARCHAR(64) |  |  |  |  |
| 10 | `ELEMENT_ID_` | VARCHAR(255) |  |  |  |  |
| 11 | `ELEMENT_NAME_` | VARCHAR(255) |  |  |  |  |
| 12 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 13 | `SUB_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 14 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 15 | `SCOPE_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |
| 16 | `CORRELATION_ID_` | VARCHAR(255) |  |  |  |  |
| 17 | `RETRIES_` | INTEGER |  |  |  |  |
| 18 | `EXCEPTION_STACK_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 19 | `EXCEPTION_MSG_` | VARCHAR(4000) |  |  |  |  |
| 20 | `DUEDATE_` | TIMESTAMP |  |  |  |  |
| 21 | `REPEAT_` | VARCHAR(255) |  |  |  |  |
| 22 | `HANDLER_TYPE_` | VARCHAR(255) |  |  |  |  |
| 23 | `HANDLER_CFG_` | VARCHAR(4000) |  |  |  |  |
| 24 | `CUSTOM_VALUES_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 25 | `CREATE_TIME_` | TIMESTAMP |  |  |  |  |
| 26 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_EJOB_CUSTOM_VAL` | `CUSTOM_VALUES_ID_` | [`ACT_GE_BYTEARRAY`](../BPM_ENGINE/ACT_GE_BYTEARRAY.md) | `ID_` | NO ACTION | `ACT_RU_EXTERNAL_JOB.CUSTOM_VALUES_ID_ = ACT_GE_BYTEARRAY.ID_` |
| `ACT_FK_EJOB_EXCEPTION` | `EXCEPTION_STACK_ID_` | [`ACT_GE_BYTEARRAY`](../BPM_ENGINE/ACT_GE_BYTEARRAY.md) | `ID_` | NO ACTION | `ACT_RU_EXTERNAL_JOB.EXCEPTION_STACK_ID_ = ACT_GE_BYTEARRAY.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_EJOB_EXCEPTION_ID` (EXCEPTION_STACK_ID_)
- `ACT_IDX_EJOB_CUSTOM_VAL_ID` (CUSTOM_VALUES_ID_)
- `ACT_IDX_EJOB_CORRELATION_ID` (CORRELATION_ID_)
- `ACT_IDX_EJOB_SCOPE` (SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_EJOB_SUB_SCOPE` (SUB_SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_EJOB_SCOPE_DEF` (SCOPE_DEFINITION_ID_, SCOPE_TYPE_)

## Check constraints

- `SQL250408061219850`: `EXCLUSIVE_ in (1,0)`

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.CATEGORY_,
       t.TYPE_,
       t.LOCK_EXP_TIME_,
       t.LOCK_OWNER_,
       t.EXCLUSIVE_,
       t.EXECUTION_ID_,
       t.PROCESS_INSTANCE_ID_,
       t.PROC_DEF_ID_,
       t.ELEMENT_ID_,
       t.ELEMENT_NAME_
FROM   DB2ADMIN.ACT_RU_EXTERNAL_JOB t
FETCH FIRST 100 ROWS ONLY;
```
