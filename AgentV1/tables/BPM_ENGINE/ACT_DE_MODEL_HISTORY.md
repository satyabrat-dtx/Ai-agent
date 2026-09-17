# DB2ADMIN.ACT_DE_MODEL_HISTORY

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 15
- **Primary key**: `ID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235255

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
| 9 | `REMOVAL_DATE` | TIMESTAMP |  |  |  |  |
| 10 | `VERSION` | INTEGER |  |  |  |  |
| 11 | `MODEL_EDITOR_JSON` | CLOB(1048576) |  |  |  |  |
| 12 | `MODEL_ID` | VARCHAR(255) | NOT NULL |  |  |  |
| 13 | `MODEL_TYPE` | INTEGER |  |  |  |  |
| 14 | `TENANT_ID` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `IDX_PROC_MOD_HISTORY_PROC` (MODEL_ID)

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
       t.REMOVAL_DATE,
       t.VERSION,
       t.MODEL_EDITOR_JSON
FROM   DB2ADMIN.ACT_DE_MODEL_HISTORY t
FETCH FIRST 100 ROWS ONLY;
```
