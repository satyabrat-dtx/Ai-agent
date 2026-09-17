# DB2ADMIN.ADTRANSLATEDIMAGE

- **Module**: `PLATFORM` (medium confidence — table name starts with 'ADTRANSLATED')
- **Roles**: `child_of_implicit_parent`, `translation`
- **Columns**: 5
- **Primary key**: `FATHERID`, `LANGUAGECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 14238

> Per-language text for a parent row addressed via FATHERID.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL | PK | primary_key implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `LANGUAGECODE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `NAME` | CHAR(50) |  |  |  |  |
| 3 | `DIRECTORY` | CHAR(50) |  |  |  |  |
| 4 | `EXTENSION` | CHAR(5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ADTRANSLATEDIMAGE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FATHERID,
       t.LANGUAGECODE,
       t.NAME,
       t.DIRECTORY,
       t.EXTENSION
FROM   DB2ADMIN.ADTRANSLATEDIMAGE t
FETCH FIRST 100 ROWS ONLY;
```
