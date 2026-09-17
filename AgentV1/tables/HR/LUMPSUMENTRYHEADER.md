# DB2ADMIN.LUMPSUMENTRYHEADER

- **Module**: `HR` (low confidence — FK neighbourhood: 4 of 4 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `PAYROLLTYPECODE`, `ATTENDANCETYPECODE`, `PAYELEMENTTYPE`, `PAYELEMENTCODE`, `EMPLOYEEIDCODE`, `FROMPRLPROCESSPERIOD`
- **FK degree**: referenced by 0 constraint(s), references 8 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 167541

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PAYROLLTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PAYELEMENTTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PAYELEMENTCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `FROMPRLPROCESSPERIOD` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 8 | `TOPRLPROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 9 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 10 | `REQUESTDATE` | DATE |  |  |  |  |
| 11 | `APPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 12 | `APPROVEDDATE` | DATE |  |  |  |  |
| 13 | `FLAGLSORFORMULA` | INTEGER | NOT NULL |  |  |  |
| 14 | `AMOUNTCALCULATED` | DECIMAL(11,2) |  |  |  |  |
| 15 | `FORMULACODE` | CHAR(6) |  | FK | foreign_key |  |
| 16 | `REQPENDINGWITH` | CHAR(10) |  |  |  |  |
| 17 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 8

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ATTENDANCETYPE_ATTENDANCETYPE` | `COMPANYCODE`, `ATTENDANCETYPECODE` | [`ATTENDANCETYPE`](../HR/ATTENDANCETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LUMPSUMENTRYHEADER.COMPANYCODE = ATTENDANCETYPE.COMPANYCODE AND LUMPSUMENTRYHEADER.ATTENDANCETYPECODE = ATTENDANCETYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LUMPSUMENTRYHEADER.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_APPROVEDBY` | `COMPANYCODE`, `APPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LUMPSUMENTRYHEADER.COMPANYCODE = EMPLOYEE.COMPANYCODE AND LUMPSUMENTRYHEADER.APPROVEDBYCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LUMPSUMENTRYHEADER.COMPANYCODE = EMPLOYEE.COMPANYCODE AND LUMPSUMENTRYHEADER.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `FORMULACODE_FORMULA` | `COMPANYCODE`, `FORMULACODE` | [`FORMULACODE`](../HR/FORMULACODE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LUMPSUMENTRYHEADER.COMPANYCODE = FORMULACODE.COMPANYCODE AND LUMPSUMENTRYHEADER.FORMULACODE = FORMULACODE.CODE` |
| `PAYELEMENT_PAYELEMENT` | `COMPANYCODE`, `PAYELEMENTTYPE`, `PAYELEMENTCODE` | [`PAYELEMENT`](../CORE_MASTER/PAYELEMENT.md) | `COMPANYCODE`, `PAYELEMENTTYPE`, `CODE` | RESTRICT | `LUMPSUMENTRYHEADER.COMPANYCODE = PAYELEMENT.COMPANYCODE AND LUMPSUMENTRYHEADER.PAYELEMENTTYPE = PAYELEMENT.PAYELEMENTTYPE AND LUMPSUMENTRYHEADER.PAYELEMENTCODE = PAYELEMENT.CODE` |
| `PAYROLLPROCESSPERIOD_FROMPRL` | `COMPANYCODE`, `PAYROLLTYPECODE`, `FROMPRLPROCESSPERIOD` | [`PAYROLLPROCESSPERIOD`](../HR/PAYROLLPROCESSPERIOD.md) | `COMPANYCODE`, `PAYROLLCODE`, `PROCESSPERIOD` | RESTRICT | `LUMPSUMENTRYHEADER.COMPANYCODE = PAYROLLPROCESSPERIOD.COMPANYCODE AND LUMPSUMENTRYHEADER.PAYROLLTYPECODE = PAYROLLPROCESSPERIOD.PAYROLLCODE AND LUMPSUMENTRYHEADER.FROMPRLPROCESSPERIOD = PAYROLLPROCESSPERIOD.PROCESSPERIOD` |
| `PAYROLLTYPE_PAYROLLTYPE` | `COMPANYCODE`, `PAYROLLTYPECODE` | [`PAYROLLTYPE`](../HR/PAYROLLTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LUMPSUMENTRYHEADER.COMPANYCODE = PAYROLLTYPE.COMPANYCODE AND LUMPSUMENTRYHEADER.PAYROLLTYPECODE = PAYROLLTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LUMPSUMENTRYHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PAYROLLTYPECODE,
       t.ATTENDANCETYPECODE,
       t.PAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.EMPLOYEEIDCODE,
       t.FROMPRLPROCESSPERIOD,
       t.FROMDATE,
       t.TOPRLPROCESSPERIOD,
       t.TODATE,
       t.REQUESTDATE,
       t.APPROVEDBYCODE
FROM   DB2ADMIN.LUMPSUMENTRYHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
