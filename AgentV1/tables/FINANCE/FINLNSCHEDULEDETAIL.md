# DB2ADMIN.FINLNSCHEDULEDETAIL

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `FINLNSFINLMASTERCOMPANYCODE`, `FINLNSFINLMLTEUGENGRPTYPECODE`, `FINLNSFINLMASTERLOANTYPECODE`, `FINLNSFINLOANMASTERLOANNO`, `FINLNSCHEDULESCHEDULENO`, `SNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 231177

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINLNSFINLMASTERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINLNSFINLMLTEUGENGRPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINLNSFINLMASTERLOANTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FINLNSFINLOANMASTERLOANNO` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `FINLNSCHEDULESCHEDULENO` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `SCHEDULEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 7 | `STARTDATE` | DATE |  |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINLNSCHEDULE_LINE` | `FINLNSFINLMASTERCOMPANYCODE`, `FINLNSFINLMLTEUGENGRPTYPECODE`, `FINLNSFINLMASTERLOANTYPECODE`, `FINLNSFINLOANMASTERLOANNO`, `FINLNSCHEDULESCHEDULENO` | [`FINLNSCHEDULE`](../FINANCE/FINLNSCHEDULE.md) | `FINLOANMASTERCOMPANYCODE`, `FINLMLTEUGENERICGROUPTYPECODE`, `FINLOANMASTERLOANTYPECODE`, `FINLOANMASTERLOANNO`, `SCHEDULENO` | RESTRICT | `FINLNSCHEDULEDETAIL.FINLNSFINLMASTERCOMPANYCODE = FINLNSCHEDULE.FINLOANMASTERCOMPANYCODE AND FINLNSCHEDULEDETAIL.FINLNSFINLMLTEUGENGRPTYPECODE = FINLNSCHEDULE.FINLMLTEUGENERICGROUPTYPECODE AND FINLNSCHEDULEDETAIL.FINLNSFINLMASTERLOANTYPECODE = FINLNSCHEDULE.FINLOANMASTERLOANTYPECODE AND FINLNSCHEDULEDETAIL.FINLNSFINLOANMASTERLOANNO = FINLNSCHEDULE.FINLOANMASTERLOANNO AND FINLNSCHEDULEDETAIL.FINLNSCHEDULESCHEDULENO = FINLNSCHEDULE.SCHEDULENO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINLNSCHEDULEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINLNSFINLMASTERCOMPANYCODE,
       t.FINLNSFINLMLTEUGENGRPTYPECODE,
       t.FINLNSFINLMASTERLOANTYPECODE,
       t.FINLNSFINLOANMASTERLOANNO,
       t.FINLNSCHEDULESCHEDULENO,
       t.SNO,
       t.SCHEDULEAMOUNT,
       t.STARTDATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.FINLNSCHEDULEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
