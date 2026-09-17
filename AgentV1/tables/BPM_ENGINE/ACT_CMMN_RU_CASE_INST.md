# DB2ADMIN.ACT_CMMN_RU_CASE_INST

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 20
- **Primary key**: `ID_`
- **FK degree**: referenced by 3 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234584

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER | NOT NULL |  |  |  |
| 2 | `BUSINESS_KEY_` | VARCHAR(255) |  |  |  |  |
| 3 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 4 | `PARENT_ID_` | VARCHAR(255) |  |  |  |  |
| 5 | `CASE_DEF_ID_` | VARCHAR(255) |  | FK | foreign_key |  |
| 6 | `STATE_` | VARCHAR(255) |  |  |  |  |
| 7 | `START_TIME_` | TIMESTAMP |  |  |  |  |
| 8 | `START_USER_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `CALLBACK_ID_` | VARCHAR(255) |  |  |  |  |
| 10 | `CALLBACK_TYPE_` | VARCHAR(255) |  |  |  |  |
| 11 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 12 | `LOCK_TIME_` | TIMESTAMP |  |  |  |  |
| 13 | `IS_COMPLETEABLE_` | BOOLEAN |  |  |  |  |
| 14 | `REFERENCE_ID_` | VARCHAR(255) |  |  |  |  |
| 15 | `REFERENCE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 16 | `LOCK_OWNER_` | VARCHAR(255) |  |  |  |  |
| 17 | `LAST_REACTIVATION_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 18 | `LAST_REACTIVATION_USER_ID_` | VARCHAR(255) |  |  |  |  |
| 19 | `BUSINESS_STATUS_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_CASE_INST_CASE_DEF` | `CASE_DEF_ID_` | [`ACT_CMMN_CASEDEF`](../BPM_ENGINE/ACT_CMMN_CASEDEF.md) | `ID_` | NO ACTION | `ACT_CMMN_RU_CASE_INST.CASE_DEF_ID_ = ACT_CMMN_CASEDEF.ID_` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACT_FK_PLAN_ITEM_CASE_INST` | [`ACT_CMMN_RU_PLAN_ITEM_INST`](../BPM_ENGINE/ACT_CMMN_RU_PLAN_ITEM_INST.md) | `CASE_INST_ID_` | `ACT_CMMN_RU_PLAN_ITEM_INST.CASE_INST_ID_ = ACT_CMMN_RU_CASE_INST.ID_` |
| `ACT_FK_SENTRY_CASE_INST` | [`ACT_CMMN_RU_SENTRY_PART_INST`](../BPM_ENGINE/ACT_CMMN_RU_SENTRY_PART_INST.md) | `CASE_INST_ID_` | `ACT_CMMN_RU_SENTRY_PART_INST.CASE_INST_ID_ = ACT_CMMN_RU_CASE_INST.ID_` |
| `ACT_FK_MIL_CASE_INST` | [`ACT_CMMN_RU_MIL_INST`](../BPM_ENGINE/ACT_CMMN_RU_MIL_INST.md) | `CASE_INST_ID_` | `ACT_CMMN_RU_MIL_INST.CASE_INST_ID_ = ACT_CMMN_RU_CASE_INST.ID_` |

## Indexes

- `ACT_IDX_CASE_INST_CASE_DEF` (CASE_DEF_ID_)
- `ACT_IDX_CASE_INST_PARENT` (PARENT_ID_)
- `ACT_IDX_CASE_INST_REF_ID_` (REFERENCE_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.BUSINESS_KEY_,
       t.NAME_,
       t.PARENT_ID_,
       t.CASE_DEF_ID_,
       t.STATE_,
       t.START_TIME_,
       t.START_USER_ID_,
       t.CALLBACK_ID_,
       t.CALLBACK_TYPE_,
       t.TENANT_ID_
FROM   DB2ADMIN.ACT_CMMN_RU_CASE_INST t
FETCH FIRST 100 ROWS ONLY;
```
