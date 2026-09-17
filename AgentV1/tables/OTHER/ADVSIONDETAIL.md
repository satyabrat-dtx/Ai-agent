# DB2ADMIN.ADVSIONDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `ADVSIONADVANCELICENSECMYCODE`, `ADVSIONADVANCELICENSECODE`, `ADVSIONSIONCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 134682

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ADVSIONADVANCELICENSECMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ADVSIONADVANCELICENSECODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ADVSIONSIONCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `ITEMDESCRIPTION` | VARCHAR(370) |  |  |  |  |
| 17 | `ITEMTECHCHARACTERISTICS` | VARCHAR(200) |  |  |  |  |
| 18 | `COMPOSITIONDETAILCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `COMPOSITIONDETAILCODE` | CHAR(10) |  | FK | foreign_key |  |
| 20 | `IMPORTENTITLEMENT` | DECIMAL(15,5) |  |  |  |  |
| 21 | `ITCCODE` | CHAR(20) |  | FK | foreign_key |  |
| 22 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `ORIGINALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `UTILIZEDQTY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 26 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 27 | `UTILIZEDVALUE` | DECIMAL(15,5) |  |  |  |  |
| 28 | `FOBFORVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 29 | `FOBFORVALUEFC` | DECIMAL(18,5) |  |  |  |  |
| 30 | `CURRENCYCCCODE` | CHAR(4) |  | FK | foreign_key |  |
| 31 | `CURRENCYFCCODE` | CHAR(4) |  | FK | foreign_key |  |
| 32 | `STEP` | CHAR(1) |  |  |  |  |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADVSION_LINE` | `ADVSIONADVANCELICENSECMYCODE`, `ADVSIONADVANCELICENSECODE`, `ADVSIONSIONCODE` | [`ADVSION`](../SALES/ADVSION.md) | `ADVANCELICENSECOMPANYCODE`, `ADVANCELICENSECODE`, `SIONCODE` | RESTRICT | `ADVSIONDETAIL.ADVSIONADVANCELICENSECMYCODE = ADVSION.ADVANCELICENSECOMPANYCODE AND ADVSIONDETAIL.ADVSIONADVANCELICENSECODE = ADVSION.ADVANCELICENSECODE AND ADVSIONDETAIL.ADVSIONSIONCODE = ADVSION.SIONCODE` |
| `COMPOSITIONCOMPONENT_COMPOSITIONDETAIL` | `COMPOSITIONDETAILCOMPANYCODE`, `COMPOSITIONDETAILCODE` | [`COMPOSITIONCOMPONENT`](../INTERNAL_ORDERS/COMPOSITIONCOMPONENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ADVSIONDETAIL.COMPOSITIONDETAILCOMPANYCODE = COMPOSITIONCOMPONENT.COMPANYCODE AND ADVSIONDETAIL.COMPOSITIONDETAILCODE = COMPOSITIONCOMPONENT.CODE` |
| `CURRENCY_CURRENCYCC` | `CURRENCYCCCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `ADVSIONDETAIL.CURRENCYCCCODE = CURRENCY.CODE` |
| `CURRENCY_CURRENCYFC` | `CURRENCYFCCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `ADVSIONDETAIL.CURRENCYFCCODE = CURRENCY.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ADVSIONDETAIL.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND ADVSIONDETAIL.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `TARIFF_ITC` | `ITCCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `ADVSIONDETAIL.ITCCODE = TARIFF.CODE` |
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `ADVSIONDETAIL.UOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADVSIONDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ADVSIONADVANCELICENSECMYCODE,
       t.ADVSIONADVANCELICENSECODE,
       t.ADVSIONSIONCODE,
       t.LINENO,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.ADVSIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
