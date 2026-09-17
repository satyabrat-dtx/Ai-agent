# DB2ADMIN.PRECOMMINVOICELINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 79
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 221344

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `PIREFNO` | BIGINT | NOT NULL |  |  |  |
| 3 | `PILINE` | INTEGER | NOT NULL |  |  |  |
| 4 | `INVOICEDATE` | DATE |  |  |  |  |
| 5 | `INVOICELINENO` | DECIMAL(3,0) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `BUYERSPOREFNO` | CHAR(100) |  |  |  |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 19 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 20 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 21 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 23 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `SECONDARYUMCODE` | CHAR(3) |  |  |  |  |
| 25 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `PACKINGUMCODE` | CHAR(3) |  |  |  |  |
| 27 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 28 | `ORDERPRICE` | DECIMAL(18,5) |  |  |  |  |
| 29 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 30 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 31 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 32 | `PRICELISTORDERTYPE` | CHAR(1) |  |  |  |  |
| 33 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 34 | `INVOICECURRENCYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 35 | `COMPANYCURRENCYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 36 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 38 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 39 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 40 | `INPUTCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 41 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 42 | `WIDTH` | DECIMAL(18,5) |  |  |  |  |
| 43 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 44 | `SIONCODE` | CHAR(15) |  |  |  |  |
| 45 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 46 | `SOLINEABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 47 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 48 | `CBM` | DECIMAL(15,5) |  |  |  |  |
| 49 | `NUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 50 | `LCORDERLINELINENO` | INTEGER | NOT NULL |  |  |  |
| 51 | `LCORDERLINELCDETAILLCNO` | CHAR(35) |  |  |  |  |
| 52 | `LCORDERLINELCDETAILLCDATE` | DATE |  |  |  |  |
| 53 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 54 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 55 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 56 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 57 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 58 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 59 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 60 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 61 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 62 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 63 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 64 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 65 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 66 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 67 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 68 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 69 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 70 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 71 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 72 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 73 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 74 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 75 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 76 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 77 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 78 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **PRECOMMINVOICE**.`ABSUNIQUEID` (high confidence — name = 'PRECOMMINVOICE' + known child suffix 'LINE')
  - JOIN predicate: `PRECOMMINVOICELINEBEAN.FATHERID = PRECOMMINVOICE.ABSUNIQUEID`

## Indexes

- `PRECOMMINVOICELINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.PIREFNO,
       t.PILINE,
       t.INVOICEDATE,
       t.INVOICELINENO,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.PRECOMMINVOICELINEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
