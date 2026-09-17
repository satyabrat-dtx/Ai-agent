# DB2ADMIN.WRKREIMBURSEMENTREGISTER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 42
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `EMPLOYEECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 163726

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(20) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 3 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 4 | `CATEGORYCODE` | CHAR(5) |  |  |  |  |
| 5 | `CATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 6 | `SUBCATEGORYCODE` | CHAR(5) |  |  |  |  |
| 7 | `SUBCATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 8 | `DIVISIONCODE` | CHAR(5) |  |  |  | Division within a company; second-level organisational discriminator. |
| 9 | `DIVISIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 10 | `FACTORYCODE` | CHAR(5) |  |  |  |  |
| 11 | `BASEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 12 | `FACTORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 13 | `DEPARTMENTCODE` | CHAR(5) |  |  |  |  |
| 14 | `DEPARTMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 15 | `FIRSTNAME` | CHAR(30) |  |  |  |  |
| 16 | `LASTNAME` | CHAR(30) |  |  |  |  |
| 17 | `MIDDLENAME` | CHAR(30) |  |  |  |  |
| 18 | `FATHERNAME` | CHAR(50) |  |  |  |  |
| 19 | `AVAILEDAMT` | DECIMAL(17,2) |  |  |  |  |
| 20 | `BALANCEAMT` | DECIMAL(17,2) |  |  |  |  |
| 21 | `REIMBURSELIGAMT` | DECIMAL(17,2) |  |  |  |  |
| 22 | `REIMBURSEMENTTYPEDESP` | VARCHAR(200) |  |  |  |  |
| 23 | `REIMBURSEMENTGRPDESP` | VARCHAR(200) |  |  |  |  |
| 24 | `REIMBURSEMENTTYPECODE` | CHAR(4) |  |  |  |  |
| 25 | `REIMBURSEMENTFROMDATE` | DATE |  |  |  |  |
| 26 | `REIMBURSEMENTTODATE` | DATE |  |  |  |  |
| 27 | `MONTH1` | DECIMAL(7,2) |  |  |  |  |
| 28 | `MONTH2` | DECIMAL(7,2) |  |  |  |  |
| 29 | `MONTH3` | DECIMAL(7,2) |  |  |  |  |
| 30 | `MONTH4` | DECIMAL(7,2) |  |  |  |  |
| 31 | `MONTH5` | DECIMAL(7,2) |  |  |  |  |
| 32 | `MONTH6` | DECIMAL(7,2) |  |  |  |  |
| 33 | `MONTH7` | DECIMAL(7,2) |  |  |  |  |
| 34 | `MONTH8` | DECIMAL(7,2) |  |  |  |  |
| 35 | `MONTH9` | DECIMAL(7,2) |  |  |  |  |
| 36 | `MONTH10` | DECIMAL(7,2) |  |  |  |  |
| 37 | `MONTH11` | DECIMAL(7,2) |  |  |  |  |
| 38 | `MONTH12` | DECIMAL(7,2) |  |  |  |  |
| 39 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 40 | `REIMBURSEMENTFLAG` | INTEGER | NOT NULL |  |  |  |
| 41 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKREIMBURSEMENTREGISTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.COMPANYDESCRIPTION,
       t.EMPLOYEECODE,
       t.CATEGORYCODE,
       t.CATEGORYDESCRIPTION,
       t.SUBCATEGORYCODE,
       t.SUBCATEGORYDESCRIPTION,
       t.DIVISIONCODE,
       t.DIVISIONDESCRIPTION,
       t.FACTORYCODE,
       t.BASEAMOUNT
FROM   DB2ADMIN.WRKREIMBURSEMENTREGISTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
