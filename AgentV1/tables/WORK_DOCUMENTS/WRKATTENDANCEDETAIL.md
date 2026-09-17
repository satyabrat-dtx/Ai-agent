# DB2ADMIN.WRKATTENDANCEDETAIL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 50
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `EMPLOYEECODE`, `ATTENDANCEDATE`, `ATTENDANCETYPECODE`, `CORRSEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 170385

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 3 | `SHORTNAME` | CHAR(10) |  |  |  |  |
| 4 | `ATTENDANCEDATE` | DATE | NOT NULL | PK | primary_key |  |
| 5 | `NUMBEROFHRS` | DECIMAL(5,2) |  |  |  |  |
| 6 | `SHIFTCODE` | CHAR(3) |  |  |  |  |
| 7 | `FROMDESIGNATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 8 | `FROMDESIGNATIONCODE` | CHAR(6) |  |  |  |  |
| 9 | `TODESIGNATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 10 | `TODESIGNATIONCODE` | CHAR(6) |  |  |  |  |
| 11 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 12 | `FACTORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 14 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 15 | `SECTIONSECTIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 16 | `SECTIONSECTIONCODE` | CHAR(6) |  |  |  |  |
| 17 | `MATYPEMACHINETYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 18 | `MACHINETYPEMACHINETYPECODE` | CHAR(6) |  |  |  |  |
| 19 | `MACHINENOMACHINENOICSTABLECODE` | CHAR(4) |  |  |  |  |
| 20 | `MACHINENOMACHINENOCODE` | CHAR(6) |  |  |  |  |
| 21 | `FROMCOSTCENTERBADLICODE` | CHAR(10) |  |  |  |  |
| 22 | `TOCOSTCENTERBADLICODE` | CHAR(10) |  |  |  |  |
| 23 | `INCENTIVEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 24 | `SPECIALPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 25 | `PERFORMANCEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 26 | `BADLICODE` | CHAR(3) |  |  |  |  |
| 27 | `PAYROLLCODE` | CHAR(3) |  |  |  |  |
| 28 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 29 | `FLAGPAYABLE` | INTEGER | NOT NULL |  |  |  |
| 30 | `FLAGATTENDANCEAUTHORIZED` | INTEGER | NOT NULL |  |  |  |
| 31 | `PROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 32 | `ATTENDANCEPERIOD` | INTEGER | NOT NULL |  |  |  |
| 33 | `LATEFLAG` | SMALLINT | NOT NULL |  |  |  |
| 34 | `INTIME` | TIME |  |  |  |  |
| 35 | `OUTTIME` | TIME |  |  |  |  |
| 36 | `ATTENDANCECODE` | CHAR(1) |  |  |  |  |
| 37 | `LEAVECODE` | CHAR(3) |  |  |  |  |
| 38 | `SESSION0NOOFHRS` | DECIMAL(5,2) |  |  |  |  |
| 39 | `SESSION1ATTENDANCECODE` | CHAR(1) |  |  |  |  |
| 40 | `SESSION1LEAVECODE` | CHAR(3) |  |  |  |  |
| 41 | `SESSION1NOOFHRS` | DECIMAL(5,2) |  |  |  |  |
| 42 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 43 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 44 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 45 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 46 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 47 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 48 | `CORRSEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 49 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKATTENDANCEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.EMPLOYEECODE,
       t.SHORTNAME,
       t.ATTENDANCEDATE,
       t.NUMBEROFHRS,
       t.SHIFTCODE,
       t.FROMDESIGNATIONICSTABLECODE,
       t.FROMDESIGNATIONCODE,
       t.TODESIGNATIONICSTABLECODE,
       t.TODESIGNATIONCODE,
       t.DIVISIONCODE
FROM   DB2ADMIN.WRKATTENDANCEDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
