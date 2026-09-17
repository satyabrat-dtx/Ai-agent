# DB2ADMIN.WRKLEAVEBALANCE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `CREATIONUSER`, `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 171202

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `EMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 4 | `FIRSTNAME` | CHAR(30) |  |  |  |  |
| 5 | `MIDDLENAME` | CHAR(30) |  |  |  |  |
| 6 | `LASTNAME` | CHAR(30) |  |  |  |  |
| 7 | `FATHERNAME` | CHAR(50) |  |  |  |  |
| 8 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 9 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 10 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 11 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 12 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 13 | `CATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 14 | `SUBCATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 15 | `DIVISIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 16 | `FACTORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 17 | `DEPARTMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 18 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 19 | `LEAVECALENDARCODE` | CHAR(25) |  |  |  |  |
| 20 | `LEAVECODE` | CHAR(25) |  |  |  |  |
| 21 | `LEAVECALDESP` | CHAR(50) |  |  |  |  |
| 22 | `NOOFLEAVEBALANCE` | DECIMAL(17,2) |  |  |  |  |
| 23 | `PAYROLLTYPEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 24 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKLEAVEBALANCEUID` (ABSUNIQUEID)

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
       t.CATEGORYCODE,
       t.SUBCATEGORYCODE,
       t.DIVISIONCODE,
       t.FACTORYCODE
FROM   DB2ADMIN.WRKLEAVEBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
