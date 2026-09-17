# DB2ADMIN.OTHERINCOME

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `FINANCIALYEARCODE`, `EMPLOYEEIDCODE`, `GROUPCODE`, `GROUPITEMCODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 167699

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FINANCIALYEARCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `GROUPCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `GROUPITEMCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `AMOUNT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `OTHERINCOME.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `OTHERINCOME.COMPANYCODE = EMPLOYEE.COMPANYCODE AND OTHERINCOME.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `GROUPITEM_GROUPITEM` | `COMPANYCODE`, `FINANCIALYEARCODE`, `GROUPCODE`, `GROUPITEMCODE` | [`GROUPITEM`](../HR/GROUPITEM.md) | `INVESTMENTGROUPCOMPANYCODE`, `INVESTMENTGRPFINANCIALYEARCOD`, `INVESTMENTGROUPCODE`, `CODE` | RESTRICT | `OTHERINCOME.COMPANYCODE = GROUPITEM.INVESTMENTGROUPCOMPANYCODE AND OTHERINCOME.FINANCIALYEARCODE = GROUPITEM.INVESTMENTGRPFINANCIALYEARCOD AND OTHERINCOME.GROUPCODE = GROUPITEM.INVESTMENTGROUPCODE AND OTHERINCOME.GROUPITEMCODE = GROUPITEM.CODE` |
| `INVESTMENTGROUP_GROUP` | `COMPANYCODE`, `FINANCIALYEARCODE`, `GROUPCODE` | [`INVESTMENTGROUP`](../HR/INVESTMENTGROUP.md) | `COMPANYCODE`, `FINANCIALYEARCODE`, `CODE` | RESTRICT | `OTHERINCOME.COMPANYCODE = INVESTMENTGROUP.COMPANYCODE AND OTHERINCOME.FINANCIALYEARCODE = INVESTMENTGROUP.FINANCIALYEARCODE AND OTHERINCOME.GROUPCODE = INVESTMENTGROUP.CODE` |
| `PAYROLLFINANCIALYEAR_FINANCIALYEAR` | `COMPANYCODE`, `FINANCIALYEARCODE` | [`PAYROLLFINANCIALYEAR`](../HR/PAYROLLFINANCIALYEAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `OTHERINCOME.COMPANYCODE = PAYROLLFINANCIALYEAR.COMPANYCODE AND OTHERINCOME.FINANCIALYEARCODE = PAYROLLFINANCIALYEAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `OTHERINCOMEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FINANCIALYEARCODE,
       t.EMPLOYEEIDCODE,
       t.GROUPCODE,
       t.GROUPITEMCODE,
       t.AMOUNT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.OTHERINCOME t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
