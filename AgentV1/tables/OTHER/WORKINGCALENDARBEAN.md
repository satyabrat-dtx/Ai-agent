# DB2ADMIN.WORKINGCALENDARBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 31
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 91174

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `CODE` | CHAR(3) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `FIRSTDAYOFWEEK` | CHAR(2) |  |  |  |  |
| 3 | `STARTHOURWORKINGDAY` | TIME |  |  |  |  |
| 4 | `WORKINGDAYMONDAY` | SMALLINT | NOT NULL |  |  |  |
| 5 | `WORKINGDAYTUESDAY` | SMALLINT | NOT NULL |  |  |  |
| 6 | `WORKINGDAYWEDNESDAY` | SMALLINT | NOT NULL |  |  |  |
| 7 | `WORKINGDAYTHURSDAY` | SMALLINT | NOT NULL |  |  |  |
| 8 | `WORKINGDAYFRIDAY` | SMALLINT | NOT NULL |  |  |  |
| 9 | `WORKINGDAYSATURDAY` | SMALLINT | NOT NULL |  |  |  |
| 10 | `WORKINGDAYSUNDAY` | SMALLINT | NOT NULL |  |  |  |
| 11 | `REGENERATEFROMDATE` | DATE |  |  |  |  |
| 12 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 13 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 14 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 15 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 16 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 17 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 18 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 24 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 25 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 26 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 27 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 28 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 29 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 30 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WORKINGCALENDARBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.CODE,
       t.FIRSTDAYOFWEEK,
       t.STARTHOURWORKINGDAY,
       t.WORKINGDAYMONDAY,
       t.WORKINGDAYTUESDAY,
       t.WORKINGDAYWEDNESDAY,
       t.WORKINGDAYTHURSDAY,
       t.WORKINGDAYFRIDAY,
       t.WORKINGDAYSATURDAY,
       t.WORKINGDAYSUNDAY,
       t.REGENERATEFROMDATE
FROM   DB2ADMIN.WORKINGCALENDARBEAN t
FETCH FIRST 100 ROWS ONLY;
```
