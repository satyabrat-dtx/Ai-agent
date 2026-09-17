# DB2ADMIN.ACT_RU_TASK

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 30
- **Primary key**: `ID_`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 231710

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `EXECUTION_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 3 | `PROC_INST_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 4 | `PROC_DEF_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 5 | `TASK_DEF_ID_` | VARCHAR(64) |  |  |  |  |
| 6 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 7 | `SUB_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 8 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 9 | `SCOPE_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |
| 10 | `PROPAGATED_STAGE_INST_ID_` | VARCHAR(255) |  |  |  |  |
| 11 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 12 | `PARENT_TASK_ID_` | VARCHAR(64) |  |  |  |  |
| 13 | `DESCRIPTION_` | VARCHAR(4000) |  |  |  |  |
| 14 | `TASK_DEF_KEY_` | VARCHAR(255) |  |  |  |  |
| 15 | `OWNER_` | VARCHAR(255) |  |  |  |  |
| 16 | `ASSIGNEE_` | VARCHAR(255) |  |  |  |  |
| 17 | `DELEGATION_` | VARCHAR(64) |  |  |  |  |
| 18 | `PRIORITY_` | INTEGER |  |  |  |  |
| 19 | `CREATE_TIME_` | TIMESTAMP |  |  |  |  |
| 20 | `DUE_DATE_` | TIMESTAMP |  |  |  |  |
| 21 | `CATEGORY_` | VARCHAR(255) |  |  |  |  |
| 22 | `SUSPENSION_STATE_` | INTEGER |  |  |  |  |
| 23 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 24 | `FORM_KEY_` | VARCHAR(255) |  |  |  |  |
| 25 | `CLAIM_TIME_` | TIMESTAMP |  |  |  |  |
| 26 | `IS_COUNT_ENABLED_` | SMALLINT |  |  |  |  |
| 27 | `VAR_COUNT_` | INTEGER |  |  |  |  |
| 28 | `ID_LINK_COUNT_` | INTEGER |  |  |  |  |
| 29 | `SUB_TASK_COUNT_` | INTEGER |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_TASK_EXE` | `EXECUTION_ID_` | [`ACT_RU_EXECUTION`](../BPM_ENGINE/ACT_RU_EXECUTION.md) | `ID_` | NO ACTION | `ACT_RU_TASK.EXECUTION_ID_ = ACT_RU_EXECUTION.ID_` |
| `ACT_FK_TASK_PROCDEF` | `PROC_DEF_ID_` | [`ACT_RE_PROCDEF`](../BPM_ENGINE/ACT_RE_PROCDEF.md) | `ID_` | NO ACTION | `ACT_RU_TASK.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |
| `ACT_FK_TASK_PROCINST` | `PROC_INST_ID_` | [`ACT_RU_EXECUTION`](../BPM_ENGINE/ACT_RU_EXECUTION.md) | `ID_` | NO ACTION | `ACT_RU_TASK.PROC_INST_ID_ = ACT_RU_EXECUTION.ID_` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACT_FK_TSKASS_TASK` | [`ACT_RU_IDENTITYLINK`](../BPM_ENGINE/ACT_RU_IDENTITYLINK.md) | `TASK_ID_` | `ACT_RU_IDENTITYLINK.TASK_ID_ = ACT_RU_TASK.ID_` |

## Indexes

- `ACT_IDX_TASK_CREATE` (CREATE_TIME_)
- `ACT_IDX_TASK_SCOPE` (SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_TASK_SUB_SCOPE` (SUB_SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_TASK_SCOPE_DEF` (SCOPE_DEFINITION_ID_, SCOPE_TYPE_)
- `ACT_IDX_TASK_EXEC` (EXECUTION_ID_)
- `ACT_IDX_TASK_PROCINST` (PROC_INST_ID_)
- `ACT_IDX_TASK_PROC_DEF_ID` (PROC_DEF_ID_)

## Check constraints

- `SQL250408061219210`: `IS_COUNT_ENABLED_ in (1,0)`

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.EXECUTION_ID_,
       t.PROC_INST_ID_,
       t.PROC_DEF_ID_,
       t.TASK_DEF_ID_,
       t.SCOPE_ID_,
       t.SUB_SCOPE_ID_,
       t.SCOPE_TYPE_,
       t.SCOPE_DEFINITION_ID_,
       t.PROPAGATED_STAGE_INST_ID_,
       t.NAME_
FROM   DB2ADMIN.ACT_RU_TASK t
FETCH FIRST 100 ROWS ONLY;
```
