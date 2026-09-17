# DB2ADMIN.ITCALCULATION

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `FINANCIALYEARCODE`, `FINANCEMONTH`, `EMPLOYEECODE`, `GROUPCODE`, `PAYELEMENTTYPE`, `ITEMCODE`, `PAYELEMENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 166529

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FINANCIALYEARCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINANCEMONTH` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 3 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `GROUPCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 5 | `GRPPRNO` | INTEGER | NOT NULL |  |  |  |
| 6 | `ITEMPRNO` | INTEGER | NOT NULL |  |  |  |
| 7 | `PAYELEMENTTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 8 | `ITEMCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `PAYELEMENTCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 10 | `CALCULATEDAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 11 | `ACTUALAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITCALCULATION.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEE` | `COMPANYCODE`, `EMPLOYEECODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITCALCULATION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ITCALCULATION.EMPLOYEECODE = EMPLOYEE.CODE` |
| `PAYROLLFINANCIALYEAR_FINANCIALYEAR` | `COMPANYCODE`, `FINANCIALYEARCODE` | [`PAYROLLFINANCIALYEAR`](../HR/PAYROLLFINANCIALYEAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITCALCULATION.COMPANYCODE = PAYROLLFINANCIALYEAR.COMPANYCODE AND ITCALCULATION.FINANCIALYEARCODE = PAYROLLFINANCIALYEAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITCALCULATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FINANCIALYEARCODE,
       t.FINANCEMONTH,
       t.EMPLOYEECODE,
       t.GROUPCODE,
       t.GRPPRNO,
       t.ITEMPRNO,
       t.PAYELEMENTTYPE,
       t.ITEMCODE,
       t.PAYELEMENTCODE,
       t.CALCULATEDAMOUNT,
       t.ACTUALAMOUNT
FROM   DB2ADMIN.ITCALCULATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
