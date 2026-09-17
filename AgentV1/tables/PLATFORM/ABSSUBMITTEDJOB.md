# DB2ADMIN.ABSSUBMITTEDJOB

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `JOBNUMBER`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70641

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `JOBNUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `QUEUENAME` | CHAR(50) |  |  |  |  |
| 2 | `DESCRIPTION` | CHAR(150) |  |  | description |  |
| 3 | `JNDINAME` | CHAR(100) |  |  |  |  |
| 4 | `XMLNAME` | CHAR(105) |  |  |  |  |
| 5 | `PRINCIPAL` | CHAR(50) |  |  |  |  |
| 6 | `PRIORITYONQUEUE` | INTEGER | NOT NULL |  |  |  |
| 7 | `OUTPUTQUEUE` | CHAR(20) |  | FK | foreign_key |  |
| 8 | `SUBMITTEDDATE` | DATE |  |  |  |  |
| 9 | `SUBMITTEDTIME` | TIME |  |  |  |  |
| 10 | `JOBDATA` | BLOB(1000000) |  |  |  |  |
| 11 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 12 | `BEGINDATE` | DATE |  |  |  |  |
| 13 | `BEGINTIME` | TIME |  |  |  |  |
| 14 | `ENDDATE` | DATE |  |  |  |  |
| 15 | `ENDTIME` | TIME |  |  |  |  |
| 16 | `JOBLOG` | CLOB(2000000) |  |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `EXECUTIONJOBENV` | CHAR(60) |  |  |  |  |
| 19 | `JOBORIGINJOBNUMBER` | BIGINT | NOT NULL |  |  |  |
| 20 | `SUBMITTEDDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `SUBMITTEDDATETIMEUTC` | TIMESTAMP |  |  |  |  |
| 22 | `BEGINDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `BEGINDATETIMEUTC` | TIMESTAMP |  |  |  |  |
| 24 | `ENDDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `ENDDATETIMEUTC` | TIMESTAMP |  |  |  |  |
| 26 | `JTHREADNAME` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSOUTQUEUE_OUTPUTQUEUE` | `OUTPUTQUEUE` | [`ABSOUTQUEUE`](../PLATFORM/ABSOUTQUEUE.md) | `NAME` | RESTRICT | `ABSSUBMITTEDJOB.OUTPUTQUEUE = ABSOUTQUEUE.NAME` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSSUBMITTEDJOB_SUBMITTEBJOB` | [`GARMENTCARTONJOBDETAIL`](../PLATFORM/GARMENTCARTONJOBDETAIL.md) | `SUBMITTEBJOBJOBNUMBER` | `GARMENTCARTONJOBDETAIL.SUBMITTEBJOBJOBNUMBER = ABSSUBMITTEDJOB.JOBNUMBER` |

## Indexes

- `ABSSUBMITTEDJOB1` (STATUS, PRIORITYONQUEUE, SUBMITTEDDATE, SUBMITTEDTIME, JOBNUMBER)
- `ABSSUBMITTEDJOBUID` (ABSUNIQUEID)
- `ABSSUBMITTEDJOB2` (STATUS, QUEUENAME)

## Starter query

```sql
SELECT t.JOBNUMBER,
       t.QUEUENAME,
       t.DESCRIPTION,
       t.JNDINAME,
       t.XMLNAME,
       t.PRINCIPAL,
       t.PRIORITYONQUEUE,
       t.OUTPUTQUEUE,
       t.SUBMITTEDDATE,
       t.SUBMITTEDTIME,
       t.JOBDATA,
       t.STATUS
FROM   DB2ADMIN.ABSSUBMITTEDJOB t
FETCH FIRST 100 ROWS ONLY;
```
