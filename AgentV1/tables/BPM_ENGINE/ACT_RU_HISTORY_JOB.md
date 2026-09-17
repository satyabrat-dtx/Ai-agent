# DB2ADMIN.ACT_RU_HISTORY_JOB

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 14
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 232718

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `LOCK_EXP_TIME_` | TIMESTAMP |  |  |  |  |
| 3 | `LOCK_OWNER_` | VARCHAR(255) |  |  |  |  |
| 4 | `RETRIES_` | INTEGER |  |  |  |  |
| 5 | `EXCEPTION_STACK_ID_` | VARCHAR(64) |  |  |  |  |
| 6 | `EXCEPTION_MSG_` | VARCHAR(4000) |  |  |  |  |
| 7 | `HANDLER_TYPE_` | VARCHAR(255) |  |  |  |  |
| 8 | `HANDLER_CFG_` | VARCHAR(4000) |  |  |  |  |
| 9 | `CUSTOM_VALUES_ID_` | VARCHAR(64) |  |  |  |  |
| 10 | `ADV_HANDLER_CFG_ID_` | VARCHAR(64) |  |  |  |  |
| 11 | `CREATE_TIME_` | TIMESTAMP |  |  |  |  |
| 12 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 13 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.LOCK_EXP_TIME_,
       t.LOCK_OWNER_,
       t.RETRIES_,
       t.EXCEPTION_STACK_ID_,
       t.EXCEPTION_MSG_,
       t.HANDLER_TYPE_,
       t.HANDLER_CFG_,
       t.CUSTOM_VALUES_ID_,
       t.ADV_HANDLER_CFG_ID_,
       t.CREATE_TIME_
FROM   DB2ADMIN.ACT_RU_HISTORY_JOB t
FETCH FIRST 100 ROWS ONLY;
```
