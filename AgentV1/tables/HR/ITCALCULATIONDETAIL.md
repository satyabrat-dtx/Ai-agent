# DB2ADMIN.ITCALCULATIONDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `FINANCIALYEARCODE`, `FINANCEMONTH`, `EMPLOYEECODE`, `PROCESSPERIOD`, `GROUPCODE`, `ITEMCODE`, `PAYELEMENTTYPE`, `PAYELEMENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 166584

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FINANCIALYEARCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINANCEMONTH` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 3 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `GROUPCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `ITEMCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `GROUPPRNUMBER` | INTEGER | NOT NULL |  |  |  |
| 8 | `ITEMPRNUMBER` | INTEGER | NOT NULL |  |  |  |
| 9 | `PAYELEMENTTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 10 | `PAYELEMENTCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 11 | `CALCULATEDAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 12 | `ACTUALAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITCALCULATIONDETAIL.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEE` | `COMPANYCODE`, `EMPLOYEECODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITCALCULATIONDETAIL.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ITCALCULATIONDETAIL.EMPLOYEECODE = EMPLOYEE.CODE` |
| `INVESTMENTGROUP_GROUP` | `COMPANYCODE`, `FINANCIALYEARCODE`, `GROUPCODE` | [`INVESTMENTGROUP`](../HR/INVESTMENTGROUP.md) | `COMPANYCODE`, `FINANCIALYEARCODE`, `CODE` | RESTRICT | `ITCALCULATIONDETAIL.COMPANYCODE = INVESTMENTGROUP.COMPANYCODE AND ITCALCULATIONDETAIL.FINANCIALYEARCODE = INVESTMENTGROUP.FINANCIALYEARCODE AND ITCALCULATIONDETAIL.GROUPCODE = INVESTMENTGROUP.CODE` |
| `PAYROLLFINANCIALYEAR_FINANCIALYEAR` | `COMPANYCODE`, `FINANCIALYEARCODE` | [`PAYROLLFINANCIALYEAR`](../HR/PAYROLLFINANCIALYEAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITCALCULATIONDETAIL.COMPANYCODE = PAYROLLFINANCIALYEAR.COMPANYCODE AND ITCALCULATIONDETAIL.FINANCIALYEARCODE = PAYROLLFINANCIALYEAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITCALCULATIONDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FINANCIALYEARCODE,
       t.FINANCEMONTH,
       t.EMPLOYEECODE,
       t.PROCESSPERIOD,
       t.GROUPCODE,
       t.ITEMCODE,
       t.GROUPPRNUMBER,
       t.ITEMPRNUMBER,
       t.PAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.CALCULATEDAMOUNT
FROM   DB2ADMIN.ITCALCULATIONDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
