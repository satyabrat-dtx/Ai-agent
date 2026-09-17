# DB2ADMIN.ADVSION

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `ADVANCELICENSECOMPANYCODE`, `ADVANCELICENSECODE`, `SIONCODE`
- **FK degree**: referenced by 1 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 134620

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ADVANCELICENSECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ADVANCELICENSECODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SIONCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `ITEMDESCRIPTION` | VARCHAR(370) |  |  |  |  |
| 19 | `ITEMTECHCHARACTERISTICS` | VARCHAR(200) |  |  |  |  |
| 20 | `ITCCODE` | CHAR(20) |  | FK | foreign_key |  |
| 21 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 23 | `FOBFORVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 24 | `FOBFORVALUEFC` | DECIMAL(18,5) |  |  |  |  |
| 25 | `CURRENCYCCCODE` | CHAR(4) |  | FK | foreign_key |  |
| 26 | `CURRENCYFCCODE` | CHAR(4) |  | FK | foreign_key |  |
| 27 | `UTILIZATIONAMT` | DECIMAL(18,5) |  |  |  |  |
| 28 | `UTILIZATIONQTY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `STEP` | CHAR(1) |  |  |  |  |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADVANCELICENSE_LINE` | `ADVANCELICENSECOMPANYCODE`, `ADVANCELICENSECODE` | [`ADVANCELICENSE`](../SALES/ADVANCELICENSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ADVSION.ADVANCELICENSECOMPANYCODE = ADVANCELICENSE.COMPANYCODE AND ADVSION.ADVANCELICENSECODE = ADVANCELICENSE.CODE` |
| `CURRENCY_CURRENCYCC` | `CURRENCYCCCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `ADVSION.CURRENCYCCCODE = CURRENCY.CODE` |
| `CURRENCY_CURRENCYFC` | `CURRENCYFCCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `ADVSION.CURRENCYFCCODE = CURRENCY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ADVSION.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ADVSION.ITEMTYPECODE = ITEMTYPE.CODE` |
| `SION_SION` | `ADVANCELICENSECOMPANYCODE`, `SIONCODE` | [`SION`](../SALES/SION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ADVSION.ADVANCELICENSECOMPANYCODE = SION.COMPANYCODE AND ADVSION.SIONCODE = SION.CODE` |
| `TARIFF_ITC` | `ITCCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `ADVSION.ITCCODE = TARIFF.CODE` |
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `ADVSION.UOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ADVSION_LINE` | [`ADVSIONDETAIL`](../OTHER/ADVSIONDETAIL.md) | `ADVSIONADVANCELICENSECMYCODE`, `ADVSIONADVANCELICENSECODE`, `ADVSIONSIONCODE` | `ADVSIONDETAIL.ADVSIONADVANCELICENSECMYCODE = ADVSION.ADVANCELICENSECOMPANYCODE AND ADVSIONDETAIL.ADVSIONADVANCELICENSECODE = ADVSION.ADVANCELICENSECODE AND ADVSIONDETAIL.ADVSIONSIONCODE = ADVSION.SIONCODE` |

## Indexes

- `ADVSIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ADVANCELICENSECOMPANYCODE,
       t.ADVANCELICENSECODE,
       t.SIONCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.ADVSION t
FETCH FIRST 100 ROWS ONLY;
```
