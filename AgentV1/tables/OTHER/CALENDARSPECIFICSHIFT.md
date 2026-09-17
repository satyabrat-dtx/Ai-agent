# DB2ADMIN.CALENDARSPECIFICSHIFT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `WORKINGCALENDARCODE`, `YEAR`, `NUMBERMONTH`, `NUMBERDAY`, `NUMBERGROUPSHIFT`, `NUMBERSHIFT`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 17683

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WORKINGCALENDARCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `NUMBERMONTH` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `NUMBERDAY` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `NUMBERGROUPSHIFT` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `NUMBERSHIFT` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `STARTSHIFT` | TIME | NOT NULL |  |  |  |
| 6 | `ENDSHIFT` | TIME | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `YEAR` | INTEGER | NOT NULL | PK | primary_key |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `WORKINGCALENDAR_CALENDARSPECIFICSHIFT` | `WORKINGCALENDARCODE` | [`WORKINGCALENDAR`](../CORE_MASTER/WORKINGCALENDAR.md) | `CODE` | RESTRICT | `CALENDARSPECIFICSHIFT.WORKINGCALENDARCODE = WORKINGCALENDAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CALENDARSPECIFICSHIFTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.WORKINGCALENDARCODE,
       t.NUMBERMONTH,
       t.NUMBERDAY,
       t.NUMBERGROUPSHIFT,
       t.NUMBERSHIFT,
       t.STARTSHIFT,
       t.ENDSHIFT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.YEAR
FROM   DB2ADMIN.CALENDARSPECIFICSHIFT t
FETCH FIRST 100 ROWS ONLY;
```
