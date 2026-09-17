# DB2ADMIN.LEAVEBALANCE

- **Module**: `HR` (high confidence — table name starts with 'LEAVE')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `LEAVECALENDARCALENDARCODE`, `EMPLOYEEIDCODE`, `LEAVECODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 167135

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LEAVECALENDARCALENDARCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LEAVECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CFLEAVEELIGIBLEDAYS` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 5 | `CYRLEAVEELIGIBLEDAYS` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 6 | `CYRAVAILEDLEAVE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 7 | `CYRBALANCELEAVE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 8 | `CYRENCASHEDLEAVE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 9 | `LEAVECANCELDAYS` | DECIMAL(5,2) |  |  |  |  |
| 10 | `LEAVEDONATED` | DECIMAL(5,2) |  |  |  |  |
| 11 | `LEAVERECEIVED` | DECIMAL(5,2) |  |  |  |  |
| 12 | `DECREMENTLEAVE` | DECIMAL(5,2) |  |  |  |  |
| 13 | `INCREMENTLEAVE` | DECIMAL(5,2) |  |  |  |  |
| 14 | `NXTYRCARRYOVERDAYS` | DECIMAL(5,2) |  |  |  |  |
| 15 | `LAPSEDAYS` | DECIMAL(5,2) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LEAVEBALANCE.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LEAVEBALANCE.COMPANYCODE = EMPLOYEE.COMPANYCODE AND LEAVEBALANCE.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `LEAVECALENDAR_LEAVECALENDAR` | `COMPANYCODE`, `LEAVECALENDARCALENDARCODE` | [`LEAVECALENDAR`](../HR/LEAVECALENDAR.md) | `COMPANYCODE`, `CALENDARCODE` | RESTRICT | `LEAVEBALANCE.COMPANYCODE = LEAVECALENDAR.COMPANYCODE AND LEAVEBALANCE.LEAVECALENDARCALENDARCODE = LEAVECALENDAR.CALENDARCODE` |
| `LEAVE_LEAVE` | `COMPANYCODE`, `LEAVECODE` | [`LEAVE`](../HR/LEAVE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LEAVEBALANCE.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVEBALANCE.LEAVECODE = LEAVE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LEAVEBALANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LEAVECALENDARCALENDARCODE,
       t.EMPLOYEEIDCODE,
       t.LEAVECODE,
       t.CFLEAVEELIGIBLEDAYS,
       t.CYRLEAVEELIGIBLEDAYS,
       t.CYRAVAILEDLEAVE,
       t.CYRBALANCELEAVE,
       t.CYRENCASHEDLEAVE,
       t.LEAVECANCELDAYS,
       t.LEAVEDONATED,
       t.LEAVERECEIVED
FROM   DB2ADMIN.LEAVEBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
