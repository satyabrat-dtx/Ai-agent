# DB2ADMIN.WRKFOB

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 55
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `CODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144775

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `CODE` | CHAR(50) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `CUSTOMINVOICECODE` | CHAR(50) | NOT NULL |  |  |  |
| 5 | `CUSTOMINVOICEDATE` | DATE |  |  |  |  |
| 6 | `EXPORTSHIPPINGBILLCODE` | CHAR(50) |  |  |  |  |
| 7 | `SHIPPINGBILLDATE` | DATE |  |  |  |  |
| 8 | `COMMISSIONAMTFC` | DECIMAL(18,5) |  |  |  |  |
| 9 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 10 | `COMMLONGDECSRIPTION` | CHAR(100) |  |  |  |  |
| 11 | `ORIGINALBILLLADINGNO` | CHAR(50) |  |  |  |  |
| 12 | `BILLLADINGDATE` | DATE |  |  |  |  |
| 13 | `PORTDESC` | CHAR(100) |  |  |  |  |
| 14 | `CONTRYDESC` | CHAR(100) |  |  |  |  |
| 15 | `INVOICECURRENCYCODE` | CHAR(5) |  |  |  |  |
| 16 | `BILLAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 17 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 18 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 19 | `FIRMADDRESS` | VARCHAR(960) |  |  |  |  |
| 20 | `BYERADDRESS` | VARCHAR(500) |  |  |  |  |
| 21 | `LEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 22 | `AREACODE` | CHAR(3) |  |  |  |  |
| 23 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 24 | `CALCULATEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 25 | `COMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 26 | `CALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 27 | `DOCUMENTCURRENCYCODESNI` | CHAR(4) |  |  |  |  |
| 28 | `CALCULATEDVALUESNI` | DECIMAL(18,5) |  |  |  |  |
| 29 | `COMPANYCURRENCY` | CHAR(4) |  |  |  |  |
| 30 | `CALCULATEDVALUERCCSNI` | DECIMAL(18,5) |  |  |  |  |
| 31 | `EXPORTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 32 | `DOCUMENTCURRENCYCODETRF` | CHAR(4) |  |  |  |  |
| 33 | `CALCULATEDVALUETRF` | DECIMAL(18,5) |  |  |  |  |
| 34 | `COMPANYCURRENCYTRF` | CHAR(4) |  |  |  |  |
| 35 | `CALCULATEDVALUERCCTRF` | DECIMAL(18,5) |  |  |  |  |
| 36 | `GREXPORTSHIPPINGCODE` | CHAR(12) |  |  |  |  |
| 37 | `SCHEMETYPECODE` | VARCHAR(80) |  |  |  |  |
| 38 | `FIRMLONGDESC` | VARCHAR(200) |  |  |  |  |
| 39 | `BANKLONGDESC` | VARCHAR(200) |  |  |  |  |
| 40 | `LCADDRESS` | VARCHAR(960) |  |  |  |  |
| 41 | `BUSINESSADDRESS` | VARCHAR(960) |  |  |  |  |
| 42 | `BUSINESSADDRESS1` | VARCHAR(960) |  |  |  |  |
| 43 | `SHIPPINGMARK` | CHAR(100) |  |  |  |  |
| 44 | `ITEMDESC` | CHAR(100) |  |  |  |  |
| 45 | `ADDTELPHONE` | VARCHAR(80) |  |  |  |  |
| 46 | `ADDFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 47 | `MARKEDFREIGHT` | INTEGER | NOT NULL |  |  |  |
| 48 | `SHORTDESCFORUM` | CHAR(50) |  |  |  |  |
| 49 | `INVOICECODEANDDATE` | VARCHAR(1000) |  |  |  |  |
| 50 | `ADDTELPHONE1` | VARCHAR(80) |  |  |  |  |
| 51 | `FOOTERLINES` | CHAR(100) |  |  |  |  |
| 52 | `ADDFAXNUMBER1` | VARCHAR(80) |  |  |  |  |
| 53 | `SHORTDESCFORWEIGHT` | VARCHAR(80) |  |  |  |  |
| 54 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.DIVISIONCODE,
       t.CODE,
       t.CUSTOMINVOICECODE,
       t.CUSTOMINVOICEDATE,
       t.EXPORTSHIPPINGBILLCODE,
       t.SHIPPINGBILLDATE,
       t.COMMISSIONAMTFC,
       t.EXCHANGERATE,
       t.COMMLONGDECSRIPTION,
       t.ORIGINALBILLLADINGNO
FROM   DB2ADMIN.WRKFOB t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
