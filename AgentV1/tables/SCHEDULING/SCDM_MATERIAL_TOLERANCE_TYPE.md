# DB2ADMIN.SCDM_MATERIAL_TOLERANCE_TYPE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `MTT_IDENTIFIER`, `MTT_MATERIAL_TOLLERANCE_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185729

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MTT_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `MTT_MATERIAL_TOLLERANCE_CODE` | VARCHAR(6) | NOT NULL | PK | primary_key |  |
| 2 | `MTT_DESCR` | VARCHAR(30) |  |  |  |  |
| 3 | `MTT_TILLQTY1` | DECIMAL(11,2) |  |  |  |  |
| 4 | `MTT_TILLQTY1PERCENT` | SMALLINT |  |  |  |  |
| 5 | `MTT_TILLQTY2` | DECIMAL(11,2) |  |  |  |  |
| 6 | `MTT_TILLQTY2PERCENT` | SMALLINT |  |  |  |  |
| 7 | `MTT_TILLQTY3` | DECIMAL(11,2) |  |  |  |  |
| 8 | `MTT_TILLQTY3PERCENT` | SMALLINT |  |  |  |  |
| 9 | `MTT_TILLQTY4` | DECIMAL(11,2) |  |  |  |  |
| 10 | `MTT_TILLQTY4PERCENT` | SMALLINT |  |  |  |  |
| 11 | `MTT_TILLQTY5` | DECIMAL(11,2) |  |  |  |  |
| 12 | `MTT_TILLQTY5PERCENT` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.MTT_IDENTIFIER,
       t.MTT_MATERIAL_TOLLERANCE_CODE,
       t.MTT_DESCR,
       t.MTT_TILLQTY1,
       t.MTT_TILLQTY1PERCENT,
       t.MTT_TILLQTY2,
       t.MTT_TILLQTY2PERCENT,
       t.MTT_TILLQTY3,
       t.MTT_TILLQTY3PERCENT,
       t.MTT_TILLQTY4,
       t.MTT_TILLQTY4PERCENT,
       t.MTT_TILLQTY5
FROM   DB2ADMIN.SCDM_MATERIAL_TOLERANCE_TYPE t
FETCH FIRST 100 ROWS ONLY;
```
