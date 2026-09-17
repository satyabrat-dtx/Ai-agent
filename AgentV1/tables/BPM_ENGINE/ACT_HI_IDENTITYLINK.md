# DB2ADMIN.ACT_HI_IDENTITYLINK

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 11
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 231387

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `GROUP_ID_` | VARCHAR(255) |  |  |  |  |
| 2 | `TYPE_` | VARCHAR(255) |  |  |  |  |
| 3 | `USER_ID_` | VARCHAR(255) |  |  |  |  |
| 4 | `TASK_ID_` | VARCHAR(64) |  |  |  |  |
| 5 | `CREATE_TIME_` | TIMESTAMP |  |  |  |  |
| 6 | `PROC_INST_ID_` | VARCHAR(64) |  |  |  |  |
| 7 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 8 | `SUB_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 10 | `SCOPE_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_HI_IDENT_LNK_USER` (USER_ID_)
- `ACT_IDX_HI_IDENT_LNK_SCOPE` (SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_HI_IDENT_LNK_SUB_SCOPE` (SUB_SCOPE_ID_, SCOPE_TYPE_)
- `ACT_IDX_HI_IDENT_LNK_SCOPE_DEF` (SCOPE_DEFINITION_ID_, SCOPE_TYPE_)
- `ACT_IDX_HI_IDENT_LNK_TASK` (TASK_ID_)
- `ACT_IDX_HI_IDENT_LNK_PROCINST` (PROC_INST_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.GROUP_ID_,
       t.TYPE_,
       t.USER_ID_,
       t.TASK_ID_,
       t.CREATE_TIME_,
       t.PROC_INST_ID_,
       t.SCOPE_ID_,
       t.SUB_SCOPE_ID_,
       t.SCOPE_TYPE_,
       t.SCOPE_DEFINITION_ID_
FROM   DB2ADMIN.ACT_HI_IDENTITYLINK t
FETCH FIRST 100 ROWS ONLY;
```
