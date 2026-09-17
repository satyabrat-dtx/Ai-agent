# DB2ADMIN.SCDC_APP_SETTINGS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `AS_IDENTIFIER`, `AS_WKST_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188372

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AS_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `AS_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `AS_SETT` | VARCHAR(40) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.AS_IDENTIFIER,
       t.AS_WKST_CODE,
       t.AS_SETT
FROM   DB2ADMIN.SCDC_APP_SETTINGS t
FETCH FIRST 100 ROWS ONLY;
```
