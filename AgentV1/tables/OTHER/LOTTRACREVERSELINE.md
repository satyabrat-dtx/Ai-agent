# DB2ADMIN.LOTTRACREVERSELINE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 125
- **Primary key**: `COMPANYCODE`, `SRCNOREVITEMTYPECODE`, `SRCNOREVDECOSUBCODE01`, `SRCNOREVDECOSUBCODE02`, `SRCNOREVDECOSUBCODE03`, `SRCNOREVDECOSUBCODE04`, `SRCNOREVDECOSUBCODE05`, `SRCNOREVDECOSUBCODE06`, `SRCNOREVDECOSUBCODE07`, `SRCNOREVDECOSUBCODE08`, `SRCNOREVDECOSUBCODE09`, `SRCNOREVDECOSUBCODE10`, `SRCNOREVLOTCODE`, `SRCNOREVQUALITYLEVELCODE`, `ITEMTYPECODE`, `DECOSUBCODE01`, `DECOSUBCODE02`, `DECOSUBCODE03`, `DECOSUBCODE04`, `DECOSUBCODE05`, `DECOSUBCODE06`, `DECOSUBCODE07`, `DECOSUBCODE08`, `DECOSUBCODE09`, `DECOSUBCODE10`, `LOTCODE`, `QUALITYLEVELCODE`, `LOTPROGR`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 113010

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONDATE` | DATE | NOT NULL |  |  |  |
| 2 | `CREATIONTIME` | TIME |  |  |  |  |
| 3 | `CREATIONUSER` | CHAR(50) | NOT NULL |  | audit | User who created the row (audit). |
| 4 | `SRCNOREVITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `SRCNOREVITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `SRCNOREVDECOCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `SRCNOREVDECOSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 8 | `SRCNOREVDECOSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `SRCNOREVDECOSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `SRCNOREVDECOSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `SRCNOREVDECOSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `SRCNOREVDECOSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `SRCNOREVDECOSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `SRCNOREVDECOSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `SRCNOREVDECOSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 16 | `SRCNOREVDECOSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 17 | `SRCNOREVLOTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 18 | `SRCNOREVLOTCODE` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 19 | `SRCNOREVQUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 20 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 21 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 22 | `DECOCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 23 | `DECOSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 24 | `DECOSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 25 | `DECOSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 26 | `DECOSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 27 | `DECOSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 28 | `DECOSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 29 | `DECOSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 30 | `DECOSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 31 | `DECOSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 32 | `DECOSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 33 | `LOTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 34 | `LOTCODE` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 35 | `QUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 36 | `REFERTRANSACTIONDATE` | DATE |  |  |  |  |
| 37 | `REFERTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 38 | `LOTPROGR` | DECIMAL(9,0) | NOT NULL | PK | primary_key |  |
| 39 | `ANALYSISSEQUENCE` | DECIMAL(9,0) |  |  |  |  |
| 40 | `LOTPROGRREF` | DECIMAL(9,0) |  |  |  |  |
| 41 | `DEVELOPMENTLEVEL` | DECIMAL(3,0) |  |  |  |  |
| 42 | `LASTLEVEL` | SMALLINT | NOT NULL |  |  |  |
| 43 | `ALREADYDEVELOPED` | SMALLINT | NOT NULL |  |  |  |
| 44 | `PRVITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 45 | `PRVITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 46 | `PRVDECOCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 47 | `PRVDECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 48 | `PRVDECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 49 | `PRVDECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 50 | `PRVDECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 51 | `PRVDECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 52 | `PRVDECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 53 | `PRVDECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 54 | `PRVDECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 55 | `PRVDECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 56 | `PRVDECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 57 | `PRVLOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 58 | `PRVLOTCODE` | CHAR(35) |  |  |  |  |
| 59 | `PRVQUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 60 | `CURITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 61 | `CURITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 62 | `CURDECOCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 63 | `CURDECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 64 | `CURDECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 65 | `CURDECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 66 | `CURDECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 67 | `CURDECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 68 | `CURDECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 69 | `CURDECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 70 | `CURDECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 71 | `CURDECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 72 | `CURDECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 73 | `CURLOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 74 | `CURLOTCODE` | CHAR(35) |  |  |  |  |
| 75 | `CURQUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 76 | `TEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 77 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 78 | `INDENTCURLOTCODE` | CHAR(120) |  |  |  |  |
| 79 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 80 | `TOTBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 81 | `ISSUEBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 82 | `ISSUETOTBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `BLNLGLWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 84 | `BALANCELOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 85 | `BLNPHYWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 86 | `BALANCEPHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 87 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 88 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 89 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 90 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 91 | `PROVISIONALDOCUMENTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 92 | `PROVISIONALDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 93 | `PROVISIONALDOCUMENTLINE` | DECIMAL(7,0) |  |  |  |  |
| 94 | `PROVISIONALDOCUMENTSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 95 | `PRVDOCUMENTCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 96 | `BILLDATE` | DATE |  |  |  |  |
| 97 | `BILLTYPE` | SMALLINT | NOT NULL |  |  |  |
| 98 | `BILLCOUNTER` | CHAR(8) |  |  |  |  |
| 99 | `BILLCODE` | CHAR(50) |  |  |  |  |
| 100 | `GENERICORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 101 | `GENORDERTEMPLATEDESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 102 | `POTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 103 | `PDTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 104 | `SOTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 105 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 106 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 107 | `PDPROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 108 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 109 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 110 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 111 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 112 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 113 | `RETURNCODE` | CHAR(15) |  |  |  |  |
| 114 | `RETURNLINE` | DECIMAL(7,0) |  |  |  |  |
| 115 | `INVOICEDATE` | DATE |  |  |  |  |
| 116 | `INVOICECODE` | CHAR(50) |  |  |  |  |
| 117 | `ONHANDUPDATE` | CHAR(2) |  |  |  |  |
| 118 | `STOCKTRANSACTIONTYPE` | CHAR(2) |  |  |  |  |
| 119 | `INFORMATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 120 | `DUPLICATE` | SMALLINT | NOT NULL |  |  |  |
| 121 | `DUPLICATEFIRST` | SMALLINT | NOT NULL |  |  |  |
| 122 | `DUPLICATEANSEQREFER` | DECIMAL(9,0) |  |  |  |  |
| 123 | `ANALYSISSEQUENCEWORK` | VARCHAR(500) |  |  |  |  |
| 124 | `NODEVELOPMENTREVERSE` | SMALLINT | NOT NULL |  |  |  |

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
       t.SRCNOREVITEMTYPECOMPANYCODE,
       t.SRCNOREVITEMTYPECODE,
       t.SRCNOREVDECOCOMPANYCODE,
       t.SRCNOREVDECOSUBCODE01,
       t.SRCNOREVDECOSUBCODE02,
       t.SRCNOREVDECOSUBCODE03,
       t.SRCNOREVDECOSUBCODE04,
       t.SRCNOREVDECOSUBCODE05
FROM   DB2ADMIN.LOTTRACREVERSELINE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
