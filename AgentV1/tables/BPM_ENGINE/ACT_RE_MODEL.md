# DB2ADMIN.ACT_RE_MODEL

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 13
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 232961

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 3 | `KEY_` | VARCHAR(255) |  |  |  |  |
| 4 | `CATEGORY_` | VARCHAR(255) |  |  |  |  |
| 5 | `CREATE_TIME_` | TIMESTAMP |  |  |  |  |
| 6 | `LAST_UPDATE_TIME_` | TIMESTAMP |  |  |  |  |
| 7 | `VERSION_` | INTEGER |  |  |  |  |
| 8 | `META_INFO_` | VARCHAR(4000) |  |  |  |  |
| 9 | `DEPLOYMENT_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 10 | `EDITOR_SOURCE_VALUE_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 11 | `EDITOR_SOURCE_EXTRA_VALUE_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 12 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_MODEL_DEPLOYMENT` | `DEPLOYMENT_ID_` | [`ACT_RE_DEPLOYMENT`](../BPM_ENGINE/ACT_RE_DEPLOYMENT.md) | `ID_` | NO ACTION | `ACT_RE_MODEL.DEPLOYMENT_ID_ = ACT_RE_DEPLOYMENT.ID_` |
| `ACT_FK_MODEL_SOURCE` | `EDITOR_SOURCE_VALUE_ID_` | [`ACT_GE_BYTEARRAY`](../BPM_ENGINE/ACT_GE_BYTEARRAY.md) | `ID_` | NO ACTION | `ACT_RE_MODEL.EDITOR_SOURCE_VALUE_ID_ = ACT_GE_BYTEARRAY.ID_` |
| `ACT_FK_MODEL_SOURCE_EXTRA` | `EDITOR_SOURCE_EXTRA_VALUE_ID_` | [`ACT_GE_BYTEARRAY`](../BPM_ENGINE/ACT_GE_BYTEARRAY.md) | `ID_` | NO ACTION | `ACT_RE_MODEL.EDITOR_SOURCE_EXTRA_VALUE_ID_ = ACT_GE_BYTEARRAY.ID_` |

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.NAME_,
       t.KEY_,
       t.CATEGORY_,
       t.CREATE_TIME_,
       t.LAST_UPDATE_TIME_,
       t.VERSION_,
       t.META_INFO_,
       t.DEPLOYMENT_ID_,
       t.EDITOR_SOURCE_VALUE_ID_,
       t.EDITOR_SOURCE_EXTRA_VALUE_ID_
FROM   DB2ADMIN.ACT_RE_MODEL t
FETCH FIRST 100 ROWS ONLY;
```
