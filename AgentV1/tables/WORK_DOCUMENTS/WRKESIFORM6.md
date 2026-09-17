# DB2ADMIN.WRKESIFORM6

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `CREATIONUSER`, `COMPANYCODE`, `CREATIONTIMESTAMP`, `EMPLOYEEIDCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 162723

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 3 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 4 | `ESINO` | CHAR(30) |  |  |  |  |
| 5 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 6 | `FIRSTNAME` | CHAR(30) |  |  |  |  |
| 7 | `MIDDLENAME` | CHAR(30) |  |  |  |  |
| 8 | `LASTNAME` | CHAR(30) |  |  |  |  |
| 9 | `FATHERNAME` | CHAR(50) |  |  |  |  |
| 10 | `JOININGDATE` | DATE |  |  |  |  |
| 11 | `DISPENSARY` | CHAR(100) |  |  |  |  |
| 12 | `NOOFDAYS` | DECIMAL(17,2) |  |  |  |  |
| 13 | `WAGESAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 14 | `EMPLOYEECONTRIB` | DECIMAL(17,2) |  |  |  |  |
| 15 | `EMPLOYERCONTRIB` | DECIMAL(17,2) |  |  |  |  |
| 16 | `DAILYWAGES` | DECIMAL(17,2) |  |  |  |  |
| 17 | `CONDITION` | CHAR(100) |  |  |  |  |
| 18 | `EXITDATE` | DATE |  |  |  |  |
| 19 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 20 | `CATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 21 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 22 | `SUBCATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 24 | `DIVISIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 25 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 26 | `FACTORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 27 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 28 | `DEPARTMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 29 | `ATTENDANCETYPEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 30 | `PAYROLLTYPEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKESIFORM6UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONUSER,
       t.COMPANYCODE,
       t.COMPANYDESCRIPTION,
       t.CREATIONTIMESTAMP,
       t.ESINO,
       t.EMPLOYEEIDCODE,
       t.FIRSTNAME,
       t.MIDDLENAME,
       t.LASTNAME,
       t.FATHERNAME,
       t.JOININGDATE,
       t.DISPENSARY
FROM   DB2ADMIN.WRKESIFORM6 t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
