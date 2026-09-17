# DB2ADMIN.WRKCOMMERCIALINVOICEREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 51
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144531

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PORTOFLOADINGCODE` | CHAR(10) |  |  |  |  |
| 1 | `PORTOFDISCHARGECODE` | CHAR(10) |  |  |  |  |
| 2 | `FINALDESTINATIONCODE` | VARCHAR(200) |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 5 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 6 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 7 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `TERMSDELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 9 | `GOODSORIGINCOUNTRY` | VARCHAR(200) |  |  |  |  |
| 10 | `LCNO` | CHAR(35) |  |  |  |  |
| 11 | `FINALDESTINATION` | VARCHAR(200) |  |  |  |  |
| 12 | `LCDATE` | DATE |  |  |  |  |
| 13 | `CODE` | CHAR(20) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 14 | `INVOICEDATE` | DATE |  |  |  |  |
| 15 | `SALESORDERCODE` | CHAR(15) |  |  |  |  |
| 16 | `TERMSPAYMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 17 | `CONTRACTDATE` | DATE |  |  |  |  |
| 18 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 19 | `KINDOFPACKAGE` | CHAR(100) |  |  |  |  |
| 20 | `CONTAINER1` | CHAR(100) |  |  |  |  |
| 21 | `CONTAINER2` | CHAR(100) |  |  |  |  |
| 22 | `SHIPPINGBILLNUMBER` | CHAR(100) |  |  |  |  |
| 23 | `CONTAINER3` | CHAR(100) |  |  |  |  |
| 24 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `BUYERADDRESS` | DECIMAL(8,0) |  |  |  |  |
| 26 | `NOTIFYADDRESS2` | DECIMAL(8,0) |  |  |  |  |
| 27 | `NOTIFYADDRESS1` | DECIMAL(8,0) |  |  |  |  |
| 28 | `CONSIGNEEADDRESS` | DECIMAL(8,0) |  |  |  |  |
| 29 | `VESSELFLIGHTNO` | CHAR(35) |  |  |  |  |
| 30 | `DESCRIPTION3` | CHAR(100) |  |  |  |  |
| 31 | `DESCRIPTION4` | CHAR(100) |  |  |  |  |
| 32 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 33 | `DESCRIPTION2` | CHAR(100) |  |  |  |  |
| 34 | `DESCRIPTION1` | CHAR(100) |  |  |  |  |
| 35 | `SALESORDERLINESUBCODE01` | CHAR(20) |  |  |  |  |
| 36 | `SALESORDERLINESUBCODE01DESC` | VARCHAR(200) |  |  |  |  |
| 37 | `SALESORDERLINESUBCODE05` | VARCHAR(200) |  |  |  |  |
| 38 | `SALESORDERLINESUBCODE06` | VARCHAR(200) |  |  |  |  |
| 39 | `SHIPPINGMARK1` | VARCHAR(1000) |  |  |  |  |
| 40 | `TARIFFCODE` | VARCHAR(200) |  |  |  |  |
| 41 | `SHIPPINGMARK2` | VARCHAR(1000) |  |  |  |  |
| 42 | `SHIPPINGMARK3` | VARCHAR(1000) |  |  |  |  |
| 43 | `INSURANCE` | DECIMAL(10,5) |  |  |  |  |
| 44 | `FREIGHT` | DECIMAL(10,5) |  |  |  |  |
| 45 | `ORIGINALBILLOFLADINGNO` | CHAR(25) |  |  |  |  |
| 46 | `ORIGINALBILLOFLADINGDATE` | DATE |  |  |  |  |
| 47 | `ADDITIONALCHARGES` | DECIMAL(10,0) |  |  |  |  |
| 48 | `SOABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 49 | `TARRIF` | CHAR(20) |  |  |  |  |
| 50 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PORTOFLOADINGCODE,
       t.PORTOFDISCHARGECODE,
       t.FINALDESTINATIONCODE,
       t.COMPANYCODE,
       t.PRIMARYUMCODE,
       t.DIVISIONCODE,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.TERMSDELIVERYDESCRIPTION,
       t.GOODSORIGINCOUNTRY,
       t.LCNO,
       t.FINALDESTINATION
FROM   DB2ADMIN.WRKCOMMERCIALINVOICEREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
