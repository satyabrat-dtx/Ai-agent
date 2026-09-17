# DB2ADMIN.ABSCOUNTER

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 2
- **Primary key**: `COUNTERKEY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 22323

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COUNTERKEY` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COUNTERKEY,
       t.UNIQUEID
FROM   DB2ADMIN.ABSCOUNTER t
FETCH FIRST 100 ROWS ONLY;
```
