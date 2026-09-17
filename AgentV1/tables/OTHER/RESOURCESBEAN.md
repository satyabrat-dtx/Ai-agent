# DB2ADMIN.RESOURCESBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 33
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 82889

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `TYPE` | CHAR(1) |  |  |  |  |
| 7 | `BATCHUOMCODE` | CHAR(3) |  |  |  |  |
| 8 | `BATCHMIN` | DECIMAL(15,5) |  |  |  |  |
| 9 | `BATCHMAX` | DECIMAL(15,5) |  |  |  |  |
| 10 | `BATHVOLUMEUOMCODE` | CHAR(3) |  |  |  |  |
| 11 | `BATHVOLUME` | DECIMAL(15,5) |  |  |  |  |
| 12 | `MAXNBROFSCREENSCYLINDERS` | DECIMAL(5,0) |  |  |  |  |
| 13 | `MANUFACTURERCODE` | CHAR(15) |  |  |  |  |
| 14 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 15 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 16 | `PURCHASEDATE` | DATE |  |  |  |  |
| 17 | `NUMBEROFWORKERS` | DECIMAL(3,0) |  |  |  |  |
| 18 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 19 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 20 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 26 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 27 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 28 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 29 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 30 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 31 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 32 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RESOURCESBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TYPE,
       t.BATCHUOMCODE,
       t.BATCHMIN,
       t.BATCHMAX,
       t.BATHVOLUMEUOMCODE,
       t.BATHVOLUME
FROM   DB2ADMIN.RESOURCESBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
