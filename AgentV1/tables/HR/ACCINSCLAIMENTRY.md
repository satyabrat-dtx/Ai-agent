# DB2ADMIN.ACCINSCLAIMENTRY

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `ACCIDENTNOCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 164612

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ACCIDENTNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `WAGEGROUPWAGEGROUP` | CHAR(4) |  | FK | foreign_key |  |
| 4 | `AVGWAGE` | DECIMAL(11,2) |  |  |  |  |
| 5 | `REPPOLICE` | INTEGER | NOT NULL |  |  |  |
| 6 | `POLICESTNAME` | CHAR(30) |  |  |  |  |
| 7 | `POLICESTADD` | CHAR(100) |  |  |  |  |
| 8 | `ADMINHOSPITAL` | INTEGER | NOT NULL |  |  |  |
| 9 | `DOCTORNAME` | CHAR(30) |  |  |  |  |
| 10 | `HOSPITALCODECODE` | BIGINT | NOT NULL |  |  |  |
| 11 | `HOSPITALADD` | CHAR(100) |  |  |  |  |
| 12 | `PERSONALACCPOLICY` | INTEGER | NOT NULL |  |  |  |
| 13 | `POLICYNUMBER` | CHAR(10) |  |  |  |  |
| 14 | `PLCYPERFROMDATE` | DATE |  |  |  |  |
| 15 | `PLCYPERTODATE` | DATE |  |  |  |  |
| 16 | `ABSFORWORK` | INTEGER | NOT NULL |  |  |  |
| 17 | `LOSSOFDAYS` | DECIMAL(10,0) |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACCINTIMATION_ACCIDENTNO` | `COMPANYCODE`, `ACCIDENTNOCODE` | [`ACCINTIMATION`](../HR/ACCINTIMATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ACCINSCLAIMENTRY.COMPANYCODE = ACCINTIMATION.COMPANYCODE AND ACCINSCLAIMENTRY.ACCIDENTNOCODE = ACCINTIMATION.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ACCINSCLAIMENTRY.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ACCINSCLAIMENTRY.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ACCINSCLAIMENTRY.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `WAGEMASTER_WAGEGROUP` | `COMPANYCODE`, `WAGEGROUPWAGEGROUP` | [`WAGEMASTER`](../HR/WAGEMASTER.md) | `COMPANYCODE`, `WAGEGROUP` | RESTRICT | `ACCINSCLAIMENTRY.COMPANYCODE = WAGEMASTER.COMPANYCODE AND ACCINSCLAIMENTRY.WAGEGROUPWAGEGROUP = WAGEMASTER.WAGEGROUP` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACCINSCLAIMENTRYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.ACCIDENTNOCODE,
       t.WAGEGROUPWAGEGROUP,
       t.AVGWAGE,
       t.REPPOLICE,
       t.POLICESTNAME,
       t.POLICESTADD,
       t.ADMINHOSPITAL,
       t.DOCTORNAME,
       t.HOSPITALCODECODE,
       t.HOSPITALADD
FROM   DB2ADMIN.ACCINSCLAIMENTRY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
