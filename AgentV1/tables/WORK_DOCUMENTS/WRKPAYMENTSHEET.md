# DB2ADMIN.WRKPAYMENTSHEET

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `CREATIONTIMESTAMP`, `CREATIONUSER`, `COMPANYCODE`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 163532

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 2 | `COMPANYCODE` | CHAR(20) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 4 | `EMPLOYEECODE` | CHAR(15) |  |  |  |  |
| 5 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 7 | `CATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 8 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 9 | `SUBCATEGORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 10 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 11 | `DIVISIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 12 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 13 | `FACTORYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 14 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 15 | `DEPARTMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 16 | `REGULARAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 17 | `REGULAROTAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 18 | `HOLIDAYEXTRAAMT` | DECIMAL(17,2) |  |  |  |  |
| 19 | `EMPLOYEENAME` | CHAR(50) |  |  |  |  |
| 20 | `FATHERNAME` | CHAR(50) |  |  |  |  |
| 21 | `HOLIDAYOTAMT` | DECIMAL(17,2) |  |  |  |  |
| 22 | `WEEKLYOFFEXTRAAMT` | DECIMAL(17,2) |  |  |  |  |
| 23 | `WEEKLYOFFOTAMT` | DECIMAL(17,2) |  |  |  |  |
| 24 | `ATTENDANCETYPEDESC` | VARCHAR(200) |  |  |  |  |
| 25 | `WORKMILLNOCODE` | CHAR(15) |  |  |  |  |
| 26 | `WORKSHIFTNOCODE` | CHAR(15) |  |  |  |  |
| 27 | `PAYROLLTYPEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPAYMENTSHEETUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.COMPANYCODE,
       t.COMPANYDESCRIPTION,
       t.EMPLOYEECODE,
       t.LINE,
       t.CATEGORYCODE,
       t.CATEGORYDESCRIPTION,
       t.SUBCATEGORYCODE,
       t.SUBCATEGORYDESCRIPTION,
       t.DIVISIONCODE,
       t.DIVISIONDESCRIPTION
FROM   DB2ADMIN.WRKPAYMENTSHEET t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
