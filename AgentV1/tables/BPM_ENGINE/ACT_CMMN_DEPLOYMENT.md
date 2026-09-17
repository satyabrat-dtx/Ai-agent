# DB2ADMIN.ACT_CMMN_DEPLOYMENT

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 7
- **Primary key**: `ID_`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234470

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 2 | `CATEGORY_` | VARCHAR(255) |  |  |  |  |
| 3 | `KEY_` | VARCHAR(255) |  |  |  |  |
| 4 | `DEPLOY_TIME_` | TIMESTAMP |  |  |  |  |
| 5 | `PARENT_DEPLOYMENT_ID_` | VARCHAR(255) |  |  |  |  |
| 6 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACT_FK_CMMN_RSRC_DPL` | [`ACT_CMMN_DEPLOYMENT_RESOURCE`](../BPM_ENGINE/ACT_CMMN_DEPLOYMENT_RESOURCE.md) | `DEPLOYMENT_ID_` | `ACT_CMMN_DEPLOYMENT_RESOURCE.DEPLOYMENT_ID_ = ACT_CMMN_DEPLOYMENT.ID_` |
| `ACT_FK_CASE_DEF_DPLY` | [`ACT_CMMN_CASEDEF`](../BPM_ENGINE/ACT_CMMN_CASEDEF.md) | `DEPLOYMENT_ID_` | `ACT_CMMN_CASEDEF.DEPLOYMENT_ID_ = ACT_CMMN_DEPLOYMENT.ID_` |

## Starter query

```sql
SELECT t.ID_,
       t.NAME_,
       t.CATEGORY_,
       t.KEY_,
       t.DEPLOY_TIME_,
       t.PARENT_DEPLOYMENT_ID_,
       t.TENANT_ID_
FROM   DB2ADMIN.ACT_CMMN_DEPLOYMENT t
FETCH FIRST 100 ROWS ONLY;
```
