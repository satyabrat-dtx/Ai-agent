# DB2ADMIN.SCDA_MULTIPLIERCOMPANY

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `IDENTIFIER`, `ENVIRONMENT`, `COMPANY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183544

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `ENVIRONMENT` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `COMPANY` | VARCHAR(3) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.ENVIRONMENT,
       t.COMPANY
FROM   DB2ADMIN.SCDA_MULTIPLIERCOMPANY t
FETCH FIRST 100 ROWS ONLY;
```
