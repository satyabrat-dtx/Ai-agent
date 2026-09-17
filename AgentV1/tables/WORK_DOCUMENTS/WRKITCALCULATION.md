# DB2ADMIN.WRKITCALCULATION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 40
- **Primary key**: `CREATIONUSER`, `COMPANYCODE`, `CREATIONTIMESTAMP`, `FINANCIALYEARCODE`, `EMPLOYEEIDCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 170910

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `FINANCIALYEARCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `FINANCEMONTH` | CHAR(4) |  |  |  |  |
| 5 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 6 | `FIRSTNAME` | CHAR(30) |  |  |  |  |
| 7 | `LASTNAME` | CHAR(30) |  |  |  |  |
| 8 | `MIDDLENAME` | CHAR(30) |  |  |  |  |
| 9 | `PAYELEMENTCODE` | CHAR(8) |  |  |  |  |
| 10 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 11 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 12 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 13 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 14 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 15 | `CATEGORYDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 16 | `SUBCATEGORYDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 17 | `DIVISIONDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 18 | `FACTORYDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 19 | `DEPARTMENTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 20 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 21 | `AMOUNT1` | DECIMAL(17,2) |  |  |  |  |
| 22 | `AMOUNT2` | DECIMAL(17,2) |  |  |  |  |
| 23 | `AMOUNT3` | DECIMAL(17,2) |  |  |  |  |
| 24 | `AMOUNT4` | DECIMAL(17,2) |  |  |  |  |
| 25 | `AMOUNT5` | DECIMAL(17,2) |  |  |  |  |
| 26 | `AMOUNT6` | DECIMAL(17,2) |  |  |  |  |
| 27 | `AMOUNT7` | DECIMAL(17,2) |  |  |  |  |
| 28 | `AMOUNT8` | DECIMAL(17,2) |  |  |  |  |
| 29 | `AMOUNT9` | DECIMAL(17,2) |  |  |  |  |
| 30 | `AMOUNT10` | DECIMAL(17,2) |  |  |  |  |
| 31 | `AMOUNT11` | DECIMAL(17,2) |  |  |  |  |
| 32 | `AMOUNT12` | DECIMAL(17,2) |  |  |  |  |
| 33 | `PROCESSTYPE` | CHAR(8) |  |  |  |  |
| 34 | `TEMPCALCULATE` | DECIMAL(17,2) |  |  |  |  |
| 35 | `PERQAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 36 | `GROUPCODE` | CHAR(10) |  |  |  |  |
| 37 | `PAYELEMENTTYPE` | CHAR(1) |  |  |  |  |
| 38 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 39 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKITCALCULATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONUSER,
       t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.FINANCIALYEARCODE,
       t.FINANCEMONTH,
       t.EMPLOYEEIDCODE,
       t.FIRSTNAME,
       t.LASTNAME,
       t.MIDDLENAME,
       t.PAYELEMENTCODE,
       t.CATEGORYCODE,
       t.SUBCATEGORYCODE
FROM   DB2ADMIN.WRKITCALCULATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
