# DB2ADMIN.DIVVSFACTORYVSDEPTVSDESG

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `FACTORYCODE`, `DEPARTMENTDEPARTMENTCODE`, `DESIGNATIONICSTABLECODE`, `DESIGNATIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 151164

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `FACTORYCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `FACTORYCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `DESIGNATIONICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `DESIGNATIONCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `DESIGNATIONLEVEL` | INTEGER | NOT NULL |  |  |  |
| 8 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 9 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 10 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DIVVSFACTORYVSDEPTVSDESG.COMPANYCODE = COMPANY.CODE` |
| `DIVISIONVSFACTORYVSDEPARTMENT_DEPARTMENT` | `COMPANYCODE`, `DIVISIONCODE`, `FACTORYCODE`, `DEPARTMENTDEPARTMENTCODE` | [`DIVISIONVSFACTORYVSDEPARTMENT`](../CORE_MASTER/DIVISIONVSFACTORYVSDEPARTMENT.md) | `COMPANYCODE`, `DIVISIONCODE`, `FACTORYCODE`, `DEPARTMENTCODE` | RESTRICT | `DIVVSFACTORYVSDEPTVSDESG.COMPANYCODE = DIVISIONVSFACTORYVSDEPARTMENT.COMPANYCODE AND DIVVSFACTORYVSDEPTVSDESG.DIVISIONCODE = DIVISIONVSFACTORYVSDEPARTMENT.DIVISIONCODE AND DIVVSFACTORYVSDEPTVSDESG.FACTORYCODE = DIVISIONVSFACTORYVSDEPARTMENT.FACTORYCODE AND DIVVSFACTORYVSDEPTVSDESG.DEPARTMENTDEPARTMENTCODE = DIVISIONVSFACTORYVSDEPARTMENT.DEPARTMENTCODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DIVVSFACTORYVSDEPTVSDESG.COMPANYCODE = DIVISION.COMPANYCODE AND DIVVSFACTORYVSDEPTVSDESG.DIVISIONCODE = DIVISION.CODE` |
| `ICSENTITY_DESIGNATION` | `COMPANYCODE`, `DESIGNATIONICSTABLECODE`, `DESIGNATIONCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `DIVVSFACTORYVSDEPTVSDESG.COMPANYCODE = ICSENTITY.COMPANYCODE AND DIVVSFACTORYVSDEPTVSDESG.DESIGNATIONICSTABLECODE = ICSENTITY.ICSTABLECODE AND DIVVSFACTORYVSDEPTVSDESG.DESIGNATIONCODE = ICSENTITY.CODE` |
| `PLANT_FACTORY` | `FACTORYCOMPANYCODE`, `FACTORYCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DIVVSFACTORYVSDEPTVSDESG.FACTORYCOMPANYCODE = PLANT.COMPANYCODE AND DIVVSFACTORYVSDEPTVSDESG.FACTORYCODE = PLANT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DIVVSFACTORYVSDEPTVSDESGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.DEPARTMENTDEPARTMENTCODE,
       t.DESIGNATIONICSTABLECODE,
       t.DESIGNATIONCODE,
       t.DESIGNATIONLEVEL,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME
FROM   DB2ADMIN.DIVVSFACTORYVSDEPTVSDESG t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
