# DB2ADMIN.WRKPAYSLIP

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `CREATIONUSER`, `COMPANYCODE`, `CREATIONTIMESTAMP`, `EMPLOYEEIDCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 163469

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 1 | `COMPANYCODE` | CHAR(20) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 4 | `FIRSTNAME` | CHAR(50) |  |  |  |  |
| 5 | `MIDDLENAME` | CHAR(50) |  |  |  |  |
| 6 | `LASTNAME` | CHAR(50) |  |  |  |  |
| 7 | `FATHERNAME` | CHAR(100) |  |  |  |  |
| 8 | `DESIGNATIONDESP` | VARCHAR(200) |  |  |  |  |
| 9 | `GRADEDESP` | VARCHAR(200) |  |  |  |  |
| 10 | `DEPARTMENTDESP` | VARCHAR(200) |  |  |  |  |
| 11 | `PANNO` | CHAR(30) |  |  |  |  |
| 12 | `WORKINGDAYS` | DECIMAL(18,5) |  |  |  |  |
| 13 | `JOININGDATE` | DATE |  |  |  |  |
| 14 | `ATTENDANCEDESP` | VARCHAR(200) |  |  |  |  |
| 15 | `PFNUMBER` | CHAR(30) |  |  |  |  |
| 16 | `BANKACCNO` | CHAR(30) |  |  |  |  |
| 17 | `ESINO` | CHAR(15) |  |  |  |  |
| 18 | `COSTCENTERDESP` | VARCHAR(200) |  |  |  |  |
| 19 | `DAYSPAYABLE` | DECIMAL(18,5) |  |  |  |  |
| 20 | `STDWAGES` | DECIMAL(18,5) |  |  |  |  |
| 21 | `SUMEARNINGS` | DECIMAL(18,5) |  |  |  |  |
| 22 | `SUMDEDUCTIONS` | DECIMAL(18,5) |  |  |  |  |
| 23 | `BANKDESP` | VARCHAR(200) |  |  |  |  |
| 24 | `ATTENDANCETYPECODE` | CHAR(3) |  |  |  |  |
| 25 | `COMPANYDESP` | VARCHAR(200) |  |  |  |  |
| 26 | `GRADECODE` | CHAR(6) |  |  |  |  |
| 27 | `DESGCODE` | CHAR(6) |  |  |  |  |
| 28 | `LINENO` | BIGINT | NOT NULL | PK | primary_key |  |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPAYSLIPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONUSER,
       t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.EMPLOYEEIDCODE,
       t.FIRSTNAME,
       t.MIDDLENAME,
       t.LASTNAME,
       t.FATHERNAME,
       t.DESIGNATIONDESP,
       t.GRADEDESP,
       t.DEPARTMENTDESP,
       t.PANNO
FROM   DB2ADMIN.WRKPAYSLIP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
