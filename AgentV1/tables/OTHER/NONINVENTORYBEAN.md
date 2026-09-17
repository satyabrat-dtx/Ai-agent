# DB2ADMIN.NONINVENTORYBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 45
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 72262

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
| 10 | `INITIALDATE` | DATE |  |  |  |  |
| 11 | `FINALDATE` | DATE |  |  |  |  |
| 12 | `BARTYPECODE` | CHAR(2) |  |  |  |  |
| 13 | `BARCODE` | VARCHAR(50) |  |  |  |  |
| 14 | `DRAWINGNUMBER` | CHAR(30) |  |  |  |  |
| 15 | `MANUFACTURERCODE` | CHAR(15) |  |  |  |  |
| 16 | `INTRASTATCODE` | CHAR(11) |  |  |  |  |
| 17 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 18 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 19 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 21 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 22 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 23 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 24 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 25 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 26 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 27 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 28 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 29 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 30 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 31 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 32 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 33 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 34 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 35 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 36 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 37 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 38 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 39 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 40 | `BARCODEOUTPUT` | CHAR(1) |  |  |  |  |
| 41 | `QRCODE` | CHAR(200) |  |  |  |  |
| 42 | `QRBARCODE` | CHAR(1) |  |  |  |  |
| 43 | `BARCODECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 44 | `QRCODECHANGED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NONINVENTORYBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
       t.INITIALDATE,
       t.FINALDATE
FROM   DB2ADMIN.NONINVENTORYBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
