# DB2ADMIN.ACT_CMMN_CASEDEF

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 13
- **Primary key**: `ID_`
- **FK degree**: referenced by 4 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234530

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER | NOT NULL |  |  |  |
| 2 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 3 | `KEY_` | VARCHAR(255) | NOT NULL |  |  |  |
| 4 | `VERSION_` | INTEGER | NOT NULL |  |  |  |
| 5 | `CATEGORY_` | VARCHAR(255) |  |  |  |  |
| 6 | `DEPLOYMENT_ID_` | VARCHAR(255) |  | FK | foreign_key |  |
| 7 | `RESOURCE_NAME_` | VARCHAR(4000) |  |  |  |  |
| 8 | `DESCRIPTION_` | VARCHAR(4000) |  |  |  |  |
| 9 | `HAS_GRAPHICAL_NOTATION_` | BOOLEAN |  |  |  |  |
| 10 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 11 | `DGRM_RESOURCE_NAME_` | VARCHAR(4000) |  |  |  |  |
| 12 | `HAS_START_FORM_KEY_` | BOOLEAN |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_CASE_DEF_DPLY` | `DEPLOYMENT_ID_` | [`ACT_CMMN_DEPLOYMENT`](../BPM_ENGINE/ACT_CMMN_DEPLOYMENT.md) | `ID_` | NO ACTION | `ACT_CMMN_CASEDEF.DEPLOYMENT_ID_ = ACT_CMMN_DEPLOYMENT.ID_` |

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACT_FK_CASE_INST_CASE_DEF` | [`ACT_CMMN_RU_CASE_INST`](../BPM_ENGINE/ACT_CMMN_RU_CASE_INST.md) | `CASE_DEF_ID_` | `ACT_CMMN_RU_CASE_INST.CASE_DEF_ID_ = ACT_CMMN_CASEDEF.ID_` |
| `ACT_FK_PLAN_ITEM_CASE_DEF` | [`ACT_CMMN_RU_PLAN_ITEM_INST`](../BPM_ENGINE/ACT_CMMN_RU_PLAN_ITEM_INST.md) | `CASE_DEF_ID_` | `ACT_CMMN_RU_PLAN_ITEM_INST.CASE_DEF_ID_ = ACT_CMMN_CASEDEF.ID_` |
| `ACT_FK_SENTRY_CASE_DEF` | [`ACT_CMMN_RU_SENTRY_PART_INST`](../BPM_ENGINE/ACT_CMMN_RU_SENTRY_PART_INST.md) | `CASE_DEF_ID_` | `ACT_CMMN_RU_SENTRY_PART_INST.CASE_DEF_ID_ = ACT_CMMN_CASEDEF.ID_` |
| `ACT_FK_MIL_CASE_DEF` | [`ACT_CMMN_RU_MIL_INST`](../BPM_ENGINE/ACT_CMMN_RU_MIL_INST.md) | `CASE_DEF_ID_` | `ACT_CMMN_RU_MIL_INST.CASE_DEF_ID_ = ACT_CMMN_CASEDEF.ID_` |

## Indexes

- `ACT_IDX_CASE_DEF_DPLY` (DEPLOYMENT_ID_)
- UNIQUE `ACT_IDX_CASE_DEF_UNIQ` (KEY_, VERSION_, TENANT_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.NAME_,
       t.KEY_,
       t.VERSION_,
       t.CATEGORY_,
       t.DEPLOYMENT_ID_,
       t.RESOURCE_NAME_,
       t.DESCRIPTION_,
       t.HAS_GRAPHICAL_NOTATION_,
       t.TENANT_ID_,
       t.DGRM_RESOURCE_NAME_
FROM   DB2ADMIN.ACT_CMMN_CASEDEF t
FETCH FIRST 100 ROWS ONLY;
```
