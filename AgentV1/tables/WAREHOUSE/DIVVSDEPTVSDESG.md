# DB2ADMIN.DIVVSDEPTVSDESG

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `DEPARTMENTCODE`, `DESIGNATIONICSTABLECODE`, `DESIGNATIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 151004

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `DEPARTMENTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DESIGNATIONICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `DESIGNATIONCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `NOOFPOST` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DIVVSDEPTVSDESG.COMPANYCODE = COMPANY.CODE` |
| `DEPARTMENT_DEPARTMENT` | `COMPANYCODE`, `DEPARTMENTCODE` | [`DEPARTMENT`](../WAREHOUSE/DEPARTMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DIVVSDEPTVSDESG.COMPANYCODE = DEPARTMENT.COMPANYCODE AND DIVVSDEPTVSDESG.DEPARTMENTCODE = DEPARTMENT.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DIVVSDEPTVSDESG.COMPANYCODE = DIVISION.COMPANYCODE AND DIVVSDEPTVSDESG.DIVISIONCODE = DIVISION.CODE` |
| `ICSENTITY_DESIGNATION` | `COMPANYCODE`, `DESIGNATIONICSTABLECODE`, `DESIGNATIONCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `DIVVSDEPTVSDESG.COMPANYCODE = ICSENTITY.COMPANYCODE AND DIVVSDEPTVSDESG.DESIGNATIONICSTABLECODE = ICSENTITY.ICSTABLECODE AND DIVVSDEPTVSDESG.DESIGNATIONCODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DIVVSDEPTVSDESGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.DEPARTMENTCODE,
       t.DESIGNATIONICSTABLECODE,
       t.DESIGNATIONCODE,
       t.NOOFPOST,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.DIVVSDEPTVSDESG t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
