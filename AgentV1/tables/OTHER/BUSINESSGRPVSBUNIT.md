# DB2ADMIN.BUSINESSGRPVSBUNIT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `ANALYSISCODE`, `DIVISIONCODE`, `PLANTCODE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125149

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ANALYSISCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 3 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `PLANTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `BUSGRPUSGENGRPTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `BUSGRPUSERGENERICGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `BUSGRPCODE` | CHAR(10) |  | FK | foreign_key |  |
| 8 | `BUSUNTCODE` | CHAR(50) |  | FK | foreign_key |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ANALYSISTYPE_ANALYSIS` | `COMPANYCODE`, `ANALYSISCODE` | [`ANALYSISTYPE`](../ITEM_MASTER/ANALYSISTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUSINESSGRPVSBUNIT.COMPANYCODE = ANALYSISTYPE.COMPANYCODE AND BUSINESSGRPVSBUNIT.ANALYSISCODE = ANALYSISTYPE.CODE` |
| `BUSINESSAREAMASTER_BUSUNT` | `BUSUNTCODE` | [`BUSINESSAREAMASTER`](../LOCALIZATION/BUSINESSAREAMASTER.md) | `CODE` | RESTRICT | `BUSINESSGRPVSBUNIT.BUSUNTCODE = BUSINESSAREAMASTER.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BUSINESSGRPVSBUNIT.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUSINESSGRPVSBUNIT.COMPANYCODE = DIVISION.COMPANYCODE AND BUSINESSGRPVSBUNIT.DIVISIONCODE = DIVISION.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUSINESSGRPVSBUNIT.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND BUSINESSGRPVSBUNIT.PLANTCODE = PLANT.CODE` |
| `USERGENERICGROUP_BUSGRP` | `BUSGRPUSGENGRPTYPECOMPANYCODE`, `BUSGRPUSERGENERICGROUPTYPECODE`, `BUSGRPCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `BUSINESSGRPVSBUNIT.BUSGRPUSGENGRPTYPECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND BUSINESSGRPVSBUNIT.BUSGRPUSERGENERICGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND BUSINESSGRPVSBUNIT.BUSGRPCODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BUSINESSGRPVSBUNITUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ANALYSISCODE,
       t.DIVISIONCODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.BUSGRPUSGENGRPTYPECOMPANYCODE,
       t.BUSGRPUSERGENERICGROUPTYPECODE,
       t.BUSGRPCODE,
       t.BUSUNTCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.BUSINESSGRPVSBUNIT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
