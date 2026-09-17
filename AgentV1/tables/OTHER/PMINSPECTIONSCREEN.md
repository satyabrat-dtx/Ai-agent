# DB2ADMIN.PMINSPECTIONSCREEN

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 87
- **Primary key**: `COMPANYCODE`, `INSPECTIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 8 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 89089

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `INSPECTIONCODE` | CHAR(12) | NOT NULL | PK | primary_key |  |
| 2 | `INSPECTIONDATE` | DATE | NOT NULL |  |  |  |
| 3 | `PMBOMCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 4 | `PMBOMCODE` | CHAR(15) |  | FK | foreign_key |  |
| 5 | `WORKCENTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 6 | `DEPARTMENTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 7 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `COSTCENTERCODE` | CHAR(20) |  | FK | foreign_key |  |
| 9 | `RESOURCECODE` | CHAR(8) |  | FK | foreign_key |  |
| 10 | `PLANTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `PLANTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 12 | `NUMERICFIELD1` | DECIMAL(10,5) |  |  |  |  |
| 13 | `NUMERICFIELD2` | DECIMAL(10,5) |  |  |  |  |
| 14 | `NUMERICFIELD3` | DECIMAL(10,5) |  |  |  |  |
| 15 | `NUMERICFIELD4` | DECIMAL(10,5) |  |  |  |  |
| 16 | `NUMERICFIELD5` | DECIMAL(10,5) |  |  |  |  |
| 17 | `NUMERICFIELD6` | DECIMAL(10,5) |  |  |  |  |
| 18 | `NUMERICFIELD7` | DECIMAL(10,5) |  |  |  |  |
| 19 | `NUMERICFIELD8` | DECIMAL(10,5) |  |  |  |  |
| 20 | `NUMERICFIELD9` | DECIMAL(10,5) |  |  |  |  |
| 21 | `NUMERICFIELD10` | DECIMAL(10,5) |  |  |  |  |
| 22 | `NUMERICFIELD11` | DECIMAL(10,5) |  |  |  |  |
| 23 | `NUMERICFIELD12` | DECIMAL(10,5) |  |  |  |  |
| 24 | `NUMERICFIELD13` | DECIMAL(10,5) |  |  |  |  |
| 25 | `NUMERICFIELD14` | DECIMAL(10,5) |  |  |  |  |
| 26 | `NUMERICFIELD15` | DECIMAL(10,5) |  |  |  |  |
| 27 | `NUMERICFIELD16` | DECIMAL(10,5) |  |  |  |  |
| 28 | `NUMERICFIELD17` | DECIMAL(10,5) |  |  |  |  |
| 29 | `NUMERICFIELD18` | DECIMAL(10,5) |  |  |  |  |
| 30 | `NUMERICFIELD19` | DECIMAL(10,5) |  |  |  |  |
| 31 | `NUMERICFIELD20` | DECIMAL(10,5) |  |  |  |  |
| 32 | `NUMERICFIELD21` | DECIMAL(10,5) |  |  |  |  |
| 33 | `NUMERICFIELD22` | DECIMAL(10,5) |  |  |  |  |
| 34 | `NUMERICFIELD23` | DECIMAL(10,5) |  |  |  |  |
| 35 | `NUMERICFIELD24` | DECIMAL(10,5) |  |  |  |  |
| 36 | `NUMERICFIELD25` | DECIMAL(10,5) |  |  |  |  |
| 37 | `NUMERICFIELD26` | DECIMAL(10,5) |  |  |  |  |
| 38 | `NUMERICFIELD27` | DECIMAL(10,5) |  |  |  |  |
| 39 | `NUMERICFIELD28` | DECIMAL(10,5) |  |  |  |  |
| 40 | `NUMERICFIELD29` | DECIMAL(10,5) |  |  |  |  |
| 41 | `NUMERICFIELD30` | DECIMAL(10,5) |  |  |  |  |
| 42 | `NUMERICFIELD31` | DECIMAL(10,5) |  |  |  |  |
| 43 | `NUMERICFIELD32` | DECIMAL(10,5) |  |  |  |  |
| 44 | `NUMERICFIELD33` | DECIMAL(10,5) |  |  |  |  |
| 45 | `NUMERICFIELD34` | DECIMAL(10,5) |  |  |  |  |
| 46 | `NUMERICFIELD35` | DECIMAL(10,5) |  |  |  |  |
| 47 | `NUMERICFIELD36` | DECIMAL(10,5) |  |  |  |  |
| 48 | `NUMERICFIELD37` | DECIMAL(10,5) |  |  |  |  |
| 49 | `NUMERICFIELD38` | DECIMAL(10,5) |  |  |  |  |
| 50 | `NUMERICFIELD39` | DECIMAL(10,5) |  |  |  |  |
| 51 | `NUMERICFIELD40` | DECIMAL(10,5) |  |  |  |  |
| 52 | `NUMERICFIELD41` | DECIMAL(10,5) |  |  |  |  |
| 53 | `NUMERICFIELD42` | DECIMAL(10,5) |  |  |  |  |
| 54 | `NUMERICFIELD43` | DECIMAL(10,5) |  |  |  |  |
| 55 | `NUMERICFIELD44` | DECIMAL(10,5) |  |  |  |  |
| 56 | `NUMERICFIELD45` | DECIMAL(10,5) |  |  |  |  |
| 57 | `NUMERICFIELD46` | DECIMAL(10,5) |  |  |  |  |
| 58 | `NUMERICFIELD47` | DECIMAL(10,5) |  |  |  |  |
| 59 | `NUMERICFIELD48` | DECIMAL(10,5) |  |  |  |  |
| 60 | `NUMERICFIELD49` | DECIMAL(10,5) |  |  |  |  |
| 61 | `NUMERICFIELD50` | DECIMAL(10,5) |  |  |  |  |
| 62 | `NUMERICFIELD51` | DECIMAL(10,5) |  |  |  |  |
| 63 | `NUMERICFIELD52` | DECIMAL(10,5) |  |  |  |  |
| 64 | `NUMERICFIELD53` | DECIMAL(10,5) |  |  |  |  |
| 65 | `NUMERICFIELD54` | DECIMAL(10,5) |  |  |  |  |
| 66 | `NUMERICFIELD55` | DECIMAL(10,5) |  |  |  |  |
| 67 | `NUMERICFIELD56` | DECIMAL(10,5) |  |  |  |  |
| 68 | `NUMERICFIELD57` | DECIMAL(10,5) |  |  |  |  |
| 69 | `NUMERICFIELD58` | DECIMAL(10,5) |  |  |  |  |
| 70 | `NUMERICFIELD59` | DECIMAL(10,5) |  |  |  |  |
| 71 | `NUMERICFIELD60` | DECIMAL(10,5) |  |  |  |  |
| 72 | `INSPECTIONTIME` | TIMESTAMP |  |  |  |  |
| 73 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 74 | `INSPECTEDBY` | CHAR(30) |  |  |  |  |
| 75 | `REMARKS` | VARCHAR(1000) |  |  |  |  |
| 76 | `SHIFT` | CHAR(3) |  |  |  |  |
| 77 | `EMPLOYEECODE` | CHAR(10) |  |  |  |  |
| 78 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 79 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 80 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 81 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 82 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 83 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 84 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 85 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 86 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 8

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PMINSPECTIONSCREEN.COMPANYCODE = COMPANY.CODE` |
| `COSTCENTER_COSTCENTER` | `COSTCENTERCOMPANYCODE`, `COSTCENTERCODE` | [`COSTCENTER`](../COSTING/COSTCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONSCREEN.COSTCENTERCOMPANYCODE = COSTCENTER.COMPANYCODE AND PMINSPECTIONSCREEN.COSTCENTERCODE = COSTCENTER.CODE` |
| `DEPARTMENT_DEPARTMENT` | `COMPANYCODE`, `DEPARTMENTCODE` | [`DEPARTMENT`](../WAREHOUSE/DEPARTMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONSCREEN.COMPANYCODE = DEPARTMENT.COMPANYCODE AND PMINSPECTIONSCREEN.DEPARTMENTCODE = DEPARTMENT.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONSCREEN.COMPANYCODE = DIVISION.COMPANYCODE AND PMINSPECTIONSCREEN.DIVISIONCODE = DIVISION.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONSCREEN.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND PMINSPECTIONSCREEN.PLANTCODE = PLANT.CODE` |
| `PMBOM_PMBOM` | `COMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE` | [`PMBOM`](../CORE_MASTER/PMBOM.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMINSPECTIONSCREEN.COMPANYCODE = PMBOM.COMPANYCODE AND PMINSPECTIONSCREEN.PMBOMCOUNTERCODE = PMBOM.COUNTERCODE AND PMINSPECTIONSCREEN.PMBOMCODE = PMBOM.CODE` |
| `RESOURCES_RESOURCE` | `COMPANYCODE`, `RESOURCECODE` | [`RESOURCES`](../PRODUCTION/RESOURCES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONSCREEN.COMPANYCODE = RESOURCES.COMPANYCODE AND PMINSPECTIONSCREEN.RESOURCECODE = RESOURCES.CODE` |
| `WORKCENTER_WORKCENTER` | `COMPANYCODE`, `WORKCENTERCODE` | [`WORKCENTER`](../PRODUCTION/WORKCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONSCREEN.COMPANYCODE = WORKCENTER.COMPANYCODE AND PMINSPECTIONSCREEN.WORKCENTERCODE = WORKCENTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMINSPECTIONSCREENUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.INSPECTIONCODE,
       t.INSPECTIONDATE,
       t.PMBOMCOUNTERCODE,
       t.PMBOMCODE,
       t.WORKCENTERCODE,
       t.DEPARTMENTCODE,
       t.COSTCENTERCOMPANYCODE,
       t.COSTCENTERCODE,
       t.RESOURCECODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE
FROM   DB2ADMIN.PMINSPECTIONSCREEN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
