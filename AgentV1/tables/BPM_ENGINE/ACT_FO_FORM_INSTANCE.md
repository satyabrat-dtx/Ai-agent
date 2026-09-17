# DB2ADMIN.ACT_FO_FORM_INSTANCE

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 12
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234239

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `FORM_DEFINITION_ID_` | VARCHAR(255) | NOT NULL |  |  |  |
| 2 | `TASK_ID_` | VARCHAR(255) |  |  |  |  |
| 3 | `PROC_INST_ID_` | VARCHAR(255) |  |  |  |  |
| 4 | `PROC_DEF_ID_` | VARCHAR(255) |  |  |  |  |
| 5 | `SUBMITTED_DATE_` | TIMESTAMP |  |  |  |  |
| 6 | `SUBMITTED_BY_` | VARCHAR(255) |  |  |  |  |
| 7 | `FORM_VALUES_ID_` | VARCHAR(255) |  |  |  |  |
| 8 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 10 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 11 | `SCOPE_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_FORM_TASK` (TASK_ID_)
- `ACT_IDX_FORM_PROC` (PROC_INST_ID_)
- `ACT_IDX_FORM_SCOPE` (SCOPE_ID_, SCOPE_TYPE_)

## Starter query

```sql
SELECT t.ID_,
       t.FORM_DEFINITION_ID_,
       t.TASK_ID_,
       t.PROC_INST_ID_,
       t.PROC_DEF_ID_,
       t.SUBMITTED_DATE_,
       t.SUBMITTED_BY_,
       t.FORM_VALUES_ID_,
       t.TENANT_ID_,
       t.SCOPE_ID_,
       t.SCOPE_TYPE_,
       t.SCOPE_DEFINITION_ID_
FROM   DB2ADMIN.ACT_FO_FORM_INSTANCE t
FETCH FIRST 100 ROWS ONLY;
```
