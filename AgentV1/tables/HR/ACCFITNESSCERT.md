# DB2ADMIN.ACCFITNESSCERT

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `YEAR`, `EMPLOYEENOCODE`, `ACCIDENTNOCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 149473

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `YEAR` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 2 | `EMPLOYEENOCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ACCIDENTNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CODE` | BIGINT | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `FLAG` | INTEGER | NOT NULL |  |  |  |
| 6 | `FITCERTDATE` | DATE | NOT NULL |  |  |  |
| 7 | `RECDATE` | DATE | NOT NULL |  |  |  |
| 8 | `REMARKS` | CHAR(100) |  |  |  |  |
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
| `ACCINTIMATION_ACCIDENTNO` | `COMPANYCODE`, `ACCIDENTNOCODE` | [`ACCINTIMATION`](../HR/ACCINTIMATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ACCFITNESSCERT.COMPANYCODE = ACCINTIMATION.COMPANYCODE AND ACCFITNESSCERT.ACCIDENTNOCODE = ACCINTIMATION.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ACCFITNESSCERT.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEENO` | `COMPANYCODE`, `EMPLOYEENOCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ACCFITNESSCERT.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ACCFITNESSCERT.EMPLOYEENOCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACCFITNESSCERTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.YEAR,
       t.EMPLOYEENOCODE,
       t.ACCIDENTNOCODE,
       t.CODE,
       t.FLAG,
       t.FITCERTDATE,
       t.RECDATE,
       t.REMARKS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.ACCFITNESSCERT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
