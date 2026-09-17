# DB2ADMIN.PENDINGDEDUCTIONDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `PAYROLLTYPECODE`, `PROCESSPERIOD`, `ATTENDANCETYPECODE`, `PAYELEMENTTYPE`, `PAYELEMENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 167955

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PAYROLLTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PAYELEMENTTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 6 | `PAYELEMENTCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 7 | `AMOUNTTODEDUCT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `AMOUNTDEDUCTED` | DECIMAL(18,5) |  |  |  |  |
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
| `ATTENDANCETYPE_ATTENDANCETYPE` | `COMPANYCODE`, `ATTENDANCETYPECODE` | [`ATTENDANCETYPE`](../HR/ATTENDANCETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PENDINGDEDUCTIONDETAIL.COMPANYCODE = ATTENDANCETYPE.COMPANYCODE AND PENDINGDEDUCTIONDETAIL.ATTENDANCETYPECODE = ATTENDANCETYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PENDINGDEDUCTIONDETAIL.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PENDINGDEDUCTIONDETAIL.COMPANYCODE = EMPLOYEE.COMPANYCODE AND PENDINGDEDUCTIONDETAIL.EMPLOYEEIDCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PENDINGDEDUCTIONDETAILUID` (ABSUNIQUEID)
- `PENDDEDDET1` (COMPANYCODE, EMPLOYEEIDCODE, PAYROLLTYPECODE, ATTENDANCETYPECODE, PAYELEMENTTYPE, PAYELEMENTCODE)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.PAYROLLTYPECODE,
       t.PROCESSPERIOD,
       t.ATTENDANCETYPECODE,
       t.PAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.AMOUNTTODEDUCT,
       t.AMOUNTDEDUCTED,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.PENDINGDEDUCTIONDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
