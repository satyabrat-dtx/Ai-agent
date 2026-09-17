# DB2ADMIN.MEDICALCOMPCALC

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 158142

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | BIGINT | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `CALYEARCODE` | CHAR(6) |  | FK | foreign_key |  |
| 3 | `ACCNOCODE` | BIGINT | NOT NULL | FK | foreign_key |  |
| 4 | `EMPLOYEEIDCODE` | CHAR(9) |  | FK | foreign_key |  |
| 5 | `DATEOFACC` | DATE |  |  |  |  |
| 6 | `AVGSALARY` | DECIMAL(11,2) |  |  |  |  |
| 7 | `MAXSALFORCOMP` | DECIMAL(6,2) |  |  |  |  |
| 8 | `MAXSALFORCOMPPERC` | DECIMAL(6,2) |  |  |  |  |
| 9 | `JOININGDATE` | DATE |  |  |  |  |
| 10 | `BIRTHDATE` | DATE |  |  |  |  |
| 11 | `AGEYRS` | DECIMAL(3,0) |  |  |  |  |
| 12 | `AGEFACTOR` | DECIMAL(7,2) |  |  |  |  |
| 13 | `MULTIFACTOR` | DECIMAL(10,0) |  |  |  |  |
| 14 | `DISABILITY` | DECIMAL(5,2) |  |  |  |  |
| 15 | `COMPAMT` | DECIMAL(11,2) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACCINTIMATION_ACCNO` | `COMPANYCODE`, `ACCNOCODE` | [`ACCINTIMATION`](../HR/ACCINTIMATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MEDICALCOMPCALC.COMPANYCODE = ACCINTIMATION.COMPANYCODE AND MEDICALCOMPCALC.ACCNOCODE = ACCINTIMATION.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MEDICALCOMPCALC.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MEDICALCOMPCALC.COMPANYCODE = EMPLOYEE.COMPANYCODE AND MEDICALCOMPCALC.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `PAYROLLFINANCIALYEAR_CALYEAR` | `COMPANYCODE`, `CALYEARCODE` | [`PAYROLLFINANCIALYEAR`](../HR/PAYROLLFINANCIALYEAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MEDICALCOMPCALC.COMPANYCODE = PAYROLLFINANCIALYEAR.COMPANYCODE AND MEDICALCOMPCALC.CALYEARCODE = PAYROLLFINANCIALYEAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MEDICALCOMPCALCUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.CALYEARCODE,
       t.ACCNOCODE,
       t.EMPLOYEEIDCODE,
       t.DATEOFACC,
       t.AVGSALARY,
       t.MAXSALFORCOMP,
       t.MAXSALFORCOMPPERC,
       t.JOININGDATE,
       t.BIRTHDATE,
       t.AGEYRS
FROM   DB2ADMIN.MEDICALCOMPCALC t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
