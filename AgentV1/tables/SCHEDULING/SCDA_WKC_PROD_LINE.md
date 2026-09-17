# DB2ADMIN.SCDA_WKC_PROD_LINE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `PL_IDENTIFIER`, `PL_WKCNTER`, `PL_PROD_LINE`, `PL_DATE_BEGIN`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184380

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PL_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PL_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `PL_PROD_LINE` | VARCHAR(4) | NOT NULL | PK | primary_key |  |
| 3 | `PL_DATE_BEGIN` | TIMESTAMP | NOT NULL | PK | primary_key |  |
| 4 | `PL_DATE_END` | TIMESTAMP |  |  |  |  |
| 5 | `PL_RES_NUM_PLN` | DECIMAL(9,3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PL_IDENTIFIER,
       t.PL_WKCNTER,
       t.PL_PROD_LINE,
       t.PL_DATE_BEGIN,
       t.PL_DATE_END,
       t.PL_RES_NUM_PLN
FROM   DB2ADMIN.SCDA_WKC_PROD_LINE t
FETCH FIRST 100 ROWS ONLY;
```
