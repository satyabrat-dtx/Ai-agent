# DB2ADMIN.WASHSYMBOLTEMPLATECATEGORY

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 2 of 2 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `WASHSYMBOLTEMPLATECODE`, `CATEGORYCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 213320

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WASHSYMBOLTEMPLATECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CATEGORYCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `WASHSYMBOLCATEGORY_CATEGORY` | `CATEGORYCODE` | [`WASHSYMBOLCATEGORY`](../ITEM_MASTER/WASHSYMBOLCATEGORY.md) | `CODE` | RESTRICT | `WASHSYMBOLTEMPLATECATEGORY.CATEGORYCODE = WASHSYMBOLCATEGORY.CODE` |
| `WASHSYMBOLTEMPLATE_CATEGORY` | `WASHSYMBOLTEMPLATECODE` | [`WASHSYMBOLTEMPLATE`](../ITEM_MASTER/WASHSYMBOLTEMPLATE.md) | `CODE` | RESTRICT | `WASHSYMBOLTEMPLATECATEGORY.WASHSYMBOLTEMPLATECODE = WASHSYMBOLTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WASHSYMBOLTEMPLATECATEGORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.WASHSYMBOLTEMPLATECODE,
       t.CATEGORYCODE,
       t.SEQUENCE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WASHSYMBOLTEMPLATECATEGORY t
FETCH FIRST 100 ROWS ONLY;
```
