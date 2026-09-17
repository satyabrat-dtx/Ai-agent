# DB2ADMIN.FINLOANSCHEDULE

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `FINLRFINLOANMASTERCOMPANYCODE`, `FINLRFINLMLTEUGENGRPTYPECODE`, `FINLRFINLMASTERLOANTYPECODE`, `FINLRFINLOANMASTERLOANNO`, `FINLOANREPAYMENTSLNO`, `SLNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 230268

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINLRFINLOANMASTERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINLRFINLMLTEUGENGRPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINLRFINLMASTERLOANTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FINLRFINLOANMASTERLOANNO` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `FINLOANREPAYMENTSLNO` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SLNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `STARTDATE` | DATE |  |  |  |  |
| 7 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `SANCTIONSCHEDULE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `PAIDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `PENDINGAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINLOANREPAYMENT_LINE` | `FINLRFINLOANMASTERCOMPANYCODE`, `FINLRFINLMLTEUGENGRPTYPECODE`, `FINLRFINLMASTERLOANTYPECODE`, `FINLRFINLOANMASTERLOANNO`, `FINLOANREPAYMENTSLNO` | [`FINLOANREPAYMENT`](../FINANCE/FINLOANREPAYMENT.md) | `FINLOANMASTERCOMPANYCODE`, `FINLMLTEUGENERICGROUPTYPECODE`, `FINLOANMASTERLOANTYPECODE`, `FINLOANMASTERLOANNO`, `SLNO` | RESTRICT | `FINLOANSCHEDULE.FINLRFINLOANMASTERCOMPANYCODE = FINLOANREPAYMENT.FINLOANMASTERCOMPANYCODE AND FINLOANSCHEDULE.FINLRFINLMLTEUGENGRPTYPECODE = FINLOANREPAYMENT.FINLMLTEUGENERICGROUPTYPECODE AND FINLOANSCHEDULE.FINLRFINLMASTERLOANTYPECODE = FINLOANREPAYMENT.FINLOANMASTERLOANTYPECODE AND FINLOANSCHEDULE.FINLRFINLOANMASTERLOANNO = FINLOANREPAYMENT.FINLOANMASTERLOANNO AND FINLOANSCHEDULE.FINLOANREPAYMENTSLNO = FINLOANREPAYMENT.SLNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINLOANSCHEDULEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINLRFINLOANMASTERCOMPANYCODE,
       t.FINLRFINLMLTEUGENGRPTYPECODE,
       t.FINLRFINLMASTERLOANTYPECODE,
       t.FINLRFINLOANMASTERLOANNO,
       t.FINLOANREPAYMENTSLNO,
       t.SLNO,
       t.STARTDATE,
       t.AMOUNT,
       t.SANCTIONSCHEDULE,
       t.PAIDAMOUNT,
       t.PENDINGAMOUNT,
       t.CREATIONDATETIME
FROM   DB2ADMIN.FINLOANSCHEDULE t
FETCH FIRST 100 ROWS ONLY;
```
