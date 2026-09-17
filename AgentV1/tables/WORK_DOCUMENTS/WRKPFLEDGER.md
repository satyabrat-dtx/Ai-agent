# DB2ADMIN.WRKPFLEDGER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `CREATIONUSER`, `COMPANYCODE`, `CREATIONTIMESTAMP`, `EMPLOYEEIDCODE`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 163406

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 1 | `COMPANYCODE` | CHAR(20) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 3 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 4 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 5 | `CATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 6 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 7 | `SUBCATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 8 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 9 | `DIVISIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 10 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 11 | `FACTORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 12 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 13 | `DEPARTMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 14 | `PFNO` | CHAR(30) |  |  |  |  |
| 15 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 16 | `FIRSTNAME` | CHAR(50) |  |  |  |  |
| 17 | `MIDDLENAME` | CHAR(50) |  |  |  |  |
| 18 | `LASTNAME` | CHAR(50) |  |  |  |  |
| 19 | `FATHERNAME` | CHAR(50) |  |  |  |  |
| 20 | `JOININGDATE` | DATE |  |  |  |  |
| 21 | `PFWAGES` | DECIMAL(17,2) |  |  |  |  |
| 22 | `NOOFDAYS` | DECIMAL(17,2) |  |  |  |  |
| 23 | `EMPLOYEECONT` | DECIMAL(17,2) |  |  |  |  |
| 24 | `EMPLOYERCONT` | DECIMAL(17,2) |  |  |  |  |
| 25 | `VOLUANTARYPF` | DECIMAL(17,2) |  |  |  |  |
| 26 | `ATTENDANCETYPEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 27 | `PAYROLLTYPEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 28 | `LINE` | BIGINT | NOT NULL | PK | primary_key |  |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPFLEDGERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONUSER,
       t.COMPANYCODE,
       t.COMPANYDESCRIPTION,
       t.CREATIONTIMESTAMP,
       t.CATEGORYCODE,
       t.CATEGORYDESCRIPTION,
       t.SUBCATEGORYCODE,
       t.SUBCATEGORYDESCRIPTION,
       t.DIVISIONCODE,
       t.DIVISIONDESCRIPTION,
       t.FACTORYCODE,
       t.FACTORYDESCRIPTION
FROM   DB2ADMIN.WRKPFLEDGER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
