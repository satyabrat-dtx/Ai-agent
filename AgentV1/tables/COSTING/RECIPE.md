# DB2ADMIN.RECIPE

- **Module**: `COSTING` (low confidence — FK neighbourhood: 1 of 1 related tables are COSTING)
- **Roles**: `business_data`
- **Columns**: 108
- **Primary key**: `COMPANYCODE`, `NUMBERID`
- **FK degree**: referenced by 2 constraint(s), references 9 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 53421

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 4 | `RECIPETEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `RECIPETYPE` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 18 | `GENERICRECIPE` | SMALLINT | NOT NULL |  |  |  |
| 19 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 20 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 21 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 22 | `REFSUBCODE01` | CHAR(20) |  |  |  |  |
| 23 | `REFSUBCODE02` | CHAR(10) |  |  |  |  |
| 24 | `REFSUBCODE03` | CHAR(10) |  |  |  |  |
| 25 | `REFSUBCODE04` | CHAR(10) |  |  |  |  |
| 26 | `REFSUBCODE05` | CHAR(10) |  |  |  |  |
| 27 | `REFSUBCODE06` | CHAR(10) |  |  |  |  |
| 28 | `REFSUBCODE07` | CHAR(10) |  |  |  |  |
| 29 | `REFSUBCODE08` | CHAR(10) |  |  |  |  |
| 30 | `REFSUBCODE09` | CHAR(10) |  |  |  |  |
| 31 | `REFSUBCODE10` | CHAR(10) |  |  |  |  |
| 32 | `REFRECIPESUFFIXCODE` | CHAR(20) |  |  |  |  |
| 33 | `REFRECIPENUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 34 | `GENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 35 | `VALIDFROMDATE` | DATE |  |  |  |  |
| 36 | `VALIDTODATE` | DATE |  |  |  |  |
| 37 | `MAXNUMBEROFUSES` | INTEGER | NOT NULL |  |  |  |
| 38 | `NUMBEROFUSES` | INTEGER | NOT NULL |  |  |  |
| 39 | `SOLUTIONPASTEUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 40 | `SOLUTIONPASTEWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 41 | `RECIPEINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 42 | `SOLUTIONPASTEUMWEIGHTUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 43 | `PRODUCTIONUMCODE` | CHAR(3) |  |  |  |  |
| 44 | `PRODUCTIONUMWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 45 | `PRODUCTIONUMWEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 46 | `BATCHSTANDARDSIZE` | DECIMAL(15,5) |  |  |  |  |
| 47 | `AVERAGELENGTH` | DECIMAL(15,5) |  |  |  |  |
| 48 | `BATCHAVERAGEUMCODE` | CHAR(3) |  |  |  |  |
| 49 | `DILUITIONPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 50 | `PICKUPPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 51 | `DRYRESIDUALPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 52 | `DRYRESIDUALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `GLOBALWASTEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 54 | `BATHVOLUME` | DECIMAL(15,5) |  |  |  |  |
| 55 | `RESIDUALBATHVOLUME` | DECIMAL(15,5) |  |  |  |  |
| 56 | `VOLUMEUMCODE` | CHAR(3) |  |  |  |  |
| 57 | `COMPOSITIONCODE` | CHAR(10) |  | FK | foreign_key |  |
| 58 | `LIQUORRATIO` | DECIMAL(5,2) |  |  |  |  |
| 59 | `MIXVOLUME` | DECIMAL(15,5) |  |  |  |  |
| 60 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 61 | `BINDERFLUIDSRATIO` | DECIMAL(5,2) |  |  |  |  |
| 62 | `BINDERMINPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 63 | `BINDERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 64 | `BSUBCODE01` | CHAR(20) |  |  |  |  |
| 65 | `BSUBCODE02` | CHAR(10) |  |  |  |  |
| 66 | `BSUBCODE03` | CHAR(10) |  |  |  |  |
| 67 | `BSUBCODE04` | CHAR(10) |  |  |  |  |
| 68 | `BSUBCODE05` | CHAR(10) |  |  |  |  |
| 69 | `BSUBCODE06` | CHAR(10) |  |  |  |  |
| 70 | `BSUBCODE07` | CHAR(10) |  |  |  |  |
| 71 | `BSUBCODE08` | CHAR(10) |  |  |  |  |
| 72 | `BSUBCODE09` | CHAR(10) |  |  |  |  |
| 73 | `BSUBCODE10` | CHAR(10) |  |  |  |  |
| 74 | `FILLERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 75 | `FSUBCODE01` | CHAR(20) |  |  |  |  |
| 76 | `FSUBCODE02` | CHAR(10) |  |  |  |  |
| 77 | `FSUBCODE03` | CHAR(10) |  |  |  |  |
| 78 | `FSUBCODE04` | CHAR(10) |  |  |  |  |
| 79 | `FSUBCODE05` | CHAR(10) |  |  |  |  |
| 80 | `FSUBCODE06` | CHAR(10) |  |  |  |  |
| 81 | `FSUBCODE07` | CHAR(10) |  |  |  |  |
| 82 | `FSUBCODE08` | CHAR(10) |  |  |  |  |
| 83 | `FSUBCODE09` | CHAR(10) |  |  |  |  |
| 84 | `FSUBCODE10` | CHAR(10) |  |  |  |  |
| 85 | `BINDERGROUPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 86 | `BINDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 87 | `FILLERGROUPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 88 | `FILLERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 89 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 90 | `APPROVALDATE` | DATE |  |  |  |  |
| 91 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 92 | `RELEASEDATE` | DATE |  |  |  |  |
| 93 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 94 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 95 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 96 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 97 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 98 | `CREATEHEADER` | CHAR(1) |  |  |  |  |
| 99 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 100 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 101 | `COMPOSITIONCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 102 | `LIMITINPOBYNUMBEROFUSES` | SMALLINT | NOT NULL |  |  |  |
| 103 | `COSTGROUPCODE` | CHAR(3) |  | FK | foreign_key |  |
| 104 | `USESUBRECIPEHEADERVALUES` | SMALLINT | NOT NULL |  |  |  |
| 105 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 106 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 107 | `ARTICLESTATUSCODE` | CHAR(8) |  | FK | foreign_key |  |

