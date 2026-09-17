# DB2ADMIN.PDMCUSTOMIZEDOPTIONSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `staging_mirror`
- **Columns**: 36
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 106426

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `SUBCODEPOLICYREFERENCECODE` | CHAR(20) |  |  |  |  |
| 3 | `PDM2QUALITYBARCODETYPE` | CHAR(10) |  |  |  |  |
| 4 | `BARCODEADENTITYNAME` | CHAR(50) |  |  |  |  |
| 5 | `BARCODEADNAME` | CHAR(50) |  |  |  |  |
| 6 | `LANGUAGEFORERRORSCODE` | CHAR(2) |  |  |  |  |
| 7 | `EXPORTENVIRONMENTCODE` | CHAR(10) |  |  |  |  |
| 8 | `EXISTSRTGPOLICYREFERENCECODE` | CHAR(20) |  |  |  |  |
| 9 | `GENERICSIZETYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `TECHDATATOFIKD` | SMALLINT | NOT NULL |  |  |  |
| 11 | `COLORHANDLING` | CHAR(1) |  |  |  |  |
| 12 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 13 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 14 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 15 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 16 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 18 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 20 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 21 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 22 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 23 | `EXPORTQADOCUMENT` | SMALLINT | NOT NULL |  |  |  |
| 24 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 25 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 26 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 27 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 28 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 31 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 32 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 33 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 34 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 35 | `BOMCMPMULTIPLERULE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PDMCUSTOMIZEDOPTIONSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.SUBCODEPOLICYREFERENCECODE,
       t.PDM2QUALITYBARCODETYPE,
       t.BARCODEADENTITYNAME,
       t.BARCODEADNAME,
       t.LANGUAGEFORERRORSCODE,
       t.EXPORTENVIRONMENTCODE,
       t.EXISTSRTGPOLICYREFERENCECODE,
       t.GENERICSIZETYPECODE,
       t.TECHDATATOFIKD,
       t.COLORHANDLING
FROM   DB2ADMIN.PDMCUSTOMIZEDOPTIONSBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
