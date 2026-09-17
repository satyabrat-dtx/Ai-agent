# DB2ADMIN.WRKGRATUITYPAIDLIST

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `EMPLOYEEIDCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 164436

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 3 | `FIRSTNAME` | CHAR(25) |  |  |  |  |
| 4 | `MIDDLENAME` | CHAR(25) |  |  |  |  |
| 5 | `LASTNAME` | CHAR(25) |  |  |  |  |
| 6 | `CATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 7 | `CATEGORYCODE` | CHAR(6) |  |  |  |  |
| 8 | `SUBCTGCATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 9 | `SUBCTGSUBCATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 10 | `SUBCATEGORYSUBCATEGORYCODE` | CHAR(6) |  |  |  |  |
| 11 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 12 | `FACTORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 14 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 15 | `FATHERNAME` | CHAR(50) |  |  |  |  |
| 16 | `DATEOFJOINING` | DATE |  |  |  |  |
| 17 | `DATEOFLEAVING` | DATE |  |  |  |  |
| 18 | `BASICAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 19 | `PAIDAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 20 | `GRATUITYYEARS` | DECIMAL(5,2) |  |  |  |  |
| 21 | `VDA` | DECIMAL(17,2) |  |  |  |  |
| 22 | `CATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `SUBCATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 24 | `DIVISIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 25 | `FACTORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 26 | `DEPARTMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 27 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKGRATUITYPAIDLISTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.EMPLOYEEIDCODE,
       t.FIRSTNAME,
       t.MIDDLENAME,
       t.LASTNAME,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.SUBCTGCATEGORYICSTABLECODE,
       t.SUBCTGSUBCATEGORYICSTABLECODE,
       t.SUBCATEGORYSUBCATEGORYCODE,
       t.DIVISIONCODE
FROM   DB2ADMIN.WRKGRATUITYPAIDLIST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
