# DB2ADMIN.FLW_RU_BATCH

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `ID_`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 232860

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `TYPE_` | VARCHAR(64) | NOT NULL |  |  |  |
| 3 | `SEARCH_KEY_` | VARCHAR(255) |  |  |  |  |
| 4 | `SEARCH_KEY2_` | VARCHAR(255) |  |  |  |  |
| 5 | `CREATE_TIME_` | TIMESTAMP | NOT NULL |  |  |  |
| 6 | `COMPLETE_TIME_` | TIMESTAMP |  |  |  |  |
| 7 | `STATUS_` | VARCHAR(255) |  |  |  |  |
| 8 | `BATCH_DOC_ID_` | VARCHAR(64) |  |  |  |  |
| 9 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FLW_FK_BATCH_PART_PARENT` | [`FLW_RU_BATCH_PART`](../OTHER/FLW_RU_BATCH_PART.md) | `BATCH_ID_` | `FLW_RU_BATCH_PART.BATCH_ID_ = FLW_RU_BATCH.ID_` |

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.TYPE_,
       t.SEARCH_KEY_,
       t.SEARCH_KEY2_,
       t.CREATE_TIME_,
       t.COMPLETE_TIME_,
       t.STATUS_,
       t.BATCH_DOC_ID_,
       t.TENANT_ID_
FROM   DB2ADMIN.FLW_RU_BATCH t
FETCH FIRST 100 ROWS ONLY;
```
