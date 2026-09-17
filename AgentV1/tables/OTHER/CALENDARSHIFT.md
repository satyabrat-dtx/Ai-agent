# DB2ADMIN.CALENDARSHIFT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `WORKINGCALENDARCODE`, `NUMBERWORKINGDAY`, `NUMBERGROUPSHIFT`, `NUMBERSHIFT`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 5719

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WORKINGCALENDARCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `NUMBERWORKINGDAY` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `NUMBERGROUPSHIFT` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `NUMBERSHIFT` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `STARTSHIFT` | TIME | NOT NULL |  |  |  |
| 5 | `ENDSHIFT` | TIME | NOT NULL |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `WORKINGCALENDAR_CALENDARSHIFT` | `WORKINGCALENDARCODE` | [`WORKINGCALENDAR`](../CORE_MASTER/WORKINGCALENDAR.md) | `CODE` | RESTRICT | `CALENDARSHIFT.WORKINGCALENDARCODE = WORKINGCALENDAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CALENDARSHIFTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.WORKINGCALENDARCODE,
       t.NUMBERWORKINGDAY,
       t.NUMBERGROUPSHIFT,
       t.NUMBERSHIFT,
       t.STARTSHIFT,
       t.ENDSHIFT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.CALENDARSHIFT t
FETCH FIRST 100 ROWS ONLY;
```
