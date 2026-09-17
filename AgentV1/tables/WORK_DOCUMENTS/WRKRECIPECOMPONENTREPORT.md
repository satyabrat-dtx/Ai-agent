# DB2ADMIN.WRKRECIPECOMPONENTREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 53
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 92943

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `RECIPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `FATHERNUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 5 | `RECIPENUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 6 | `RECIPEITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `RECIPESUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 8 | `RECIPESUBCODE02` | CHAR(10) |  |  |  |  |
| 9 | `RECIPESUBCODE03` | CHAR(10) |  |  |  |  |
| 10 | `RECIPESUBCODE04` | CHAR(10) |  |  |  |  |
| 11 | `RECIPESUBCODE05` | CHAR(10) |  |  |  |  |
| 12 | `RECIPESUBCODE06` | CHAR(10) |  |  |  |  |
| 13 | `RECIPESUBCODE07` | CHAR(10) |  |  |  |  |
| 14 | `RECIPESUBCODE08` | CHAR(10) |  |  |  |  |
| 15 | `RECIPESUBCODE09` | CHAR(10) |  |  |  |  |
| 16 | `RECIPESUBCODE10` | CHAR(10) |  |  |  |  |
| 17 | `RECIPESUFFIXCODE` | CHAR(20) |  |  |  |  |
| 18 | `GROUPNUMBER` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 19 | `GROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `LINETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 21 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 22 | `ALTERNATIVE` | CHAR(3) | NOT NULL |  |  |  |
| 23 | `SUBSEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 24 | `COMPONENTINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 25 | `REFRECIPEGROUPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 26 | `REFRECIPESEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 27 | `REFRECIPEALTERNATIVE` | CHAR(3) |  |  |  |  |
| 28 | `REFRECIPESUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 29 | `REFRECIPESTATUS` | CHAR(2) |  |  |  |  |
| 30 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 31 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 32 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 41 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 42 | `COMMENTLINE` | CHAR(100) |  |  |  |  |
| 43 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 44 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 45 | `CONSUMPTIONTYPE` | CHAR(2) |  |  |  |  |
| 46 | `ASSEMBLYUOMCODE` | CHAR(3) |  |  |  |  |
| 47 | `COMPONENTUOMCODE` | CHAR(3) |  |  |  |  |
| 48 | `COMPONENTUOMTYPE` | CHAR(2) |  |  |  |  |
| 49 | `CONSUMPTION` | DECIMAL(15,5) |  |  |  |  |
| 50 | `TOTALCONSUMPTION` | DECIMAL(15,5) |  |  |  |  |
| 51 | `INITIALDATE` | DATE |  |  |  |  |
| 52 | `FINALDATE` | DATE |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.RECIPECOMPANYCODE,
       t.FATHERNUMBERID,
       t.RECIPENUMBERID,
       t.RECIPEITEMTYPECODE,
       t.RECIPESUBCODE01,
       t.RECIPESUBCODE02,
       t.RECIPESUBCODE03,
       t.RECIPESUBCODE04,
       t.RECIPESUBCODE05
FROM   DB2ADMIN.WRKRECIPECOMPONENTREPORT t
FETCH FIRST 100 ROWS ONLY;
```
