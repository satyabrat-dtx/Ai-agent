# DB2ADMIN.SCDA_NOW_TABLES_COLUMNS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `TABLE_NAME`, `COLUMN_NAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184816

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TABLE_NAME` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 1 | `COLUMN_NAME` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `TYPE_NAME` | VARCHAR(9) |  |  |  |  |
| 3 | `LENGTH` | SMALLINT |  |  |  |  |
| 4 | `SCALE` | SMALLINT |  |  |  |  |
| 5 | `RELATEDCLASSENTITYNAME` | VARCHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.TABLE_NAME,
       t.COLUMN_NAME,
       t.TYPE_NAME,
       t.LENGTH,
       t.SCALE,
       t.RELATEDCLASSENTITYNAME
FROM   DB2ADMIN.SCDA_NOW_TABLES_COLUMNS t
FETCH FIRST 100 ROWS ONLY;
```
