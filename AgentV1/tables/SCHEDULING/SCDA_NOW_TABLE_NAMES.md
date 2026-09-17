# DB2ADMIN.SCDA_NOW_TABLE_NAMES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 1
- **Primary key**: `TABLE_NAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184796

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TABLE_NAME` | VARCHAR(30) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.TABLE_NAME
FROM   DB2ADMIN.SCDA_NOW_TABLE_NAMES t
FETCH FIRST 100 ROWS ONLY;
```
