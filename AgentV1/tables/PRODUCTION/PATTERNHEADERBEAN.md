# DB2ADMIN.PATTERNHEADERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (low confidence — table name starts with 'PATTERN')
- **Roles**: `staging_mirror`
- **Columns**: 27
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 91285

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `PATTERNTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 3 | `WARPWEFTTYPE` | CHAR(1) |  |  |  |  |
| 4 | `PATTERNCODE` | CHAR(20) |  |  |  |  |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `HDRNOOFENDS` | DECIMAL(7,0) |  |  |  |  |
| 9 | `HDRNOOFENDSEXTRA` | DECIMAL(11,4) |  |  |  |  |
| 10 | `HDRREEDWIDTH` | DECIMAL(11,4) |  |  |  |  |
| 11 | `HDRREEDWIDTHEXTRA` | DECIMAL(11,4) |  |  |  |  |
| 12 | `HDRWASTEPERCENT` | DECIMAL(5,2) |  |  |  |  |
| 13 | `HDRNOOFYARNSFORUOM` | DECIMAL(11,4) |  |  |  |  |
| 14 | `HDRMULTIPLIER` | DECIMAL(5,0) |  |  |  |  |
| 15 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 16 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 17 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 18 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 19 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 21 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 23 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 24 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 25 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 26 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PATTERNHEADERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.PATTERNTEMPLATECODE,
       t.WARPWEFTTYPE,
       t.PATTERNCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.HDRNOOFENDS,
       t.HDRNOOFENDSEXTRA,
       t.HDRREEDWIDTH,
       t.HDRREEDWIDTHEXTRA
FROM   DB2ADMIN.PATTERNHEADERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
