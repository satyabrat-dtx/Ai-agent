# DB2ADMIN.DESIGNSCREENSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 69
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 71993

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DESIGNITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `DESIGNSUBCODE01` | CHAR(20) |  |  |  |  |
| 4 | `DESIGNSUBCODE02` | CHAR(10) |  |  |  |  |
| 5 | `DESIGNSUBCODE03` | CHAR(10) |  |  |  |  |
| 6 | `DESIGNSUBCODE04` | CHAR(10) |  |  |  |  |
| 7 | `DESIGNSUBCODE05` | CHAR(10) |  |  |  |  |
| 8 | `DESIGNSUBCODE06` | CHAR(10) |  |  |  |  |
| 9 | `DESIGNSUBCODE07` | CHAR(10) |  |  |  |  |
| 10 | `DESIGNSUBCODE08` | CHAR(10) |  |  |  |  |
| 11 | `DESIGNSUBCODE09` | CHAR(10) |  |  |  |  |
| 12 | `DESIGNSUBCODE10` | CHAR(10) |  |  |  |  |
| 13 | `DESIGNSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 14 | `LINETYPE` | CHAR(2) |  |  |  |  |
| 15 | `SEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 16 | `SCREENDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 17 | `SCREENITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 18 | `SCREENSUBCODE01` | CHAR(20) |  |  |  |  |
| 19 | `SCREENSUBCODE02` | CHAR(10) |  |  |  |  |
| 20 | `SCREENSUBCODE03` | CHAR(10) |  |  |  |  |
| 21 | `SCREENSUBCODE04` | CHAR(10) |  |  |  |  |
| 22 | `SCREENSUBCODE05` | CHAR(10) |  |  |  |  |
| 23 | `SCREENSUBCODE06` | CHAR(10) |  |  |  |  |
| 24 | `SCREENSUBCODE07` | CHAR(10) |  |  |  |  |
| 25 | `SCREENSUBCODE08` | CHAR(10) |  |  |  |  |
| 26 | `SCREENSUBCODE09` | CHAR(10) |  |  |  |  |
| 27 | `SCREENSUBCODE10` | CHAR(10) |  |  |  |  |
| 28 | `RECIPEITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 29 | `RECIPENUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 30 | `RECIPESUBCODE01` | CHAR(20) |  |  |  |  |
| 31 | `RECIPESUBCODE02` | CHAR(10) |  |  |  |  |
| 32 | `SCREENITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 33 | `RECIPESUBCODE03` | CHAR(10) |  |  |  |  |
| 34 | `RECIPESUBCODE04` | CHAR(10) |  |  |  |  |
| 35 | `RECIPESUBCODE05` | CHAR(10) |  |  |  |  |
| 36 | `RECIPESUBCODE06` | CHAR(10) |  |  |  |  |
| 37 | `RECIPESUBCODE07` | CHAR(10) |  |  |  |  |
| 38 | `RECIPESUBCODE08` | CHAR(10) |  |  |  |  |
| 39 | `RECIPESUBCODE09` | CHAR(10) |  |  |  |  |
| 40 | `RECIPESUBCODE10` | CHAR(10) |  |  |  |  |
| 41 | `RECIPESUFFIXCODE` | CHAR(20) |  |  |  |  |
| 42 | `RECIPEDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 43 | `RECIPEITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 44 | `COLORANTRATIO` | INTEGER | NOT NULL |  |  |  |
| 45 | `RATIO` | CHAR(5) |  |  |  |  |
| 46 | `BINDERFILLERRATIO` | INTEGER | NOT NULL |  |  |  |
| 47 | `TOTALCONSUMPTIONFORDISPLAY` | CHAR(16) |  |  |  |  |
| 48 | `PASTECONSUMPTION` | DECIMAL(15,5) |  |  |  |  |
| 49 | `PASTEUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `WASTEPERBATCH` | DECIMAL(5,2) |  |  |  |  |
| 51 | `WASTEFORRETURN` | DECIMAL(5,2) |  |  |  |  |
| 52 | `TOTALCOSTFORDISPLAY` | CHAR(16) |  |  |  |  |
| 53 | `INITIALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 54 | `FINALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 55 | `COMPONENTUOMTYPE` | CHAR(2) |  |  |  |  |
| 56 | `TOTALCOST` | DECIMAL(18,5) |  |  |  |  |
| 57 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 58 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 59 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 60 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 61 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 62 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 63 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 64 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 65 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 66 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 67 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 68 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `DESIGNSCREENSBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `DESIGNSCREENSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.DESIGNITEMTYPECODE,
       t.DESIGNSUBCODE01,
       t.DESIGNSUBCODE02,
       t.DESIGNSUBCODE03,
       t.DESIGNSUBCODE04,
       t.DESIGNSUBCODE05,
       t.DESIGNSUBCODE06,
       t.DESIGNSUBCODE07,
       t.DESIGNSUBCODE08,
       t.DESIGNSUBCODE09
FROM   DB2ADMIN.DESIGNSCREENSBEAN t
FETCH FIRST 100 ROWS ONLY;
```
