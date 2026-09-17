# DB2ADMIN.FINDOCUMENTLINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 72
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 204244

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 3 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `GLCODE` | CHAR(20) |  |  |  |  |
| 6 | `CREDITLINE` | SMALLINT | NOT NULL |  |  |  |
| 7 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 8 | `DIRECTENTRY` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `AMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 12 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 13 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 14 | `AMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 15 | `COMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 16 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 17 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 18 | `PROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 19 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 20 | `COMMENTS` | VARCHAR(255) |  |  |  |  |
| 21 | `DESTINATIONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `ICFDLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `ICFDLBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 24 | `ICFDLFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 25 | `ICFDLDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 26 | `ICFDLSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 27 | `ICFDLCODE` | CHAR(15) |  |  |  |  |
| 28 | `REFERENCETEXT1` | CHAR(100) |  |  |  |  |
| 29 | `REFERENCETEXT2` | CHAR(50) |  |  |  |  |
| 30 | `REFERENCETEXT3` | CHAR(50) |  |  |  |  |
| 31 | `REFERENCETEXT4` | CHAR(50) |  |  |  |  |
| 32 | `REFERENCETEXT5` | CHAR(50) |  |  |  |  |
| 33 | `FIRSTUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 34 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 35 | `SNDUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 36 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 37 | `THIRDUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 39 | `FRUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 40 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 41 | `FIFTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 42 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 43 | `SIXTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 44 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 45 | `SEUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 46 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 47 | `REFERENCEAMT1` | DECIMAL(18,5) |  |  |  |  |
| 48 | `REFERENCEAMT2` | DECIMAL(18,5) |  |  |  |  |
| 49 | `REFERENCEAMT3` | DECIMAL(18,5) |  |  |  |  |
| 50 | `REFERENCEAMT4` | DECIMAL(18,5) |  |  |  |  |
| 51 | `REFERENCEAMT5` | DECIMAL(18,5) |  |  |  |  |
| 52 | `RECONCILIATIONDATE` | DATE |  |  |  |  |
| 53 | `RECONCILEDBY` | CHAR(50) |  |  |  |  |
| 54 | `RECONCILETRANNO` | CHAR(15) |  |  |  |  |
| 55 | `RECONCILEDON` | TIMESTAMP |  |  |  |  |
| 56 | `ASSETNOCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 57 | `ASSETNOCODE` | CHAR(15) |  |  |  |  |
| 58 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 59 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 60 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 61 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 62 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 63 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 64 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 65 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 66 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 67 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 68 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 69 | `DESTBUCODE` | CHAR(10) |  |  |  |  |
| 70 | `ICGLCODE` | CHAR(20) |  |  |  |  |
| 71 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **FINDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'FINDOCUMENT' + known child suffix 'LINE')
  - JOIN predicate: `FINDOCUMENTLINEBEAN.FATHERID = FINDOCUMENT.ABSUNIQUEID`

## Indexes

- `FINDOCUMENTLINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINENUMBER,
       t.LINETEMPLATECODE,
       t.COMPANYCODE,
       t.GLCODE,
       t.CREDITLINE,
       t.CURRENTSTATUS,
       t.DIRECTENTRY,
       t.SLCUSTOMERSUPPLIERTYPE,
       t.SLCUSTOMERSUPPLIERCODE,
       t.AMOUNTINDC
FROM   DB2ADMIN.FINDOCUMENTLINEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
