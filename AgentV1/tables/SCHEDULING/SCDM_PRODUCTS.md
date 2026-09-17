# DB2ADMIN.SCDM_PRODUCTS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `PAR_IDENTIFIER`, `PAR_TYPE_PROD`, `PAR_PRODUCT_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187805

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PAR_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PAR_TYPE_PROD` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `PAR_PRODUCT_CODE` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 3 | `PAR_PRODUT_NATURE` | CHAR(1) |  |  |  |  |
| 4 | `PAR_STR_CONS_POINT` | CHAR(1) |  |  |  |  |
| 5 | `PAR_END_CONS_POINT` | CHAR(1) |  |  |  |  |
| 6 | `PAR_INFO_AREA` | VARCHAR(120) |  |  |  |  |
| 7 | `PAR_STDPURCORPRODTIME` | SMALLINT |  |  |  |  |
| 8 | `PAR_IGNOR_MAT_CHECK` | CHAR(1) |  |  |  |  |
| 9 | `PAR_MATERIAL_TOLLERANCE_CODE` | VARCHAR(6) |  |  |  |  |
| 10 | `PAR_HOURSTODOWNFROMMACHINE` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PAR_IDENTIFIER,
       t.PAR_TYPE_PROD,
       t.PAR_PRODUCT_CODE,
       t.PAR_PRODUT_NATURE,
       t.PAR_STR_CONS_POINT,
       t.PAR_END_CONS_POINT,
       t.PAR_INFO_AREA,
       t.PAR_STDPURCORPRODTIME,
       t.PAR_IGNOR_MAT_CHECK,
       t.PAR_MATERIAL_TOLLERANCE_CODE,
       t.PAR_HOURSTODOWNFROMMACHINE
FROM   DB2ADMIN.SCDM_PRODUCTS t
FETCH FIRST 100 ROWS ONLY;
```
