# DB2ADMIN.DIRECTINVOICEDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 56
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 218580

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 16 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 18 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 19 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 20 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 22 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 23 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 24 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |
| 25 | `REFERENCETEXT2` | CHAR(20) |  |  |  |  |
| 26 | `REFERENCETEXT3` | CHAR(20) |  |  |  |  |
| 27 | `REFERENCETEXT4` | CHAR(20) |  |  |  |  |
| 28 | `REFERENCETEXT5` | CHAR(20) |  |  |  |  |
| 29 | `FIRSTUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 30 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 31 | `SNDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 32 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 33 | `THIRDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 34 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 35 | `FRUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 36 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 37 | `FIFTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 39 | `SIXTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 40 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 41 | `SEUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 42 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 43 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 44 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 45 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 46 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 47 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 48 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 49 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 50 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 51 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 52 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 53 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 54 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 55 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **DIRECTINVOICE**.`ABSUNIQUEID` (high confidence — name = 'DIRECTINVOICE' + known child suffix 'DETAIL')
  - JOIN predicate: `DIRECTINVOICEDETAILBEAN.FATHERID = DIRECTINVOICE.ABSUNIQUEID`

## Indexes

- `DIRECTINVOICEDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINENO,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.DIRECTINVOICEDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
