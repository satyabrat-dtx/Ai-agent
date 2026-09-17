# DB2ADMIN.NETCURDAILYEXCHAGERATEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `staging_mirror`
- **Columns**: 32
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239540

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `ORIGINCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 2 | `REFERENCEDCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 3 | `INITIALDATE` | DATE |  |  |  |  |
| 4 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 5 | `PURCHASEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 6 | `SALESEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 7 | `VALUATIONEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 8 | `SALESTAXLISTEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 9 | `REPORTINGEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 17 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 20 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 21 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 22 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 23 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 24 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 26 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 28 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 29 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 30 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 31 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETCURDAILYEXCHAGERATEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.ORIGINCURRENCYCODE,
       t.REFERENCEDCURRENCYCODE,
       t.INITIALDATE,
       t.EXCHANGERATE,
       t.PURCHASEEXCHANGERATE,
       t.SALESEXCHANGERATE,
       t.VALUATIONEXCHANGERATE,
       t.SALESTAXLISTEXCHANGERATE,
       t.REPORTINGEXCHANGERATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.NETCURDAILYEXCHAGERATEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
