# DB2ADMIN.REIMBURSEMENTELIGIBILITY

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `GROUPGROUPCODE`, `EMPLOYEEIDCODE`, `PROCESSYEAR`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 168424

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `GROUPGROUPCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PROCESSYEAR` | CHAR(7) | NOT NULL | PK | primary_key |  |
| 4 | `BASEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `REIMBURSEMENTELIGIBILITY.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `REIMBURSEMENTELIGIBILITY.COMPANYCODE = EMPLOYEE.COMPANYCODE AND REIMBURSEMENTELIGIBILITY.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `REIMBURSEMENTGRPHEADER_GROUP` | `COMPANYCODE`, `GROUPGROUPCODE` | [`REIMBURSEMENTGRPHEADER`](../HR/REIMBURSEMENTGRPHEADER.md) | `COMPANYCODE`, `GROUPCODE` | RESTRICT | `REIMBURSEMENTELIGIBILITY.COMPANYCODE = REIMBURSEMENTGRPHEADER.COMPANYCODE AND REIMBURSEMENTELIGIBILITY.GROUPGROUPCODE = REIMBURSEMENTGRPHEADER.GROUPCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `REIMBURSEMENTELIGIBILITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.GROUPGROUPCODE,
       t.EMPLOYEEIDCODE,
       t.PROCESSYEAR,
       t.BASEAMOUNT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.REIMBURSEMENTELIGIBILITY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
