# DB2ADMIN.WRKFINSALESINVOICE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 101
- **Primary key**: `CREATIONTIMESTAMP`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181113

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `LINENUMBER` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 4 | `INVOICENO` | CHAR(30) |  |  |  |  |
| 5 | `INVOICEDATE` | DATE |  |  |  |  |
| 6 | `INVOICETYPEORTEMPLATE` | CHAR(10) |  |  |  |  |
| 7 | `INVPREFDT` | CHAR(10) |  |  |  |  |
| 8 | `DDPISR` | CHAR(20) |  |  |  |  |
| 9 | `LOCATION` | VARCHAR(200) |  |  |  |  |
| 10 | `LOCATIONGSTNO` | CHAR(15) |  |  |  |  |
| 11 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 12 | `PARTYNAME` | VARCHAR(200) |  |  |  |  |
| 13 | `PARTYNAMEBUYER` | VARCHAR(200) |  |  |  |  |
| 14 | `PARTYADDRESS` | VARCHAR(1000) |  |  |  |  |
| 15 | `PARTYADDRESSBUYER` | VARCHAR(1000) |  |  |  |  |
| 16 | `STATECODE` | VARCHAR(200) |  |  |  |  |
| 17 | `STATECODEBUYER` | VARCHAR(200) |  |  |  |  |
| 18 | `GSTIN` | CHAR(50) |  |  |  |  |
| 19 | `GSTINBUYER` | CHAR(50) |  |  |  |  |
| 20 | `GSTNSTATUS` | CHAR(50) |  |  |  |  |
| 21 | `GSTNSTATUSBUYER` | CHAR(50) |  |  |  |  |
| 22 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 23 | `FINDOCNO` | CHAR(15) |  |  |  |  |
| 24 | `FINDOCDATE` | DATE |  |  |  |  |
| 25 | `GLCODE` | CHAR(20) |  |  |  |  |
| 26 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 27 | `WAREHOUSEDESC` | VARCHAR(200) |  |  |  |  |
| 28 | `HSNCODE` | CHAR(20) |  |  |  |  |
| 29 | `PRODUCTLONGDESC` | VARCHAR(200) |  |  |  |  |
| 30 | `PRODUCTCODE` | CHAR(100) |  |  |  |  |
| 31 | `NOOFELEMENTS` | INTEGER | NOT NULL |  |  |  |
| 32 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `UOMCODE` | CHAR(50) |  |  |  |  |
| 34 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 35 | `FREIGHT` | CHAR(10) |  |  |  |  |
| 36 | `TAXCOLUMN1` | DECIMAL(18,5) |  |  |  |  |
| 37 | `TAXCOLUMN2` | DECIMAL(18,5) |  |  |  |  |
| 38 | `TAXCOLUMN3` | DECIMAL(18,5) |  |  |  |  |
| 39 | `TAXCOLUMN4` | DECIMAL(18,5) |  |  |  |  |
| 40 | `TAXCOLUMN5` | DECIMAL(18,5) |  |  |  |  |
| 41 | `TAXCOLUMN6` | DECIMAL(18,5) |  |  |  |  |
| 42 | `TAXCOLUMN7` | DECIMAL(18,5) |  |  |  |  |
| 43 | `TAXCOLUMN8` | DECIMAL(18,5) |  |  |  |  |
| 44 | `TAXCOLUMN9` | DECIMAL(18,5) |  |  |  |  |
| 45 | `TAXCOLUMN10` | DECIMAL(18,5) |  |  |  |  |
| 46 | `TAXCOLUMN11` | DECIMAL(18,5) |  |  |  |  |
| 47 | `TAXCOLUMN12` | DECIMAL(18,5) |  |  |  |  |
| 48 | `TAXCOLUMN13` | DECIMAL(18,5) |  |  |  |  |
| 49 | `SALESORDERNO` | CHAR(20) |  |  |  |  |
| 50 | `SALESORDERDATE` | DATE |  |  |  |  |
| 51 | `REFERENCENO` | CHAR(100) |  |  |  |  |
| 52 | `REVERSECHARGE` | CHAR(50) |  |  |  |  |
| 53 | `INVOICESTATUS` | VARCHAR(200) |  |  |  |  |
| 54 | `SHIPPINGBILLNO` | CHAR(15) |  |  |  |  |
| 55 | `SHIPPINGBILLDATE` | DATE |  |  |  |  |
| 56 | `PORTOFDISCHARGECODE` | CHAR(10) |  |  |  |  |
| 57 | `PORTOFLOADINGCODE` | CHAR(10) |  |  |  |  |
| 58 | `OIARECEIPTNO` | CHAR(15) |  |  |  |  |
| 59 | `OIARECEIPTDATE` | DATE |  |  |  |  |
| 60 | `TYPEOFDOCUMENT` | INTEGER | NOT NULL |  |  |  |
| 61 | `DDDOCUMENTTYPE` | CHAR(20) |  |  |  |  |
| 62 | `DDCOUNTERCODE` | CHAR(10) |  |  |  |  |
| 63 | `DDDOCUMENTNO` | CHAR(15) |  |  |  |  |
| 64 | `COLUMNTITLE1` | CHAR(50) |  |  |  |  |
| 65 | `COLUMNTITLE2` | CHAR(50) |  |  |  |  |
| 66 | `COLUMNTITLE3` | CHAR(50) |  |  |  |  |
| 67 | `COLUMNTITLE4` | CHAR(50) |  |  |  |  |
| 68 | `COLUMNTITLE5` | CHAR(50) |  |  |  |  |
| 69 | `COLUMNTITLE6` | CHAR(50) |  |  |  |  |
| 70 | `COLUMNTITLE7` | CHAR(50) |  |  |  |  |
| 71 | `COLUMNTITLE8` | CHAR(50) |  |  |  |  |
| 72 | `COLUMNTITLE9` | CHAR(50) |  |  |  |  |
| 73 | `COLUMNTITLE10` | CHAR(50) |  |  |  |  |
| 74 | `COLUMNTITLE11` | CHAR(50) |  |  |  |  |
| 75 | `COLUMNTITLE12` | CHAR(50) |  |  |  |  |
| 76 | `COLUMNTITLE13` | CHAR(50) |  |  |  |  |
| 77 | `CALCULATIONTYPECOL1` | INTEGER | NOT NULL |  |  |  |
| 78 | `CALCULATIONTYPECOL2` | INTEGER | NOT NULL |  |  |  |
| 79 | `CALCULATIONTYPECOL3` | INTEGER | NOT NULL |  |  |  |
| 80 | `CALCULATIONTYPECOL4` | INTEGER | NOT NULL |  |  |  |
| 81 | `CALCULATIONTYPECOL5` | INTEGER | NOT NULL |  |  |  |
| 82 | `CALCULATIONTYPECOL6` | INTEGER | NOT NULL |  |  |  |
| 83 | `CALCULATIONTYPECOL7` | INTEGER | NOT NULL |  |  |  |
| 84 | `CALCULATIONTYPECOL8` | INTEGER | NOT NULL |  |  |  |
| 85 | `CALCULATIONTYPECOL9` | INTEGER | NOT NULL |  |  |  |
| 86 | `CALCULATIONTYPECOL10` | INTEGER | NOT NULL |  |  |  |
| 87 | `CALCULATIONTYPECOL11` | INTEGER | NOT NULL |  |  |  |
| 88 | `CALCULATIONTYPECOL12` | INTEGER | NOT NULL |  |  |  |
| 89 | `CALCULATIONTYPECOL13` | INTEGER | NOT NULL |  |  |  |
| 90 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 91 | `PROVISIONALCODE` | CHAR(30) |  |  |  |  |
| 92 | `PROVISIONALDOCUMENTDATE` | DATE |  |  |  |  |
| 93 | `TERMSOFSHIPPINGDESC` | VARCHAR(200) |  |  |  |  |
| 94 | `RATEFC` | DECIMAL(18,5) |  |  |  |  |
| 95 | `EXCHANGERATE` | DECIMAL(18,5) |  |  |  |  |
| 96 | `INRRATE` | DECIMAL(18,5) |  |  |  |  |
| 97 | `BASICVALUEFCY` | DECIMAL(29,9) |  |  |  |  |
| 98 | `BASICVALUEINR` | DECIMAL(29,9) |  |  |  |  |
| 99 | `SALESCOMMISSION` | DECIMAL(29,9) |  |  |  |  |
| 100 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINSALESINVOICEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CREATIONTIMESTAMP,
       t.LINENUMBER,
       t.INVOICENO,
       t.INVOICEDATE,
       t.INVOICETYPEORTEMPLATE,
       t.INVPREFDT,
       t.DDPISR,
       t.LOCATION,
       t.LOCATIONGSTNO,
       t.CUSTOMERCODE
FROM   DB2ADMIN.WRKFINSALESINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
