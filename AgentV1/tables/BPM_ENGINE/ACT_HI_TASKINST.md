# DB2ADMIN.ACT_HI_TASKINST

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 28
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 231832

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `PROC_DEF_ID_` | VARCHAR(64) |  |  |  |  |
| 3 | `TASK_DEF_ID_` | VARCHAR(64) |  |  |  |  |
| 4 | `TASK_DEF_KEY_` | VARCHAR(255) |  |  |  |  |
| 5 | `PROC_INST_ID_` | VARCHAR(64) |  |  |  |  |
| 6 | `EXECUTION_ID_` | VARCHAR(64) |  |  |  |  |
| 7 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 8 | `SUB_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 10 | `SCOPE_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |
| 11 | `PROPAGATED_STAGE_INST_ID_` | VARCHAR(255) |  |  |  |  |
| 12 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 13 | `PARENT_TASK_ID_` | VARCHAR(64) |  |  |  |  |
| 14 | `DESCRIPTION_` | VARCHAR(4000) |  |  |  |  |
| 15 | `OWNER_` | VARCHAR(255) |  |  |  |  |
| 16 | `ASSIGNEE_` | VARCHAR(255) |  |  |  |  |
| 17 | `START_TIME_` | TIMESTAMP | NOT NULL |  |  |  |
| 18 | `CLAIM_TIME_` | TIMESTAMP |  |  |  |  |
| 19 | `END_TIME_` | TIMESTAMP |  |  |  |  |
| 20 | `DURATION_` | BIGINT |  |  |  |  |
| 21 | `DELETE_REASON_` | VARCHAR(4000) |  |  |  |  |
| 22 | `PRIORITY_` | INTEGER |  |  |  |  |
| 23 | `DUE_DATE_` | TIMESTAMP |  |  |  |  |
| 24 | `FORM_KEY_` | VARCHAR(255) |  |  |  |  |
| 25 | `CATEGORY_` | VARCHAR(255) |  |  |  |  |
| 26 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 27 | `LAST_UPDATED_TIME_` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_HI_TASK_SCOPE` (SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_HI_TASK_SUB_SCOPE` (SUB_SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_HI_TASK_SCOPE_DEF` (SCOPE_DEFINITION_ID_, SCOPE_TYPE_)
- `ACT_IDX_HI_TASK_INST_PROCINST` (PROC_INST_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.PROC_DEF_ID_,
       t.TASK_DEF_ID_,
       t.TASK_DEF_KEY_,
       t.PROC_INST_ID_,
       t.EXECUTION_ID_,
       t.SCOPE_ID_,
       t.SUB_SCOPE_ID_,
       t.SCOPE_TYPE_,
       t.SCOPE_DEFINITION_ID_,
       t.PROPAGATED_STAGE_INST_ID_
FROM   DB2ADMIN.ACT_HI_TASKINST t
FETCH FIRST 100 ROWS ONLY;
```
