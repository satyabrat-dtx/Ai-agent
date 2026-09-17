# DB2ADMIN.WRKRG1TRANSACTION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 51
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `UNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 145688

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHAPTERID` | CHAR(5) |  |  |  |  |
| 1 | `CHAPTERINDICATION` | INTEGER | NOT NULL |  |  |  |
| 2 | `EXCISECATEGORYCODE` | CHAR(10) |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 5 | `GROUPING` | CHAR(20) |  |  |  |  |
| 6 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 7 | `RG1TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `EXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 9 | `EXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 10 | `SEQNO` | INTEGER | NOT NULL |  |  |  |
| 11 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 12 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 13 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 14 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 15 | `ADDDEDUCT` | INTEGER | NOT NULL |  |  |  |
| 16 | `ITDATE` | DATE |  |  |  |  |
| 17 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 19 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 20 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 32 | `QUALITYCATEGORYCODE` | CHAR(2) |  |  |  |  |
| 33 | `BALESCOUNT` | INTEGER | NOT NULL |  |  |  |
| 34 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 35 | `WIDTH` | DECIMAL(18,5) |  |  |  |  |
| 36 | `CONTAINER` | CHAR(15) |  |  |  |  |
| 37 | `ELEMENT` | CHAR(15) |  |  |  |  |
| 38 | `PLANT` | CHAR(8) |  |  |  |  |
| 39 | `SQMTRS` | DECIMAL(18,5) |  |  |  |  |
| 40 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 41 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 42 | `ORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 44 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 45 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 46 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 47 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 48 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 49 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 50 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CHAPTERID,
       t.CHAPTERINDICATION,
       t.EXCISECATEGORYCODE,
       t.COMPANYCODE,
       t.UNIQUEID,
       t.GROUPING,
       t.DIVISIONCODE,
       t.RG1TEMPLATECODE,
       t.EXCISEYEARREGNO,
       t.EXCISEYEARCODE,
       t.SEQNO,
       t.TARIFFCODE
FROM   DB2ADMIN.WRKRG1TRANSACTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
