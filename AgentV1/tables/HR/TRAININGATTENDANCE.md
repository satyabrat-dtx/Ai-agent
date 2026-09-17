# DB2ADMIN.TRAININGATTENDANCE

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `SNUMBERTSTTYPEICSTABLECODE`, `SNUMBERTSTRAININGTYPECODE`, `SNUMBERTSCHEDULETRAININGCODE`, `SNUMBERTRAININGSCHEDULECODE`, `SCHEDULENUMBERSCHEDULENUMBER`, `TRAININGDATE`, `EMPLOYEEIDCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 201447

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SNUMBERTSTTYPEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SNUMBERTSTRAININGTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SNUMBERTSCHEDULETRAININGCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SNUMBERTRAININGSCHEDULECODE` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SCHEDULENUMBERSCHEDULENUMBER` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `TRAININGDATE` | DATE | NOT NULL | PK | primary_key |  |
| 7 | `NUMBEROFHRS` | DECIMAL(5,2) |  |  |  |  |
| 8 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRAININGATTENDANCE.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TRAININGATTENDANCE.COMPANYCODE = EMPLOYEE.COMPANYCODE AND TRAININGATTENDANCE.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `TRAININGSCHEDULEDETAIL_SCHEDULENUMBER` | `COMPANYCODE`, `SNUMBERTSTTYPEICSTABLECODE`, `SNUMBERTSTRAININGTYPECODE`, `SNUMBERTSCHEDULETRAININGCODE`, `SNUMBERTRAININGSCHEDULECODE`, `SCHEDULENUMBERSCHEDULENUMBER` | [`TRAININGSCHEDULEDETAIL`](../HR/TRAININGSCHEDULEDETAIL.md) | `TRAININGSCHEDULECOMPANYCODE`, `TSTRAININGTYPEICSTABLECODE`, `TSCHEDULETRAININGTYPECODE`, `TRAININGSCHEDULETRAININGCODE`, `TRAININGSCHEDULECODE`, `SCHEDULENUMBER` | RESTRICT | `TRAININGATTENDANCE.COMPANYCODE = TRAININGSCHEDULEDETAIL.TRAININGSCHEDULECOMPANYCODE AND TRAININGATTENDANCE.SNUMBERTSTTYPEICSTABLECODE = TRAININGSCHEDULEDETAIL.TSTRAININGTYPEICSTABLECODE AND TRAININGATTENDANCE.SNUMBERTSTRAININGTYPECODE = TRAININGSCHEDULEDETAIL.TSCHEDULETRAININGTYPECODE AND TRAININGATTENDANCE.SNUMBERTSCHEDULETRAININGCODE = TRAININGSCHEDULEDETAIL.TRAININGSCHEDULETRAININGCODE AND TRAININGATTENDANCE.SNUMBERTRAININGSCHEDULECODE = TRAININGSCHEDULEDETAIL.TRAININGSCHEDULECODE AND TRAININGATTENDANCE.SCHEDULENUMBERSCHEDULENUMBER = TRAININGSCHEDULEDETAIL.SCHEDULENUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TRAININGATTENDANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SNUMBERTSTTYPEICSTABLECODE,
       t.SNUMBERTSTRAININGTYPECODE,
       t.SNUMBERTSCHEDULETRAININGCODE,
       t.SNUMBERTRAININGSCHEDULECODE,
       t.SCHEDULENUMBERSCHEDULENUMBER,
       t.TRAININGDATE,
       t.NUMBEROFHRS,
       t.EMPLOYEEIDCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.TRAININGATTENDANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
