# DB2ADMIN.SIZESALIAS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `child_of_implicit_parent`
- **Columns**: 4
- **Primary key**: `FATHERID`, `MARKETCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 11830

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL | PK | primary_key implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `CODE` | CHAR(40) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `MARKETCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `TOBEPRINTED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SIZES**.`ABSUNIQUEID` (high confidence — name = 'SIZES' + known child suffix 'ALIAS')
  - JOIN predicate: `SIZESALIAS.FATHERID = SIZES.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FATHERID,
       t.CODE,
       t.MARKETCODE,
       t.TOBEPRINTED
FROM   DB2ADMIN.SIZESALIAS t
FETCH FIRST 100 ROWS ONLY;
```
