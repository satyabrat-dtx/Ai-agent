# DB2ADMIN.CSRMTEMPLATE

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118757

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 1 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `PLANTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `PLANTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 9 | `DEPARTMENTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 10 | `LETTERTEMPLATECODE` | CHAR(30) |  | FK | foreign_key |  |
| 11 | `ORDERPARTNERTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `TERMSOFLOGCODE` | CHAR(2) |  | FK | foreign_key |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSLETTERTEMPLATE_LETTERTEMPLATE` | `COMPANYCODE`, `LETTERTEMPLATECODE` | [`ABSLETTERTEMPLATE`](../PLATFORM/ABSLETTERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMTEMPLATE.COMPANYCODE = ABSLETTERTEMPLATE.COMPANYCODE AND CSRMTEMPLATE.LETTERTEMPLATECODE = ABSLETTERTEMPLATE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CSRMTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `CSRMTERMSOFLOG_TERMSOFLOG` | `COMPANYCODE`, `TERMSOFLOGCODE` | [`CSRMTERMSOFLOG`](../PLATFORM/CSRMTERMSOFLOG.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMTEMPLATE.COMPANYCODE = CSRMTERMSOFLOG.COMPANYCODE AND CSRMTEMPLATE.TERMSOFLOGCODE = CSRMTERMSOFLOG.CODE` |
| `DEPARTMENT_DEPARTMENT` | `COMPANYCODE`, `DEPARTMENTCODE` | [`DEPARTMENT`](../WAREHOUSE/DEPARTMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMTEMPLATE.COMPANYCODE = DEPARTMENT.COMPANYCODE AND CSRMTEMPLATE.DEPARTMENTCODE = DEPARTMENT.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMTEMPLATE.COMPANYCODE = DIVISION.COMPANYCODE AND CSRMTEMPLATE.DIVISIONCODE = DIVISION.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMTEMPLATE.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND CSRMTEMPLATE.PLANTCODE = PLANT.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `CSRMTEMPLATE_TEMPLATE` | [`CSRM`](../PLATFORM/CSRM.md) | `COMPANYCODE`, `TEMPLATECODE` | `CSRM.COMPANYCODE = CSRMTEMPLATE.COMPANYCODE AND CSRM.TEMPLATECODE = CSRMTEMPLATE.CODE` |
| `CSRMTEMPLATE_CSRMTEMPLATE` | [`CSRMCOUNTERDEFINITION`](../PLATFORM/CSRMCOUNTERDEFINITION.md) | `COMPANYCODE`, `CSRMTEMPLATECODE` | `CSRMCOUNTERDEFINITION.COMPANYCODE = CSRMTEMPLATE.COMPANYCODE AND CSRMCOUNTERDEFINITION.CSRMTEMPLATECODE = CSRMTEMPLATE.CODE` |
| `CSRMTEMPLATE_TEAM` | [`CSRMTEMPLATETEAM`](../PLATFORM/CSRMTEMPLATETEAM.md) | `CSRMTEMPLATECOMPANYCODE`, `CSRMTEMPLATECODE` | `CSRMTEMPLATETEAM.CSRMTEMPLATECOMPANYCODE = CSRMTEMPLATE.COMPANYCODE AND CSRMTEMPLATETEAM.CSRMTEMPLATECODE = CSRMTEMPLATE.CODE` |

## Indexes

- `CSRMTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.DEPARTMENTCODE,
       t.LETTERTEMPLATECODE,
       t.ORDERPARTNERTYPE
FROM   DB2ADMIN.CSRMTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
