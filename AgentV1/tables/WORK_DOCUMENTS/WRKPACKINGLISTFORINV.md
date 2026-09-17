# DB2ADMIN.WRKPACKINGLISTFORINV

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 97
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `DIVISIONCODE`, `PLANTINVOICECODE`, `STOCKTRANSACTIONNUMBER`, `STOCKTRANSACTIONDETAILNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144987

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `PLANTINVOICECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `LINE` | INTEGER | NOT NULL |  |  |  |
| 5 | `SALESDOCABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 6 | `STOCKTRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 7 | `STOCKTRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `CUSTOMINVOICECODE` | CHAR(20) |  |  |  |  |
| 9 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 10 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 11 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 12 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 13 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 14 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 15 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 17 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 18 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `BASEPRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 21 | `BASESECODARYUMCODE` | CHAR(3) |  |  |  |  |
| 22 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `BASESECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `LENGTH` | DECIMAL(15,5) |  |  |  |  |
| 26 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 27 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 30 | `TAPPERGRP` | CHAR(3) |  |  |  |  |
| 31 | `PCS` | INTEGER | NOT NULL |  |  |  |
| 32 | `QUANTITYSQMTS` | DECIMAL(15,5) |  |  |  |  |
| 33 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 34 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 35 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 36 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 37 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 38 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 39 | `SORTOF` | VARCHAR(250) |  |  |  |  |
| 40 | `SUMMARIZEDDESC` | VARCHAR(250) |  |  |  |  |
| 41 | `BEDITAXCODE` | CHAR(3) |  |  |  |  |
| 42 | `BEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 43 | `LCDATE` | DATE |  |  |  |  |
| 44 | `INSURANCEPOLICYDATE` | DATE |  |  |  |  |
| 45 | `BEDCALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 46 | `ECITAXCODE` | CHAR(3) |  |  |  |  |
| 47 | `ECVALUE` | DECIMAL(18,5) |  |  |  |  |
| 48 | `ECCALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 49 | `CSITAXCODE` | CHAR(3) |  |  |  |  |
| 50 | `CSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 51 | `CSCALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 52 | `SSITAXCODE` | CHAR(3) |  |  |  |  |
| 53 | `SSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 54 | `SSCALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 55 | `TOTALDUTY` | DECIMAL(18,5) |  |  |  |  |
| 56 | `TAV` | DECIMAL(18,5) |  |  |  |  |
| 57 | `TRF` | DECIMAL(18,5) |  |  |  |  |
| 58 | `NAM` | DECIMAL(18,5) |  |  |  |  |
| 59 | `CALCULATEDVALUERCCFORSYS` | DECIMAL(18,5) |  |  |  |  |
| 60 | `CALCULATEDVALUERCCFOROTH` | DECIMAL(18,5) |  |  |  |  |
| 61 | `OTHVALUE` | DECIMAL(18,5) |  |  |  |  |
| 62 | `BEDDESC` | VARCHAR(200) |  |  |  |  |
| 63 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 64 | `ORDERCOUNTERCODE` | CHAR(15) |  |  |  |  |
| 65 | `CSDDESC` | VARCHAR(200) |  |  |  |  |
| 66 | `QUALITYCAT` | VARCHAR(200) |  |  |  |  |
| 67 | `ECDESC` | VARCHAR(200) |  |  |  |  |
| 68 | `REMARK` | VARCHAR(200) |  |  |  |  |
| 69 | `LCNO` | VARCHAR(200) |  |  |  |  |
| 70 | `INSURANCEPOLICYNO` | VARCHAR(200) |  |  |  |  |
| 71 | `SSDDESC` | VARCHAR(200) |  |  |  |  |
| 72 | `CASHDISCPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 73 | `NOOFDAYS` | INTEGER | NOT NULL |  |  |  |
| 74 | `WIDTH` | DECIMAL(5,2) |  |  |  |  |
| 75 | `SALESORDERCOUNTER` | CHAR(8) |  |  |  |  |
| 76 | `SALESORDERCODE` | CHAR(15) |  |  |  |  |
| 77 | `SALESORDERLINENO` | DECIMAL(7,0) |  |  |  |  |
| 78 | `AGENTFORM` | CHAR(50) |  |  |  |  |
| 79 | `AGENTDESC` | VARCHAR(200) |  |  |  |  |
| 80 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 81 | `TARRIFCODE` | CHAR(20) |  |  |  |  |
| 82 | `STUSERPRIMARYQTY` | DECIMAL(18,5) |  |  |  |  |
| 83 | `SR1` | DECIMAL(18,5) |  |  |  |  |
| 84 | `VAT` | DECIMAL(18,5) |  |  |  |  |
| 85 | `CS1` | DECIMAL(18,5) |  |  |  |  |
| 86 | `BE1` | DECIMAL(18,5) |  |  |  |  |
| 87 | `ED1` | DECIMAL(18,5) |  |  |  |  |
| 88 | `SH1` | DECIMAL(18,5) |  |  |  |  |
| 89 | `TC1` | DECIMAL(18,5) |  |  |  |  |
| 90 | `BED` | DECIMAL(18,5) |  |  |  |  |
| 91 | `EDC` | DECIMAL(18,5) |  |  |  |  |
| 92 | `SHC` | DECIMAL(18,5) |  |  |  |  |
| 93 | `INVLINEQTYFORSEL` | DECIMAL(18,5) |  |  |  |  |
| 94 | `PKUOMFORSEL` | CHAR(20) |  |  |  |  |
| 95 | `PKUOMQTYFORSEL` | INTEGER | NOT NULL |  |  |  |
| 96 | `NUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.PLANTINVOICECODE,
       t.LINE,
       t.SALESDOCABSUNIQUEID,
       t.STOCKTRANSACTIONNUMBER,
       t.STOCKTRANSACTIONDETAILNUMBER,
       t.CUSTOMINVOICECODE,
       t.ITEMELEMENTSUBCODEKEY,
       t.ITEMELEMENTCODE,
       t.CONTAINERITEMTYPECODE
FROM   DB2ADMIN.WRKPACKINGLISTFORINV t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
