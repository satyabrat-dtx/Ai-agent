# DB2ADMIN.PMINSPECTION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `COMPANYCODE`, `INSPECTIONITEMCOUNTERCODE`, `INSPECTIONITEMCODE`, `INSPECTIONDATE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 8 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 83973

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `INSPECTIONDATE` | DATE | NOT NULL | PK | primary_key |  |
| 2 | `INSPECTIONITEMCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `INSPECTIONITEMCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ITEMLINENOLINENO` | INTEGER | NOT NULL | FK | foreign_key |  |
| 5 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `PMBOMCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 9 | `PMBOMCODE` | CHAR(15) |  | FK | foreign_key |  |
| 10 | `DEPARTMENTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 11 | `RESOURCECODE` | CHAR(8) |  | FK | foreign_key |  |
| 12 | `MANNUALITEM` | CHAR(15) |  |  |  |  |
| 13 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 14 | `INSPECTIONTIME` | TIMESTAMP |  |  |  |  |
| 15 | `INITIALREADING` | DECIMAL(15,5) |  |  |  |  |
| 16 | `CURRENTREADING` | DECIMAL(15,5) |  |  |  |  |
| 17 | `READINGDIFF` | DECIMAL(15,5) |  |  |  |  |
| 18 | `READINGUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `INSPECTIONBY` | CHAR(100) |  |  |  |  |
| 20 | `STATUSTYPE` | INTEGER | NOT NULL |  |  |  |
| 21 | `REMARKS` | VARCHAR(1000) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 8

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PMINSPECTION.COMPANYCODE = COMPANY.CODE` |
| `DEPARTMENT_DEPARTMENT` | `COMPANYCODE`, `DEPARTMENTCODE` | [`DEPARTMENT`](../WAREHOUSE/DEPARTMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTION.COMPANYCODE = DEPARTMENT.COMPANYCODE AND PMINSPECTION.DEPARTMENTCODE = DEPARTMENT.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTION.COMPANYCODE = DIVISION.COMPANYCODE AND PMINSPECTION.DIVISIONCODE = DIVISION.CODE` |
| `PMBOM_PMBOM` | `COMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE` | [`PMBOM`](../CORE_MASTER/PMBOM.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMINSPECTION.COMPANYCODE = PMBOM.COMPANYCODE AND PMINSPECTION.PMBOMCOUNTERCODE = PMBOM.COUNTERCODE AND PMINSPECTION.PMBOMCODE = PMBOM.CODE` |
| `PMINSPECTIONITEMDETAIL_ITEMLINENO` | `COMPANYCODE`, `INSPECTIONITEMCOUNTERCODE`, `INSPECTIONITEMCODE`, `ITEMLINENOLINENO` | [`PMINSPECTIONITEMDETAIL`](../OTHER/PMINSPECTIONITEMDETAIL.md) | `PMINSPECTIONITEMCOMPANYCODE`, `PMINSPECTIONITEMCOUNTERCODE`, `PMINSPECTIONITEMCODE`, `LINENO` | RESTRICT | `PMINSPECTION.COMPANYCODE = PMINSPECTIONITEMDETAIL.PMINSPECTIONITEMCOMPANYCODE AND PMINSPECTION.INSPECTIONITEMCOUNTERCODE = PMINSPECTIONITEMDETAIL.PMINSPECTIONITEMCOUNTERCODE AND PMINSPECTION.INSPECTIONITEMCODE = PMINSPECTIONITEMDETAIL.PMINSPECTIONITEMCODE AND PMINSPECTION.ITEMLINENOLINENO = PMINSPECTIONITEMDETAIL.LINENO` |
| `PMINSPECTIONITEM_INSPECTIONITEM` | `COMPANYCODE`, `INSPECTIONITEMCOUNTERCODE`, `INSPECTIONITEMCODE` | [`PMINSPECTIONITEM`](../OTHER/PMINSPECTIONITEM.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMINSPECTION.COMPANYCODE = PMINSPECTIONITEM.COMPANYCODE AND PMINSPECTION.INSPECTIONITEMCOUNTERCODE = PMINSPECTIONITEM.COUNTERCODE AND PMINSPECTION.INSPECTIONITEMCODE = PMINSPECTIONITEM.CODE` |
| `RESOURCES_RESOURCE` | `COMPANYCODE`, `RESOURCECODE` | [`RESOURCES`](../PRODUCTION/RESOURCES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTION.COMPANYCODE = RESOURCES.COMPANYCODE AND PMINSPECTION.RESOURCECODE = RESOURCES.CODE` |
| `UNITOFMEASURE_READINGUOM` | `READINGUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PMINSPECTION.READINGUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMINSPECTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.INSPECTIONDATE,
       t.INSPECTIONITEMCOUNTERCODE,
       t.INSPECTIONITEMCODE,
       t.ITEMLINENOLINENO,
       t.LINENO,
       t.ABSUNIQUEID,
       t.SHORTDESCRIPTION,
       t.PMBOMCOUNTERCODE,
       t.PMBOMCODE,
       t.DEPARTMENTCODE,
       t.RESOURCECODE
FROM   DB2ADMIN.PMINSPECTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
