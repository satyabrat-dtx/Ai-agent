# DB2ADMIN.SCLDIRECTORYBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 20
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 99468

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COUNTRYISOCODE` | CHAR(2) |  |  |  |  |
| 2 | `BIC` | CHAR(11) |  |  |  |  |
| 3 | `DESCRIPTION` | CHAR(100) |  |  | description |  |
| 4 | `SCT` | SMALLINT | NOT NULL |  |  |  |
| 5 | `SDD` | SMALLINT | NOT NULL |  |  |  |
| 6 | `COR1` | SMALLINT | NOT NULL |  |  |  |
| 7 | `B2B` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SCC` | SMALLINT | NOT NULL |  |  |  |
| 9 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 10 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 11 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 12 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 13 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 14 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 15 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 17 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 18 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 19 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COUNTRYISOCODE,
       t.BIC,
       t.DESCRIPTION,
       t.SCT,
       t.SDD,
       t.COR1,
       t.B2B,
       t.SCC,
       t.WSOPERATION,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME
FROM   DB2ADMIN.SCLDIRECTORYBEAN t
FETCH FIRST 100 ROWS ONLY;
```
