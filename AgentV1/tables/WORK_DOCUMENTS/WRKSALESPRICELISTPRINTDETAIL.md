# DB2ADMIN.WRKSALESPRICELISTPRINTDETAIL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 76
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `LINENUMBER`, `LINEDETAILNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 16574

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `LINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `LINEDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ELEMENTTYPE` | CHAR(2) |  |  |  |  |
| 5 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 6 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `PRICETEMPLATEDEFINITIONTYPE` | CHAR(1) |  |  |  |  |
| 8 | `PRICETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 9 | `INITIALDATE` | DATE |  |  |  |  |
| 10 | `FINALDATE` | DATE |  |  |  |  |
| 11 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 12 | `TYPE` | CHAR(1) |  |  |  |  |
| 13 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 14 | `TEMPLATEORDERTYPE` | CHAR(1) |  |  |  |  |
| 15 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 16 | `DISCOUNTCATEGORYORDERTYPE` | CHAR(1) |  |  |  |  |
| 17 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 18 | `BREAKDOWNTYPE` | CHAR(2) |  |  |  |  |
| 19 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 20 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 21 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 22 | `LIMITTYPE` | CHAR(1) |  |  |  |  |
| 23 | `ORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 24 | `AREACODE` | CHAR(3) |  |  |  |  |
| 25 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 26 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 27 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 28 | `AGENTCODE` | CHAR(3) |  |  |  |  |
| 29 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 30 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 31 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 32 | `FNCORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 33 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 34 | `ORDERCATEGORYORDERTYPE` | CHAR(1) |  |  |  |  |
| 35 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 36 | `ORDPRNGRPSTDORDGRPTYPEORDTYPE` | CHAR(1) |  |  |  |  |
| 37 | `ORDPRNGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `ORDERPARTNERGROUPCODE` | CHAR(3) |  |  |  |  |
| 39 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 40 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 41 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 42 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 43 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 44 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 45 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 46 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 47 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 48 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 49 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 50 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 51 | `ORDITEMGRPSTDORDGRPTYPEORDTYPE` | CHAR(1) |  |  |  |  |
| 52 | `ORDITEMGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 53 | `ORDERITEMGROUPCODE` | CHAR(3) |  |  |  |  |
| 54 | `BREAKDOWNLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 55 | `DISCOUNTTYPE` | CHAR(2) |  |  |  |  |
| 56 | `EXCLUDEDINCMSCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 57 | `EXCLUDEDINCOMMISSIONRETRIEVING` | SMALLINT | NOT NULL |  |  |  |
| 58 | `DISCOUNTGROUPCODE` | CHAR(3) |  |  |  |  |
| 59 | `PAYMENTDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 60 | `FREEGIFTDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 61 | `FREEGIFTDISCOUNTEQUALITEMSOLD` | SMALLINT | NOT NULL |  |  |  |
| 62 | `LIMITCALCULATIONMODE` | CHAR(2) |  |  |  |  |
| 63 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 64 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 65 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 66 | `DISCOUNTUOMCODE` | CHAR(3) |  |  |  |  |
| 67 | `SIGN` | CHAR(2) |  |  |  |  |
| 68 | `TAXAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 69 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 70 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 71 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 72 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 73 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 74 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 75 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.LINENUMBER,
       t.LINEDETAILNUMBER,
       t.ELEMENTTYPE,
       t.COMPANYCODE,
       t.ORDERTYPE,
       t.PRICETEMPLATEDEFINITIONTYPE,
       t.PRICETEMPLATECODE,
       t.INITIALDATE,
       t.FINALDATE,
       t.PRICELISTCODE
FROM   DB2ADMIN.WRKSALESPRICELISTPRINTDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
