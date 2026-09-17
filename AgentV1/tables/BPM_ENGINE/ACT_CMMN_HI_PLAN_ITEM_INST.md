# DB2ADMIN.ACT_CMMN_HI_PLAN_ITEM_INST

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 33
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234914

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER | NOT NULL |  |  |  |
| 2 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 3 | `STATE_` | VARCHAR(255) |  |  |  |  |
| 4 | `CASE_DEF_ID_` | VARCHAR(255) |  |  |  |  |
| 5 | `CASE_INST_ID_` | VARCHAR(255) |  |  |  |  |
| 6 | `STAGE_INST_ID_` | VARCHAR(255) |  |  |  |  |
| 7 | `IS_STAGE_` | BOOLEAN |  |  |  |  |
| 8 | `ELEMENT_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `ITEM_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |
| 10 | `ITEM_DEFINITION_TYPE_` | VARCHAR(255) |  |  |  |  |
| 11 | `CREATE_TIME_` | TIMESTAMP |  |  |  |  |
| 12 | `LAST_AVAILABLE_TIME_` | TIMESTAMP |  |  |  |  |
| 13 | `LAST_ENABLED_TIME_` | TIMESTAMP |  |  |  |  |
| 14 | `LAST_DISABLED_TIME_` | TIMESTAMP |  |  |  |  |
| 15 | `LAST_STARTED_TIME_` | TIMESTAMP |  |  |  |  |
| 16 | `LAST_SUSPENDED_TIME_` | TIMESTAMP |  |  |  |  |
| 17 | `COMPLETED_TIME_` | TIMESTAMP |  |  |  |  |
| 18 | `OCCURRED_TIME_` | TIMESTAMP |  |  |  |  |
| 19 | `TERMINATED_TIME_` | TIMESTAMP |  |  |  |  |
| 20 | `EXIT_TIME_` | TIMESTAMP |  |  |  |  |
| 21 | `ENDED_TIME_` | TIMESTAMP |  |  |  |  |
| 22 | `LAST_UPDATED_TIME_` | TIMESTAMP |  |  |  |  |
| 23 | `START_USER_ID_` | VARCHAR(255) |  |  |  |  |
| 24 | `REFERENCE_ID_` | VARCHAR(255) |  |  |  |  |
| 25 | `REFERENCE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 26 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 27 | `ENTRY_CRITERION_ID_` | VARCHAR(255) |  |  |  |  |
| 28 | `EXIT_CRITERION_ID_` | VARCHAR(255) |  |  |  |  |
| 29 | `SHOW_IN_OVERVIEW_` | BOOLEAN |  |  |  |  |
| 30 | `EXTRA_VALUE_` | VARCHAR(255) |  |  |  |  |
| 31 | `DERIVED_CASE_DEF_ID_` | VARCHAR(255) |  |  |  |  |
| 32 | `LAST_UNAVAILABLE_TIME_` | TIMESTAMP(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.NAME_,
       t.STATE_,
       t.CASE_DEF_ID_,
       t.CASE_INST_ID_,
       t.STAGE_INST_ID_,
       t.IS_STAGE_,
       t.ELEMENT_ID_,
       t.ITEM_DEFINITION_ID_,
       t.ITEM_DEFINITION_TYPE_,
       t.CREATE_TIME_
FROM   DB2ADMIN.ACT_CMMN_HI_PLAN_ITEM_INST t
FETCH FIRST 100 ROWS ONLY;
```
