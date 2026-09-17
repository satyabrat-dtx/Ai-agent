# DB2ADMIN.ACT_FO_FORM_DEFINITION

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 9
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234199

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 2 | `VERSION_` | INTEGER |  |  |  |  |
| 3 | `KEY_` | VARCHAR(255) |  |  |  |  |
| 4 | `CATEGORY_` | VARCHAR(255) |  |  |  |  |
| 5 | `DEPLOYMENT_ID_` | VARCHAR(255) |  |  |  |  |
| 6 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 7 | `RESOURCE_NAME_` | VARCHAR(255) |  |  |  |  |
| 8 | `DESCRIPTION_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- UNIQUE `ACT_IDX_FORM_DEF_UNIQ` (KEY_, VERSION_, TENANT_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.NAME_,
       t.VERSION_,
       t.KEY_,
       t.CATEGORY_,
       t.DEPLOYMENT_ID_,
       t.TENANT_ID_,
       t.RESOURCE_NAME_,
       t.DESCRIPTION_
FROM   DB2ADMIN.ACT_FO_FORM_DEFINITION t
FETCH FIRST 100 ROWS ONLY;
```
