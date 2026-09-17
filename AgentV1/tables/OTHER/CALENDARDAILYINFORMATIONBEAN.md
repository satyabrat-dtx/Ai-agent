# DB2ADMIN.CALENDARDAILYINFORMATIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 24
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 90713

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `CALENDARYEAR` | INTEGER | NOT NULL |  |  |  |
| 3 | `CALENDARDATE` | DATE |  |  |  |  |
| 4 | `WORKINGDAY` | SMALLINT | NOT NULL |  |  |  |
| 5 | `HOURWORKINGDAY` | DECIMAL(15,5) |  |  |  |  |
| 6 | `DAYOFWEEK` | CHAR(2) |  |  |  |  |
| 7 | `PROGRESSIVEDAYATSTARTYEAR` | INTEGER | NOT NULL |  |  |  |
| 8 | `PROGRESSIVEWRKDAYATSTARTYEAR` | INTEGER | NOT NULL |  |  |  |
| 9 | `PROGRESSIVEDAYATSTARTCALENDAR` | INTEGER | NOT NULL |  |  |  |
| 10 | `PROGRESSIVEWRKDAYATSTARTCLD` | INTEGER | NOT NULL |  |  |  |
| 11 | `PROGRESSIVEWRKHOURSATSTARTYEAR` | DECIMAL(15,5) |  |  |  |  |
| 12 | `PROGRESSIVEWRKHOURSATSTARTCLD` | DECIMAL(15,5) |  |  |  |  |
| 13 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 14 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 15 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 17 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 18 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 19 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 21 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 22 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 23 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `CALENDARDAILYINFORMATIONBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `CLDDAILYINFORMATIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.CALENDARYEAR,
       t.CALENDARDATE,
       t.WORKINGDAY,
       t.HOURWORKINGDAY,
       t.DAYOFWEEK,
       t.PROGRESSIVEDAYATSTARTYEAR,
       t.PROGRESSIVEWRKDAYATSTARTYEAR,
       t.PROGRESSIVEDAYATSTARTCALENDAR,
       t.PROGRESSIVEWRKDAYATSTARTCLD,
       t.PROGRESSIVEWRKHOURSATSTARTYEAR
FROM   DB2ADMIN.CALENDARDAILYINFORMATIONBEAN t
FETCH FIRST 100 ROWS ONLY;
```
