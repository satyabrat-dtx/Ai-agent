# DB2ADMIN.WRKBANKSHEETREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 37
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `PROCESSPERIOD`, `EMPLOYEEID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 169527

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(20) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 3 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 4 | `CATEGORYDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 5 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 6 | `SUBCATEGORYDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 7 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 8 | `DIVISIONDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 9 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 10 | `FACTORYDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 11 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 12 | `DEPARTMENTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 13 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 14 | `PROCESSTYPE` | CHAR(10) |  |  |  |  |
| 15 | `ATTENDANCETYPECODE` | VARCHAR(200) |  |  |  |  |
| 16 | `EMPLOYEEID` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 17 | `FIRSTNAME` | CHAR(25) | NOT NULL |  |  |  |
| 18 | `MIDDLENAME` | CHAR(25) |  |  |  |  |
| 19 | `DESIGNATION` | CHAR(10) |  |  |  |  |
| 20 | `LASTNAME` | CHAR(25) |  |  |  |  |
| 21 | `DESIGNATIONDESC` | VARCHAR(80) |  |  |  |  |
| 22 | `CALCULATEDAMT` | DECIMAL(9,2) |  |  |  |  |
| 23 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 24 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 25 | `BANKCODE` | CHAR(10) |  |  |  |  |
| 26 | `BANKBRANCHCODE` | CHAR(10) |  |  |  |  |
| 27 | `REPORTTYPE` | INTEGER | NOT NULL |  |  |  |
| 28 | `ACCOUNTNUMBER` | CHAR(20) |  |  |  |  |
| 29 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 30 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 31 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 32 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 33 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 34 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 35 | `FATHERNAME` | CHAR(50) |  |  |  |  |
| 36 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKBANKSHEETREPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.COMPANYDESCRIPTION,
       t.CATEGORYCODE,
       t.CATEGORYDESCRIPTION,
       t.SUBCATEGORYCODE,
       t.SUBCATEGORYDESCRIPTION,
       t.DIVISIONCODE,
       t.DIVISIONDESCRIPTION,
       t.FACTORYCODE,
       t.FACTORYDESCRIPTION,
       t.DEPARTMENTCODE
FROM   DB2ADMIN.WRKBANKSHEETREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
