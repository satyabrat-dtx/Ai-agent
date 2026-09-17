# DB2ADMIN.ACT_RU_VARIABLE

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 15
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 231962

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `TYPE_` | VARCHAR(255) | NOT NULL |  |  |  |
| 3 | `NAME_` | VARCHAR(255) | NOT NULL |  |  |  |
| 4 | `EXECUTION_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 5 | `PROC_INST_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 6 | `TASK_ID_` | VARCHAR(64) |  |  |  |  |
| 7 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 8 | `SUB_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 10 | `BYTEARRAY_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 11 | `DOUBLE_` | DOUBLE |  |  |  |  |
| 12 | `LONG_` | BIGINT |  |  |  |  |
| 13 | `TEXT_` | VARCHAR(4000) |  |  |  |  |
| 14 | `TEXT2_` | VARCHAR(4000) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_VAR_BYTEARRAY` | `BYTEARRAY_ID_` | [`ACT_GE_BYTEARRAY`](../BPM_ENGINE/ACT_GE_BYTEARRAY.md) | `ID_` | NO ACTION | `ACT_RU_VARIABLE.BYTEARRAY_ID_ = ACT_GE_BYTEARRAY.ID_` |
| `ACT_FK_VAR_EXE` | `EXECUTION_ID_` | [`ACT_RU_EXECUTION`](../BPM_ENGINE/ACT_RU_EXECUTION.md) | `ID_` | NO ACTION | `ACT_RU_VARIABLE.EXECUTION_ID_ = ACT_RU_EXECUTION.ID_` |
| `ACT_FK_VAR_PROCINST` | `PROC_INST_ID_` | [`ACT_RU_EXECUTION`](../BPM_ENGINE/ACT_RU_EXECUTION.md) | `ID_` | NO ACTION | `ACT_RU_VARIABLE.PROC_INST_ID_ = ACT_RU_EXECUTION.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_RU_VAR_SCOPE_ID_TYPE` (SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_RU_VAR_SUB_ID_TYPE` (SUB_SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_VARIABLE_BA` (BYTEARRAY_ID_)
- `ACT_IDX_VARIABLE_TASK_ID` (TASK_ID_)
- `ACT_IDX_VARIABLE_EXEC` (EXECUTION_ID_)
- `ACT_IDX_VARIABLE_PROCINST` (PROC_INST_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.TYPE_,
       t.NAME_,
       t.EXECUTION_ID_,
       t.PROC_INST_ID_,
       t.TASK_ID_,
       t.SCOPE_ID_,
       t.SUB_SCOPE_ID_,
       t.SCOPE_TYPE_,
       t.BYTEARRAY_ID_,
       t.DOUBLE_
FROM   DB2ADMIN.ACT_RU_VARIABLE t
FETCH FIRST 100 ROWS ONLY;
```
