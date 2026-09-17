# DB2ADMIN.ACT_CMMN_RU_PLAN_ITEM_INST

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 35
- **Primary key**: `ID_`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234653

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER | NOT NULL |  |  |  |
| 2 | `CASE_DEF_ID_` | VARCHAR(255) |  | FK | foreign_key |  |
| 3 | `CASE_INST_ID_` | VARCHAR(255) |  | FK | foreign_key |  |
| 4 | `STAGE_INST_ID_` | VARCHAR(255) |  |  |  |  |
| 5 | `IS_STAGE_` | BOOLEAN |  |  |  |  |
| 6 | `ELEMENT_ID_` | VARCHAR(255) |  |  |  |  |
| 7 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 8 | `STATE_` | VARCHAR(255) |  |  |  |  |
| 9 | `CREATE_TIME_` | TIMESTAMP |  |  |  |  |
| 10 | `START_USER_ID_` | VARCHAR(255) |  |  |  |  |
| 11 | `REFERENCE_ID_` | VARCHAR(255) |  |  |  |  |
| 12 | `REFERENCE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 13 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 14 | `ITEM_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |
| 15 | `ITEM_DEFINITION_TYPE_` | VARCHAR(255) |  |  |  |  |
| 16 | `IS_COMPLETEABLE_` | BOOLEAN |  |  |  |  |
| 17 | `IS_COUNT_ENABLED_` | BOOLEAN |  |  |  |  |
| 18 | `VAR_COUNT_` | INTEGER |  |  |  |  |
| 19 | `SENTRY_PART_INST_COUNT_` | INTEGER |  |  |  |  |
| 20 | `LAST_AVAILABLE_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 21 | `LAST_ENABLED_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 22 | `LAST_DISABLED_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 23 | `LAST_STARTED_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 24 | `LAST_SUSPENDED_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 25 | `COMPLETED_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 26 | `OCCURRED_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 27 | `TERMINATED_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 28 | `EXIT_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 29 | `ENDED_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 30 | `ENTRY_CRITERION_ID_` | VARCHAR(255) |  |  |  |  |
| 31 | `EXIT_CRITERION_ID_` | VARCHAR(255) |  |  |  |  |
| 32 | `EXTRA_VALUE_` | VARCHAR(255) |  |  |  |  |
| 33 | `DERIVED_CASE_DEF_ID_` | VARCHAR(255) |  |  |  |  |
| 34 | `LAST_UNAVAILABLE_TIME_` | TIMESTAMP(3) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_PLAN_ITEM_CASE_DEF` | `CASE_DEF_ID_` | [`ACT_CMMN_CASEDEF`](../BPM_ENGINE/ACT_CMMN_CASEDEF.md) | `ID_` | NO ACTION | `ACT_CMMN_RU_PLAN_ITEM_INST.CASE_DEF_ID_ = ACT_CMMN_CASEDEF.ID_` |
| `ACT_FK_PLAN_ITEM_CASE_INST` | `CASE_INST_ID_` | [`ACT_CMMN_RU_CASE_INST`](../BPM_ENGINE/ACT_CMMN_RU_CASE_INST.md) | `ID_` | NO ACTION | `ACT_CMMN_RU_PLAN_ITEM_INST.CASE_INST_ID_ = ACT_CMMN_RU_CASE_INST.ID_` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACT_FK_SENTRY_PLAN_ITEM` | [`ACT_CMMN_RU_SENTRY_PART_INST`](../BPM_ENGINE/ACT_CMMN_RU_SENTRY_PART_INST.md) | `PLAN_ITEM_INST_ID_` | `ACT_CMMN_RU_SENTRY_PART_INST.PLAN_ITEM_INST_ID_ = ACT_CMMN_RU_PLAN_ITEM_INST.ID_` |

## Indexes

- `ACT_IDX_PLAN_ITEM_CASE_DEF` (CASE_DEF_ID_)
- `ACT_IDX_PLAN_ITEM_CASE_INST` (CASE_INST_ID_)
- `ACT_IDX_PLAN_ITEM_STAGE_INST` (STAGE_INST_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.CASE_DEF_ID_,
       t.CASE_INST_ID_,
       t.STAGE_INST_ID_,
       t.IS_STAGE_,
       t.ELEMENT_ID_,
       t.NAME_,
       t.STATE_,
       t.CREATE_TIME_,
       t.START_USER_ID_,
       t.REFERENCE_ID_
FROM   DB2ADMIN.ACT_CMMN_RU_PLAN_ITEM_INST t
FETCH FIRST 100 ROWS ONLY;
```
