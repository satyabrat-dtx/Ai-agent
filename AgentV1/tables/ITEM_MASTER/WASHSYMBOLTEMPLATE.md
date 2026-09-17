# DB2ADMIN.WASHSYMBOLTEMPLATE

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `CODE`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 211365

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `WASHSYMBOLTEMPLATE_WASHSYMBOLTEMPLATE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `WASHSYMBOLTEMPLATECODE` | `ITEMTYPE.WASHSYMBOLTEMPLATECODE = WASHSYMBOLTEMPLATE.CODE` |
| `WASHSYMBOLTEMPLATE_TEMPLATE` | [`WASHSYMBOLLABEL`](../ITEM_MASTER/WASHSYMBOLLABEL.md) | `TEMPLATECODE` | `WASHSYMBOLLABEL.TEMPLATECODE = WASHSYMBOLTEMPLATE.CODE` |
| `WASHSYMBOLTEMPLATE_CATEGORY` | [`WASHSYMBOLTEMPLATECATEGORY`](../ITEM_MASTER/WASHSYMBOLTEMPLATECATEGORY.md) | `WASHSYMBOLTEMPLATECODE` | `WASHSYMBOLTEMPLATECATEGORY.WASHSYMBOLTEMPLATECODE = WASHSYMBOLTEMPLATE.CODE` |

## Indexes

- `WASHSYMBOLTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WASHSYMBOLTEMPLATE t
FETCH FIRST 100 ROWS ONLY;
```
