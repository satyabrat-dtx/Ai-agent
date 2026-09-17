# DB2ADMIN.ABSCALENDAREVENT

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `INVUUID`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 117597

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INVUUID` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 2 | `EVENTTYPE` | INTEGER | NOT NULL |  |  |  |
| 3 | `TITLE` | CHAR(150) | NOT NULL |  |  |  |
| 4 | `DTSTARTDATE` | DATE |  |  |  |  |
| 5 | `DTSTARTDATEUTC` | TIMESTAMP |  |  |  |  |
| 6 | `DTSTARTTIME` | TIME |  |  |  |  |
| 7 | `DTENDDATE` | DATE |  |  |  |  |
| 8 | `DTENDDATEUTC` | TIMESTAMP |  |  |  |  |
| 9 | `DTENDTIME` | TIME |  |  |  |  |
| 10 | `FULLDAYEVENT` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ZONEID` | CHAR(35) |  |  |  |  |
| 12 | `LOCATION` | VARCHAR(150) |  |  |  |  |
| 13 | `MESSAGEBODY` | CLOB(1000000) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `RELATEDABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSCALENDAREVENT_ATTENDEES` | [`ABSCALENDAREVENTATTENDEE`](../PLATFORM/ABSCALENDAREVENTATTENDEE.md) | `ABSCALENDAREVENTINVUUID` | `ABSCALENDAREVENTATTENDEE.ABSCALENDAREVENTINVUUID = ABSCALENDAREVENT.INVUUID` |
| `ABSCALENDAREVENT_PK` | [`ABSCALENDARLINKEVENT`](../PLATFORM/ABSCALENDARLINKEVENT.md) | `PKINVUUID` | `ABSCALENDARLINKEVENT.PKINVUUID = ABSCALENDAREVENT.INVUUID` |
| `ABSCALENDAREVENT_ATTACHMENTS` | [`ABSCALENDEREVENTATTACH`](../PLATFORM/ABSCALENDEREVENTATTACH.md) | `ABSCALENDAREVENTINVUUID` | `ABSCALENDEREVENTATTACH.ABSCALENDAREVENTINVUUID = ABSCALENDAREVENT.INVUUID` |

## Indexes

- `ABSCALENDAREVENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INVUUID,
       t.STATUS,
       t.EVENTTYPE,
       t.TITLE,
       t.DTSTARTDATE,
       t.DTSTARTDATEUTC,
       t.DTSTARTTIME,
       t.DTENDDATE,
       t.DTENDDATEUTC,
       t.DTENDTIME,
       t.FULLDAYEVENT,
       t.ZONEID
FROM   DB2ADMIN.ABSCALENDAREVENT t
FETCH FIRST 100 ROWS ONLY;
```
