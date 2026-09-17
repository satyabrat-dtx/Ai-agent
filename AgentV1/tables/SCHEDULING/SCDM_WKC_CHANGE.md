# DB2ADMIN.SCDM_WKC_CHANGE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `WG_IDENTIFIER`, `WG_WKCNTER`, `WG_UPD_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187423

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WG_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WG_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `WG_UPD_CODE` | INTEGER | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.WG_IDENTIFIER,
       t.WG_WKCNTER,
       t.WG_UPD_CODE
FROM   DB2ADMIN.SCDM_WKC_CHANGE t
FETCH FIRST 100 ROWS ONLY;
```
