# DB2ADMIN.SCDA_NOW_RELATED_TABLE_COLUMNS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `no_primary_key`
- **Columns**: 2
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189712

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RELATEDCLASSENTITYNAME` | VARCHAR(50) |  |  |  |  |
| 1 | `COLUMN_NAME` | VARCHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.RELATEDCLASSENTITYNAME,
       t.COLUMN_NAME
FROM   DB2ADMIN.SCDA_NOW_RELATED_TABLE_COLUMNS t
FETCH FIRST 100 ROWS ONLY;
```
