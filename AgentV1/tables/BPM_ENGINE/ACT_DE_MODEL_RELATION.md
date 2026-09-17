# DB2ADMIN.ACT_DE_MODEL_RELATION

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 4
- **Primary key**: `ID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235299

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `PARENT_MODEL_ID` | VARCHAR(255) |  | FK | foreign_key |  |
| 2 | `MODEL_ID` | VARCHAR(255) |  | FK | foreign_key |  |
| 3 | `RELATION_TYPE` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FK_RELATION_CHILD` | `MODEL_ID` | [`ACT_DE_MODEL`](../BPM_ENGINE/ACT_DE_MODEL.md) | `ID` | NO ACTION | `ACT_DE_MODEL_RELATION.MODEL_ID = ACT_DE_MODEL.ID` |
| `FK_RELATION_PARENT` | `PARENT_MODEL_ID` | [`ACT_DE_MODEL`](../BPM_ENGINE/ACT_DE_MODEL.md) | `ID` | NO ACTION | `ACT_DE_MODEL_RELATION.PARENT_MODEL_ID = ACT_DE_MODEL.ID` |

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID,
       t.PARENT_MODEL_ID,
       t.MODEL_ID,
       t.RELATION_TYPE
FROM   DB2ADMIN.ACT_DE_MODEL_RELATION t
FETCH FIRST 100 ROWS ONLY;
```
