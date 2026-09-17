# DB2ADMIN.RECIPETEMPLATE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 92
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 8 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 18677

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `RECIPETYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `CALCULATEDCONSUMPTIONTYPE` | CHAR(2) |  |  |  |  |
| 7 | `REFERENCERECIPEREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `COMPONENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `SOLUTIONPASTEUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `SOLUTIONPASTEWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 11 | `SOLUTIONPASTEWEIGHTUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `WATERMANAGEMENTFORCOMPONENT` | SMALLINT | NOT NULL |  |  |  |
| 13 | `WATERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 14 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 15 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `REFERENCETYPEREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 25 | `CHECKCODE` | CHAR(2) |  | FK | foreign_key |  |
| 26 | `USERGENERICGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `GROUPSTRUCTUREHANDLED` | CHAR(2) |  |  |  |  |
| 28 | `CHECKGROUPCODE` | CHAR(3) |  | FK | foreign_key |  |
| 29 | `REACTIVEDYEING` | CHAR(2) |  |  |  |  |
| 30 | `DYESTUFFCHEMICALRATIO` | DECIMAL(5,2) |  |  |  |  |
| 31 | `ALKALIRATIO` | DECIMAL(5,2) |  |  |  |  |
| 32 | `HANDLEPRODUCTIONUM` | CHAR(2) |  |  |  |  |
| 33 | `BATCHSTANDARDSIZE` | CHAR(2) | NOT NULL |  |  |  |
| 34 | `HANDLEAVERAGELENGTH` | CHAR(2) |  |  |  |  |
| 35 | `PRODUCTIONUMWEIGHT` | CHAR(2) | NOT NULL |  |  |  |
| 36 | `PICKUPPERCENTAGE` | CHAR(2) |  |  |  |  |
| 37 | `DRYRESIDUALPERCENTAGE` | CHAR(2) |  |  |  |  |
| 38 | `DRYRESIDUALQUANTITY` | CHAR(2) |  |  |  |  |
| 39 | `GLOBALWASTEPERCENTAGE` | CHAR(2) |  |  |  |  |
| 40 | `RESIDUALBATHVOLUME` | CHAR(2) |  |  |  |  |
| 41 | `BATHVOLUME` | CHAR(2) |  |  |  |  |
| 42 | `LIQUORRATIO` | CHAR(2) |  |  |  |  |
| 43 | `DILUITIONPERCENTAGE` | CHAR(2) |  |  |  |  |
| 44 | `COMPONENTCONSUMPTIONRULL` | CHAR(2) | NOT NULL |  |  |  |
| 45 | `COMPONENTCONSUMPTIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 46 | `QUANTITYFORSTEPWEIGHT` | CHAR(2) | NOT NULL |  |  |  |
| 47 | `QUANTITYFORSTEPLENGTH` | CHAR(2) | NOT NULL |  |  |  |
| 48 | `CALCULATIONFORMULACODE` | CHAR(20) |  |  |  |  |
| 49 | `MIXVOLUME` | CHAR(2) |  |  |  |  |
| 50 | `CONSUMPTIONTITLE` | CHAR(20) |  |  |  |  |
| 51 | `CONSUMPTIONTYPETITLE` | CHAR(15) |  |  |  |  |
| 52 | `WATERLINECOLORCOLOR` | CHAR(30) |  |  |  |  |
| 53 | `EXPLOSIONLINECOLORCOLOR` | CHAR(30) |  | FK | foreign_key |  |
| 54 | `HANDLETOTALLINE` | CHAR(2) |  |  |  |  |
| 55 | `TOTALLINEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 56 | `TOTALLINECOLORCOLOR` | CHAR(30) |  | FK | foreign_key |  |
| 57 | `TOTALLINEUMCODE` | CHAR(3) |  |  |  |  |
| 58 | `HANDLEBINDERINHEADER` | CHAR(2) |  |  |  |  |
| 59 | `BINDERMINPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 60 | `BINDERFLUIDSRATIO` | DECIMAL(5,2) |  |  |  |  |
| 61 | `BINDERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 62 | `BSUBCODE01` | CHAR(20) |  |  |  |  |
| 63 | `BSUBCODE02` | CHAR(10) |  |  |  |  |
| 64 | `BSUBCODE03` | CHAR(10) |  |  |  |  |
| 65 | `BSUBCODE04` | CHAR(10) |  |  |  |  |
| 66 | `BSUBCODE05` | CHAR(10) |  |  |  |  |
| 67 | `BSUBCODE06` | CHAR(10) |  |  |  |  |
| 68 | `BSUBCODE07` | CHAR(10) |  |  |  |  |
| 69 | `BSUBCODE08` | CHAR(10) |  |  |  |  |
| 70 | `BSUBCODE09` | CHAR(10) |  |  |  |  |
| 71 | `BSUBCODE10` | CHAR(10) |  |  |  |  |
| 72 | `HANDLEFILLERINHEADER` | CHAR(2) |  |  |  |  |
| 73 | `FILLERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 74 | `FSUBCODE01` | CHAR(20) |  |  |  |  |
| 75 | `FSUBCODE02` | CHAR(10) |  |  |  |  |
| 76 | `FSUBCODE03` | CHAR(10) |  |  |  |  |
| 77 | `FSUBCODE04` | CHAR(10) |  |  |  |  |
| 78 | `FSUBCODE05` | CHAR(10) |  |  |  |  |
| 79 | `FSUBCODE06` | CHAR(10) |  |  |  |  |
| 80 | `FSUBCODE07` | CHAR(10) |  |  |  |  |
| 81 | `FSUBCODE08` | CHAR(10) |  |  |  |  |
| 82 | `FSUBCODE09` | CHAR(10) |  |  |  |  |
| 83 | `FSUBCODE10` | CHAR(10) |  |  |  |  |
| 84 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 85 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 86 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 87 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 88 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 89 | `USERGENGROUPTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 90 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 91 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 8

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECIPETEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `RECIPECHECKGROUP_CHECKGROUP` | `COMPANYCODE`, `CHECKGROUPCODE` | [`RECIPECHECKGROUP`](../INTERNAL_ORDERS/RECIPECHECKGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPETEMPLATE.COMPANYCODE = RECIPECHECKGROUP.COMPANYCODE AND RECIPETEMPLATE.CHECKGROUPCODE = RECIPECHECKGROUP.CODE` |
| `RECIPECOLORS_EXPLOSIONLINECOLOR` | `EXPLOSIONLINECOLORCOLOR` | [`RECIPECOLORS`](../OTHER/RECIPECOLORS.md) | `COLOR` | RESTRICT | `RECIPETEMPLATE.EXPLOSIONLINECOLORCOLOR = RECIPECOLORS.COLOR` |
| `RECIPECOLORS_TOTALLINECOLOR` | `TOTALLINECOLORCOLOR` | [`RECIPECOLORS`](../OTHER/RECIPECOLORS.md) | `COLOR` | RESTRICT | `RECIPETEMPLATE.TOTALLINECOLORCOLOR = RECIPECOLORS.COLOR` |
| `REFERENCECHECKTYPE_CHECK` | `CHECKCODE` | [`REFERENCECHECKTYPE`](../PRODUCTION/REFERENCECHECKTYPE.md) | `CODE` | RESTRICT | `RECIPETEMPLATE.CHECKCODE = REFERENCECHECKTYPE.CODE` |
| `UNITOFMEASURE_SOLUTIONPASTEUM` | `SOLUTIONPASTEUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `RECIPETEMPLATE.SOLUTIONPASTEUMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_SOLUTIONPASTEWEIGHTUM` | `SOLUTIONPASTEWEIGHTUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `RECIPETEMPLATE.SOLUTIONPASTEWEIGHTUMCODE = UNITOFMEASURE.CODE` |
| `USERGENERICGROUPTYPE_USERGENERICGROUPTYPE` | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE` | [`USERGENERICGROUPTYPE`](../CORE_MASTER/USERGENERICGROUPTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPETEMPLATE.USERGENGROUPTYPECOMPANYCODE = USERGENERICGROUPTYPE.COMPANYCODE AND RECIPETEMPLATE.USERGENERICGROUPTYPECODE = USERGENERICGROUPTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RECIPETEMPLATE_RECIPETEMPLATE` | [`RECIPE`](../COSTING/RECIPE.md) | `COMPANYCODE`, `RECIPETEMPLATECODE` | `RECIPE.COMPANYCODE = RECIPETEMPLATE.COMPANYCODE AND RECIPE.RECIPETEMPLATECODE = RECIPETEMPLATE.CODE` |

## Indexes

- `RECIPETEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.RECIPETYPE,
       t.CALCULATEDCONSUMPTIONTYPE,
       t.REFERENCERECIPEREQUIRED,
       t.COMPONENTTYPE,
       t.SOLUTIONPASTEUMCODE,
       t.SOLUTIONPASTEWEIGHT,
       t.SOLUTIONPASTEWEIGHTUMCODE
FROM   DB2ADMIN.RECIPETEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
