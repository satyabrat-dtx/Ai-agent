# DB2ADMIN.ESSEMPLOYEESKILL

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `SKILLIDICSTABLECODE`, `SKILLIDCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183209

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SKILLIDICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SKILLIDCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 5 | `EXPERIENCEINYEARS` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 6 | `SKILLLASTUSEDYEAR` | DECIMAL(5,0) |  |  |  |  |
| 7 | `REQUESTFLAG` | INTEGER | NOT NULL |  |  |  |
| 8 | `REQPENDINGWITH` | CHAR(10) |  |  |  |  |
| 9 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ESSEMPLOYEESKILL.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ESSEMPLOYEESKILL.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ESSEMPLOYEESKILL.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `ICSENTITY_SKILLID` | `COMPANYCODE`, `SKILLIDICSTABLECODE`, `SKILLIDCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `ESSEMPLOYEESKILL.COMPANYCODE = ICSENTITY.COMPANYCODE AND ESSEMPLOYEESKILL.SKILLIDICSTABLECODE = ICSENTITY.ICSTABLECODE AND ESSEMPLOYEESKILL.SKILLIDCODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ESSEMPLOYEESKILLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.SKILLIDICSTABLECODE,
       t.SKILLIDCODE,
       t.FROMDATE,
       t.EXPERIENCEINYEARS,
       t.SKILLLASTUSEDYEAR,
       t.REQUESTFLAG,
       t.REQPENDINGWITH,
       t.AUTHLEVEL,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.ESSEMPLOYEESKILL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
