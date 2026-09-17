# DB2ADMIN.SCDA_PRODUCTION_ORDER_GRP

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `PG_IDENTIFIER`, `PG_PRODUCTION_ORDER`, `PG_GROUP_STEP_NUM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185499

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PG_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PG_PRODUCTION_ORDER` | VARCHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `PG_GROUP_STEP_NUM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `PG_FORCED_GROUP_NUM` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PG_IDENTIFIER,
       t.PG_PRODUCTION_ORDER,
       t.PG_GROUP_STEP_NUM,
       t.PG_FORCED_GROUP_NUM
FROM   DB2ADMIN.SCDA_PRODUCTION_ORDER_GRP t
FETCH FIRST 100 ROWS ONLY;
```
