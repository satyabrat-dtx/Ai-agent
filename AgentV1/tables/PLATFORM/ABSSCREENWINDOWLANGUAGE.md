# DB2ADMIN.ABSSCREENWINDOWLANGUAGE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `child_of_implicit_parent`, `translation`
- **Columns**: 3
- **Primary key**: `FATHERID`, `LANGUAGECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118095

> Per-language text for a parent row addressed via FATHERID.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL | PK | primary_key implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `LANGUAGECODE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `TITLE` | VARCHAR(100) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **ABSSCREENWINDOW**.`ABSUNIQUEID` (high confidence — name = 'ABSSCREENWINDOW' + known child suffix 'LANGUAGE')
  - JOIN predicate: `ABSSCREENWINDOWLANGUAGE.FATHERID = ABSSCREENWINDOW.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FATHERID,
       t.LANGUAGECODE,
       t.TITLE
FROM   DB2ADMIN.ABSSCREENWINDOWLANGUAGE t
FETCH FIRST 100 ROWS ONLY;
```
