# DB2ADMIN.QUALITYCHARACTERISTICTYPEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `staging_mirror`
- **Columns**: 43
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 116294

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(10) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `DATATYPE` | CHAR(2) |  |  |  |  |
| 7 | `GROUPCODE` | CHAR(3) |  |  |  |  |
| 8 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 9 | `INTERNALSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 10 | `ISOSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 11 | `QACERTIFICATETYPE` | CHAR(2) |  |  |  |  |
| 12 | `QASHOWCERTIFICATE` | CHAR(2) |  |  |  |  |
| 13 | `ALTERNATIVEUOMCODE` | CHAR(3) |  |  |  |  |
| 14 | `SUBCODEMIN` | CHAR(50) |  |  |  |  |
| 15 | `SUBCODEMAX` | CHAR(50) |  |  |  |  |
| 16 | `SUBCODEMEDIOMIN` | CHAR(50) |  |  |  |  |
| 17 | `SUBCODEMEDIOMAX` | CHAR(50) |  |  |  |  |
| 18 | `SUBCODESTANDARD` | CHAR(50) |  |  |  |  |
| 19 | `ADPRODUCTMIN` | CHAR(50) |  |  |  |  |
| 20 | `ADPRODUCTMAX` | CHAR(50) |  |  |  |  |
| 21 | `ADPRODUCTSTD` | CHAR(50) |  |  |  |  |
| 22 | `ADSTEPMIN` | CHAR(50) |  |  |  |  |
| 23 | `ADSTEPMAX` | CHAR(50) |  |  |  |  |
| 24 | `ADSTEPSTD` | CHAR(50) |  |  |  |  |
| 25 | `ADFIKDMIN` | CHAR(50) |  |  |  |  |
| 26 | `ADFIKDMAX` | CHAR(50) |  |  |  |  |
| 27 | `ADFIKDSTD` | CHAR(50) |  |  |  |  |
| 28 | `CHECKCHARACTERISTICCODE` | CHAR(20) |  |  |  |  |
| 29 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 30 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 31 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 32 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 33 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 34 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 35 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 36 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 37 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 38 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 39 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 40 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 41 | `MINMAXINPERCENTAGE` | SMALLINT | NOT NULL |  |  |  |
| 42 | `FORMULACODE` | CHAR(6) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LITYCHARACTERISTICTYPEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DATATYPE,
       t.GROUPCODE,
       t.UOMCODE,
       t.INTERNALSPECIFICATIONCODE,
       t.ISOSPECIFICATIONCODE,
       t.QACERTIFICATETYPE
FROM   DB2ADMIN.QUALITYCHARACTERISTICTYPEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
