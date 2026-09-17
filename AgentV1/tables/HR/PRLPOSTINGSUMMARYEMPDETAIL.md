# DB2ADMIN.PRLPOSTINGSUMMARYEMPDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 3 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `SNO`, `PAYROLLCODE`, `PROCESSPERIOD`, `LINEID`, `EMPLOYEECODE`, `PAYELEMENTTYPE`, `PAYELEMENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 168095

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SNO` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `PAYROLLCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `LINEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 5 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `PAYELEMENTTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `PAYELEMENTCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 8 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `COSTCENTERCODE` | CHAR(20) |  | FK | foreign_key |  |
| 10 | `GLCODEFLAG` | CHAR(1) |  |  |  |  |
| 11 | `GLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `GLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 13 | `AMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 14 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 15 | `FLAG` | CHAR(10) |  |  |  |  |
| 16 | `SAPMESSAGE` | VARCHAR(500) |  |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRLPOSTINGSUMMARYEMPDETAIL.COMPANYCODE = COMPANY.CODE` |
| `COSTCENTER_COSTCENTER` | `COSTCENTERCOMPANYCODE`, `COSTCENTERCODE` | [`COSTCENTER`](../COSTING/COSTCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRLPOSTINGSUMMARYEMPDETAIL.COSTCENTERCOMPANYCODE = COSTCENTER.COMPANYCODE AND PRLPOSTINGSUMMARYEMPDETAIL.COSTCENTERCODE = COSTCENTER.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `PRLPOSTINGSUMMARYEMPDETAIL.CURRENCYCODE = CURRENCY.CODE` |
| `EMPLOYEE_EMPLOYEE` | `COMPANYCODE`, `EMPLOYEECODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRLPOSTINGSUMMARYEMPDETAIL.COMPANYCODE = EMPLOYEE.COMPANYCODE AND PRLPOSTINGSUMMARYEMPDETAIL.EMPLOYEECODE = EMPLOYEE.CODE` |
| `GLMASTER_GL` | `GLCOMPANYCODE`, `GLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRLPOSTINGSUMMARYEMPDETAIL.GLCOMPANYCODE = GLMASTER.COMPANYCODE AND PRLPOSTINGSUMMARYEMPDETAIL.GLCODE = GLMASTER.CODE` |
| `PAYELEMENT_PAYELEMENT` | `COMPANYCODE`, `PAYELEMENTTYPE`, `PAYELEMENTCODE` | [`PAYELEMENT`](../CORE_MASTER/PAYELEMENT.md) | `COMPANYCODE`, `PAYELEMENTTYPE`, `CODE` | RESTRICT | `PRLPOSTINGSUMMARYEMPDETAIL.COMPANYCODE = PAYELEMENT.COMPANYCODE AND PRLPOSTINGSUMMARYEMPDETAIL.PAYELEMENTTYPE = PAYELEMENT.PAYELEMENTTYPE AND PRLPOSTINGSUMMARYEMPDETAIL.PAYELEMENTCODE = PAYELEMENT.CODE` |
| `PAYROLLTYPE_PAYROLL` | `COMPANYCODE`, `PAYROLLCODE` | [`PAYROLLTYPE`](../HR/PAYROLLTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRLPOSTINGSUMMARYEMPDETAIL.COMPANYCODE = PAYROLLTYPE.COMPANYCODE AND PRLPOSTINGSUMMARYEMPDETAIL.PAYROLLCODE = PAYROLLTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRLPOSTINGSUMMARYEMPDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SNO,
       t.PAYROLLCODE,
       t.PROCESSPERIOD,
       t.LINEID,
       t.EMPLOYEECODE,
       t.PAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.COSTCENTERCOMPANYCODE,
       t.COSTCENTERCODE,
       t.GLCODEFLAG,
       t.GLCOMPANYCODE
FROM   DB2ADMIN.PRLPOSTINGSUMMARYEMPDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
