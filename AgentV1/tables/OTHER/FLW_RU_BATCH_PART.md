# DB2ADMIN.FLW_RU_BATCH_PART

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 232889

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `BATCH_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 3 | `TYPE_` | VARCHAR(64) | NOT NULL |  |  |  |
| 4 | `SCOPE_ID_` | VARCHAR(64) |  |  |  |  |
| 5 | `SUB_SCOPE_ID_` | VARCHAR(64) |  |  |  |  |
| 6 | `SCOPE_TYPE_` | VARCHAR(64) |  |  |  |  |
| 7 | `SEARCH_KEY_` | VARCHAR(255) |  |  |  |  |
| 8 | `SEARCH_KEY2_` | VARCHAR(255) |  |  |  |  |
| 9 | `CREATE_TIME_` | TIMESTAMP | NOT NULL |  |  |  |
| 10 | `COMPLETE_TIME_` | TIMESTAMP |  |  |  |  |
| 11 | `STATUS_` | VARCHAR(255) |  |  |  |  |
| 12 | `RESULT_DOC_ID_` | VARCHAR(64) |  |  |  |  |
| 13 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FLW_FK_BATCH_PART_PARENT` | `BATCH_ID_` | [`FLW_RU_BATCH`](../OTHER/FLW_RU_BATCH.md) | `ID_` | NO ACTION | `FLW_RU_BATCH_PART.BATCH_ID_ = FLW_RU_BATCH.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FLW_IDX_BATCH_PART` (BATCH_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.BATCH_ID_,
       t.TYPE_,
       t.SCOPE_ID_,
       t.SUB_SCOPE_ID_,
       t.SCOPE_TYPE_,
       t.SEARCH_KEY_,
       t.SEARCH_KEY2_,
       t.CREATE_TIME_,
       t.COMPLETE_TIME_,
       t.STATUS_
FROM   DB2ADMIN.FLW_RU_BATCH_PART t
FETCH FIRST 100 ROWS ONLY;
```
