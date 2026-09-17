# DB2ADMIN.WFMINBOXMAILACTIONAUDIT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `JOBNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189871

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `JOBNUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `EVENTDATE` | DATE | NOT NULL |  |  |  |
| 2 | `EVENTTIME` | TIME | NOT NULL |  |  |  |
| 3 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 4 | `ERRORFAULT` | CHAR(20) |  |  |  |  |
| 5 | `ERRORFAULTDETAIL` | CHAR(65) |  |  |  |  |
| 6 | `EMAILSERVERADDR` | CHAR(64) |  |  |  |  |
| 7 | `EMAILSERVERPORT` | CHAR(5) |  |  |  |  |
| 8 | `EMAILSERVERPROTOCOL` | CHAR(15) |  |  |  |  |
| 9 | `SENDEREMAIL` | CHAR(150) |  |  |  |  |
| 10 | `EMAILSENTDATE` | TIMESTAMP |  |  |  |  |
| 11 | `EMAILRECEIVINGDATE` | TIMESTAMP |  |  |  |  |
| 12 | `MAILSUBJECT` | VARCHAR(250) | NOT NULL |  |  |  |
| 13 | `MAILEML` | CLOB(1000000) |  |  |  |  |
| 14 | `INBOXFOLDERNAME` | VARCHAR(250) | NOT NULL |  |  |  |
| 15 | `DESTINATIONFOLDERNAME` | VARCHAR(250) |  |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `TASKID` | CHAR(120) |  |  |  |  |
| 18 | `PROCESSDEFINITIONID` | CHAR(120) |  |  |  |  |
| 19 | `EMAILUSER` | CHAR(150) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WFMINBOXMAILACTIONAUDITUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.JOBNUMBER,
       t.EVENTDATE,
       t.EVENTTIME,
       t.STATUS,
       t.ERRORFAULT,
       t.ERRORFAULTDETAIL,
       t.EMAILSERVERADDR,
       t.EMAILSERVERPORT,
       t.EMAILSERVERPROTOCOL,
       t.SENDEREMAIL,
       t.EMAILSENTDATE,
       t.EMAILRECEIVINGDATE
FROM   DB2ADMIN.WFMINBOXMAILACTIONAUDIT t
FETCH FIRST 100 ROWS ONLY;
```
