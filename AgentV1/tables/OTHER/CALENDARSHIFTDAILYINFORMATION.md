# DB2ADMIN.CALENDARSHIFTDAILYINFORMATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `CLDDAILYINFWRKCALENDARCODE`, `CLDDAILYINFCALENDARYEAR`, `CLDDAILYINFCALENDARDATE`, `NUMBERGROUPSHIFT`, `SHIFTNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 5064

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CLDDAILYINFWRKCALENDARCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CLDDAILYINFCALENDARYEAR` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CLDDAILYINFCALENDARDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `NUMBERGROUPSHIFT` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `SHIFTNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `STARTSHIFT` | TIME | NOT NULL |  |  |  |
| 6 | `ENDSHIFT` | TIME | NOT NULL |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CALENDARDAILYINFORMATION_CALENDARSHIFTDAILYINFORMATION` | `CLDDAILYINFWRKCALENDARCODE`, `CLDDAILYINFCALENDARYEAR`, `CLDDAILYINFCALENDARDATE` | [`CALENDARDAILYINFORMATION`](../OTHER/CALENDARDAILYINFORMATION.md) | `WORKINGCALENDARCODE`, `CALENDARYEAR`, `CALENDARDATE` | RESTRICT | `CALENDARSHIFTDAILYINFORMATION.CLDDAILYINFWRKCALENDARCODE = CALENDARDAILYINFORMATION.WORKINGCALENDARCODE AND CALENDARSHIFTDAILYINFORMATION.CLDDAILYINFCALENDARYEAR = CALENDARDAILYINFORMATION.CALENDARYEAR AND CALENDARSHIFTDAILYINFORMATION.CLDDAILYINFCALENDARDATE = CALENDARDAILYINFORMATION.CALENDARDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CLDSHIFTDAILYINFORMATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CLDDAILYINFWRKCALENDARCODE,
       t.CLDDAILYINFCALENDARYEAR,
       t.CLDDAILYINFCALENDARDATE,
       t.NUMBERGROUPSHIFT,
       t.SHIFTNUMBER,
       t.STARTSHIFT,
       t.ENDSHIFT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.CALENDARSHIFTDAILYINFORMATION t
FETCH FIRST 100 ROWS ONLY;
```
