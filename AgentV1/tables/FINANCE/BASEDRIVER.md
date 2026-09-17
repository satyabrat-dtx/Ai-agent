# DB2ADMIN.BASEDRIVER

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 3 of 3 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 4 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 100957

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(5) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `BASETYPE` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `BASEGROUPSYSTEMTABLECODE` | CHAR(5) |  | FK | foreign_key |  |
| 9 | `BASEGROUPCODE` | CHAR(10) |  | FK | foreign_key |  |
| 10 | `BASEDIMENSION` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `UNITOFMAESURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `ACCOUNTACTIVITYALLOCCODE` | CHAR(10) |  | FK | foreign_key |  |
| 13 | `INITIALDATE` | DATE |  |  |  |  |
| 14 | `FINALDATE` | DATE |  |  |  |  |
| 15 | `INACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BASEDRIVER.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BASEDRIVER.COMPANYCODE = DIVISION.COMPANYCODE AND BASEDRIVER.DIVISIONCODE = DIVISION.CODE` |
| `GENERALLEDGERACCOUNT_ACCOUNTACTIVITYALLOC` | `COMPANYCODE`, `ACCOUNTACTIVITYALLOCCODE` | [`GENERALLEDGERACCOUNT`](../FINANCE/GENERALLEDGERACCOUNT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BASEDRIVER.COMPANYCODE = GENERALLEDGERACCOUNT.COMPANYCODE AND BASEDRIVER.ACCOUNTACTIVITYALLOCCODE = GENERALLEDGERACCOUNT.CODE` |
| `SYSTEMTABLERECORDS_BASEGROUP` | `BASEGROUPSYSTEMTABLECODE`, `BASEGROUPCODE` | [`SYSTEMTABLERECORDS`](../FINANCE/SYSTEMTABLERECORDS.md) | `SYSTEMTABLECODE`, `CODE` | RESTRICT | `BASEDRIVER.BASEGROUPSYSTEMTABLECODE = SYSTEMTABLERECORDS.SYSTEMTABLECODE AND BASEDRIVER.BASEGROUPCODE = SYSTEMTABLERECORDS.CODE` |
| `UNITOFMEASURE_UNITOFMAESURE` | `UNITOFMAESURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `BASEDRIVER.UNITOFMAESURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `BASEDRIVER_QUANTITYUNIT` | [`FINVOULINES`](../FINANCE/FINVOULINES.md) | `FINVOUHEADERCOMPANYCODE`, `QUANTITYUNITCODE` | `FINVOULINES.FINVOUHEADERCOMPANYCODE = BASEDRIVER.COMPANYCODE AND FINVOULINES.QUANTITYUNITCODE = BASEDRIVER.CODE` |
| `BASEDRIVER_QUANTITYUNIT` | [`FINVOULINESCRIT`](../FINANCE/FINVOULINESCRIT.md) | `FINVOULINFINVOUHDRCOMPANYCODE`, `QUANTITYUNITCODE` | `FINVOULINESCRIT.FINVOULINFINVOUHDRCOMPANYCODE = BASEDRIVER.COMPANYCODE AND FINVOULINESCRIT.QUANTITYUNITCODE = BASEDRIVER.CODE` |
| `BASEDRIVER_BASEDRIVER` | [`ASSETVALUATIONAREA`](../FINANCE/ASSETVALUATIONAREA.md) | `ASSETMASTERCOMPANYCODE`, `BASEDRIVERCODE` | `ASSETVALUATIONAREA.ASSETMASTERCOMPANYCODE = BASEDRIVER.COMPANYCODE AND ASSETVALUATIONAREA.BASEDRIVERCODE = BASEDRIVER.CODE` |
| `BASEDRIVER_BASEDRIVER` | [`FINALLOCATION`](../FINANCE/FINALLOCATION.md) | `COMPANYCODE`, `BASEDRIVERCODE` | `FINALLOCATION.COMPANYCODE = BASEDRIVER.COMPANYCODE AND FINALLOCATION.BASEDRIVERCODE = BASEDRIVER.CODE` |

## Indexes

- `BASEDRIVERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.BASETYPE,
       t.BASEGROUPSYSTEMTABLECODE,
       t.BASEGROUPCODE,
       t.BASEDIMENSION,
       t.UNITOFMAESURECODE
FROM   DB2ADMIN.BASEDRIVER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
