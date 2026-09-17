# DB2ADMIN.WRKFINPURCHASEREGISTER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 90
- **Primary key**: `CREATIONTIMESTAMP`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 180993

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `LINENUMBER` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 4 | `INVOICELINENO` | INTEGER | NOT NULL |  |  |  |
| 5 | `DDPIEI` | CHAR(30) |  |  |  |  |
| 6 | `RCMAPPLICABLE` | CHAR(30) |  |  |  |  |
| 7 | `NATUREOFSUPPLY` | CHAR(30) |  |  |  |  |
| 8 | `INVPREFDT` | CHAR(10) |  |  |  |  |
| 9 | `INVOICENO` | CHAR(32) |  |  |  |  |
| 10 | `DEBITCREDITNO` | CHAR(30) |  |  |  |  |
| 11 | `INVOICEDATE` | DATE |  |  |  |  |
| 12 | `DEBITCREDITDATE` | DATE |  |  |  |  |
| 13 | `INVOICECREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 14 | `TYPEOFDOCUMENT` | INTEGER | NOT NULL |  |  |  |
| 15 | `DDDOCUMENTTYPE` | CHAR(20) |  |  |  |  |
| 16 | `DDCOUNTERCODE` | CHAR(20) |  |  |  |  |
| 17 | `DDDOCUMENTNO` | CHAR(20) |  |  |  |  |
| 18 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 19 | `DOCTYPE` | VARCHAR(80) |  |  |  |  |
| 20 | `PURCHASEORDERNO` | CHAR(30) |  |  |  |  |
| 21 | `LOCATION` | VARCHAR(200) |  |  |  |  |
| 22 | `PARTYNAME` | VARCHAR(200) |  |  |  |  |
| 23 | `PARTYADDRESS` | VARCHAR(1000) |  |  |  |  |
| 24 | `PLANTGSTIN` | CHAR(50) |  |  |  |  |
| 25 | `STATECODE` | VARCHAR(200) |  |  |  |  |
| 26 | `GSTIN` | CHAR(50) |  |  |  |  |
| 27 | `GSTNSTATUS` | CHAR(50) |  |  |  |  |
| 28 | `FINDOCNO` | CHAR(20) |  |  |  |  |
| 29 | `FINDOCDATE` | DATE |  |  |  |  |
| 30 | `BOENO` | CHAR(50) |  |  |  |  |
| 31 | `BOEDATE` | DATE |  |  |  |  |
| 32 | `HSNCODE` | CHAR(20) |  |  |  |  |
| 33 | `PRODUCTLONGDESC` | VARCHAR(200) |  |  |  |  |
| 34 | `PRODUCTCODE` | CHAR(100) |  |  |  |  |
| 35 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `ITEMTYPECODE` | CHAR(10) |  |  |  |  |
| 37 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 38 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 39 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 40 | `RATEFC` | DECIMAL(18,5) |  |  |  |  |
| 41 | `RATECC` | DECIMAL(28,15) |  |  |  |  |
| 42 | `BASICVALUEFC` | DECIMAL(18,5) |  |  |  |  |
| 43 | `BASICVALUETAXABLE` | DECIMAL(18,5) |  |  |  |  |
| 44 | `BASICVALUETHIRDPARTY` | DECIMAL(18,5) |  |  |  |  |
| 45 | `FREIGHT` | DECIMAL(18,5) |  |  |  |  |
| 46 | `INTRAORINTER` | CHAR(30) |  |  |  |  |
| 47 | `NARRATION` | VARCHAR(255) |  |  |  |  |
| 48 | `TAXCOLUMN1` | DECIMAL(18,5) |  |  |  |  |
| 49 | `TAXCOLUMN2` | DECIMAL(18,5) |  |  |  |  |
| 50 | `TAXCOLUMN3` | DECIMAL(18,5) |  |  |  |  |
| 51 | `TAXCOLUMN4` | DECIMAL(18,5) |  |  |  |  |
| 52 | `TAXCOLUMN5` | DECIMAL(18,5) |  |  |  |  |
| 53 | `TAXCOLUMN6` | DECIMAL(18,5) |  |  |  |  |
| 54 | `TAXCOLUMN7` | DECIMAL(18,5) |  |  |  |  |
| 55 | `TAXCOLUMN8` | DECIMAL(18,5) |  |  |  |  |
| 56 | `TAXCOLUMN9` | DECIMAL(18,5) |  |  |  |  |
| 57 | `TAXCOLUMN10` | DECIMAL(18,5) |  |  |  |  |
| 58 | `TAXCOLUMN11` | DECIMAL(18,5) |  |  |  |  |
| 59 | `TAXCOLUMN12` | DECIMAL(18,5) |  |  |  |  |
| 60 | `TAXCOLUMN13` | DECIMAL(18,5) |  |  |  |  |
| 61 | `COLUMNTITLE1` | CHAR(50) |  |  |  |  |
| 62 | `COLUMNTITLE2` | CHAR(50) |  |  |  |  |
| 63 | `COLUMNTITLE3` | CHAR(50) |  |  |  |  |
| 64 | `COLUMNTITLE4` | CHAR(50) |  |  |  |  |
| 65 | `COLUMNTITLE5` | CHAR(50) |  |  |  |  |
| 66 | `COLUMNTITLE6` | CHAR(50) |  |  |  |  |
| 67 | `COLUMNTITLE7` | CHAR(50) |  |  |  |  |
| 68 | `COLUMNTITLE8` | CHAR(50) |  |  |  |  |
| 69 | `COLUMNTITLE9` | CHAR(50) |  |  |  |  |
| 70 | `COLUMNTITLE10` | CHAR(50) |  |  |  |  |
| 71 | `COLUMNTITLE11` | CHAR(50) |  |  |  |  |
| 72 | `COLUMNTITLE12` | CHAR(50) |  |  |  |  |
| 73 | `COLUMNTITLE13` | CHAR(50) |  |  |  |  |
| 74 | `CALCULATIONTYPECOL1` | INTEGER | NOT NULL |  |  |  |
| 75 | `CALCULATIONTYPECOL2` | INTEGER | NOT NULL |  |  |  |
| 76 | `CALCULATIONTYPECOL3` | INTEGER | NOT NULL |  |  |  |
| 77 | `CALCULATIONTYPECOL4` | INTEGER | NOT NULL |  |  |  |
| 78 | `CALCULATIONTYPECOL5` | INTEGER | NOT NULL |  |  |  |
| 79 | `CALCULATIONTYPECOL6` | INTEGER | NOT NULL |  |  |  |
| 80 | `CALCULATIONTYPECOL7` | INTEGER | NOT NULL |  |  |  |
| 81 | `CALCULATIONTYPECOL8` | INTEGER | NOT NULL |  |  |  |
| 82 | `CALCULATIONTYPECOL9` | INTEGER | NOT NULL |  |  |  |
| 83 | `CALCULATIONTYPECOL10` | INTEGER | NOT NULL |  |  |  |
| 84 | `CALCULATIONTYPECOL11` | INTEGER | NOT NULL |  |  |  |
| 85 | `CALCULATIONTYPECOL12` | INTEGER | NOT NULL |  |  |  |
| 86 | `CALCULATIONTYPECOL13` | INTEGER | NOT NULL |  |  |  |
| 87 | `TOTALINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 88 | `TOTALMRNVALUE` | DECIMAL(18,5) |  |  |  |  |
| 89 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINPURCHASEREGISTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CREATIONTIMESTAMP,
       t.LINENUMBER,
       t.INVOICELINENO,
       t.DDPIEI,
       t.RCMAPPLICABLE,
       t.NATUREOFSUPPLY,
       t.INVPREFDT,
       t.INVOICENO,
       t.DEBITCREDITNO,
       t.INVOICEDATE
FROM   DB2ADMIN.WRKFINPURCHASEREGISTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
