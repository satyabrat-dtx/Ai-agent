# DB2ADMIN.INSURANCEINTIMATION

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 166869

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 5 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 6 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 7 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INSURANCEINTIMATION.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INSURANCEINTIMATION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND INSURANCEINTIMATION.EMPLOYEEIDCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `INSURANCEINTIMATION_LINE` | [`INSURANCEINTIMATIONDETAIL`](../HR/INSURANCEINTIMATIONDETAIL.md) | `INSURANCEINTIMATIONCOMPANYCODE`, `ININTIMATIONEMPLOYEEIDCODE` | `INSURANCEINTIMATIONDETAIL.INSURANCEINTIMATIONCOMPANYCODE = INSURANCEINTIMATION.COMPANYCODE AND INSURANCEINTIMATIONDETAIL.ININTIMATIONEMPLOYEEIDCODE = INSURANCEINTIMATION.EMPLOYEEIDCODE` |

## Indexes

- `INSURANCEINTIMATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.INSURANCEINTIMATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
