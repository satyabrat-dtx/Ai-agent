# DB2ADMIN.INITIALSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 34
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 199248

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(50) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `SYUSERUSERID` | CHAR(50) |  |  |  |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 9 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 10 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 18 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 21 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 22 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 23 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 25 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 27 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 29 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 31 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 32 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 33 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INITIALSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.SYUSERUSERID,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.OWNINGCOMPANYCODE,
       t.TRANSLATEDLONGDESCRIPTION,
       t.TRANSLATEDLANGUAGECODE,
       t.TRANSLATEDSHORTDESCRIPTION,
       t.CREATIONDATETIME
FROM   DB2ADMIN.INITIALSBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
