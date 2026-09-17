# DB2ADMIN.WRKPACKINGLISTFORARE1

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 51
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `DIVISIONCODE`, `PLANTINVOICECODE`, `INVOICELINENO`, `STOCKTRANSACTIONNUMBER`, `STOCKTRANSACTIONDETAILNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144911

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXCISECATEGORYCODE` | CHAR(10) |  |  |  |  |
| 1 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `CHAPTERID` | CHAR(5) | NOT NULL |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `VALUE` | DECIMAL(15,5) |  |  |  |  |
| 6 | `HTO` | DECIMAL(15,5) |  |  |  |  |
| 7 | `EVA` | DECIMAL(15,5) |  |  |  |  |
| 8 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 9 | `PLANTINVOICECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 10 | `CUSTOMINVOICECODE` | CHAR(15) |  |  |  |  |
| 11 | `STOCKTRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 12 | `STOCKTRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 13 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 14 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 15 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `ARE1CODE` | CHAR(20) |  |  |  |  |
| 17 | `ARE3CODE` | CHAR(20) |  |  |  |  |
| 18 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 19 | `ARE1DATE` | DATE |  |  |  |  |
| 20 | `ARE3DATE` | DATE |  |  |  |  |
| 21 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 22 | `INVOICELINENO` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 23 | `PLANTINVOICEDATE` | DATE |  |  |  |  |
| 24 | `CUSTOMINVOICEDATE` | DATE |  |  |  |  |
| 25 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 26 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 27 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 28 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 29 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `BASEPRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 31 | `BASESECODARYUMCODE` | CHAR(3) |  |  |  |  |
| 32 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `BASESECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 34 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 36 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 37 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 39 | `TAPPERGRP` | CHAR(3) |  |  |  |  |
| 40 | `PCS` | INTEGER | NOT NULL |  |  |  |
| 41 | `QUANTITYSQMTS` | DECIMAL(15,5) |  |  |  |  |
| 42 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 43 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 44 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 45 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 46 | `SORTOF` | VARCHAR(250) |  |  |  |  |
| 47 | `SUMMARIZEDDESC` | VARCHAR(250) |  |  |  |  |
| 48 | `CALCULATEDVALUERCCFOROTH` | DECIMAL(18,5) |  |  |  |  |
| 49 | `OTHVALUE` | DECIMAL(18,5) |  |  |  |  |
| 50 | `WIDTH` | DECIMAL(5,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.EXCISECATEGORYCODE,
       t.TARIFFCODE,
       t.CREATIONTIMESTAMP,
       t.CHAPTERID,
       t.COMPANYCODE,
       t.VALUE,
       t.HTO,
       t.EVA,
       t.DIVISIONCODE,
       t.PLANTINVOICECODE,
       t.CUSTOMINVOICECODE,
       t.STOCKTRANSACTIONNUMBER
FROM   DB2ADMIN.WRKPACKINGLISTFORARE1 t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
