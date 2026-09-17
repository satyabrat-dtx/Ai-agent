# DB2ADMIN.SCDC_APP_GLOBALSETTINGS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `no_primary_key`
- **Columns**: 1
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188265

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `GS_GLOBALSETTINGS` | VARCHAR(2000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.GS_GLOBALSETTINGS
FROM   DB2ADMIN.SCDC_APP_GLOBALSETTINGS t
FETCH FIRST 100 ROWS ONLY;
```
