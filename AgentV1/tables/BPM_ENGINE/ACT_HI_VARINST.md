# DB2ADMIN.ACT_HI_VARINST

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 17
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 232058

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `PROC_INST_ID_` | VARCHAR(64) |  |  |  |  |
| 3 | `EXECUTION_ID_` | VARCHAR(64) |  |  |  |  |
| 4 | `TASK_ID_` | VARCHAR(64) |  |  |  |  |
| 5 | `NAME_` | VARCHAR(255) | NOT NULL |  |  |  |
| 6 | `VAR_TYPE_` | VARCHAR(100) |  |  |  |  |
| 7 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 8 | `SUB_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 10 | `BYTEARRAY_ID_` | VARCHAR(64) |  |  |  |  |
| 11 | `DOUBLE_` | DOUBLE |  |  |  |  |
| 12 | `LONG_` | BIGINT |  |  |  |  |
| 13 | `TEXT_` | VARCHAR(4000) |  |  |  |  |
| 14 | `TEXT2_` | VARCHAR(4000) |  |  |  |  |
| 15 | `CREATE_TIME_` | TIMESTAMP |  |  |  |  |
| 16 | `LAST_UPDATED_TIME_` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_HI_PROCVAR_NAME_TYPE` (NAME_, VAR_TYPE_)
- `ACT_IDX_HI_VAR_SCOPE_ID_TYPE` (SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_HI_VAR_SUB_ID_TYPE` (SUB_SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_HI_PROCVAR_PROC_INST` (PROC_INST_ID_)
- `ACT_IDX_HI_PROCVAR_TASK_ID` (TASK_ID_)
- `ACT_IDX_HI_PROCVAR_EXE` (EXECUTION_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.PROC_INST_ID_,
       t.EXECUTION_ID_,
       t.TASK_ID_,
       t.NAME_,
       t.VAR_TYPE_,
       t.SCOPE_ID_,
       t.SUB_SCOPE_ID_,
       t.SCOPE_TYPE_,
       t.BYTEARRAY_ID_,
       t.DOUBLE_
FROM   DB2ADMIN.ACT_HI_VARINST t
FETCH FIRST 100 ROWS ONLY;
```
