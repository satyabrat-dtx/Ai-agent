# DB2ADMIN.WRKESIFORM7

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 80
- **Primary key**: `CREATIONUSER`, `COMPANYCODE`, `CREATIONTIMESTAMP`, `EMPLOYEEIDCODE`, `LINE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 162787

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 1 | `COMPANYCODE` | CHAR(20) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 3 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 4 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 5 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `MONTH1` | CHAR(12) |  |  |  |  |
| 7 | `MONTH2` | CHAR(12) |  |  |  |  |
| 8 | `MONTH3` | CHAR(12) |  |  |  |  |
| 9 | `MONTH4` | CHAR(12) |  |  |  |  |
| 10 | `MONTH5` | CHAR(12) |  |  |  |  |
| 11 | `MONTH6` | CHAR(12) |  |  |  |  |
| 12 | `MONTH7` | CHAR(12) |  |  |  |  |
| 13 | `MONTH8` | CHAR(12) |  |  |  |  |
| 14 | `MONTH9` | CHAR(12) |  |  |  |  |
| 15 | `MONTH10` | CHAR(12) |  |  |  |  |
| 16 | `MONTH11` | CHAR(12) |  |  |  |  |
| 17 | `MONTH12` | CHAR(12) |  |  |  |  |
| 18 | `AMTCALCULATEDWAG1` | DECIMAL(9,2) |  |  |  |  |
| 19 | `AMTCALCULATEDDAYS1` | DECIMAL(9,2) |  |  |  |  |
| 20 | `AMTCALCULATEDESI1` | DECIMAL(9,2) |  |  |  |  |
| 21 | `AMTCALCULATEDWAG2` | DECIMAL(9,2) |  |  |  |  |
| 22 | `AMTCALCULATEDDAYS2` | DECIMAL(9,2) |  |  |  |  |
| 23 | `AMTCALCULATEDESI2` | DECIMAL(9,2) |  |  |  |  |
| 24 | `AMTCALCULATEDWAG3` | DECIMAL(9,2) |  |  |  |  |
| 25 | `AMTCALCULATEDDAYS3` | DECIMAL(9,2) |  |  |  |  |
| 26 | `AMTCALCULATEDESI3` | DECIMAL(9,2) |  |  |  |  |
| 27 | `AMTCALCULATEDWAG4` | DECIMAL(9,2) |  |  |  |  |
| 28 | `AMTCALCULATEDDAYS4` | DECIMAL(9,2) |  |  |  |  |
| 29 | `AMTCALCULATEDESI4` | DECIMAL(9,2) |  |  |  |  |
| 30 | `AMTCALCULATEDWAG5` | DECIMAL(9,2) |  |  |  |  |
| 31 | `AMTCALCULATEDDAYS5` | DECIMAL(9,2) |  |  |  |  |
| 32 | `AMTCALCULATEDESI5` | DECIMAL(9,2) |  |  |  |  |
| 33 | `AMTCALCULATEDWAG6` | DECIMAL(9,2) |  |  |  |  |
| 34 | `AMTCALCULATEDDAYS6` | DECIMAL(9,2) |  |  |  |  |
| 35 | `AMTCALCULATEDESI6` | DECIMAL(9,2) |  |  |  |  |
| 36 | `AMTCALCULATEDWAG7` | DECIMAL(9,2) |  |  |  |  |
| 37 | `AMTCALCULATEDDAYS7` | DECIMAL(9,2) |  |  |  |  |
| 38 | `AMTCALCULATEDESI7` | DECIMAL(9,2) |  |  |  |  |
| 39 | `AMTCALCULATEDWAG8` | DECIMAL(9,2) |  |  |  |  |
| 40 | `AMTCALCULATEDDAYS8` | DECIMAL(9,2) |  |  |  |  |
| 41 | `AMTCALCULATEDESI8` | DECIMAL(9,2) |  |  |  |  |
| 42 | `AMTCALCULATEDWAG9` | DECIMAL(9,2) |  |  |  |  |
| 43 | `AMTCALCULATEDDAYS9` | DECIMAL(9,2) |  |  |  |  |
| 44 | `AMTCALCULATEDESI9` | DECIMAL(9,2) |  |  |  |  |
| 45 | `AMTCALCULATEDWAG10` | DECIMAL(9,2) |  |  |  |  |
| 46 | `AMTCALCULATEDDAYS10` | DECIMAL(9,2) |  |  |  |  |
| 47 | `AMTCALCULATEDESI10` | DECIMAL(9,2) |  |  |  |  |
| 48 | `AMTCALCULATEDWAG11` | DECIMAL(9,2) |  |  |  |  |
| 49 | `AMTCALCULATEDDAYS11` | DECIMAL(9,2) |  |  |  |  |
| 50 | `AMTCALCULATEDESI11` | DECIMAL(9,2) |  |  |  |  |
| 51 | `AMTCALCULATEDWAG12` | DECIMAL(9,2) |  |  |  |  |
| 52 | `AMTCALCULATEDDAYS12` | DECIMAL(9,2) |  |  |  |  |
| 53 | `AMTCALCULATEDESI12` | DECIMAL(9,2) |  |  |  |  |
| 54 | `WAGESAMT` | DECIMAL(17,2) |  |  |  |  |
| 55 | `DAYS` | DECIMAL(17,2) |  |  |  |  |
| 56 | `ESIAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 57 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 58 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 59 | `ESINO` | CHAR(30) |  |  |  |  |
| 60 | `FIRSTNAME` | CHAR(30) |  |  |  |  |
| 61 | `MIDDLENAME` | CHAR(30) |  |  |  |  |
| 62 | `LASTNAME` | CHAR(30) |  |  |  |  |
| 63 | `FATHERNAME` | CHAR(100) |  |  |  |  |
| 64 | `JOININGDATE` | DATE |  |  |  |  |
| 65 | `EXITDATE` | DATE |  |  |  |  |
| 66 | `EMPLOYEECONTRIB` | DECIMAL(17,2) |  |  |  |  |
| 67 | `NOOFDAYS` | DECIMAL(17,2) |  |  |  |  |
| 68 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 69 | `CATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 70 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 71 | `SUBCATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 72 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 73 | `DIVISIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 74 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 75 | `FACTORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 76 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 77 | `DEPARTMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 78 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 79 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKESIFORM7UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONUSER,
       t.COMPANYCODE,
       t.COMPANYDESCRIPTION,
       t.CREATIONTIMESTAMP,
       t.EMPLOYEEIDCODE,
       t.LINE,
       t.MONTH1,
       t.MONTH2,
       t.MONTH3,
       t.MONTH4,
       t.MONTH5,
       t.MONTH6
FROM   DB2ADMIN.WRKESIFORM7 t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
