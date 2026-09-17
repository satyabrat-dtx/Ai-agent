# DB2ADMIN.WRKMRNHEADER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 94
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239757

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CUSER` | CHAR(50) |  |  |  |  |
| 4 | `PURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 6 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 7 | `MRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 8 | `MRNNO` | DECIMAL(11,0) |  |  |  |  |
| 9 | `MRNDATE` | DATE |  |  |  |  |
| 10 | `SUPPLIERCODE` | CHAR(15) |  |  |  |  |
| 11 | `ORDERNO` | CHAR(15) |  |  |  |  |
| 12 | `CHALLANNO` | CHAR(15) |  |  |  |  |
| 13 | `CHALLANDATE` | DATE |  |  |  |  |
| 14 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 15 | `INVOICEDATE` | DATE |  |  |  |  |
| 16 | `MAINGATEENTRYSRNO` | CHAR(15) |  |  |  |  |
| 17 | `MAINGATEENTRYDATE` | DATE |  |  |  |  |
| 18 | `REMARK` | VARCHAR(100) |  |  |  |  |
| 19 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 20 | `TERMSOFPAYMENTLD` | VARCHAR(200) |  |  |  |  |
| 21 | `TERMSOFDELIVERYLD` | VARCHAR(200) |  |  |  |  |
| 22 | `TERMSOFSHIPPINGLD` | VARCHAR(200) |  |  |  |  |
| 23 | `PODATE` | DATE |  |  |  |  |
| 24 | `COMPANYLD` | VARCHAR(200) |  |  |  |  |
| 25 | `COMPANYCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 26 | `DIVISIONNAME` | VARCHAR(200) |  |  |  |  |
| 27 | `ADDRESSEE` | VARCHAR(200) |  |  |  |  |
| 28 | `ADDRESSEE2` | VARCHAR(200) |  |  |  |  |
| 29 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 30 | `ADDCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 31 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 32 | `CADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 33 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 34 | `CADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 35 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 36 | `CADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 37 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 38 | `CADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 39 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 40 | `CADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 41 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 42 | `CPOSTALCODE` | CHAR(20) |  |  |  |  |
| 43 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 44 | `CTOWN` | VARCHAR(200) |  |  |  |  |
| 45 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 46 | `CDISTRICT` | VARCHAR(200) |  |  |  |  |
| 47 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 48 | `CADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 49 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 50 | `CONSIGNEELEGALNAME1` | VARCHAR(270) | NOT NULL |  |  |  |
| 51 | `MRNCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 52 | `POTYPE` | CHAR(8) |  |  |  |  |
| 53 | `ORDERTYPE` | CHAR(8) |  |  |  |  |
| 54 | `LINEID` | INTEGER | NOT NULL |  |  |  |
| 55 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 56 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 57 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 59 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 60 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 61 | `GRANDTOTALBASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 62 | `TOTALBASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 63 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 64 | `ENTRYSUBCODE01` | CHAR(20) |  |  |  |  |
| 65 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 66 | `ENTRYSUBCODE02` | CHAR(10) |  |  |  |  |
| 67 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 68 | `ENTRYSUBCODE03` | CHAR(10) |  |  |  |  |
| 69 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 70 | `ENTRYSUBCODE04` | CHAR(10) |  |  |  |  |
| 71 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 72 | `ENTRYSUBCODE05` | CHAR(10) |  |  |  |  |
| 73 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 74 | `ENTRYSUBCODE06` | CHAR(10) |  |  |  |  |
| 75 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 76 | `ENTRYSUBCODE07` | CHAR(10) |  |  |  |  |
| 77 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 78 | `ENTRYSUBCODE08` | CHAR(10) |  |  |  |  |
| 79 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 80 | `ENTRYSUBCODE09` | CHAR(10) |  |  |  |  |
| 81 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 82 | `ENTRYSUBCODE10` | CHAR(10) |  |  |  |  |
| 83 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 84 | `ENTRYITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 85 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 86 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 87 | `REJECTEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 88 | `ACTUALRECVQTY` | DECIMAL(15,5) |  |  |  |  |
| 89 | `RECEIVEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 90 | `GSTINNUMBER` | CHAR(15) |  |  |  |  |
| 91 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 92 | `ENTRYITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 93 | `DETAILABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.CUSER,
       t.PURCHASEORDERCODE,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.MRNPREFIXCODE,
       t.MRNNO,
       t.MRNDATE,
       t.SUPPLIERCODE,
       t.ORDERNO
FROM   DB2ADMIN.WRKMRNHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
