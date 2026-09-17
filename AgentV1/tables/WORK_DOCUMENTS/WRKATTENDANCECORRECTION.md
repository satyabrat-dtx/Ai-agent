# DB2ADMIN.WRKATTENDANCECORRECTION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `TIMEOFENTRY`, `DATEOFENTRY`, `DAYSESSION`, `PAYROLLCODE`, `ATTENDANCETYPECODE`, `EMPLOYEEIDCODE`, `SERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183376

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TIMEOFENTRY` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `DATEOFENTRY` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `PAYROLLCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `DAYSESSION` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 7 | `EMPNAME` | CHAR(25) |  |  |  |  |
| 8 | `SHIFTCODE` | CHAR(3) |  |  |  |  |
| 9 | `SESSIONHRS` | DECIMAL(5,2) |  |  |  |  |
| 10 | `ATTENDANCECODE` | CHAR(1) |  |  |  |  |
| 11 | `FROMDESIGNATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 12 | `FROMDESIGNATIONCODE` | CHAR(6) |  |  |  |  |
| 13 | `TODESIGNATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 14 | `TODESIGNATIONCODE` | CHAR(6) |  |  |  |  |
| 15 | `LEAVECODE` | CHAR(3) |  |  |  |  |
| 16 | `SERIALNO` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 17 | `PROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 18 | `ATTENDANCEPERIOD` | INTEGER | NOT NULL |  |  |  |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKATTENDANCECORRECTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TIMEOFENTRY,
       t.DATEOFENTRY,
       t.PAYROLLCODE,
       t.ATTENDANCETYPECODE,
       t.DAYSESSION,
       t.EMPLOYEEIDCODE,
       t.EMPNAME,
       t.SHIFTCODE,
       t.SESSIONHRS,
       t.ATTENDANCECODE,
       t.FROMDESIGNATIONICSTABLECODE
FROM   DB2ADMIN.WRKATTENDANCECORRECTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
