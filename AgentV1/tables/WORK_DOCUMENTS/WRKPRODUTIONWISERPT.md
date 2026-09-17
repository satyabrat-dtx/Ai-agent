# DB2ADMIN.WRKPRODUTIONWISERPT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `PAYROLLTYPE`, `ATTENDANCETYPE`, `PROCESSPERIOD`, `EMPLOYEECODE`, `RESOURCENO`, `OPERATIONTYPE`, `SERIAL`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 163593

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `PAYROLLTYPE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `ATTENDANCETYPE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `CATEGORY` | CHAR(6) |  |  |  |  |
| 6 | `SUBCATEGORY` | CHAR(6) |  |  |  |  |
| 7 | `DIVISION` | CHAR(3) |  |  |  |  |
| 8 | `FACTORY` | CHAR(3) |  |  |  |  |
| 9 | `DEPARTMENT` | CHAR(8) |  |  |  |  |
| 10 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 11 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 12 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 13 | `EMPLOYEENAME` | CHAR(50) |  |  |  |  |
| 14 | `ATTENDDATE` | DATE |  |  |  |  |
| 15 | `RESOURCENO` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 16 | `OPERATIONTYPE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 17 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 18 | `SUBCODE02` | CHAR(20) |  |  | generic_classification_code |  |
| 19 | `SUBCODE03` | CHAR(20) |  |  | generic_classification_code |  |
| 20 | `SUBCODE04` | CHAR(20) |  |  | generic_classification_code |  |
| 21 | `SUBCODE05` | CHAR(20) |  |  | generic_classification_code |  |
| 22 | `SUBCODE06` | CHAR(20) |  |  | generic_classification_code |  |
| 23 | `SUBCODE07` | CHAR(20) |  |  | generic_classification_code |  |
| 24 | `SUBCODE08` | CHAR(20) |  |  | generic_classification_code |  |
| 25 | `SUBCODE09` | CHAR(20) |  |  | generic_classification_code |  |
| 26 | `SUBCODE10` | CHAR(20) |  |  | generic_classification_code |  |
| 27 | `QUALITY` | DECIMAL(2,0) |  |  |  |  |
| 28 | `QUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 29 | `SERIAL` | INTEGER | NOT NULL | PK | primary_key |  |
| 30 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 31 | `EMPSERIAL` | INTEGER | NOT NULL |  |  |  |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPRODUTIONWISERPTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.PAYROLLTYPE,
       t.ATTENDANCETYPE,
       t.PROCESSPERIOD,
       t.CATEGORY,
       t.SUBCATEGORY,
       t.DIVISION,
       t.FACTORY,
       t.DEPARTMENT,
       t.FROMDATE,
       t.TODATE
FROM   DB2ADMIN.WRKPRODUTIONWISERPT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
