# DB2ADMIN.ABSCALENDARLINKEVENT

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `CTYPE`, `CALENDARID`, `PKINVUUID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 117688

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CTYPE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CALENDARID` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PKINVUUID` | VARCHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSCALENDAREVENT_PK` | `PKINVUUID` | [`ABSCALENDAREVENT`](../PLATFORM/ABSCALENDAREVENT.md) | `INVUUID` | RESTRICT | `ABSCALENDARLINKEVENT.PKINVUUID = ABSCALENDAREVENT.INVUUID` |
| `ABSCALENDAR_EVENTS` | `CTYPE`, `CALENDARID` | [`ABSCALENDAR`](../PLATFORM/ABSCALENDAR.md) | `CTYPE`, `CALENDARID` | RESTRICT | `ABSCALENDARLINKEVENT.CTYPE = ABSCALENDAR.CTYPE AND ABSCALENDARLINKEVENT.CALENDARID = ABSCALENDAR.CALENDARID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSCALENDARLINKEVENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CTYPE,
       t.CALENDARID,
       t.PKINVUUID,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSCALENDARLINKEVENT t
FETCH FIRST 100 ROWS ONLY;
```
