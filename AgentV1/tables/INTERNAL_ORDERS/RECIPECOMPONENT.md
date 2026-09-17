# DB2ADMIN.RECIPECOMPONENT

- **Module**: `INTERNAL_ORDERS` (low confidence — FK neighbourhood: 1 of 1 related tables are INTERNAL_ORDERS)
- **Roles**: `business_data`
- **Columns**: 64
- **Primary key**: `RECIPECOMPANYCODE`, `RECIPENUMBERID`, `GROUPNUMBER`, `SEQUENCE`, `ALTERNATIVE`, `SUBSEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 53581

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RECIPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RECIPENUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RECIPEITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 3 | `RECIPESUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 4 | `RECIPESUBCODE02` | CHAR(10) |  |  |  |  |
| 5 | `RECIPESUBCODE03` | CHAR(10) |  |  |  |  |
| 6 | `RECIPESUBCODE04` | CHAR(10) |  |  |  |  |
| 7 | `RECIPESUBCODE05` | CHAR(10) |  |  |  |  |
| 8 | `RECIPESUBCODE06` | CHAR(10) |  |  |  |  |
| 9 | `RECIPESUBCODE07` | CHAR(10) |  |  |  |  |
| 10 | `RECIPESUBCODE08` | CHAR(10) |  |  |  |  |
| 11 | `RECIPESUBCODE09` | CHAR(10) |  |  |  |  |
| 12 | `RECIPESUBCODE10` | CHAR(10) |  |  |  |  |
| 13 | `RECIPESUFFIXCODE` | CHAR(20) |  |  |  |  |
| 14 | `GROUPNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 15 | `GROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `LINETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 17 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 18 | `ALTERNATIVE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 19 | `SUBSEQUENCE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 20 | `COMPONENTINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 21 | `REFRECIPEGROUPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 22 | `REFRECIPESEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 23 | `REFRECIPEALTERNATIVE` | CHAR(3) |  |  |  |  |
| 24 | `REFRECIPESUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 25 | `REFRECIPESTATUS` | CHAR(2) |  |  |  |  |
| 26 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 27 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 28 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 38 | `COMMENTLINE` | CHAR(100) |  |  |  |  |
| 39 | `CONSUMPTIONTYPE` | CHAR(2) |  |  |  |  |
| 40 | `ASSEMBLYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 41 | `COMPONENTUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `COMPONENTUOMTYPE` | CHAR(2) |  |  |  |  |
| 43 | `CONSUMPTION` | DECIMAL(15,5) |  |  |  |  |
| 44 | `COMPOSITIONCOMPONENTCODE` | CHAR(10) |  | FK | foreign_key |  |
| 45 | `WATERMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 46 | `BINDERFILLERCOMPONENT` | CHAR(2) |  |  |  |  |
| 47 | `PRODUCED` | SMALLINT | NOT NULL |  |  |  |
| 48 | `PRICELISTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 49 | `COSTINGPLANTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 50 | `INITIALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 51 | `FINALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 52 | `INITIALDATE` | DATE |  |  |  |  |
| 53 | `FINALDATE` | DATE |  |  |  |  |
| 54 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 55 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 56 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 57 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 58 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 59 | `RECIPEITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 60 | `COMPOSITIONCMPCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 61 | `COSTINGPLANTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 62 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 63 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPOSITIONCOMPONENT_COMPOSITIONCOMPONENT` | `COMPOSITIONCMPCOMPANYCODE`, `COMPOSITIONCOMPONENTCODE` | [`COMPOSITIONCOMPONENT`](../INTERNAL_ORDERS/COMPOSITIONCOMPONENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPECOMPONENT.COMPOSITIONCMPCOMPANYCODE = COMPOSITIONCOMPONENT.COMPANYCODE AND RECIPECOMPONENT.COMPOSITIONCOMPONENTCODE = COMPOSITIONCOMPONENT.CODE` |
| `INTERNALPRICELIST_PRICELIST` | `RECIPECOMPANYCODE`, `PRICELISTCODE` | [`INTERNALPRICELIST`](../INTERNAL_ORDERS/INTERNALPRICELIST.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPECOMPONENT.RECIPECOMPANYCODE = INTERNALPRICELIST.COMPANYCODE AND RECIPECOMPONENT.PRICELISTCODE = INTERNALPRICELIST.CODE` |
| `ITEMTYPE_RECIPEITEMTYPE` | `RECIPEITEMTYPECOMPANYCODE`, `RECIPEITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPECOMPONENT.RECIPEITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND RECIPECOMPONENT.RECIPEITEMTYPECODE = ITEMTYPE.CODE` |
| `PLANT_COSTINGPLANT` | `COSTINGPLANTCOMPANYCODE`, `COSTINGPLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPECOMPONENT.COSTINGPLANTCOMPANYCODE = PLANT.COMPANYCODE AND RECIPECOMPONENT.COSTINGPLANTCODE = PLANT.CODE` |
| `RECIPEGROUP_GROUPTYPE` | `RECIPECOMPANYCODE`, `GROUPTYPECODE` | [`RECIPEGROUP`](../INTERNAL_ORDERS/RECIPEGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPECOMPONENT.RECIPECOMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECOMPONENT.GROUPTYPECODE = RECIPEGROUP.CODE` |
| `RECIPE_RECIPECOMPONENT` | `RECIPECOMPANYCODE`, `RECIPENUMBERID` | [`RECIPE`](../COSTING/RECIPE.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `RECIPECOMPONENT.RECIPECOMPANYCODE = RECIPE.COMPANYCODE AND RECIPECOMPONENT.RECIPENUMBERID = RECIPE.NUMBERID` |
| `UNITOFMEASURE_ASSEMBLYUOM` | `ASSEMBLYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `RECIPECOMPONENT.ASSEMBLYUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECIPECOMPONENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RECIPECOMPANYCODE,
       t.RECIPENUMBERID,
       t.RECIPEITEMTYPECODE,
       t.RECIPESUBCODE01,
       t.RECIPESUBCODE02,
       t.RECIPESUBCODE03,
       t.RECIPESUBCODE04,
       t.RECIPESUBCODE05,
       t.RECIPESUBCODE06,
       t.RECIPESUBCODE07,
       t.RECIPESUBCODE08,
       t.RECIPESUBCODE09
FROM   DB2ADMIN.RECIPECOMPONENT t
FETCH FIRST 100 ROWS ONLY;
```
