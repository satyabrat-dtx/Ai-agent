# DB2ADMIN.LOTTRACLINE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 110
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `DECOSUBCODE01`, `DECOSUBCODE02`, `DECOSUBCODE03`, `DECOSUBCODE04`, `DECOSUBCODE05`, `DECOSUBCODE06`, `DECOSUBCODE07`, `DECOSUBCODE08`, `DECOSUBCODE09`, `DECOSUBCODE10`, `LOTCODE`, `QUALITYLEVELCODE`, `LOTPROGR`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 112814

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONDATE` | DATE | NOT NULL |  |  |  |
| 2 | `CREATIONTIME` | TIME |  |  |  |  |
| 3 | `CREATIONUSER` | CHAR(50) | NOT NULL |  | audit | User who created the row (audit). |
| 4 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `DECOCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `DECOSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 8 | `DECOSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `DECOSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `DECOSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `DECOSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `DECOSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `DECOSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `DECOSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `DECOSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 16 | `DECOSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 17 | `LOTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 18 | `LOTCODE` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 19 | `QUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 20 | `REFERTRANSACTIONDATE` | DATE |  |  |  |  |
| 21 | `REFERTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 22 | `LOTPROGR` | DECIMAL(9,0) | NOT NULL | PK | primary_key |  |
| 23 | `LOTPROGRREF` | DECIMAL(9,0) |  |  |  |  |
| 24 | `ANALYSISSEQUENCE` | DECIMAL(9,0) |  |  |  |  |
| 25 | `DEVELOPMENTLEVEL` | DECIMAL(3,0) |  |  |  |  |
| 26 | `LASTLEVEL` | SMALLINT | NOT NULL |  |  |  |
| 27 | `ALREADYDEVELOPED` | SMALLINT | NOT NULL |  |  |  |
| 28 | `PRVITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `PRVITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 30 | `PRVDECOCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `PRVDECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 32 | `PRVDECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 33 | `PRVDECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 34 | `PRVDECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 35 | `PRVDECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 36 | `PRVDECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 37 | `PRVDECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 38 | `PRVDECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 39 | `PRVDECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 40 | `PRVDECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 41 | `PRVLOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 42 | `PRVLOTCODE` | CHAR(35) |  |  |  |  |
| 43 | `PRVQUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 44 | `CURITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 45 | `CURITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 46 | `CURDECOCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 47 | `CURDECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 48 | `CURDECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 49 | `CURDECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 50 | `CURDECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 51 | `CURDECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 52 | `CURDECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 53 | `CURDECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 54 | `CURDECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 55 | `CURDECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 56 | `CURDECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 57 | `CURLOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 58 | `CURLOTCODE` | CHAR(35) |  |  |  |  |
| 59 | `CURQUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 60 | `TEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 61 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 62 | `INDENTCURLOTCODE` | CHAR(120) |  |  |  |  |
| 63 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 64 | `TOTBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `ISSUEBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 66 | `ISSUETOTBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 67 | `BLNLGLWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 68 | `BALANCELOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 69 | `BLNPHYWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 70 | `BALANCEPHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 71 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 72 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 73 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 74 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 75 | `PROVISIONALDOCUMENTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 76 | `PROVISIONALDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 77 | `PROVISIONALDOCUMENTLINE` | DECIMAL(7,0) |  |  |  |  |
| 78 | `PROVISIONALDOCUMENTSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 79 | `PRVDOCUMENTCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 80 | `BILLDATE` | DATE |  |  |  |  |
| 81 | `BILLTYPE` | SMALLINT | NOT NULL |  |  |  |
| 82 | `BILLCOUNTER` | CHAR(8) |  |  |  |  |
| 83 | `BILLCODE` | CHAR(50) |  |  |  |  |
| 84 | `GENERICORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 85 | `GENORDERTEMPLATEDESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 86 | `POTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 87 | `PDTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 88 | `SOTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 89 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 90 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 91 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 92 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 93 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 94 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 95 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 96 | `PDPROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 97 | `RETURNCODE` | CHAR(15) |  |  |  |  |
| 98 | `RETURNLINE` | DECIMAL(7,0) |  |  |  |  |
| 99 | `INVOICEDATE` | DATE |  |  |  |  |
| 100 | `INVOICECODE` | CHAR(50) |  |  |  |  |
| 101 | `ONHANDUPDATE` | CHAR(2) |  |  |  |  |
| 102 | `STOCKTRANSACTIONTYPE` | CHAR(2) |  |  |  |  |
| 103 | `INFORMATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 104 | `DUPLICATE` | SMALLINT | NOT NULL |  |  |  |
| 105 | `DUPLICATEFIRST` | SMALLINT | NOT NULL |  |  |  |
| 106 | `DUPLICATEANSEQREFER` | DECIMAL(9,0) |  |  |  |  |
| 107 | `ANALYSISSEQUENCEWORK` | VARCHAR(500) |  |  |  |  |
| 108 | `NODEVELOPMENTREVERSE` | SMALLINT | NOT NULL |  |  |  |
| 109 | `RECURSION` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONDATE,
       t.CREATIONTIME,
       t.CREATIONUSER,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.DECOCOMPANYCODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05
FROM   DB2ADMIN.LOTTRACLINE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
