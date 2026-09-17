# DB2ADMIN.ACT_CO_CONTENT_ITEM

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 17
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234352

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `NAME_` | VARCHAR(255) | NOT NULL |  |  |  |
| 2 | `MIME_TYPE_` | VARCHAR(255) |  |  |  |  |
| 3 | `TASK_ID_` | VARCHAR(255) |  |  |  |  |
| 4 | `PROC_INST_ID_` | VARCHAR(255) |  |  |  |  |
| 5 | `CONTENT_STORE_ID_` | VARCHAR(255) |  |  |  |  |
| 6 | `CONTENT_STORE_NAME_` | VARCHAR(255) |  |  |  |  |
| 7 | `FIELD_` | VARCHAR(400) |  |  |  |  |
| 8 | `CONTENT_AVAILABLE_` | BOOLEAN |  |  |  |  |
| 9 | `CREATED_` | TIMESTAMP |  |  |  |  |
| 10 | `CREATED_BY_` | VARCHAR(255) |  |  |  |  |
| 11 | `LAST_MODIFIED_` | TIMESTAMP |  |  |  |  |
| 12 | `LAST_MODIFIED_BY_` | VARCHAR(255) |  |  |  |  |
| 13 | `CONTENT_SIZE_` | BIGINT |  |  |  |  |
| 14 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 15 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 16 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `IDX_CONTITEM_TASKID` (TASK_ID_)
- `IDX_CONTITEM_PROCID` (PROC_INST_ID_)
- `IDX_CONTITEM_SCOPE` (SCOPE_ID_, SCOPE_TYPE_)

## Starter query

```sql
SELECT t.ID_,
       t.NAME_,
       t.MIME_TYPE_,
       t.TASK_ID_,
       t.PROC_INST_ID_,
       t.CONTENT_STORE_ID_,
       t.CONTENT_STORE_NAME_,
       t.FIELD_,
       t.CONTENT_AVAILABLE_,
       t.CREATED_,
       t.CREATED_BY_,
       t.LAST_MODIFIED_
FROM   DB2ADMIN.ACT_CO_CONTENT_ITEM t
FETCH FIRST 100 ROWS ONLY;
```
