# DB2ADMIN.WEAVERGROUP

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `FACTORYCODE`, `DEPARTMENTDEPARTMENTCODE`, `SECTIONSECTIONICSTABLECODE`, `SECTIONSECTIONCODE`, `MATYPEMACHINETYPEICSTABLECODE`, `MACHINETYPEMACHINETYPECODE`, `MACHINENOMACHINENOICSTABLECODE`, `MACHINENOMACHINENOCODE`, `LOOMCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 162315

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `FACTORYCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `FACTORYCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `SECTIONSECTIONICSTABLECODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 6 | `SECTIONSECTIONCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 7 | `MATYPEMACHINETYPEICSTABLECODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 8 | `MACHINETYPEMACHINETYPECODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 9 | `MACHINENOMACHINENOICSTABLECODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 10 | `MACHINENOMACHINENOCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 11 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 12 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 13 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 14 | `PROGRESSTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `STOPPAGETEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `LOOMCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `PROGRESSTEMPLATECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 25 | `STOPPAGETEMPLATECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WEAVERGROUP.COMPANYCODE = COMPANY.CODE` |
| `PRODUCTIONPROGRESSTEMPLATE_PROGRESSTEMPLATE` | `PROGRESSTEMPLATECOMPANYCODE`, `PROGRESSTEMPLATECODE` | [`PRODUCTIONPROGRESSTEMPLATE`](../PRODUCTION/PRODUCTIONPROGRESSTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WEAVERGROUP.PROGRESSTEMPLATECOMPANYCODE = PRODUCTIONPROGRESSTEMPLATE.COMPANYCODE AND WEAVERGROUP.PROGRESSTEMPLATECODE = PRODUCTIONPROGRESSTEMPLATE.CODE` |
| `PRODUCTIONPROGRESSTEMPLATE_STOPPAGETEMPLATE` | `STOPPAGETEMPLATECOMPANYCODE`, `STOPPAGETEMPLATECODE` | [`PRODUCTIONPROGRESSTEMPLATE`](../PRODUCTION/PRODUCTIONPROGRESSTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WEAVERGROUP.STOPPAGETEMPLATECOMPANYCODE = PRODUCTIONPROGRESSTEMPLATE.COMPANYCODE AND WEAVERGROUP.STOPPAGETEMPLATECODE = PRODUCTIONPROGRESSTEMPLATE.CODE` |
| `RESOURCES_LOOM` | `COMPANYCODE`, `LOOMCODE` | [`RESOURCES`](../PRODUCTION/RESOURCES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WEAVERGROUP.COMPANYCODE = RESOURCES.COMPANYCODE AND WEAVERGROUP.LOOMCODE = RESOURCES.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WEAVERGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.DEPARTMENTDEPARTMENTCODE,
       t.SECTIONSECTIONICSTABLECODE,
       t.SECTIONSECTIONCODE,
       t.MATYPEMACHINETYPEICSTABLECODE,
       t.MACHINETYPEMACHINETYPECODE,
       t.MACHINENOMACHINENOICSTABLECODE,
       t.MACHINENOMACHINENOCODE,
       t.LONGDESCRIPTION
FROM   DB2ADMIN.WEAVERGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
