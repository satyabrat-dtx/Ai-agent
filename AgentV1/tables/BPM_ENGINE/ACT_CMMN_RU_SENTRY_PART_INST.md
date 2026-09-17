# DB2ADMIN.ACT_CMMN_RU_SENTRY_PART_INST

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 8
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234737

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER | NOT NULL |  |  |  |
| 2 | `CASE_DEF_ID_` | VARCHAR(255) |  | FK | foreign_key |  |
| 3 | `CASE_INST_ID_` | VARCHAR(255) |  | FK | foreign_key |  |
| 4 | `PLAN_ITEM_INST_ID_` | VARCHAR(255) |  | FK | foreign_key |  |
| 5 | `ON_PART_ID_` | VARCHAR(255) |  |  |  |  |
| 6 | `IF_PART_ID_` | VARCHAR(255) |  |  |  |  |
| 7 | `TIME_STAMP_` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_SENTRY_CASE_DEF` | `CASE_DEF_ID_` | [`ACT_CMMN_CASEDEF`](../BPM_ENGINE/ACT_CMMN_CASEDEF.md) | `ID_` | NO ACTION | `ACT_CMMN_RU_SENTRY_PART_INST.CASE_DEF_ID_ = ACT_CMMN_CASEDEF.ID_` |
| `ACT_FK_SENTRY_CASE_INST` | `CASE_INST_ID_` | [`ACT_CMMN_RU_CASE_INST`](../BPM_ENGINE/ACT_CMMN_RU_CASE_INST.md) | `ID_` | NO ACTION | `ACT_CMMN_RU_SENTRY_PART_INST.CASE_INST_ID_ = ACT_CMMN_RU_CASE_INST.ID_` |
| `ACT_FK_SENTRY_PLAN_ITEM` | `PLAN_ITEM_INST_ID_` | [`ACT_CMMN_RU_PLAN_ITEM_INST`](../BPM_ENGINE/ACT_CMMN_RU_PLAN_ITEM_INST.md) | `ID_` | NO ACTION | `ACT_CMMN_RU_SENTRY_PART_INST.PLAN_ITEM_INST_ID_ = ACT_CMMN_RU_PLAN_ITEM_INST.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_SENTRY_CASE_DEF` (CASE_DEF_ID_)
- `ACT_IDX_SENTRY_CASE_INST` (CASE_INST_ID_)
- `ACT_IDX_SENTRY_PLAN_ITEM` (PLAN_ITEM_INST_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.CASE_DEF_ID_,
       t.CASE_INST_ID_,
       t.PLAN_ITEM_INST_ID_,
       t.ON_PART_ID_,
       t.IF_PART_ID_,
       t.TIME_STAMP_
FROM   DB2ADMIN.ACT_CMMN_RU_SENTRY_PART_INST t
FETCH FIRST 100 ROWS ONLY;
```
