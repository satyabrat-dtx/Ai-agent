# DB2ADMIN.REIMBURSEMENTBALANCE

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `REIMBURSEMENTTYPECODE`, `EMPLOYEEIDCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 168212

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `REIMBURSEMENTTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `REIMBURSEMENTELIGIBILITYAMOUNT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 4 | `CARRYFORWARDAMOUNT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 5 | `AVAILEDAMOUNT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 6 | `BALANCEAMOUNT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 7 | `PAYELEMENTTYPE` | CHAR(1) |  |  |  |  |
| 8 | `PAYELEMENTCODE` | CHAR(6) |  |  |  |  |
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
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `REIMBURSEMENTBALANCE.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `REIMBURSEMENTBALANCE.COMPANYCODE = EMPLOYEE.COMPANYCODE AND REIMBURSEMENTBALANCE.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `REIMBURSEMENTTYPE_REIMBURSEMENTTYPE` | `COMPANYCODE`, `REIMBURSEMENTTYPECODE` | [`REIMBURSEMENTTYPE`](../HR/REIMBURSEMENTTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `REIMBURSEMENTBALANCE.COMPANYCODE = REIMBURSEMENTTYPE.COMPANYCODE AND REIMBURSEMENTBALANCE.REIMBURSEMENTTYPECODE = REIMBURSEMENTTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `REIMBURSEMENTBALANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.REIMBURSEMENTTYPECODE,
       t.EMPLOYEEIDCODE,
       t.REIMBURSEMENTELIGIBILITYAMOUNT,
       t.CARRYFORWARDAMOUNT,
       t.AVAILEDAMOUNT,
       t.BALANCEAMOUNT,
       t.PAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.REIMBURSEMENTBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
