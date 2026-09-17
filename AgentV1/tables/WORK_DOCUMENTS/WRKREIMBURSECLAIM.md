# DB2ADMIN.WRKREIMBURSECLAIM

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `EMPLOYEEIDCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 163663

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `REIMBURSEMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 4 | `FIRSTNAME` | CHAR(30) |  |  |  |  |
| 5 | `MIDDLENAME` | CHAR(30) |  |  |  |  |
| 6 | `LASTNAME` | CHAR(30) |  |  |  |  |
| 7 | `FATHERNAME` | CHAR(50) |  |  |  |  |
| 8 | `MAXIMUMAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 9 | `CLAIMDATE` | DATE |  |  |  |  |
| 10 | `TOTCLAIMAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 11 | `SANCTIONAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 12 | `PAYMENTDATE` | DATE |  |  |  |  |
| 13 | `CLAIMAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 14 | `BALANCEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 15 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 16 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 17 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 18 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 19 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 20 | `CATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 21 | `SUBCATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 22 | `DIVISIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `FACTORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 24 | `DEPARTMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 25 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 26 | `REIMBURSEMENTTYPEDESP` | VARCHAR(200) |  |  |  |  |
| 27 | `REIMBURSEMENTGRPDESP` | VARCHAR(200) |  |  |  |  |
| 28 | `CLAIMNO` | BIGINT | NOT NULL |  |  |  |
| 29 | `LINENO` | BIGINT | NOT NULL | PK | primary_key |  |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKREIMBURSECLAIMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.REIMBURSEMENTTYPECODE,
       t.EMPLOYEEIDCODE,
       t.FIRSTNAME,
       t.MIDDLENAME,
       t.LASTNAME,
       t.FATHERNAME,
       t.MAXIMUMAMOUNT,
       t.CLAIMDATE,
       t.TOTCLAIMAMOUNT,
       t.SANCTIONAMOUNT
FROM   DB2ADMIN.WRKREIMBURSECLAIM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
