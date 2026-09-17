# DB2ADMIN.INTERNALPRICELISTLINE

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `business_data`
- **Columns**: 63
- **Primary key**: `INTPRCLISTDLTINTPRCLISTCMYCOD`, `INTPRCLISTDLTINTPRICELISTCODE`, `INTPRCLISTDETAILCOSTGROUPCODE`, `INTPRCLISTDETAILITEMTYPECODE`, `INTPRICELISTDETAILPLANTCODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `VALIDFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 32504

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTPRCLISTDLTINTPRCLISTCMYCOD` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `INTPRCLISTDLTINTPRICELISTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INTPRCLISTDETAILCOSTGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `INTPRCLISTDETAILITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `INTPRICELISTDETAILPLANTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 15 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `VALIDFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 17 | `PRICE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 18 | `PRICEUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `VALIDTODATE` | DATE |  |  |  |  |
| 20 | `QUANTITYLIMITFROM` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 21 | `QUANTITYLIMITTO` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 22 | `SELECTPRIMORSEC` | INTEGER | NOT NULL |  |  |  |
| 23 | `PRICECHANGEOVER` | DECIMAL(5,2) |  |  |  |  |
| 24 | `EVERYQTYADD` | DECIMAL(9,0) |  |  |  |  |
| 25 | `PRICECHANGEUNDER` | DECIMAL(5,2) |  |  |  |  |
| 26 | `EVERYQTYSUB` | DECIMAL(9,0) |  |  |  |  |
| 27 | `LOWESTPRICE` | DECIMAL(18,5) |  |  |  |  |
| 28 | `PRICE1` | DECIMAL(18,5) |  |  |  |  |
| 29 | `QUANTITYLIMIT1FROM` | DECIMAL(15,5) |  |  |  |  |
| 30 | `QUANTITYLIMIT1TO` | DECIMAL(15,5) |  |  |  |  |
| 31 | `PRICE2` | DECIMAL(18,5) |  |  |  |  |
| 32 | `QUANTITYLIMIT2FROM` | DECIMAL(9,0) |  |  |  |  |
| 33 | `QUANTITYLIMIT2TO` | DECIMAL(15,5) |  |  |  |  |
| 34 | `PRICE3` | DECIMAL(18,5) |  |  |  |  |
| 35 | `QUANTITYLIMIT3FROM` | DECIMAL(9,0) |  |  |  |  |
| 36 | `QUANTITYLIMIT3TO` | DECIMAL(15,5) |  |  |  |  |
| 37 | `PRICE4` | DECIMAL(18,5) |  |  |  |  |
| 38 | `QUANTITYLIMIT4FROM` | DECIMAL(9,0) |  |  |  |  |
| 39 | `QUANTITYLIMIT4TO` | DECIMAL(15,5) |  |  |  |  |
| 40 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 41 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 42 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 43 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 44 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 45 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 46 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 47 | `PERCENTCATEGORY1` | DECIMAL(6,3) |  |  |  |  |
| 48 | `PERCENTCATEGORY2` | DECIMAL(6,3) |  |  |  |  |
| 49 | `PERCENTCATEGORY3` | DECIMAL(6,3) |  |  |  |  |
| 50 | `PERCENTCATEGORY4` | DECIMAL(6,3) |  |  |  |  |
| 51 | `PERCENTCATEGORY5` | DECIMAL(6,3) |  |  |  |  |
| 52 | `PERCENTCATEGORY6` | DECIMAL(6,3) |  |  |  |  |
| 53 | `PERCENTCATEGORY7` | DECIMAL(6,3) |  |  |  |  |
| 54 | `PERCENTCATEGORY8` | DECIMAL(6,3) |  |  |  |  |
| 55 | `PERCENTCATEGORY9` | DECIMAL(6,3) |  |  |  |  |
| 56 | `PERCENTCATEGORY10` | DECIMAL(6,3) |  |  |  |  |
| 57 | `PERCENTCATEGORY11` | DECIMAL(6,3) |  |  |  |  |
| 58 | `PERCENTCATEGORY12` | DECIMAL(6,3) |  |  |  |  |
| 59 | `PERCENTCATEGORY0` | DECIMAL(6,3) |  |  |  |  |
| 60 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 61 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 62 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `INTERNALPRICELISTLINE.CURRENCYCODE = CURRENCY.CODE` |
| `INTERNALPRICELISTDETAIL_LINE` | `INTPRCLISTDLTINTPRCLISTCMYCOD`, `INTPRCLISTDLTINTPRICELISTCODE`, `INTPRCLISTDETAILCOSTGROUPCODE`, `INTPRCLISTDETAILITEMTYPECODE`, `INTPRICELISTDETAILPLANTCODE` | [`INTERNALPRICELISTDETAIL`](../INTERNAL_ORDERS/INTERNALPRICELISTDETAIL.md) | `INTERNALPRICELISTCOMPANYCODE`, `INTERNALPRICELISTCODE`, `COSTGROUPCODE`, `ITEMTYPECODE`, `PLANTCODE` | RESTRICT | `INTERNALPRICELISTLINE.INTPRCLISTDLTINTPRCLISTCMYCOD = INTERNALPRICELISTDETAIL.INTERNALPRICELISTCOMPANYCODE AND INTERNALPRICELISTLINE.INTPRCLISTDLTINTPRICELISTCODE = INTERNALPRICELISTDETAIL.INTERNALPRICELISTCODE AND INTERNALPRICELISTLINE.INTPRCLISTDETAILCOSTGROUPCODE = INTERNALPRICELISTDETAIL.COSTGROUPCODE AND INTERNALPRICELISTLINE.INTPRCLISTDETAILITEMTYPECODE = INTERNALPRICELISTDETAIL.ITEMTYPECODE AND INTERNALPRICELISTLINE.INTPRICELISTDETAILPLANTCODE = INTERNALPRICELISTDETAIL.PLANTCODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALPRICELISTLINE.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND INTERNALPRICELISTLINE.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `LOGREASON_LOGREASON` | `INTPRCLISTDLTINTPRCLISTCMYCOD`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALPRICELISTLINE.INTPRCLISTDLTINTPRCLISTCMYCOD = LOGREASON.COMPANYCODE AND INTERNALPRICELISTLINE.LOGREASONCODE = LOGREASON.CODE` |
| `UNITOFMEASURE_PRICEUOM` | `PRICEUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `INTERNALPRICELISTLINE.PRICEUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INTERNALPRICELISTLINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INTPRCLISTDLTINTPRCLISTCMYCOD,
       t.INTPRCLISTDLTINTPRICELISTCODE,
       t.INTPRCLISTDETAILCOSTGROUPCODE,
       t.INTPRCLISTDETAILITEMTYPECODE,
       t.INTPRICELISTDETAILPLANTCODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.INTERNALPRICELISTLINE t
FETCH FIRST 100 ROWS ONLY;
```
