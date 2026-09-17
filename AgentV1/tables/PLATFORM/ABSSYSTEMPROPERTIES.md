# DB2ADMIN.ABSSYSTEMPROPERTIES

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 64
- **Primary key**: `SYSPROPKEY`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 61103

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SYSPROPKEY` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 1 | `DEFAULTBATCHQUEUENAME` | CHAR(20) |  | FK | foreign_key |  |
| 2 | `DEFAULTOUTQUEUENAME` | CHAR(20) |  | FK | foreign_key |  |
| 3 | `REMINDERTIMEOUT` | INTEGER | NOT NULL |  |  |  |
| 4 | `LINKSPOOLTODOCCODE` | CHAR(20) |  |  |  |  |
| 5 | `SENDEREMAIL` | CHAR(150) |  |  |  |  |
| 6 | `SENDERSMTPID` | CHAR(150) |  |  |  |  |
| 7 | `SENDERSMTPPWD` | CHAR(20) |  |  |  |  |
| 8 | `SMTPSERVERADDR` | CHAR(64) |  |  |  |  |
| 9 | `SMTPSERVERPORT` | CHAR(5) |  |  |  |  |
| 10 | `SMTPUSETLS` | INTEGER | NOT NULL |  |  |  |
| 11 | `SMTPUSEAUTH` | INTEGER | NOT NULL |  |  |  |
| 12 | `MAILSIGNATURE` | VARCHAR(250) |  |  |  |  |
| 13 | `NOTIFYOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 14 | `NOTIFYRETURNOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 15 | `RETURNRECEIPT` | INTEGER | NOT NULL |  |  |  |
| 16 | `SENDPARTIAL` | SMALLINT | NOT NULL |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `CALENDARSUPPORTCODE` | CHAR(20) |  |  |  |  |
| 19 | `COLOR` | CHAR(9) |  |  |  |  |
| 20 | `EXTERNALCALENDAR` | CHAR(3) |  |  |  |  |
| 21 | `WMONDAY` | SMALLINT | NOT NULL |  |  |  |
| 22 | `WTUESDAY` | SMALLINT | NOT NULL |  |  |  |
| 23 | `WWEDNESDAY` | SMALLINT | NOT NULL |  |  |  |
| 24 | `WTHURSDAY` | SMALLINT | NOT NULL |  |  |  |
| 25 | `WFRIDAY` | SMALLINT | NOT NULL |  |  |  |
| 26 | `WSATURDAY` | SMALLINT | NOT NULL |  |  |  |
| 27 | `WSUNDAY` | SMALLINT | NOT NULL |  |  |  |
| 28 | `FIRSTDAYOFTHEWEEK` | INTEGER | NOT NULL |  |  |  |
| 29 | `ALLOWEVENTSINNOTWORKINGDAYS` | SMALLINT | NOT NULL |  |  |  |
| 30 | `SHOWDESCRIPTIONINHEADER` | SMALLINT | NOT NULL |  |  |  |
| 31 | `DEFAULTVIEW` | CHAR(1) |  |  |  |  |
| 32 | `CALENDARCSS` | VARCHAR(50) |  |  |  |  |
| 33 | `COLUMNHEADERCSS` | VARCHAR(50) |  |  |  |  |
| 34 | `SELECTEDCELLCSS` | VARCHAR(50) |  |  |  |  |
| 35 | `TODAYCELLCSS` | VARCHAR(50) |  |  |  |  |
| 36 | `TODAYCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 37 | `NOTWORKINGDAYCELLCSS` | VARCHAR(50) |  |  |  |  |
| 38 | `NOTWORKINGDAYCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 39 | `PASTWEEKENDCELLCSS` | VARCHAR(50) |  |  |  |  |
| 40 | `PASTWEEKENDCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 41 | `FUTUREWEEKENDCELLCSS` | VARCHAR(50) |  |  |  |  |
| 42 | `FUTUREWEEKENDCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 43 | `WEEKENDCELLCSS` | VARCHAR(50) |  |  |  |  |
| 44 | `WEEKENDCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 45 | `PASTCELLCSS` | VARCHAR(50) |  |  |  |  |
| 46 | `PASTCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 47 | `FUTURECELLCSS` | VARCHAR(50) |  |  |  |  |
| 48 | `FUTURECELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 49 | `WEEKCELLCSS` | VARCHAR(50) |  |  |  |  |
| 50 | `WEEKCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 51 | `SIDEBARPOSITION` | CHAR(1) |  |  |  |  |
| 52 | `SIDEBARHIDDEN` | SMALLINT | NOT NULL |  |  |  |
| 53 | `SIDEBARSTARTCOLLAPSED` | SMALLINT | NOT NULL |  |  |  |
| 54 | `CLICKSTOOPENDESKTOPTILE` | INTEGER | NOT NULL |  |  |  |
| 55 | `CLICKSTOOPENROWINCOLLECTION` | INTEGER | NOT NULL |  |  |  |
| 56 | `SMTPUSEUTF8` | INTEGER | NOT NULL |  |  |  |
| 57 | `SMTPCUSTOMPROPS` | CLOB(1000000) |  |  |  |  |
| 58 | `TRANSLATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 59 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 60 | `COUNTRYCODE` | CHAR(2) |  |  |  |  |
| 61 | `DISABLEINNERGROUPS` | SMALLINT | NOT NULL |  |  |  |
| 62 | `ENABLECELLHIGHLIGHTINGRID` | SMALLINT | NOT NULL |  |  |  |
| 63 | `PLYPRINTINGMODECODE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSBATCHQUEUE_DEFAULTBATCHQUEUE` | `DEFAULTBATCHQUEUENAME` | [`ABSBATCHQUEUE`](../PLATFORM/ABSBATCHQUEUE.md) | `NAME` | RESTRICT | `ABSSYSTEMPROPERTIES.DEFAULTBATCHQUEUENAME = ABSBATCHQUEUE.NAME` |
| `ABSOUTQUEUE_DEFAULTOUTQUEUE` | `DEFAULTOUTQUEUENAME` | [`ABSOUTQUEUE`](../PLATFORM/ABSOUTQUEUE.md) | `NAME` | RESTRICT | `ABSSYSTEMPROPERTIES.DEFAULTOUTQUEUENAME = ABSOUTQUEUE.NAME` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSSYSTEMPROPERTIESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SYSPROPKEY,
       t.DEFAULTBATCHQUEUENAME,
       t.DEFAULTOUTQUEUENAME,
       t.REMINDERTIMEOUT,
       t.LINKSPOOLTODOCCODE,
       t.SENDEREMAIL,
       t.SENDERSMTPID,
       t.SENDERSMTPPWD,
       t.SMTPSERVERADDR,
       t.SMTPSERVERPORT,
       t.SMTPUSETLS,
       t.SMTPUSEAUTH
FROM   DB2ADMIN.ABSSYSTEMPROPERTIES t
FETCH FIRST 100 ROWS ONLY;
```