## References (this table → parent) — 9

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ARTICLESTATUS_ARTICLESTATUS` | `COMPANYCODE`, `ITEMTYPECODE`, `ARTICLESTATUSCODE` | [`ARTICLESTATUS`](../OTHER/ARTICLESTATUS.md) | `COMPANYCODE`, `ITEMTYPECODE`, `CODE` | RESTRICT | `RECIPE.COMPANYCODE = ARTICLESTATUS.COMPANYCODE AND RECIPE.ITEMTYPECODE = ARTICLESTATUS.ITEMTYPECODE AND RECIPE.ARTICLESTATUSCODE = ARTICLESTATUS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECIPE.COMPANYCODE = COMPANY.CODE` |
| `COMPOSITION_COMPOSITION` | `COMPOSITIONCOMPANYCODE`, `COMPOSITIONCODE` | [`COMPOSITION`](../ITEM_MASTER/COMPOSITION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPE.COMPOSITIONCOMPANYCODE = COMPOSITION.COMPANYCODE AND RECIPE.COMPOSITIONCODE = COMPOSITION.CODE` |
| `COSTGROUP_COSTGROUP` | `COMPANYCODE`, `COSTGROUPCODE` | [`COSTGROUP`](../COSTING/COSTGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPE.COMPANYCODE = COSTGROUP.COMPANYCODE AND RECIPE.COSTGROUPCODE = COSTGROUP.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPE.COMPANYCODE = DIVISION.COMPANYCODE AND RECIPE.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND RECIPE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `RECIPETEMPLATE_RECIPETEMPLATE` | `COMPANYCODE`, `RECIPETEMPLATECODE` | [`RECIPETEMPLATE`](../OTHER/RECIPETEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPE.COMPANYCODE = RECIPETEMPLATE.COMPANYCODE AND RECIPE.RECIPETEMPLATECODE = RECIPETEMPLATE.CODE` |
| `UNITOFMEASURE_SOLUTIONPASTEUM` | `SOLUTIONPASTEUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `RECIPE.SOLUTIONPASTEUMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_SOLUTIONPASTEUMWEIGHTUM` | `SOLUTIONPASTEUMWEIGHTUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `RECIPE.SOLUTIONPASTEUMWEIGHTUMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RECIPE_ENGINEERINGCHANGELOG` | [`RECIPEENGINEERINGCHANGELOG`](../LOGISTICS/RECIPEENGINEERINGCHANGELOG.md) | `RECIPECOMPANYCODE`, `RECIPENUMBERID` | `RECIPEENGINEERINGCHANGELOG.RECIPECOMPANYCODE = RECIPE.COMPANYCODE AND RECIPEENGINEERINGCHANGELOG.RECIPENUMBERID = RECIPE.NUMBERID` |
| `RECIPE_RECIPECOMPONENT` | [`RECIPECOMPONENT`](../INTERNAL_ORDERS/RECIPECOMPONENT.md) | `RECIPECOMPANYCODE`, `RECIPENUMBERID` | `RECIPECOMPONENT.RECIPECOMPANYCODE = RECIPE.COMPANYCODE AND RECIPECOMPONENT.RECIPENUMBERID = RECIPE.NUMBERID` |

## Implicit links (NOT declared in the DDL — inferred)

- child `RECIPECOMPONENTBEAN`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)

## Indexes

- `RECIPE1` (COMPANYCODE, ITEMTYPECODE, SUBCODE01, SUBCODE02, SUBCODE03, SUBCODE04, SUBCODE05, SUBCODE06, SUBCODE07, SUBCODE08, SUBCODE09, SUBCODE10, SUFFIXCODE)
- `RECIPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.NUMBERID,
       t.RECIPETEMPLATECODE,
       t.ITEMTYPECODE,
       t.RECIPETYPE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.RECIPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
