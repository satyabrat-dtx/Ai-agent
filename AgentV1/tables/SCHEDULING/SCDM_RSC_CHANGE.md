# DB2ADMIN.SCDM_RSC_CHANGE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `RG_IDENTIFIER`, `RG_RSC_CODE`, `RG_UPD_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187447

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RG_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `RG_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `RG_UPD_CODE` | INTEGER | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.RG_IDENTIFIER,
       t.RG_RSC_CODE,
       t.RG_UPD_CODE
FROM   DB2ADMIN.SCDM_RSC_CHANGE t
FETCH FIRST 100 ROWS ONLY;
```
