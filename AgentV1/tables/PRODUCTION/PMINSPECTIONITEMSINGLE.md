# DB2ADMIN.PMINSPECTIONITEMSINGLE

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 9 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108678

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `PLANTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `PLANTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 11 | `DEPARTMENTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 12 | `HALLUSERGENGRPTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `HALLUSERGENERICGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `HALLCODE` | CHAR(10) |  | FK | foreign_key |  |
| 15 | `WORKCENTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 16 | `PMBOMCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 17 | `PMBOMCODE` | CHAR(15) |  | FK | foreign_key |  |
| 18 | `FREQUENCY` | DECIMAL(11,2) | NOT NULL |  |  |  |
| 19 | `FREQUENCYUOM` | INTEGER | NOT NULL |  |  |  |
| 20 | `INSPECTIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 21 | `READINGUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 22 | `MINIMUMREADING` | DECIMAL(15,5) |  |  |  |  |
| 23 | `MAXIMUMREADING` | DECIMAL(15,5) |  |  |  |  |
| 24 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 30 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 31 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 9

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PMINSPECTIONITEMSINGLE.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONITEMSINGLE.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PMINSPECTIONITEMSINGLE.COUNTERCODE = COUNTER.CODE` |
| `DEPARTMENT_DEPARTMENT` | `COMPANYCODE`, `DEPARTMENTCODE` | [`DEPARTMENT`](../WAREHOUSE/DEPARTMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONITEMSINGLE.COMPANYCODE = DEPARTMENT.COMPANYCODE AND PMINSPECTIONITEMSINGLE.DEPARTMENTCODE = DEPARTMENT.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONITEMSINGLE.COMPANYCODE = DIVISION.COMPANYCODE AND PMINSPECTIONITEMSINGLE.DIVISIONCODE = DIVISION.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONITEMSINGLE.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND PMINSPECTIONITEMSINGLE.PLANTCODE = PLANT.CODE` |
| `PMBOM_PMBOM` | `COMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE` | [`PMBOM`](../CORE_MASTER/PMBOM.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMINSPECTIONITEMSINGLE.COMPANYCODE = PMBOM.COMPANYCODE AND PMINSPECTIONITEMSINGLE.PMBOMCOUNTERCODE = PMBOM.COUNTERCODE AND PMINSPECTIONITEMSINGLE.PMBOMCODE = PMBOM.CODE` |
| `UNITOFMEASURE_READINGUOM` | `READINGUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PMINSPECTIONITEMSINGLE.READINGUOMCODE = UNITOFMEASURE.CODE` |
| `USERGENERICGROUP_HALL` | `HALLUSERGENGRPTYPECOMPANYCODE`, `HALLUSERGENERICGROUPTYPECODE`, `HALLCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `PMINSPECTIONITEMSINGLE.HALLUSERGENGRPTYPECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND PMINSPECTIONITEMSINGLE.HALLUSERGENERICGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND PMINSPECTIONITEMSINGLE.HALLCODE = USERGENERICGROUP.CODE` |
| `WORKCENTER_WORKCENTER` | `COMPANYCODE`, `WORKCENTERCODE` | [`WORKCENTER`](../PRODUCTION/WORKCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONITEMSINGLE.COMPANYCODE = WORKCENTER.COMPANYCODE AND PMINSPECTIONITEMSINGLE.WORKCENTERCODE = WORKCENTER.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PMINSPECTIONITEMSINGLE_INSPECTIONITEM` | [`PMINSPECTIONHEADERSINGLE`](../PRODUCTION/PMINSPECTIONHEADERSINGLE.md) | `COMPANYCODE`, `INSPECTIONITEMCOUNTERCODE`, `INSPECTIONITEMCODE` | `PMINSPECTIONHEADERSINGLE.COMPANYCODE = PMINSPECTIONITEMSINGLE.COMPANYCODE AND PMINSPECTIONHEADERSINGLE.INSPECTIONITEMCOUNTERCODE = PMINSPECTIONITEMSINGLE.COUNTERCODE AND PMINSPECTIONHEADERSINGLE.INSPECTIONITEMCODE = PMINSPECTIONITEMSINGLE.CODE` |

## Indexes

- `PMINSPECTIONITEMSINGLEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.DEPARTMENTCODE
FROM   DB2ADMIN.PMINSPECTIONITEMSINGLE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
