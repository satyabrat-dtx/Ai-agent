# DB2ADMIN.REIMBURSEMENTCLAIM

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 168259

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | BIGINT | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) |  | FK | foreign_key |  |
| 3 | `TRANSACTIONNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 4 | `CLAIMDATE` | DATE | NOT NULL |  |  |  |
| 5 | `CLAIMAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 6 | `SANCTIONAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 7 | `PAYMENTDATE` | DATE |  |  |  |  |
| 8 | `PAYMENTMODE` | CHAR(1) |  |  |  |  |
| 9 | `PAYROLLCODE` | CHAR(3) |  |  |  |  |
| 10 | `PROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 11 | `CHEQUENO` | CHAR(15) |  |  |  |  |
| 12 | `CHEQUEDATE` | DATE |  |  |  |  |
| 13 | `BANKNAME` | CHAR(15) |  |  |  |  |
| 14 | `CHKFAVOUROF` | CHAR(35) |  |  |  |  |
| 15 | `FLAGAUTHORIZED` | INTEGER | NOT NULL |  |  |  |
| 16 | `APPROVALSTATUS` | INTEGER | NOT NULL |  |  |  |
| 17 | `APPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 18 | `APPROVEDDATE` | DATE |  |  |  |  |
| 19 | `REMARK` | CHAR(100) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 26 | `STEP` | CHAR(1) |  |  |  |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `REIMBURSEMENTCLAIM.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_APPROVEDBY` | `COMPANYCODE`, `APPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `REIMBURSEMENTCLAIM.COMPANYCODE = EMPLOYEE.COMPANYCODE AND REIMBURSEMENTCLAIM.APPROVEDBYCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `REIMBURSEMENTCLAIM.COMPANYCODE = EMPLOYEE.COMPANYCODE AND REIMBURSEMENTCLAIM.EMPLOYEEIDCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `REIMBURSEMENTCLAIM_DETAIL` | [`REIMBURSEMENTCLAIMDETAIL`](../HR/REIMBURSEMENTCLAIMDETAIL.md) | `REIMBURSEMENTCLAIMCOMPANYCODE`, `REIMBURSEMENTCLAIMCODE` | `REIMBURSEMENTCLAIMDETAIL.REIMBURSEMENTCLAIMCOMPANYCODE = REIMBURSEMENTCLAIM.COMPANYCODE AND REIMBURSEMENTCLAIMDETAIL.REIMBURSEMENTCLAIMCODE = REIMBURSEMENTCLAIM.CODE` |

## Indexes

- `REIMBURSEMENTCLAIMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.EMPLOYEEIDCODE,
       t.TRANSACTIONNUMBER,
       t.CLAIMDATE,
       t.CLAIMAMOUNT,
       t.SANCTIONAMOUNT,
       t.PAYMENTDATE,
       t.PAYMENTMODE,
       t.PAYROLLCODE,
       t.PROCESSPERIOD,
       t.CHEQUENO
FROM   DB2ADMIN.REIMBURSEMENTCLAIM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
