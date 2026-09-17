# DB2ADMIN.ACT_HI_TSK_LOG

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 14
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 231922

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `TYPE_` | VARCHAR(64) |  |  |  |  |
| 2 | `TASK_ID_` | VARCHAR(64) | NOT NULL |  |  |  |
| 3 | `TIME_STAMP_` | TIMESTAMP | NOT NULL |  |  |  |
| 4 | `USER_ID_` | VARCHAR(255) |  |  |  |  |
| 5 | `DATA_` | VARCHAR(4000) |  |  |  |  |
| 6 | `EXECUTION_ID_` | VARCHAR(64) |  |  |  |  |
| 7 | `PROC_INST_ID_` | VARCHAR(64) |  |  |  |  |
| 8 | `PROC_DEF_ID_` | VARCHAR(64) |  |  |  |  |
| 9 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 10 | `SCOPE_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |
| 11 | `SUB_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 12 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 13 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID_,
       t.TYPE_,
       t.TASK_ID_,
       t.TIME_STAMP_,
       t.USER_ID_,
       t.DATA_,
       t.EXECUTION_ID_,
       t.PROC_INST_ID_,
       t.PROC_DEF_ID_,
       t.SCOPE_ID_,
       t.SCOPE_DEFINITION_ID_,
       t.SUB_SCOPE_ID_
FROM   DB2ADMIN.ACT_HI_TSK_LOG t
FETCH FIRST 100 ROWS ONLY;
```
