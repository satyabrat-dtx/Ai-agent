# DB2ADMIN.ACT_CMMN_DEPLOYMENT_RESOURCE

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 5
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234496

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 2 | `DEPLOYMENT_ID_` | VARCHAR(255) |  | FK | foreign_key |  |
| 3 | `RESOURCE_BYTES_` | BLOB(1048576) |  |  |  |  |
| 4 | `GENERATED_` | BOOLEAN |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_CMMN_RSRC_DPL` | `DEPLOYMENT_ID_` | [`ACT_CMMN_DEPLOYMENT`](../BPM_ENGINE/ACT_CMMN_DEPLOYMENT.md) | `ID_` | NO ACTION | `ACT_CMMN_DEPLOYMENT_RESOURCE.DEPLOYMENT_ID_ = ACT_CMMN_DEPLOYMENT.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_CMMN_RSRC_DPL` (DEPLOYMENT_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.NAME_,
       t.DEPLOYMENT_ID_,
       t.RESOURCE_BYTES_,
       t.GENERATED_
FROM   DB2ADMIN.ACT_CMMN_DEPLOYMENT_RESOURCE t
FETCH FIRST 100 ROWS ONLY;
```
