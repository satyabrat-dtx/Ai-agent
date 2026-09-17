# DB2ADMIN.ABSCALENDAR

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 42
- **Primary key**: `CTYPE`, `CALENDARID`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 117486

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `CALENDARID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | description |  |
| 3 | `USEDEFAULTWORKINGDAYS` | SMALLINT | NOT NULL |  |  |  |
| 4 | `COLOR` | CHAR(9) |  |  |  |  |
| 5 | `EXTERNALCALENDAR` | CHAR(3) |  |  |  |  |
| 6 | `WMONDAY` | SMALLINT | NOT NULL |  |  |  |
| 7 | `WTUESDAY` | SMALLINT | NOT NULL |  |  |  |
| 8 | `WWEDNESDAY` | SMALLINT | NOT NULL |  |  |  |
| 9 | `WTHURSDAY` | SMALLINT | NOT NULL |  |  |  |
| 10 | `WFRIDAY` | SMALLINT | NOT NULL |  |  |  |
| 11 | `WSATURDAY` | SMALLINT | NOT NULL |  |  |  |
| 12 | `WSUNDAY` | SMALLINT | NOT NULL |  |  |  |
| 13 | `FIRSTDAYOFTHEWEEK` | INTEGER | NOT NULL |  |  |  |
| 14 | `ALLOWEVENTSINNOTWORKINGDAYS` | SMALLINT | NOT NULL |  |  |  |
| 15 | `SHOWDESCRIPTIONINHEADER` | SMALLINT | NOT NULL |  |  |  |
| 16 | `DEFAULTVIEW` | CHAR(1) |  |  |  |  |
| 17 | `CALENDARCSS` | VARCHAR(50) |  |  |  |  |
| 18 | `COLUMNHEADERCSS` | VARCHAR(50) |  |  |  |  |
| 19 | `SELECTEDCELLCSS` | VARCHAR(50) |  |  |  |  |
| 20 | `TODAYCELLCSS` | VARCHAR(50) |  |  |  |  |
| 21 | `TODAYCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 22 | `NOTWORKINGDAYCELLCSS` | VARCHAR(50) |  |  |  |  |
| 23 | `NOTWORKINGDAYCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 24 | `PASTWEEKENDCELLCSS` | VARCHAR(50) |  |  |  |  |
| 25 | `PASTWEEKENDCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 26 | `FUTUREWEEKENDCELLCSS` | VARCHAR(50) |  |  |  |  |
| 27 | `FUTUREWEEKENDCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 28 | `WEEKENDCELLCSS` | VARCHAR(50) |  |  |  |  |
| 29 | `WEEKENDCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 30 | `PASTCELLCSS` | VARCHAR(50) |  |  |  |  |
| 31 | `PASTCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 32 | `FUTURECELLCSS` | VARCHAR(50) |  |  |  |  |
| 33 | `FUTURECELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 34 | `WEEKCELLCSS` | VARCHAR(50) |  |  |  |  |
| 35 | `WEEKCELLTEXTCSS` | VARCHAR(50) |  |  |  |  |
| 36 | `SIDEBARPOSITION` | CHAR(1) |  |  |  |  |
| 37 | `SIDEBARHIDDEN` | SMALLINT | NOT NULL |  |  |  |
| 38 | `SIDEBARSTARTCOLLAPSED` | SMALLINT | NOT NULL |  |  |  |
| 39 | `CALENDARSESSIONSUPPORTPATH` | VARCHAR(50) |  |  |  |  |
| 40 | `CALENDARSESSIONSUPPORTNAME` | VARCHAR(54) |  |  |  |  |
| 41 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSCALENDAR_AUTHS` | [`ABSCALENDARAUTH`](../PLATFORM/ABSCALENDARAUTH.md) | `CTYPE`, `CALENDARID` | `ABSCALENDARAUTH.CTYPE = ABSCALENDAR.CTYPE AND ABSCALENDARAUTH.CALENDARID = ABSCALENDAR.CALENDARID` |
| `ABSCALENDAR_EVENTS` | [`ABSCALENDARLINKEVENT`](../PLATFORM/ABSCALENDARLINKEVENT.md) | `CTYPE`, `CALENDARID` | `ABSCALENDARLINKEVENT.CTYPE = ABSCALENDAR.CTYPE AND ABSCALENDARLINKEVENT.CALENDARID = ABSCALENDAR.CALENDARID` |

## Indexes

- `ABSCALENDARUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CTYPE,
       t.CALENDARID,
       t.DESCRIPTION,
       t.USEDEFAULTWORKINGDAYS,
       t.COLOR,
       t.EXTERNALCALENDAR,
       t.WMONDAY,
       t.WTUESDAY,
       t.WWEDNESDAY,
       t.WTHURSDAY,
       t.WFRIDAY,
       t.WSATURDAY
FROM   DB2ADMIN.ABSCALENDAR t
FETCH FIRST 100 ROWS ONLY;
```
