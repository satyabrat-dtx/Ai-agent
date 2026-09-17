# DB2ADMIN.SKETCHBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 50
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235391

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(10) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 8 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 10 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 11 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 12 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `PRODUCTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 22 | `COPYFROM` | SMALLINT | NOT NULL |  |  |  |
| 23 | `SKETCHTEMPLATECODE` | CHAR(10) |  |  |  |  |
| 24 | `MEASURE` | DECIMAL(5,2) |  |  |  |  |
| 25 | `TOLERANCEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 26 | `SKETCHPARTDETAILIMAGE` | CHAR(1) |  |  |  |  |
| 27 | `TYPE` | CHAR(20) |  |  |  |  |
| 28 | `MATRIXDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 29 | `COMPONENTMATRIXMANAGEMENT` | INTEGER | NOT NULL |  |  |  |
| 30 | `FILTERON` | SMALLINT | NOT NULL |  |  |  |
| 31 | `MATRIXROWNR` | INTEGER | NOT NULL |  |  |  |
| 32 | `MATRIXCOLUMNNR` | INTEGER | NOT NULL |  |  |  |
| 33 | `MATRIXLABEL` | CHAR(100) |  |  |  |  |
| 34 | `PREVIOUSGB` | BLOB(1000000) |  |  |  |  |
| 35 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 36 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 37 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 38 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 39 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 40 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 41 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 42 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 43 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 44 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 45 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 46 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 47 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 48 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 49 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SKETCHBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ITEMTYPECODE,
       t.ITEMCODE,
       t.PROTOTYPE,
       t.PROTOTYPEPROJECT,
       t.PROTOTYPEVERSION,
       t.SUBCODE01
FROM   DB2ADMIN.SKETCHBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
