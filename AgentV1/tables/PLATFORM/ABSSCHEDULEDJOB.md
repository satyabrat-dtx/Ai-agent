# DB2ADMIN.ABSSCHEDULEDJOB

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 40
- **Primary key**: `JOBNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70561

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `JOBNUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 2 | `QUEUENAME` | CHAR(50) |  |  |  |  |
| 3 | `DESCRIPTION` | CHAR(150) |  |  | description |  |
| 4 | `JNDINAME` | CHAR(100) |  |  |  |  |
| 5 | `XMLNAME` | CHAR(105) |  |  |  |  |
| 6 | `PRINCIPAL` | CHAR(50) |  |  |  |  |
| 7 | `PRIORITYONQUEUE` | INTEGER | NOT NULL |  |  |  |
| 8 | `OUTPUTQUEUE` | CHAR(20) |  | FK | foreign_key |  |
| 9 | `SUBMITTEDDATE` | DATE |  |  |  |  |
| 10 | `SUBMITTEDTIME` | TIME |  |  |  |  |
| 11 | `JOBDATA` | BLOB(1000000) |  |  |  |  |
| 12 | `SCHEDULETYPE` | INTEGER | NOT NULL |  |  |  |
| 13 | `STARTDATE` | DATE | NOT NULL |  |  |  |
| 14 | `ENDDATE` | DATE |  |  |  |  |
| 15 | `STARTTIME` | TIME | NOT NULL |  |  |  |
| 16 | `NEXTSCHEDULE` | TIMESTAMP |  |  |  |  |
| 17 | `EMONDAY` | SMALLINT | NOT NULL |  |  |  |
| 18 | `ETUESDAY` | SMALLINT | NOT NULL |  |  |  |
| 19 | `EWEDNESDAY` | SMALLINT | NOT NULL |  |  |  |
| 20 | `ETHURSDAY` | SMALLINT | NOT NULL |  |  |  |
| 21 | `EFRIDAY` | SMALLINT | NOT NULL |  |  |  |
| 22 | `ESATURDAY` | SMALLINT | NOT NULL |  |  |  |
| 23 | `ESUNDAY` | SMALLINT | NOT NULL |  |  |  |
| 24 | `EDAYINMONTH` | INTEGER | NOT NULL |  |  |  |
| 25 | `EJAN` | SMALLINT | NOT NULL |  |  |  |
| 26 | `EFEB` | SMALLINT | NOT NULL |  |  |  |
| 27 | `EMAR` | SMALLINT | NOT NULL |  |  |  |
| 28 | `EAPR` | SMALLINT | NOT NULL |  |  |  |
| 29 | `EMAY` | SMALLINT | NOT NULL |  |  |  |
| 30 | `EJUN` | SMALLINT | NOT NULL |  |  |  |
| 31 | `EJUL` | SMALLINT | NOT NULL |  |  |  |
| 32 | `EAUG` | SMALLINT | NOT NULL |  |  |  |
| 33 | `ESEP` | SMALLINT | NOT NULL |  |  |  |
| 34 | `EOCT` | SMALLINT | NOT NULL |  |  |  |
| 35 | `ENOV` | SMALLINT | NOT NULL |  |  |  |
| 36 | `EDIC` | SMALLINT | NOT NULL |  |  |  |
| 37 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 38 | `SUBMITTEDDATETIME` | TIMESTAMP |  |  |  |  |
| 39 | `SUBMITTEDDATETIMEUTC` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSOUTQUEUE_OUTPUTQUEUE` | `OUTPUTQUEUE` | [`ABSOUTQUEUE`](../PLATFORM/ABSOUTQUEUE.md) | `NAME` | RESTRICT | `ABSSCHEDULEDJOB.OUTPUTQUEUE = ABSOUTQUEUE.NAME` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSSCHEDULEDJOBUID` (ABSUNIQUEID)
- `ABSSCHEDDJOBIDX1` (STATUS, NEXTSCHEDULE)

## Starter query

```sql
SELECT t.JOBNUMBER,
       t.STATUS,
       t.QUEUENAME,
       t.DESCRIPTION,
       t.JNDINAME,
       t.XMLNAME,
       t.PRINCIPAL,
       t.PRIORITYONQUEUE,
       t.OUTPUTQUEUE,
       t.SUBMITTEDDATE,
       t.SUBMITTEDTIME,
       t.JOBDATA
FROM   DB2ADMIN.ABSSCHEDULEDJOB t
FETCH FIRST 100 ROWS ONLY;
```
