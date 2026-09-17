# DB2ADMIN.WASHSYMBOLCATEGORY

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CODE`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 83050

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 5 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `WASHSYMBOLCATEGORY_WASHSYMBOLCATEGORY` | [`WASHSYMBOL`](../ITEM_MASTER/WASHSYMBOL.md) | `WASHSYMBOLCATEGORYCODE` | `WASHSYMBOL.WASHSYMBOLCATEGORYCODE = WASHSYMBOLCATEGORY.CODE` |
| `WASHSYMBOLCATEGORY_CATEGORY` | [`WASHSYMBOLTEMPLATECATEGORY`](../ITEM_MASTER/WASHSYMBOLTEMPLATECATEGORY.md) | `CATEGORYCODE` | `WASHSYMBOLTEMPLATECATEGORY.CATEGORYCODE = WASHSYMBOLCATEGORY.CODE` |

## Indexes

- `WASHSYMBOLCATEGORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ABSUNIQUEID,
       t.SEQUENCE
FROM   DB2ADMIN.WASHSYMBOLCATEGORY t
FETCH FIRST 100 ROWS ONLY;
```
