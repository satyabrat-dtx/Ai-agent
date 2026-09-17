# DB2ADMIN.LEAVEENTRYINHRS

- **Module**: `HR` (high confidence — table name starts with 'LEAVE')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `EMPLOYEECODE`, `ATTENDANCEDATE`, `DAYSESSION`, `ATTENDANCETYPECODE`, `CORRSEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 170140

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ATTENDANCEDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `DAYSESSION` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `CORRSEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `LEAVECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `NUMBEROFHRS` | DECIMAL(7,3) |  |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LEAVEENTRYINHRS.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEE` | `COMPANYCODE`, `EMPLOYEECODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LEAVEENTRYINHRS.COMPANYCODE = EMPLOYEE.COMPANYCODE AND LEAVEENTRYINHRS.EMPLOYEECODE = EMPLOYEE.CODE` |
| `LEAVE_LEAVE` | `COMPANYCODE`, `LEAVECODE` | [`LEAVE`](../HR/LEAVE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LEAVEENTRYINHRS.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVEENTRYINHRS.LEAVECODE = LEAVE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LEAVEENTRYINHRSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEECODE,
       t.ATTENDANCEDATE,
       t.DAYSESSION,
       t.ATTENDANCETYPECODE,
       t.CORRSEQUENCE,
       t.LEAVECODE,
       t.NUMBEROFHRS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.LEAVEENTRYINHRS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
