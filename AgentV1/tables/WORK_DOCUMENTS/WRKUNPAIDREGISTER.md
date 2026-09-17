# DB2ADMIN.WRKUNPAIDREGISTER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `EMPLOYEEIDCODE`, `UNPAIDTYPEICSTABLECODE`, `UNPAIDTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 164556

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `UNPAIDTYPEICSTABLECODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 4 | `UNPAIDTYPECODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 5 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 6 | `FIRSTNAME` | CHAR(25) |  |  |  |  |
| 7 | `MIDDLENAME` | CHAR(25) |  |  |  |  |
| 8 | `LASTNAME` | CHAR(25) |  |  |  |  |
| 9 | `CATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 10 | `CATEGORYCODE` | CHAR(6) |  |  |  |  |
| 11 | `SUBCTGCATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 12 | `SUBCTGSUBCATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 13 | `SUBCATEGORYSUBCATEGORYCODE` | CHAR(6) |  |  |  |  |
| 14 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 15 | `FACTORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 17 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 18 | `FATHERNAME` | CHAR(30) |  |  |  |  |
| 19 | `PERIODFROM` | DATE |  |  |  |  |
| 20 | `PERIODTO` | DATE |  |  |  |  |
| 21 | `AMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKUNPAIDREGISTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CHOOSE,
       t.COMPANYCODE,
       t.UNPAIDTYPEICSTABLECODE,
       t.UNPAIDTYPECODE,
       t.EMPLOYEEIDCODE,
       t.FIRSTNAME,
       t.MIDDLENAME,
       t.LASTNAME,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.SUBCTGCATEGORYICSTABLECODE
FROM   DB2ADMIN.WRKUNPAIDREGISTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
