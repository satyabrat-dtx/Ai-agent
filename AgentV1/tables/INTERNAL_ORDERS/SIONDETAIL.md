# DB2ADMIN.SIONDETAIL

- **Module**: `INTERNAL_ORDERS` (low confidence — FK neighbourhood: 1 of 1 related tables are INTERNAL_ORDERS)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `SIONCOMPANYCODE`, `SIONCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 123551

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SIONCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `ITEMDESCRIPTION` | VARCHAR(370) |  |  |  |  |
| 16 | `ITEMTECHCHARACTERISTICS` | VARCHAR(200) |  |  |  |  |
| 17 | `COMPOSITIONDETAILCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `COMPOSITIONDETAILCODE` | CHAR(10) |  | FK | foreign_key |  |
| 19 | `ITCCODE` | CHAR(20) |  | FK | foreign_key |  |
| 20 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 22 | `STEP` | CHAR(1) |  |  |  |  |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPOSITIONCOMPONENT_COMPOSITIONDETAIL` | `COMPOSITIONDETAILCOMPANYCODE`, `COMPOSITIONDETAILCODE` | [`COMPOSITIONCOMPONENT`](../INTERNAL_ORDERS/COMPOSITIONCOMPONENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SIONDETAIL.COMPOSITIONDETAILCOMPANYCODE = COMPOSITIONCOMPONENT.COMPANYCODE AND SIONDETAIL.COMPOSITIONDETAILCODE = COMPOSITIONCOMPONENT.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SIONDETAIL.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND SIONDETAIL.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `SION_LINE` | `SIONCOMPANYCODE`, `SIONCODE` | [`SION`](../SALES/SION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SIONDETAIL.SIONCOMPANYCODE = SION.COMPANYCODE AND SIONDETAIL.SIONCODE = SION.CODE` |
| `TARIFF_ITC` | `ITCCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `SIONDETAIL.ITCCODE = TARIFF.CODE` |
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `SIONDETAIL.UOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SIONDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SIONCOMPANYCODE,
       t.SIONCODE,
       t.LINENO,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.SIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
