# DB2ADMIN.ABSOUTQUEUE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `NAME`
- **FK degree**: referenced by 6 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70356

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NAME` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 1 | `DESCRIPTION` | CHAR(50) |  |  | description |  |
| 2 | `PRINTSERVICENAME` | CHAR(100) |  |  |  |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `PLYPRINTINGMODECODE` | CHAR(20) |  |  |  |  |
| 11 | `FORCEORIENTATION` | SMALLINT | NOT NULL |  |  |  |
| 12 | `ORIENTATIONMODE` | INTEGER | NOT NULL |  |  |  |
| 13 | `PAPERWIDTH` | DECIMAL(6,2) |  |  |  |  |
| 14 | `PAPERHEIGHT` | DECIMAL(6,2) |  |  |  |  |
| 15 | `FORCEMARGIN` | SMALLINT | NOT NULL |  |  |  |
| 16 | `MARGINX` | DECIMAL(6,2) |  |  |  |  |
| 17 | `MARGINY` | DECIMAL(6,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 6

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSOUTQUEUE_SPOOLFILE` | [`ABSSPOOLFILE`](../PLATFORM/ABSSPOOLFILE.md) | `ABSOUTQUEUENAME` | `ABSSPOOLFILE.ABSOUTQUEUENAME = ABSOUTQUEUE.NAME` |
| `ABSOUTQUEUE_OUTPUTQUEUE` | [`ABSREPORTDEFCUSTOMVALUE`](../PLATFORM/ABSREPORTDEFCUSTOMVALUE.md) | `OUTPUTQUEUENAME` | `ABSREPORTDEFCUSTOMVALUE.OUTPUTQUEUENAME = ABSOUTQUEUE.NAME` |
| `ABSOUTQUEUE_DEFAULTOUTQUEUE` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `DEFAULTOUTQUEUENAME` | `ABSUSERDEF.DEFAULTOUTQUEUENAME = ABSOUTQUEUE.NAME` |
| `ABSOUTQUEUE_DEFAULTOUTQUEUE` | [`ABSSYSTEMPROPERTIES`](../PLATFORM/ABSSYSTEMPROPERTIES.md) | `DEFAULTOUTQUEUENAME` | `ABSSYSTEMPROPERTIES.DEFAULTOUTQUEUENAME = ABSOUTQUEUE.NAME` |
| `ABSOUTQUEUE_OUTPUTQUEUE` | [`ABSSCHEDULEDJOB`](../PLATFORM/ABSSCHEDULEDJOB.md) | `OUTPUTQUEUE` | `ABSSCHEDULEDJOB.OUTPUTQUEUE = ABSOUTQUEUE.NAME` |
| `ABSOUTQUEUE_OUTPUTQUEUE` | [`ABSSUBMITTEDJOB`](../PLATFORM/ABSSUBMITTEDJOB.md) | `OUTPUTQUEUE` | `ABSSUBMITTEDJOB.OUTPUTQUEUE = ABSOUTQUEUE.NAME` |

## Indexes

- `ABSOUTQUEUEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.NAME,
       t.DESCRIPTION,
       t.PRINTSERVICENAME,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.PLYPRINTINGMODECODE,
       t.FORCEORIENTATION
FROM   DB2ADMIN.ABSOUTQUEUE t
FETCH FIRST 100 ROWS ONLY;
```
