# DB2ADMIN.SCDM_ASSIGNED_PROPERTIES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `PA_IDENTIFIER`, `PA_ASSIGNED_PROP`, `PA_PROPERTY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188189

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PA_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PA_ASSIGNED_PROP` | VARCHAR(20) | NOT NULL | PK | primary_key |  |
| 2 | `PA_PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PA_IDENTIFIER,
       t.PA_ASSIGNED_PROP,
       t.PA_PROPERTY
FROM   DB2ADMIN.SCDM_ASSIGNED_PROPERTIES t
FETCH FIRST 100 ROWS ONLY;
```
