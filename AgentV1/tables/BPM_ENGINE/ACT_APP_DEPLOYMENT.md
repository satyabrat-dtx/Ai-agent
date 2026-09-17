# DB2ADMIN.ACT_APP_DEPLOYMENT

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 6
- **Primary key**: `ID_`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235017

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 2 | `CATEGORY_` | VARCHAR(255) |  |  |  |  |
| 3 | `KEY_` | VARCHAR(255) |  |  |  |  |
| 4 | `DEPLOY_TIME_` | TIMESTAMP |  |  |  |  |
| 5 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACT_FK_APP_RSRC_DPL` | [`ACT_APP_DEPLOYMENT_RESOURCE`](../BPM_ENGINE/ACT_APP_DEPLOYMENT_RESOURCE.md) | `DEPLOYMENT_ID_` | `ACT_APP_DEPLOYMENT_RESOURCE.DEPLOYMENT_ID_ = ACT_APP_DEPLOYMENT.ID_` |
| `ACT_FK_APP_DEF_DPLY` | [`ACT_APP_APPDEF`](../BPM_ENGINE/ACT_APP_APPDEF.md) | `DEPLOYMENT_ID_` | `ACT_APP_APPDEF.DEPLOYMENT_ID_ = ACT_APP_DEPLOYMENT.ID_` |

## Starter query

```sql
SELECT t.ID_,
       t.NAME_,
       t.CATEGORY_,
       t.KEY_,
       t.DEPLOY_TIME_,
       t.TENANT_ID_
FROM   DB2ADMIN.ACT_APP_DEPLOYMENT t
FETCH FIRST 100 ROWS ONLY;
```
