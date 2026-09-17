# DB2ADMIN.TOOLBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 66
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 90969

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 10 | `BASECOSTUNITCODE` | CHAR(3) |  |  |  |  |
| 11 | `COSTCATEGORYCODE` | CHAR(20) |  |  |  |  |
| 12 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |
| 13 | `ELEMENTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `ELEMENTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 15 | `CHOOSEELEMENTSCODE` | CHAR(20) |  |  |  |  |
| 16 | `OWNERTYPE` | CHAR(2) |  |  |  |  |
| 17 | `REUSABLE` | SMALLINT | NOT NULL |  |  |  |
| 18 | `BARTYPECODE` | CHAR(2) |  |  |  |  |
| 19 | `BARCODE` | VARCHAR(50) |  |  |  |  |
| 20 | `DRAWINGNUMBER` | CHAR(100) |  |  |  |  |
| 21 | `MANUFACTURERCODE` | CHAR(15) |  |  |  |  |
| 22 | `STANDARDLIFEUOMCODE` | CHAR(3) |  |  |  |  |
| 23 | `STANDARDLIFEMEASURE` | DECIMAL(15,5) |  |  |  |  |
| 24 | `INTRASTATCODE` | CHAR(11) |  |  |  |  |
| 25 | `LIFOGRPCODE` | CHAR(3) |  |  |  |  |
| 26 | `FOREUSESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 27 | `FOREUSECODE` | CHAR(3) |  |  |  |  |
| 28 | `STOCKTAKESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 29 | `STOCKTAKECODE` | CHAR(3) |  |  |  |  |
| 30 | `REPLENSTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 31 | `REPLENCODE` | CHAR(3) |  |  |  |  |
| 32 | `FAMILYGRPCODE` | CHAR(3) |  |  |  |  |
| 33 | `VALUATIONTYPE` | CHAR(2) |  |  |  |  |
| 34 | `NATURE` | CHAR(2) |  |  |  |  |
| 35 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 36 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 37 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 38 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 39 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 40 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 41 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 42 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 43 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 44 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 45 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 46 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 47 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 48 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 49 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 50 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 51 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 52 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 53 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 54 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 55 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 56 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 57 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 58 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 59 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 60 | `CHECKELEMENTSCODE` | CHAR(20) |  |  |  |  |
| 61 | `BARCODEOUTPUT` | CHAR(1) |  |  |  |  |
| 62 | `QRCODE` | CHAR(200) |  |  |  |  |
| 63 | `QRBARCODE` | CHAR(1) |  |  |  |  |
| 64 | `BARCODECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 65 | `QRCODECHANGED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TOOLBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.BASEPRIMARYUNITCODE,
       t.BASECOSTUNITCODE,
       t.COSTCATEGORYCODE
FROM   DB2ADMIN.TOOLBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
