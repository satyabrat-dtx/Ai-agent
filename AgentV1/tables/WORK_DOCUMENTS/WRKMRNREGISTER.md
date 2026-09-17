# DB2ADMIN.WRKMRNREGISTER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 67
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239871

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `MRNNO` | DECIMAL(11,0) |  |  |  |  |
| 6 | `MRNDATE` | DATE |  |  |  |  |
| 7 | `SUPPLIERCODE` | CHAR(15) |  |  |  |  |
| 8 | `ORDERNO` | CHAR(15) |  |  |  |  |
| 9 | `CHALLANNO` | CHAR(15) |  |  |  |  |
| 10 | `CHALLANDATE` | DATE |  |  |  |  |
| 11 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 12 | `INVOICEDATE` | DATE |  |  |  |  |
| 13 | `MAINGATEENTRYSRNO` | CHAR(15) |  |  |  |  |
| 14 | `MAINGATEENTRYDATE` | DATE |  |  |  |  |
| 15 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 16 | `TERMSOFPAYMENTLD` | VARCHAR(200) |  |  |  |  |
| 17 | `ORDERDATE` | DATE |  |  |  |  |
| 18 | `COMPANYLD` | VARCHAR(200) |  |  |  |  |
| 19 | `ITEMTYPELD` | VARCHAR(200) |  |  |  |  |
| 20 | `STLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 21 | `COMPANYCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 22 | `DIVISIONNAME` | VARCHAR(200) |  |  |  |  |
| 23 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 24 | `CADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 25 | `CADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 26 | `CADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 27 | `CADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 28 | `CADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 29 | `CPOSTALCODE` | CHAR(20) |  |  |  |  |
| 30 | `CTOWN` | VARCHAR(200) |  |  |  |  |
| 31 | `CDISTRICT` | VARCHAR(200) |  |  |  |  |
| 32 | `CADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 33 | `CONSIGNEELEGALNAME1` | VARCHAR(270) |  |  |  |  |
| 34 | `ORDERTYPE` | CHAR(8) |  |  |  |  |
| 35 | `LINEID` | INTEGER | NOT NULL |  |  |  |
| 36 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 37 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 38 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 41 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 42 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 43 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 44 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 45 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 46 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 47 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 48 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 49 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 50 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 51 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 52 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 53 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 54 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 55 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 56 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 57 | `REJECTEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 59 | `ACTUALRECVQTY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `RECEIVEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `GSTINNUMBER` | CHAR(15) |  |  |  |  |
| 62 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 63 | `WAREHOUSE` | CHAR(8) |  |  |  |  |
| 64 | `TAXESCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 65 | `BUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 66 | `DETAILABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.MRNNO,
       t.MRNDATE,
       t.SUPPLIERCODE,
       t.ORDERNO,
       t.CHALLANNO,
       t.CHALLANDATE,
       t.INVOICENO
FROM   DB2ADMIN.WRKMRNREGISTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
