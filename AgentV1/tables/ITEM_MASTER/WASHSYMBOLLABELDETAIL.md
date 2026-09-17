# DB2ADMIN.WASHSYMBOLLABELDETAIL

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 2 of 2 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `WASHSYMBOLLABELCODE`, `WASHSYMBOLCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 212348

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WASHSYMBOLLABELCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `WASHSYMBOLCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `WASHSYMBOLLABEL_DETAIL` | `WASHSYMBOLLABELCODE` | [`WASHSYMBOLLABEL`](../ITEM_MASTER/WASHSYMBOLLABEL.md) | `CODE` | RESTRICT | `WASHSYMBOLLABELDETAIL.WASHSYMBOLLABELCODE = WASHSYMBOLLABEL.CODE` |
| `WASHSYMBOL_WASHSYMBOL` | `WASHSYMBOLCODE` | [`WASHSYMBOL`](../ITEM_MASTER/WASHSYMBOL.md) | `CODE` | RESTRICT | `WASHSYMBOLLABELDETAIL.WASHSYMBOLCODE = WASHSYMBOL.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WASHSYMBOLLABELDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.WASHSYMBOLLABELCODE,
       t.WASHSYMBOLCODE,
       t.SEQUENCE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WASHSYMBOLLABELDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
