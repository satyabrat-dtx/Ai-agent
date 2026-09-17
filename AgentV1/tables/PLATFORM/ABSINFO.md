# DB2ADMIN.ABSINFO

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `child_of_implicit_parent`
- **Columns**: 3
- **Primary key**: `FATHERID`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 29048

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL | PK | primary_key implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `INFODEFINITIONSTREAM` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ABSINFO.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FATHERID,
       t.SEQUENCE,
       t.INFODEFINITIONSTREAM
FROM   DB2ADMIN.ABSINFO t
FETCH FIRST 100 ROWS ONLY;
```
