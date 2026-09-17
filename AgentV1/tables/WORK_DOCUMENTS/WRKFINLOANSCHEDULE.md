# DB2ADMIN.WRKFINLOANSCHEDULE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `FINLOANREPAYMENTMCOMPANYCODE`, `FINLRMBUSINESSUNITCODE`, `FINLRMFINANCIALYEARCODE`, `FINLRMLTEUGENGROUPTYPECODE`, `FINLOANREPAYMENTMLOANTYPECODE`, `FINLOANREPAYMENTMCODELOANNO`, `FINLOANREPAYMENTMREPAYMENTDATE`, `FINLOANREPAYMENTMSLNO`, `TIMEDAYSINC`, `SCHEDULENO`, `SCHEDULESEQNO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 226860

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINLOANREPAYMENTMCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `FINLRMBUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `FINLRMFINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 3 | `FINLRMLTEUGENGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `FINLOANREPAYMENTMLOANTYPECODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 5 | `FINLOANREPAYMENTMCODELOANNO` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 6 | `FINLOANREPAYMENTMREPAYMENTDATE` | DATE | NOT NULL | PK | primary_key |  |
| 7 | `FINLOANREPAYMENTMSLNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `TIMEDAYSINC` | BIGINT | NOT NULL | PK | primary_key |  |
| 9 | `SCHEDULENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 10 | `SCHEDULESEQNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 11 | `SCHEDULEAMOUNT` | DECIMAL(20,0) |  |  |  |  |
| 12 | `PAIDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 13 | `SCHEDULEDATE` | DATE |  |  |  |  |
| 14 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 15 | `PENDINGAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 16 | `PREPAIDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINLOANSCHEDULEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINLOANREPAYMENTMCOMPANYCODE,
       t.FINLRMBUSINESSUNITCODE,
       t.FINLRMFINANCIALYEARCODE,
       t.FINLRMLTEUGENGROUPTYPECODE,
       t.FINLOANREPAYMENTMLOANTYPECODE,
       t.FINLOANREPAYMENTMCODELOANNO,
       t.FINLOANREPAYMENTMREPAYMENTDATE,
       t.FINLOANREPAYMENTMSLNO,
       t.TIMEDAYSINC,
       t.SCHEDULENO,
       t.SCHEDULESEQNO,
       t.SCHEDULEAMOUNT
FROM   DB2ADMIN.WRKFINLOANSCHEDULE t
FETCH FIRST 100 ROWS ONLY;
```
