# DB2ADMIN.ABSLETTERTEMPLATELANGUAGE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `child_of_implicit_parent`, `translation`
- **Columns**: 4
- **Primary key**: `FATHERID`, `LANGUAGECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 8675

> Per-language text for a parent row addressed via FATHERID.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL | PK | primary_key implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `LANGUAGECODE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `MAILSUBJECT` | VARCHAR(100) |  |  |  |  |
| 3 | `MAILBODY` | LONG VARCHAR |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **ABSLETTERTEMPLATE**.`ABSUNIQUEID` (high confidence — name = 'ABSLETTERTEMPLATE' + known child suffix 'LANGUAGE')
  - JOIN predicate: `ABSLETTERTEMPLATELANGUAGE.FATHERID = ABSLETTERTEMPLATE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FATHERID,
       t.LANGUAGECODE,
       t.MAILSUBJECT,
       t.MAILBODY
FROM   DB2ADMIN.ABSLETTERTEMPLATELANGUAGE t
FETCH FIRST 100 ROWS ONLY;
```
