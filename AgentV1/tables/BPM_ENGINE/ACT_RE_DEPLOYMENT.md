# DB2ADMIN.ACT_RE_DEPLOYMENT

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 10
- **Primary key**: `ID_`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 232932

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 2 | `CATEGORY_` | VARCHAR(255) |  |  |  |  |
| 3 | `KEY_` | VARCHAR(255) |  |  |  |  |
| 4 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 5 | `DEPLOY_TIME_` | TIMESTAMP |  |  |  |  |
| 6 | `DERIVED_FROM_` | VARCHAR(64) |  |  |  |  |
| 7 | `DERIVED_FROM_ROOT_` | VARCHAR(64) |  |  |  |  |
| 8 | `PARENT_DEPLOYMENT_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `ENGINE_VERSION_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACT_FK_BYTEARR_DEPL` | [`ACT_GE_BYTEARRAY`](../BPM_ENGINE/ACT_GE_BYTEARRAY.md) | `DEPLOYMENT_ID_` | `ACT_GE_BYTEARRAY.DEPLOYMENT_ID_ = ACT_RE_DEPLOYMENT.ID_` |
| `ACT_FK_MODEL_DEPLOYMENT` | [`ACT_RE_MODEL`](../BPM_ENGINE/ACT_RE_MODEL.md) | `DEPLOYMENT_ID_` | `ACT_RE_MODEL.DEPLOYMENT_ID_ = ACT_RE_DEPLOYMENT.ID_` |

## Starter query

```sql
SELECT t.ID_,
       t.NAME_,
       t.CATEGORY_,
       t.KEY_,
       t.TENANT_ID_,
       t.DEPLOY_TIME_,
       t.DERIVED_FROM_,
       t.DERIVED_FROM_ROOT_,
       t.PARENT_DEPLOYMENT_ID_,
       t.ENGINE_VERSION_
FROM   DB2ADMIN.ACT_RE_DEPLOYMENT t
FETCH FIRST 100 ROWS ONLY;
```
