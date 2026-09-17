# DB2ADMIN.TAXBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 29
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 120658

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(3) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `TYPE` | CHAR(2) |  |  |  |  |
| 7 | `RATE` | DECIMAL(6,3) |  |  |  |  |
| 8 | `USEDFORINTRASTAT` | SMALLINT | NOT NULL |  |  |  |
| 9 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 10 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 11 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 12 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 13 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 14 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 15 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 16 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 18 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 19 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 20 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 21 | `MANAGERATEPERDATE` | SMALLINT | NOT NULL |  |  |  |
| 22 | `EXCLUDEFROMTAXSTAMP` | SMALLINT | NOT NULL |  |  |  |
| 23 | `PLAFONDHANDLING` | CHAR(1) |  |  |  |  |
| 24 | `ART17` | SMALLINT | NOT NULL |  |  |  |
| 25 | `TAXNATURECODE` | CHAR(4) |  |  |  |  |
| 26 | `PAYABILITYCODE` | CHAR(1) |  |  |  |  |
| 27 | `LAWREFERENCE` | VARCHAR(200) |  |  |  |  |
| 28 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TAXBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TYPE,
       t.RATE,
       t.USEDFORINTRASTAT,
       t.WSOPERATION,
       t.IMPOPERATIONUSER,
       t.IMPORTSTATUS
FROM   DB2ADMIN.TAXBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
