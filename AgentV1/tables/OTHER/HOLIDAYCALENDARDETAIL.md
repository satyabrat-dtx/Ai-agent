# DB2ADMIN.HOLIDAYCALENDARDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `HOLIDAYCALENDARCOMPANYCODE`, `HOLIDAYCALENDARCODE`, `HOLIDAYDATE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 153596

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `HOLIDAYCALENDARCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `HOLIDAYCALENDARCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `HOLIDAYDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `TYPEOFHOLIDAY` | INTEGER | NOT NULL |  |  |  |
| 7 | `DAYSBEFOREHOLIDAY` | DECIMAL(3,2) | NOT NULL |  |  |  |
| 8 | `DAYSAFTERHOLIDAY` | DECIMAL(3,2) | NOT NULL |  |  |  |
| 9 | `ISWEEKLYOFFOVERLAPPINGALLOWED` | INTEGER | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `HOLIDAYCALENDAR_LINE` | `HOLIDAYCALENDARCOMPANYCODE`, `HOLIDAYCALENDARCODE` | [`HOLIDAYCALENDAR`](../OTHER/HOLIDAYCALENDAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `HOLIDAYCALENDARDETAIL.HOLIDAYCALENDARCOMPANYCODE = HOLIDAYCALENDAR.COMPANYCODE AND HOLIDAYCALENDARDETAIL.HOLIDAYCALENDARCODE = HOLIDAYCALENDAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `HOLIDAYCALENDARDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.HOLIDAYCALENDARCOMPANYCODE,
       t.HOLIDAYCALENDARCODE,
       t.HOLIDAYDATE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TYPEOFHOLIDAY,
       t.DAYSBEFOREHOLIDAY,
       t.DAYSAFTERHOLIDAY,
       t.ISWEEKLYOFFOVERLAPPINGALLOWED,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.HOLIDAYCALENDARDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
