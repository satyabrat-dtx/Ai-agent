# DB2ADMIN.ABSTILETEMPLATEDESCRIPTIONS

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `child_of_implicit_parent`
- **Columns**: 3
- **Primary key**: `FATHERID`, `LANGUAGECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 210206

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL | PK | primary_key implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `LANGUAGECODE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `DESCRIPTION` | CHAR(50) |  |  | description |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **ABSTILETEMPLATE**.`ABSUNIQUEID` (high confidence — name = 'ABSTILETEMPLATE' + known child suffix 'DESCRIPTIONS')
  - JOIN predicate: `ABSTILETEMPLATEDESCRIPTIONS.FATHERID = ABSTILETEMPLATE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FATHERID,
       t.LANGUAGECODE,
       t.DESCRIPTION
FROM   DB2ADMIN.ABSTILETEMPLATEDESCRIPTIONS t
FETCH FIRST 100 ROWS ONLY;
```
