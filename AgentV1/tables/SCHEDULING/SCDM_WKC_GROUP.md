# DB2ADMIN.SCDM_WKC_GROUP

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `WG_IDENTIFIER`, `WG_WK_CNTER_GROUP`, `WG_PLANT_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187218

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WG_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WG_WK_CNTER_GROUP` | VARCHAR(4) | NOT NULL | PK | primary_key |  |
| 2 | `WG_PLANT_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `WG_MAIN_WC` | VARCHAR(8) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.WG_IDENTIFIER,
       t.WG_WK_CNTER_GROUP,
       t.WG_PLANT_CODE,
       t.WG_MAIN_WC
FROM   DB2ADMIN.SCDM_WKC_GROUP t
FETCH FIRST 100 ROWS ONLY;
```
