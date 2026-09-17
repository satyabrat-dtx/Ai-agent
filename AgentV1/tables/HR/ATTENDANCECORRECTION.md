# DB2ADMIN.ATTENDANCECORRECTION

- **Module**: `HR` (high confidence — table name starts with 'ATTENDANCE')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `PAYROLLCODE`, `ATTDTYPEATTENDANCETYPECODE`, `PROCESSPERIOD`, `ATTENDANCEDATE`, `DAYSESSION`, `EMPLOYEECODE`, `SNO`
- **FK degree**: referenced by 0 constraint(s), references 8 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 165317

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PAYROLLCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ATTDTYPEATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ATTENDANCEDATE` | DATE | NOT NULL | PK | primary_key |  |
| 5 | `DAYSESSION` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `SNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `ATTENDANCEPERIOD` | INTEGER | NOT NULL |  |  |  |
| 9 | `ATTENDANCECODE` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `NUMBEROFHRS` | DECIMAL(5,2) |  |  |  |  |
| 11 | `LEAVECODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `DESIGNATIONICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 13 | `DESIGNATIONCODE` | CHAR(6) |  | FK | foreign_key |  |
| 14 | `SHIFTCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `STATUSFLAG` | CHAR(10) |  |  |  |  |
| 22 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 23 | `APPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 8

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ATTENDANCECORRECTION.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_APPROVEDBY` | `COMPANYCODE`, `APPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ATTENDANCECORRECTION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ATTENDANCECORRECTION.APPROVEDBYCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_EMPLOYEE` | `COMPANYCODE`, `EMPLOYEECODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ATTENDANCECORRECTION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ATTENDANCECORRECTION.EMPLOYEECODE = EMPLOYEE.CODE` |
| `ICSENTITY_DESIGNATION` | `COMPANYCODE`, `DESIGNATIONICSTABLECODE`, `DESIGNATIONCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `ATTENDANCECORRECTION.COMPANYCODE = ICSENTITY.COMPANYCODE AND ATTENDANCECORRECTION.DESIGNATIONICSTABLECODE = ICSENTITY.ICSTABLECODE AND ATTENDANCECORRECTION.DESIGNATIONCODE = ICSENTITY.CODE` |
| `LEAVE_LEAVE` | `COMPANYCODE`, `LEAVECODE` | [`LEAVE`](../HR/LEAVE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ATTENDANCECORRECTION.COMPANYCODE = LEAVE.COMPANYCODE AND ATTENDANCECORRECTION.LEAVECODE = LEAVE.CODE` |
| `PAYROLLTYPEDETAIL_ATTDTYPE` | `COMPANYCODE`, `PAYROLLCODE`, `ATTDTYPEATTENDANCETYPECODE` | [`PAYROLLTYPEDETAIL`](../HR/PAYROLLTYPEDETAIL.md) | `PAYROLLTYPECOMPANYCODE`, `PAYROLLTYPECODE`, `ATTENDANCETYPECODE` | RESTRICT | `ATTENDANCECORRECTION.COMPANYCODE = PAYROLLTYPEDETAIL.PAYROLLTYPECOMPANYCODE AND ATTENDANCECORRECTION.PAYROLLCODE = PAYROLLTYPEDETAIL.PAYROLLTYPECODE AND ATTENDANCECORRECTION.ATTDTYPEATTENDANCETYPECODE = PAYROLLTYPEDETAIL.ATTENDANCETYPECODE` |
| `PAYROLLTYPE_PAYROLL` | `COMPANYCODE`, `PAYROLLCODE` | [`PAYROLLTYPE`](../HR/PAYROLLTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ATTENDANCECORRECTION.COMPANYCODE = PAYROLLTYPE.COMPANYCODE AND ATTENDANCECORRECTION.PAYROLLCODE = PAYROLLTYPE.CODE` |
| `SHIFT_SHIFT` | `COMPANYCODE`, `SHIFTCODE` | [`SHIFT`](../HR/SHIFT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ATTENDANCECORRECTION.COMPANYCODE = SHIFT.COMPANYCODE AND ATTENDANCECORRECTION.SHIFTCODE = SHIFT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ATTENDANCECORRECTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PAYROLLCODE,
       t.ATTDTYPEATTENDANCETYPECODE,
       t.PROCESSPERIOD,
       t.ATTENDANCEDATE,
       t.DAYSESSION,
       t.EMPLOYEECODE,
       t.SNO,
       t.ATTENDANCEPERIOD,
       t.ATTENDANCECODE,
       t.NUMBEROFHRS,
       t.LEAVECODE
FROM   DB2ADMIN.ATTENDANCECORRECTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
