# DB2ADMIN.CALENDARDAILYINFORMATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `WORKINGCALENDARCODE`, `CALENDARYEAR`, `CALENDARDATE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 15074

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WORKINGCALENDARCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CALENDARYEAR` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CALENDARDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `WORKINGDAY` | SMALLINT | NOT NULL |  |  |  |
| 4 | `HOURWORKINGDAY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 5 | `DAYOFWEEK` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `PROGRESSIVEDAYATSTARTYEAR` | INTEGER | NOT NULL |  |  |  |
| 7 | `PROGRESSIVEWRKDAYATSTARTYEAR` | INTEGER | NOT NULL |  |  |  |
| 8 | `PROGRESSIVEDAYATSTARTCALENDAR` | INTEGER | NOT NULL |  |  |  |
| 9 | `PROGRESSIVEWRKDAYATSTARTCLD` | INTEGER | NOT NULL |  |  |  |
| 10 | `PROGRESSIVEWRKHOURSATSTARTYEAR` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 11 | `PROGRESSIVEWRKHOURSATSTARTCLD` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `WORKINGCALENDAR_CALENDARDAILYINFORMATION` | `WORKINGCALENDARCODE` | [`WORKINGCALENDAR`](../CORE_MASTER/WORKINGCALENDAR.md) | `CODE` | RESTRICT | `CALENDARDAILYINFORMATION.WORKINGCALENDARCODE = WORKINGCALENDAR.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `CALENDARDAILYINFORMATION_CALENDARSHIFTDAILYINFORMATION` | [`CALENDARSHIFTDAILYINFORMATION`](../OTHER/CALENDARSHIFTDAILYINFORMATION.md) | `CLDDAILYINFWRKCALENDARCODE`, `CLDDAILYINFCALENDARYEAR`, `CLDDAILYINFCALENDARDATE` | `CALENDARSHIFTDAILYINFORMATION.CLDDAILYINFWRKCALENDARCODE = CALENDARDAILYINFORMATION.WORKINGCALENDARCODE AND CALENDARSHIFTDAILYINFORMATION.CLDDAILYINFCALENDARYEAR = CALENDARDAILYINFORMATION.CALENDARYEAR AND CALENDARSHIFTDAILYINFORMATION.CLDDAILYINFCALENDARDATE = CALENDARDAILYINFORMATION.CALENDARDATE` |

## Indexes

- `CALENDARDAILYINFORMATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.WORKINGCALENDARCODE,
       t.CALENDARYEAR,
       t.CALENDARDATE,
       t.WORKINGDAY,
       t.HOURWORKINGDAY,
       t.DAYOFWEEK,
       t.PROGRESSIVEDAYATSTARTYEAR,
       t.PROGRESSIVEWRKDAYATSTARTYEAR,
       t.PROGRESSIVEDAYATSTARTCALENDAR,
       t.PROGRESSIVEWRKDAYATSTARTCLD,
       t.PROGRESSIVEWRKHOURSATSTARTYEAR,
       t.PROGRESSIVEWRKHOURSATSTARTCLD
FROM   DB2ADMIN.CALENDARDAILYINFORMATION t
FETCH FIRST 100 ROWS ONLY;
```
