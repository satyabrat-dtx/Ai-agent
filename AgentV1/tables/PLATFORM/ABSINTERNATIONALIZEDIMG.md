# DB2ADMIN.ABSINTERNATIONALIZEDIMG

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `child_of_implicit_parent`
- **Columns**: 5
- **Primary key**: `FATHERID`, `LANGUAGECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 13364

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL | PK | primary_key implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `LANGUAGECODE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `IMAGEPATH` | VARCHAR(1000) |  |  |  |  |
| 3 | `IMAGENAME` | VARCHAR(250) | NOT NULL |  |  |  |
| 4 | `LABELUI` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ABSINTERNATIONALIZEDIMG.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FATHERID,
       t.LANGUAGECODE,
       t.IMAGEPATH,
       t.IMAGENAME,
       t.LABELUI
FROM   DB2ADMIN.ABSINTERNATIONALIZEDIMG t
FETCH FIRST 100 ROWS ONLY;
```
