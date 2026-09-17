# DB2ADMIN.WASHSYMBOLLABEL

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 2 of 2 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CODE`
- **FK degree**: referenced by 3 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 209088

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `TEMPLATECODE` | CHAR(10) |  | FK | foreign_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `WASHSYMBOLTEMPLATE_TEMPLATE` | `TEMPLATECODE` | [`WASHSYMBOLTEMPLATE`](../ITEM_MASTER/WASHSYMBOLTEMPLATE.md) | `CODE` | RESTRICT | `WASHSYMBOLLABEL.TEMPLATECODE = WASHSYMBOLTEMPLATE.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `WASHSYMBOLLABEL_WASHSYMBOLLABEL` | [`PRODUCTSPECIALIZEDSIZE`](../ITEM_MASTER/PRODUCTSPECIALIZEDSIZE.md) | `WASHSYMBOLLABELCODE` | `PRODUCTSPECIALIZEDSIZE.WASHSYMBOLLABELCODE = WASHSYMBOLLABEL.CODE` |
| `WASHSYMBOLLABEL_PRODWASHSYMBOLLABEL` | [`PRODUCT`](../ITEM_MASTER/PRODUCT.md) | `PRODWASHSYMBOLLABELCODE` | `PRODUCT.PRODWASHSYMBOLLABELCODE = WASHSYMBOLLABEL.CODE` |
| `WASHSYMBOLLABEL_DETAIL` | [`WASHSYMBOLLABELDETAIL`](../ITEM_MASTER/WASHSYMBOLLABELDETAIL.md) | `WASHSYMBOLLABELCODE` | `WASHSYMBOLLABELDETAIL.WASHSYMBOLLABELCODE = WASHSYMBOLLABEL.CODE` |

## Indexes

- `WASHSYMBOLLABELUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TEMPLATECODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WASHSYMBOLLABEL t
FETCH FIRST 100 ROWS ONLY;
```
