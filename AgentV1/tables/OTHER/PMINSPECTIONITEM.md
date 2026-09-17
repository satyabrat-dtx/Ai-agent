# DB2ADMIN.PMINSPECTIONITEM

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 84035

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `FREQUENCY` | DECIMAL(11,2) | NOT NULL |  |  |  |
| 8 | `FREQUENCYUOM` | INTEGER | NOT NULL |  |  |  |
| 9 | `INSPECTIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 10 | `READINGUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `MINIMUMREADING` | DECIMAL(15,5) |  |  |  |  |
| 12 | `MAXIMUMREADING` | DECIMAL(15,5) |  |  |  |  |
| 13 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 20 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PMINSPECTIONITEM.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONITEM.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PMINSPECTIONITEM.COUNTERCODE = COUNTER.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMINSPECTIONITEM.COMPANYCODE = DIVISION.COMPANYCODE AND PMINSPECTIONITEM.DIVISIONCODE = DIVISION.CODE` |
| `UNITOFMEASURE_READINGUOM` | `READINGUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PMINSPECTIONITEM.READINGUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PMINSPECTIONITEM_INSPECTIONITEM` | [`PMINSPECTION`](../OTHER/PMINSPECTION.md) | `COMPANYCODE`, `INSPECTIONITEMCOUNTERCODE`, `INSPECTIONITEMCODE` | `PMINSPECTION.COMPANYCODE = PMINSPECTIONITEM.COMPANYCODE AND PMINSPECTION.INSPECTIONITEMCOUNTERCODE = PMINSPECTIONITEM.COUNTERCODE AND PMINSPECTION.INSPECTIONITEMCODE = PMINSPECTIONITEM.CODE` |
| `PMINSPECTIONITEM_LINE` | [`PMINSPECTIONITEMDETAIL`](../OTHER/PMINSPECTIONITEMDETAIL.md) | `PMINSPECTIONITEMCOMPANYCODE`, `PMINSPECTIONITEMCOUNTERCODE`, `PMINSPECTIONITEMCODE` | `PMINSPECTIONITEMDETAIL.PMINSPECTIONITEMCOMPANYCODE = PMINSPECTIONITEM.COMPANYCODE AND PMINSPECTIONITEMDETAIL.PMINSPECTIONITEMCOUNTERCODE = PMINSPECTIONITEM.COUNTERCODE AND PMINSPECTIONITEMDETAIL.PMINSPECTIONITEMCODE = PMINSPECTIONITEM.CODE` |

## Indexes

- `PMINSPECTIONITEMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.FREQUENCY,
       t.FREQUENCYUOM,
       t.INSPECTIONTYPE,
       t.READINGUOMCODE,
       t.MINIMUMREADING
FROM   DB2ADMIN.PMINSPECTIONITEM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
