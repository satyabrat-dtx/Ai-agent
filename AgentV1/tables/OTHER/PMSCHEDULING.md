# DB2ADMIN.PMSCHEDULING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `PRVMAINTENANCECOUNTERCODE`, `PREVENTIVEMAINTENANCECODE`, `SCHEDULEID`
- **FK degree**: referenced by 0 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 84394

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRVMAINTENANCECOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PREVENTIVEMAINTENANCECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SCHEDULEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `PMBOMCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 5 | `PMBOMCODE` | CHAR(15) |  | FK | foreign_key |  |
| 6 | `PLANTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `PLANTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 8 | `DEPARTMENTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 9 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 10 | `SCHEDULEDDATE` | DATE | NOT NULL |  |  |  |
| 11 | `ESTIMATEDDURATION` | DECIMAL(11,2) | NOT NULL |  |  |  |
| 12 | `DURATIONUOMCODE` | INTEGER | NOT NULL |  |  |  |
| 13 | `WORKORDERCREATED` | INTEGER | NOT NULL |  |  |  |
| 14 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 21 | `LINEIDPMWORKORDERCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 22 | `LINEIDPMWORKORDERCODE` | CHAR(15) |  | FK | foreign_key |  |
| 23 | `LINEIDSCHEDULEID` | INTEGER | NOT NULL | FK | foreign_key |  |
| 24 | `LINEIDLINEID` | INTEGER | NOT NULL | FK | foreign_key |  |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PMSCHEDULING.COMPANYCODE = COMPANY.CODE` |
| `DEPARTMENT_DEPARTMENT` | `COMPANYCODE`, `DEPARTMENTCODE` | [`DEPARTMENT`](../WAREHOUSE/DEPARTMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMSCHEDULING.COMPANYCODE = DEPARTMENT.COMPANYCODE AND PMSCHEDULING.DEPARTMENTCODE = DEPARTMENT.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMSCHEDULING.COMPANYCODE = DIVISION.COMPANYCODE AND PMSCHEDULING.DIVISIONCODE = DIVISION.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMSCHEDULING.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND PMSCHEDULING.PLANTCODE = PLANT.CODE` |
| `PMBOM_PMBOM` | `COMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE` | [`PMBOM`](../CORE_MASTER/PMBOM.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMSCHEDULING.COMPANYCODE = PMBOM.COMPANYCODE AND PMSCHEDULING.PMBOMCOUNTERCODE = PMBOM.COUNTERCODE AND PMSCHEDULING.PMBOMCODE = PMBOM.CODE` |
| `PMPRVMNT_PREVENTIVEMAINTENANCE` | `COMPANYCODE`, `PRVMAINTENANCECOUNTERCODE`, `PREVENTIVEMAINTENANCECODE` | [`PMPRVMNT`](../PLATFORM/PMPRVMNT.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMSCHEDULING.COMPANYCODE = PMPRVMNT.COMPANYCODE AND PMSCHEDULING.PRVMAINTENANCECOUNTERCODE = PMPRVMNT.COUNTERCODE AND PMSCHEDULING.PREVENTIVEMAINTENANCECODE = PMPRVMNT.CODE` |
| `PMWRKORDSCHEDULEDETAIL_LINEID` | `COMPANYCODE`, `LINEIDPMWORKORDERCOUNTERCODE`, `LINEIDPMWORKORDERCODE`, `LINEIDSCHEDULEID`, `LINEIDLINEID` | [`PMWRKORDSCHEDULEDETAIL`](../OTHER/PMWRKORDSCHEDULEDETAIL.md) | `COMPANYCODE`, `PMWORKORDERCOUNTERCODE`, `PMWORKORDERCODE`, `SCHEDULEID`, `LINEID` | RESTRICT | `PMSCHEDULING.COMPANYCODE = PMWRKORDSCHEDULEDETAIL.COMPANYCODE AND PMSCHEDULING.LINEIDPMWORKORDERCOUNTERCODE = PMWRKORDSCHEDULEDETAIL.PMWORKORDERCOUNTERCODE AND PMSCHEDULING.LINEIDPMWORKORDERCODE = PMWRKORDSCHEDULEDETAIL.PMWORKORDERCODE AND PMSCHEDULING.LINEIDSCHEDULEID = PMWRKORDSCHEDULEDETAIL.SCHEDULEID AND PMSCHEDULING.LINEIDLINEID = PMWRKORDSCHEDULEDETAIL.LINEID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMSCHEDULINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRVMAINTENANCECOUNTERCODE,
       t.PREVENTIVEMAINTENANCECODE,
       t.SCHEDULEID,
       t.PMBOMCOUNTERCODE,
       t.PMBOMCODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.DEPARTMENTCODE,
       t.DIVISIONCODE,
       t.SCHEDULEDDATE,
       t.ESTIMATEDDURATION
FROM   DB2ADMIN.PMSCHEDULING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
