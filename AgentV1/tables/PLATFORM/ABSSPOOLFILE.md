# DB2ADMIN.ABSSPOOLFILE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `ABSOUTQUEUENAME`, `SPOOLID`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 14359

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSOUTQUEUENAME` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SPOOLID` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `REPORTID` | CHAR(50) |  |  |  |  |
| 3 | `USERID` | CHAR(50) |  |  |  |  |
| 4 | `BATCHJOB` | BIGINT | NOT NULL |  |  |  |
| 5 | `USERDESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 6 | `SEARCHKEY` | VARCHAR(500) |  |  |  |  |
| 7 | `CONTENTTYPE` | INTEGER | NOT NULL |  |  |  |
| 8 | `PRINTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 9 | `CREATIONDATE` | DATE |  |  |  |  |
| 10 | `CREATIONTIME` | TIME |  |  |  |  |
| 11 | `NRCOPIES` | INTEGER | NOT NULL |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `DOWNLOADFILENAME` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSOUTQUEUE_SPOOLFILE` | `ABSOUTQUEUENAME` | [`ABSOUTQUEUE`](../PLATFORM/ABSOUTQUEUE.md) | `NAME` | RESTRICT | `ABSSPOOLFILE.ABSOUTQUEUENAME = ABSOUTQUEUE.NAME` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSSPOOLFILE_SPLITDATA` | [`ABSSPOOLFILEDATA`](../PLATFORM/ABSSPOOLFILEDATA.md) | `ABSSPOOLFILEABSOUTQUEUENAME`, `ABSSPOOLFILESPOOLID` | `ABSSPOOLFILEDATA.ABSSPOOLFILEABSOUTQUEUENAME = ABSSPOOLFILE.ABSOUTQUEUENAME AND ABSSPOOLFILEDATA.ABSSPOOLFILESPOOLID = ABSSPOOLFILE.SPOOLID` |

## Indexes

- `ABSSPOOLFILEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSOUTQUEUENAME,
       t.SPOOLID,
       t.REPORTID,
       t.USERID,
       t.BATCHJOB,
       t.USERDESCRIPTION,
       t.SEARCHKEY,
       t.CONTENTTYPE,
       t.PRINTSTATUS,
       t.CREATIONDATE,
       t.CREATIONTIME,
       t.NRCOPIES
FROM   DB2ADMIN.ABSSPOOLFILE t
FETCH FIRST 100 ROWS ONLY;
```
