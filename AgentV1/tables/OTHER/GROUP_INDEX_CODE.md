# DB2ADMIN.GROUP_INDEX_CODE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 2
- **Primary key**: `GI_GROUP_INDEX`, `GI_GROUP_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185558

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `GI_GROUP_INDEX` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `GI_GROUP_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.GI_GROUP_INDEX,
       t.GI_GROUP_CODE
FROM   DB2ADMIN.GROUP_INDEX_CODE t
FETCH FIRST 100 ROWS ONLY;
```
