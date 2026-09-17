# DB2ADMIN.DESIGNBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 61
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 71758

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `DESIGNTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 18 | `GENERICDESIGN` | SMALLINT | NOT NULL |  |  |  |
| 19 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 20 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 21 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 22 | `IMAGENAME` | CHAR(80) |  |  |  |  |
| 23 | `IMAGEPATH` | CHAR(30) |  |  |  |  |
| 24 | `GENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 25 | `VALIDFROMDATE` | DATE |  |  |  |  |
| 26 | `VALIDTODATE` | DATE |  |  |  |  |
| 27 | `STANDARDBATCHSIZE` | DECIMAL(15,5) |  |  |  |  |
| 28 | `STANDARDBATCHSIZEUMCODE` | CHAR(3) |  |  |  |  |
| 29 | `NUMBEROFSCREENS` | INTEGER | NOT NULL |  |  |  |
| 30 | `HANDLESCREENS` | CHAR(2) |  |  |  |  |
| 31 | `RESERVATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 32 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 33 | `AVERAGESCREENLIFEINUM` | INTEGER | NOT NULL |  |  |  |
| 34 | `AVERAGESCREENLIFEINMONTH` | INTEGER | NOT NULL |  |  |  |
| 35 | `COSTELMFORSCREENITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 36 | `COSTELEMENTFORSCREENSUBCODE01` | CHAR(20) |  |  |  |  |
| 37 | `COSTELMFORINTRESTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `COSTELEMENTFORINTRESTSUBCODE01` | CHAR(20) |  |  |  |  |
| 39 | `SCREENSTANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 40 | `STATUS` | CHAR(1) |  |  |  |  |
| 41 | `APPROVALDATE` | DATE |  |  |  |  |
| 42 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 43 | `RELEASEDATE` | DATE |  |  |  |  |
| 44 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 45 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 46 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 47 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 48 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 49 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 50 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 51 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 52 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 53 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 54 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 55 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 56 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 57 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 58 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 59 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 60 | `ARTICLESTATUSCODE` | CHAR(8) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DESIGNBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.NUMBERID,
       t.ITEMTYPECODE,
       t.DESIGNTEMPLATECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.DESIGNBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
