# DB2ADMIN.ACT_DMN_HI_DECISION_EXECUTION

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 12
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234059

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `DECISION_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |
| 2 | `DEPLOYMENT_ID_` | VARCHAR(255) |  |  |  |  |
| 3 | `START_TIME_` | TIMESTAMP |  |  |  |  |
| 4 | `END_TIME_` | TIMESTAMP |  |  |  |  |
| 5 | `INSTANCE_ID_` | VARCHAR(255) |  |  |  |  |
| 6 | `EXECUTION_ID_` | VARCHAR(255) |  |  |  |  |
| 7 | `ACTIVITY_ID_` | VARCHAR(255) |  |  |  |  |
| 8 | `FAILED_` | BOOLEAN |  |  |  |  |
| 9 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 10 | `EXECUTION_JSON_` | CLOB(1048576) |  |  |  |  |
| 11 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_DMN_INSTANCE_ID` (INSTANCE_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.DECISION_DEFINITION_ID_,
       t.DEPLOYMENT_ID_,
       t.START_TIME_,
       t.END_TIME_,
       t.INSTANCE_ID_,
       t.EXECUTION_ID_,
       t.ACTIVITY_ID_,
       t.FAILED_,
       t.TENANT_ID_,
       t.EXECUTION_JSON_,
       t.SCOPE_TYPE_
FROM   DB2ADMIN.ACT_DMN_HI_DECISION_EXECUTION t
FETCH FIRST 100 ROWS ONLY;
```
