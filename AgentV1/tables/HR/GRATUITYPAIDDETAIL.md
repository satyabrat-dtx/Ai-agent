# DB2ADMIN.GRATUITYPAIDDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `FINANCIALYEARCODE`, `EMPLOYEECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 166482

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FINANCIALYEARCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EXITDATE` | DATE |  |  |  |  |
| 4 | `GRATUITYAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 5 | `NUMBEROFDAYS` | DECIMAL(5,2) |  |  |  |  |
| 6 | `NUMBEROFYEARS` | DECIMAL(5,2) |  |  |  |  |
| 7 | `GRATUITYBASEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 8 | `PRPROCESSINGNO` | INTEGER | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `GRATUITYPAIDDETAIL.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEE` | `COMPANYCODE`, `EMPLOYEECODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GRATUITYPAIDDETAIL.COMPANYCODE = EMPLOYEE.COMPANYCODE AND GRATUITYPAIDDETAIL.EMPLOYEECODE = EMPLOYEE.CODE` |
| `PAYROLLFINANCIALYEAR_FINANCIALYEAR` | `COMPANYCODE`, `FINANCIALYEARCODE` | [`PAYROLLFINANCIALYEAR`](../HR/PAYROLLFINANCIALYEAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GRATUITYPAIDDETAIL.COMPANYCODE = PAYROLLFINANCIALYEAR.COMPANYCODE AND GRATUITYPAIDDETAIL.FINANCIALYEARCODE = PAYROLLFINANCIALYEAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `GRATUITYPAIDDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FINANCIALYEARCODE,
       t.EMPLOYEECODE,
       t.EXITDATE,
       t.GRATUITYAMOUNT,
       t.NUMBEROFDAYS,
       t.NUMBEROFYEARS,
       t.GRATUITYBASEAMOUNT,
       t.PRPROCESSINGNO,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.GRATUITYPAIDDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
