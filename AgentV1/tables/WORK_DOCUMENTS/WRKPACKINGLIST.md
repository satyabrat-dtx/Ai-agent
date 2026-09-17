# DB2ADMIN.WRKPACKINGLIST

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 35
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `DIVISIONCODE`, `PLANTINVOICECODE`, `STOCKTRANSACTIONNUMBER`, `STOCKTRANSACTIONDETAILNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144852

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `PLANTINVOICECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `STOCKTRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `STOCKTRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CUSTOMINVOICECODE` | CHAR(20) |  |  |  |  |
| 7 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 8 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 9 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 11 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 12 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 13 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 14 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 15 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 16 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 17 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 20 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 22 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 24 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 26 | `TAPPERGRP` | CHAR(3) |  |  |  |  |
| 27 | `PCS` | INTEGER | NOT NULL |  |  |  |
| 28 | `QUANTITYSQMTS` | DECIMAL(15,5) |  |  |  |  |
| 29 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 30 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 31 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 32 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 33 | `SORTOF` | VARCHAR(250) |  |  |  |  |
| 34 | `SOCODE` | VARCHAR(200) |  |  |  |  |

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
       t.STOCKTRANSACTIONNUMBER,
       t.STOCKTRANSACTIONDETAILNUMBER,
       t.CUSTOMINVOICECODE,
       t.ITEMELEMENTSUBCODEKEY,
       t.ITEMELEMENTCODE,
       t.CONTAINERITEMTYPECODE,
       t.CONTAINERSUBCODE01,
       t.CONTAINERELEMENTCODE
FROM   DB2ADMIN.WRKPACKINGLIST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
