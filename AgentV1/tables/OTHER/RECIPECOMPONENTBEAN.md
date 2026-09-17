# DB2ADMIN.RECIPECOMPONENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 76
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 67555

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `OWNEDCOMPONENT` | CHAR(2) |  |  |  |  |
| 3 | `RECIPEITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `RECIPESUBCODE01` | CHAR(20) |  |  |  |  |
| 5 | `RECIPESUBCODE02` | CHAR(10) |  |  |  |  |
| 6 | `RECIPESUBCODE03` | CHAR(10) |  |  |  |  |
| 7 | `RECIPESUBCODE04` | CHAR(10) |  |  |  |  |
| 8 | `RECIPESUBCODE05` | CHAR(10) |  |  |  |  |
| 9 | `RECIPESUBCODE06` | CHAR(10) |  |  |  |  |
| 10 | `RECIPESUBCODE07` | CHAR(10) |  |  |  |  |
| 11 | `RECIPESUBCODE08` | CHAR(10) |  |  |  |  |
| 12 | `RECIPESUBCODE09` | CHAR(10) |  |  |  |  |
| 13 | `RECIPESUBCODE10` | CHAR(10) |  |  |  |  |
| 14 | `RECIPESUFFIXCODE` | CHAR(20) |  |  |  |  |
| 15 | `GROUPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 16 | `GROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `LINETYPE` | CHAR(2) |  |  |  |  |
| 18 | `SEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 19 | `ALTERNATIVE` | CHAR(3) |  |  |  |  |
| 20 | `SUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 21 | `COMPONENTINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 22 | `REFRECIPEGROUPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 23 | `REFRECIPESEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 24 | `REFRECIPEALTERNATIVE` | CHAR(3) |  |  |  |  |
| 25 | `REFRECIPESUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 26 | `REFRECIPESTATUS` | CHAR(2) |  |  |  |  |
| 27 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 28 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 29 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 39 | `COMMENTLINE` | CHAR(100) |  |  |  |  |
| 40 | `CONSUMPTIONTYPE` | CHAR(2) |  |  |  |  |
| 41 | `ASSEMBLYUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `COMPONENTUOMCODE` | CHAR(3) |  |  |  |  |
| 43 | `COMPONENTUOMTYPE` | CHAR(2) |  |  |  |  |
| 44 | `CONSUMPTION` | DECIMAL(15,5) |  |  |  |  |
| 45 | `COMPOSITIONCOMPONENTCODE` | CHAR(10) |  |  |  |  |
| 46 | `WATERMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 47 | `BINDERFILLERCOMPONENT` | CHAR(2) |  |  |  |  |
| 48 | `PRODUCED` | SMALLINT | NOT NULL |  |  |  |
| 49 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 50 | `COSTINGPLANTCODE` | CHAR(8) |  |  |  |  |
| 51 | `INITIALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 52 | `FINALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 53 | `INITIALDATE` | DATE |  |  |  |  |
| 54 | `FINALDATE` | DATE |  |  |  |  |
| 55 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 56 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 57 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 58 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 59 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 60 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 61 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 62 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 63 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 64 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 65 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 66 | `ALLOWDELETEBINDERFILLER` | SMALLINT | NOT NULL |  |  |  |
| 67 | `CONSPERLABEL` | CHAR(16) |  |  |  |  |
| 68 | `CONSFORMIXLABEL` | CHAR(16) |  |  |  |  |
| 69 | `CONSPERBATCHLABEL` | CHAR(16) |  |  |  |  |
| 70 | `TOTALCOSTTEXT` | CHAR(20) |  |  |  |  |
| 71 | `UNITARYBATCHSTANDARDSIZE` | DECIMAL(15,5) |  |  |  |  |
| 72 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 73 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 74 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 75 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **RECIPE**.`ABSUNIQUEID` (medium confidence — name = 'RECIPE' + recurring fragment 'COMPONENT' (seen in 11 tables))
  - JOIN predicate: `RECIPECOMPONENTBEAN.FATHERID = RECIPE.ABSUNIQUEID`

## Indexes

- `RECIPECOMPONENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.OWNEDCOMPONENT,
       t.RECIPEITEMTYPECODE,
       t.RECIPESUBCODE01,
       t.RECIPESUBCODE02,
       t.RECIPESUBCODE03,
       t.RECIPESUBCODE04,
       t.RECIPESUBCODE05,
       t.RECIPESUBCODE06,
       t.RECIPESUBCODE07,
       t.RECIPESUBCODE08
FROM   DB2ADMIN.RECIPECOMPONENTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
