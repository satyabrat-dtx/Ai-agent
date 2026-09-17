# DB2ADMIN.ACT_RU_IDENTITYLINK

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 12
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 231273

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `GROUP_ID_` | VARCHAR(255) |  |  |  |  |
| 3 | `TYPE_` | VARCHAR(255) |  |  |  |  |
| 4 | `USER_ID_` | VARCHAR(255) |  |  |  |  |
| 5 | `TASK_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 6 | `PROC_INST_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 7 | `PROC_DEF_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 8 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `SUB_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 10 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 11 | `SCOPE_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_ATHRZ_PROCEDEF` | `PROC_DEF_ID_` | [`ACT_RE_PROCDEF`](../BPM_ENGINE/ACT_RE_PROCDEF.md) | `ID_` | NO ACTION | `ACT_RU_IDENTITYLINK.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |
| `ACT_FK_IDL_PROCINST` | `PROC_INST_ID_` | [`ACT_RU_EXECUTION`](../BPM_ENGINE/ACT_RU_EXECUTION.md) | `ID_` | NO ACTION | `ACT_RU_IDENTITYLINK.PROC_INST_ID_ = ACT_RU_EXECUTION.ID_` |
| `ACT_FK_TSKASS_TASK` | `TASK_ID_` | [`ACT_RU_TASK`](../BPM_ENGINE/ACT_RU_TASK.md) | `ID_` | NO ACTION | `ACT_RU_IDENTITYLINK.TASK_ID_ = ACT_RU_TASK.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_IDENT_LNK_USER` (USER_ID_)
- `ACT_IDX_IDENT_LNK_GROUP` (GROUP_ID_)
- `ACT_IDX_IDENT_LNK_SCOPE` (SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_IDENT_LNK_SUB_SCOPE` (SUB_SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_IDENT_LNK_SCOPE_DEF` (SCOPE_DEFINITION_ID_, SCOPE_TYPE_)
- `ACT_IDX_ATHRZ_PROCEDEF` (PROC_DEF_ID_)
- `ACT_IDX_IDENT_LNK_TASK` (TASK_ID_)
- `ACT_IDX_IDENT_LNK_PROCINST` (PROC_INST_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.GROUP_ID_,
       t.TYPE_,
       t.USER_ID_,
       t.TASK_ID_,
       t.PROC_INST_ID_,
       t.PROC_DEF_ID_,
       t.SCOPE_ID_,
       t.SUB_SCOPE_ID_,
       t.SCOPE_TYPE_,
       t.SCOPE_DEFINITION_ID_
FROM   DB2ADMIN.ACT_RU_IDENTITYLINK t
FETCH FIRST 100 ROWS ONLY;
```
