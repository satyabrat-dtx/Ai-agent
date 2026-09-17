# DB2ADMIN.NOTE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `child_of_implicit_parent`
- **Columns**: 4
- **Primary key**: `FATHERID`, `LANGUAGECODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 45610

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL | PK | primary_key implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `LANGUAGECODE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `NOTE` | LONG VARCHAR |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `NOTE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FATHERID,
       t.LANGUAGECODE,
       t.CODE,
       t.NOTE
FROM   DB2ADMIN.NOTE t
FETCH FIRST 100 ROWS ONLY;
```
