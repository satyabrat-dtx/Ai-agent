# DB2ADMIN.SCDM_PROPERTY_AS_RGB

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 2
- **Primary key**: `PRGB_IDENTIFIER`, `PRGB_PROPERTY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188167

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PRGB_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PRGB_PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PRGB_IDENTIFIER,
       t.PRGB_PROPERTY
FROM   DB2ADMIN.SCDM_PROPERTY_AS_RGB t
FETCH FIRST 100 ROWS ONLY;
```
