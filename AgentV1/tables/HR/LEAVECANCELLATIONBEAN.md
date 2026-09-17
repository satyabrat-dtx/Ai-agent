# DB2ADMIN.LEAVECANCELLATIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `HR` (high confidence — table name starts with 'LEAVE')
- **Roles**: `staging_mirror`
- **Columns**: 30
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 173367

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LEAVECALENDARCALENDARCODE` | CHAR(3) |  |  |  |  |
| 3 | `EMPLOYEECODE` | CHAR(9) |  |  |  |  |
| 4 | `LEAVECODE` | CHAR(3) |  |  |  |  |
| 5 | `CANCELLATIONSERIALNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 6 | `CANCELLATIONFROMDATE` | DATE |  |  |  |  |
| 7 | `CANCELLATIONTODATE` | DATE |  |  |  |  |
| 8 | `SESSIONLEAVECANCELFROM` | INTEGER | NOT NULL |  |  |  |
| 9 | `SESSIONLEAVECANCELTO` | INTEGER | NOT NULL |  |  |  |
| 10 | `NOOFLEAVEDAYS` | DECIMAL(5,2) |  |  |  |  |
| 11 | `CANCELLATIONREASON` | VARCHAR(1000) |  |  |  |  |
| 12 | `LEAVECANCELAPPROVEDBYCODE` | CHAR(9) |  |  |  |  |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 15 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 18 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 19 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 20 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 21 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 22 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 26 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 28 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 29 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LEAVECANCELLATIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.LEAVECALENDARCALENDARCODE,
       t.EMPLOYEECODE,
       t.LEAVECODE,
       t.CANCELLATIONSERIALNUMBER,
       t.CANCELLATIONFROMDATE,
       t.CANCELLATIONTODATE,
       t.SESSIONLEAVECANCELFROM,
       t.SESSIONLEAVECANCELTO,
       t.NOOFLEAVEDAYS,
       t.CANCELLATIONREASON
FROM   DB2ADMIN.LEAVECANCELLATIONBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
