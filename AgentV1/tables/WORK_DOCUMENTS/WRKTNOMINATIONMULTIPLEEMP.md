# DB2ADMIN.WRKTNOMINATIONMULTIPLEEMP

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 37
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 201499

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `CATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 3 | `CATEGORYCODE` | CHAR(6) |  |  |  |  |
| 4 | `SUBCTGSUBCATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 5 | `SUBCATEGORYSUBCATEGORYCODE` | CHAR(6) |  |  |  |  |
| 6 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 7 | `FACTORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 9 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 10 | `GRADEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 11 | `GRADECODE` | CHAR(6) |  |  |  |  |
| 12 | `TRAININGTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 13 | `TRAININGTYPECODE` | CHAR(6) |  |  |  |  |
| 14 | `TRAININGCODE` | CHAR(6) |  |  |  |  |
| 15 | `SCHEDULECODE` | DECIMAL(5,0) |  |  |  |  |
| 16 | `SCHEDULENUMBERSCHEDULENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 17 | `SCHEDULEDESC` | CHAR(50) |  |  |  |  |
| 18 | `EMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 19 | `EMPNOMINATIONDATE` | DATE |  |  |  |  |
| 20 | `DEPTHEADAPPROVAL` | INTEGER | NOT NULL |  |  |  |
| 21 | `DEPTHEADIDCODE` | CHAR(9) |  |  |  |  |
| 22 | `REQUESTDATE` | DATE |  |  |  |  |
| 23 | `APPROVEDBYCODE` | CHAR(9) |  |  |  |  |
| 24 | `HEADAPPROVALDATE` | DATE |  |  |  |  |
| 25 | `APPROVEDDATE` | DATE |  |  |  |  |
| 26 | `HRAPPROVAL` | INTEGER | NOT NULL |  |  |  |
| 27 | `HRIDCODE` | CHAR(9) |  |  |  |  |
| 28 | `HRAPPROVALDATE` | DATE |  |  |  |  |
| 29 | `REQPENDINGWITH` | CHAR(10) |  |  |  |  |
| 30 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 31 | `STEP` | CHAR(1) |  |  |  |  |
| 32 | `CHOICETYPE` | CHAR(2) |  |  |  |  |
| 33 | `PROCESSTYPE` | INTEGER | NOT NULL |  |  |  |
| 34 | `ALREADYRECORDEXIST` | SMALLINT | NOT NULL |  |  |  |
| 35 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 36 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKTNOMINATIONMULTIPLEEMPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.SUBCTGSUBCATEGORYICSTABLECODE,
       t.SUBCATEGORYSUBCATEGORYCODE,
       t.DIVISIONCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.DEPARTMENTCODE,
       t.GRADEICSTABLECODE,
       t.GRADECODE
FROM   DB2ADMIN.WRKTNOMINATIONMULTIPLEEMP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
