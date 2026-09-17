# DB2ADMIN.ACT_DE_MODEL

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 14
- **Primary key**: `ID`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235212

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `NAME` | VARCHAR(400) | NOT NULL |  |  |  |
| 2 | `MODEL_KEY` | VARCHAR(400) | NOT NULL |  |  |  |
| 3 | `DESCRIPTION` | VARCHAR(4000) |  |  | description |  |
| 4 | `MODEL_COMMENT` | VARCHAR(4000) |  |  |  |  |
| 5 | `CREATED` | TIMESTAMP |  |  |  |  |
| 6 | `CREATED_BY` | VARCHAR(255) |  |  |  |  |
| 7 | `LAST_UPDATED` | TIMESTAMP |  |  |  |  |
| 8 | `LAST_UPDATED_BY` | VARCHAR(255) |  |  |  |  |
| 9 | `VERSION` | INTEGER |  |  |  |  |
| 10 | `MODEL_EDITOR_JSON` | CLOB(1048576) |  |  |  |  |
| 11 | `THUMBNAIL` | BLOB(1048576) |  |  |  |  |
| 12 | `MODEL_TYPE` | INTEGER |  |  |  |  |
| 13 | `TENANT_ID` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FK_RELATION_CHILD` | [`ACT_DE_MODEL_RELATION`](../BPM_ENGINE/ACT_DE_MODEL_RELATION.md) | `MODEL_ID` | `ACT_DE_MODEL_RELATION.MODEL_ID = ACT_DE_MODEL.ID` |
| `FK_RELATION_PARENT` | [`ACT_DE_MODEL_RELATION`](../BPM_ENGINE/ACT_DE_MODEL_RELATION.md) | `PARENT_MODEL_ID` | `ACT_DE_MODEL_RELATION.PARENT_MODEL_ID = ACT_DE_MODEL.ID` |

## Indexes

- `IDX_PROC_MOD_CREATED` (CREATED_BY)

## Starter query

```sql
SELECT t.ID,
       t.NAME,
       t.MODEL_KEY,
       t.DESCRIPTION,
       t.MODEL_COMMENT,
       t.CREATED,
       t.CREATED_BY,
       t.LAST_UPDATED,
       t.LAST_UPDATED_BY,
       t.VERSION,
       t.MODEL_EDITOR_JSON,
       t.THUMBNAIL
FROM   DB2ADMIN.ACT_DE_MODEL t
FETCH FIRST 100 ROWS ONLY;
```
