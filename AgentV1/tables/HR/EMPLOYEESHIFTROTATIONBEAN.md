# DB2ADMIN.EMPLOYEESHIFTROTATIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `HR` (high confidence — table name starts with 'EMPLOYEE')
- **Roles**: `staging_mirror`
- **Columns**: 28
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 172719

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 3 | `EFFECTIVEDATE` | DATE |  |  |  |  |
| 4 | `SHIFTROTATIONCODE` | CHAR(3) |  |  |  |  |
| 5 | `WEEKLYOFF` | INTEGER | NOT NULL |  |  |  |
| 6 | `FREQUENCY` | INTEGER | NOT NULL |  |  |  |
| 7 | `FREQUENCYDAYS` | DECIMAL(3,0) |  |  |  |  |
| 8 | `SECONDWEEKOFFTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `SPECIFICWEEKS1` | SMALLINT | NOT NULL |  |  |  |
| 10 | `SPECIFICWEEKS2` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SPECIFICWEEKS3` | SMALLINT | NOT NULL |  |  |  |
| 12 | `SPECIFICWEEKS4` | SMALLINT | NOT NULL |  |  |  |
| 13 | `SPECIFICWEEKS5` | SMALLINT | NOT NULL |  |  |  |
| 14 | `SPECIFICWEEKS6` | SMALLINT | NOT NULL |  |  |  |
| 15 | `SECONDWEEKLYOFF` | INTEGER | NOT NULL |  |  |  |
| 16 | `STEP` | CHAR(1) |  |  |  |  |
| 17 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 18 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 19 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 20 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 26 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 27 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPLOYEESHIFTROTATIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.EFFECTIVEDATE,
       t.SHIFTROTATIONCODE,
       t.WEEKLYOFF,
       t.FREQUENCY,
       t.FREQUENCYDAYS,
       t.SECONDWEEKOFFTYPE,
       t.SPECIFICWEEKS1,
       t.SPECIFICWEEKS2,
       t.SPECIFICWEEKS3
FROM   DB2ADMIN.EMPLOYEESHIFTROTATIONBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
