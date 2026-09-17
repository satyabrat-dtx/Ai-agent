# DB2ADMIN.SCDA_GROUPBY_PROP_RULES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `GR_IDENTIFIER`, `GR_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 205792

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `GR_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `GR_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `GR_S_DESCR` | VARCHAR(28) |  |  |  |  |
| 3 | `GR_PROPERTYCODE1` | VARCHAR(5) |  |  |  |  |
| 4 | `GR_PROPERTYCODE2` | VARCHAR(5) |  |  |  |  |
| 5 | `GR_PROPERTYCODE3` | VARCHAR(5) |  |  |  |  |
| 6 | `GR_PROPERTYCODE4` | VARCHAR(5) |  |  |  |  |
| 7 | `GR_PROPERTYCODE5` | VARCHAR(5) |  |  |  |  |
| 8 | `GR_PROPERTYCODE6` | VARCHAR(5) |  |  |  |  |
| 9 | `GR_PROPERTYCODE7` | VARCHAR(5) |  |  |  |  |
| 10 | `GR_PROPERTYCODE8` | VARCHAR(5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.GR_IDENTIFIER,
       t.GR_CODE,
       t.GR_S_DESCR,
       t.GR_PROPERTYCODE1,
       t.GR_PROPERTYCODE2,
       t.GR_PROPERTYCODE3,
       t.GR_PROPERTYCODE4,
       t.GR_PROPERTYCODE5,
       t.GR_PROPERTYCODE6,
       t.GR_PROPERTYCODE7,
       t.GR_PROPERTYCODE8
FROM   DB2ADMIN.SCDA_GROUPBY_PROP_RULES t
FETCH FIRST 100 ROWS ONLY;
```
