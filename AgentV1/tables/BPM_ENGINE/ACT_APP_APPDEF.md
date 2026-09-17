# DB2ADMIN.ACT_APP_APPDEF

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 10
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235075

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
| 9 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_APP_DEF_DPLY` | `DEPLOYMENT_ID_` | [`ACT_APP_DEPLOYMENT`](../BPM_ENGINE/ACT_APP_DEPLOYMENT.md) | `ID_` | NO ACTION | `ACT_APP_APPDEF.DEPLOYMENT_ID_ = ACT_APP_DEPLOYMENT.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_APP_DEF_DPLY` (DEPLOYMENT_ID_)
- UNIQUE `ACT_IDX_APP_DEF_UNIQ` (KEY_, VERSION_, TENANT_ID_)

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
       t.TENANT_ID_
FROM   DB2ADMIN.ACT_APP_APPDEF t
FETCH FIRST 100 ROWS ONLY;
```
