# DB2ADMIN.WRKBONUSEXGRATIAREGISTER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 52
- **Primary key**: `CREATIONUSER`, `COMPANYCODE`, `CREATIONTIMESTAMP`, `EMPLOYEEIDCODE`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 170469

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 1 | `COMPANYCODE` | CHAR(20) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 3 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 4 | `FINANCIALYEARCODE` | CHAR(6) |  |  |  |  |
| 5 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 6 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `CATEGORYCODE` | CHAR(30) |  |  |  |  |
| 8 | `CATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 9 | `SUBCATEGORYCODE` | CHAR(30) |  |  |  |  |
| 10 | `SUBCATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 11 | `DIVISIONCODE` | CHAR(30) |  |  |  | Division within a company; second-level organisational discriminator. |
| 12 | `DIVISIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 13 | `FACTORYCODE` | CHAR(30) |  |  |  |  |
| 14 | `FACTORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 15 | `DEPARTMENTCODE` | CHAR(30) |  |  |  |  |
| 16 | `DEPARTMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 17 | `MONTH1` | DECIMAL(7,2) |  |  |  |  |
| 18 | `MONTH2` | DECIMAL(7,2) |  |  |  |  |
| 19 | `MONTH3` | DECIMAL(7,2) |  |  |  |  |
| 20 | `MONTH4` | DECIMAL(7,2) |  |  |  |  |
| 21 | `MONTH5` | DECIMAL(7,2) |  |  |  |  |
| 22 | `MONTH6` | DECIMAL(7,2) |  |  |  |  |
| 23 | `MONTH7` | DECIMAL(7,2) |  |  |  |  |
| 24 | `MONTH8` | DECIMAL(7,2) |  |  |  |  |
| 25 | `MONTH9` | DECIMAL(7,2) |  |  |  |  |
| 26 | `MONTH10` | DECIMAL(7,2) |  |  |  |  |
| 27 | `MONTH11` | DECIMAL(7,2) |  |  |  |  |
| 28 | `MONTH12` | DECIMAL(7,2) |  |  |  |  |
| 29 | `WAGESAMT` | DECIMAL(7,2) |  |  |  |  |
| 30 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 31 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 32 | `FIRSTNAME` | CHAR(30) |  |  |  |  |
| 33 | `MIDDLENAME` | CHAR(30) |  |  |  |  |
| 34 | `LASTNAME` | CHAR(30) |  |  |  |  |
| 35 | `FATHERNAME` | CHAR(50) |  |  |  |  |
| 36 | `JOININGDATE` | DATE |  |  |  |  |
| 37 | `DESIGNATION` | CHAR(50) |  |  |  |  |
| 38 | `DESIGNATIONDESC` | VARCHAR(200) |  |  |  |  |
| 39 | `EXGRATIAMONTH1` | DECIMAL(7,2) |  |  |  |  |
| 40 | `EXGRATIAMONTH2` | DECIMAL(7,2) |  |  |  |  |
| 41 | `EXGRATIAMONTH3` | DECIMAL(7,2) |  |  |  |  |
| 42 | `EXGRATIAMONTH4` | DECIMAL(7,2) |  |  |  |  |
| 43 | `EXGRATIAMONTH5` | DECIMAL(7,2) |  |  |  |  |
| 44 | `EXGRATIAMONTH6` | DECIMAL(7,2) |  |  |  |  |
| 45 | `EXGRATIAMONTH7` | DECIMAL(7,2) |  |  |  |  |
| 46 | `EXGRATIAMONTH8` | DECIMAL(7,2) |  |  |  |  |
| 47 | `EXGRATIAMONTH9` | DECIMAL(7,2) |  |  |  |  |
| 48 | `EXGRATIAMONTH10` | DECIMAL(7,2) |  |  |  |  |
| 49 | `EXGRATIAMONTH11` | DECIMAL(7,2) |  |  |  |  |
| 50 | `EXGRATIAMONTH12` | DECIMAL(7,2) |  |  |  |  |
| 51 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKBONUSEXGRATIAREGISTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONUSER,
       t.COMPANYCODE,
       t.COMPANYDESCRIPTION,
       t.CREATIONTIMESTAMP,
       t.FINANCIALYEARCODE,
       t.EMPLOYEEIDCODE,
       t.LINE,
       t.CATEGORYCODE,
       t.CATEGORYDESCRIPTION,
       t.SUBCATEGORYCODE,
       t.SUBCATEGORYDESCRIPTION,
       t.DIVISIONCODE
FROM   DB2ADMIN.WRKBONUSEXGRATIAREGISTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
