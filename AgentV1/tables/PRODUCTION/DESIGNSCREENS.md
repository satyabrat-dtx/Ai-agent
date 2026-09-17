# DB2ADMIN.DESIGNSCREENS

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 61
- **Primary key**: `DESIGNCMPDESIGNCOMPANYCODE`, `DESIGNCOMPONENTDESIGNNUMBERID`, `DESIGNCOMPONENTVARIANTCODE`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 17288

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DESIGNCMPDESIGNCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DESIGNCOMPONENTDESIGNNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DESIGNCOMPONENTVARIANTCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DESIGNITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `DESIGNSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 5 | `DESIGNSUBCODE02` | CHAR(10) |  |  |  |  |
| 6 | `DESIGNSUBCODE03` | CHAR(10) |  |  |  |  |
| 7 | `DESIGNSUBCODE04` | CHAR(10) |  |  |  |  |
| 8 | `DESIGNSUBCODE05` | CHAR(10) |  |  |  |  |
| 9 | `DESIGNSUBCODE06` | CHAR(10) |  |  |  |  |
| 10 | `DESIGNSUBCODE07` | CHAR(10) |  |  |  |  |
| 11 | `DESIGNSUBCODE08` | CHAR(10) |  |  |  |  |
| 12 | `DESIGNSUBCODE09` | CHAR(10) |  |  |  |  |
| 13 | `DESIGNSUBCODE10` | CHAR(10) |  |  |  |  |
| 14 | `DESIGNSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 15 | `LINETYPE` | CHAR(2) |  |  |  |  |
| 16 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 17 | `SCREENDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 18 | `SCREENITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 19 | `SCREENSUBCODE01` | CHAR(20) |  |  |  |  |
| 20 | `SCREENSUBCODE02` | CHAR(10) |  |  |  |  |
| 21 | `SCREENSUBCODE03` | CHAR(10) |  |  |  |  |
| 22 | `SCREENSUBCODE04` | CHAR(10) |  |  |  |  |
| 23 | `SCREENSUBCODE05` | CHAR(10) |  |  |  |  |
| 24 | `SCREENSUBCODE06` | CHAR(10) |  |  |  |  |
| 25 | `SCREENSUBCODE07` | CHAR(10) |  |  |  |  |
| 26 | `SCREENSUBCODE08` | CHAR(10) |  |  |  |  |
| 27 | `SCREENSUBCODE09` | CHAR(10) |  |  |  |  |
| 28 | `SCREENSUBCODE10` | CHAR(10) |  |  |  |  |
| 29 | `RECIPEITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 30 | `RECIPENUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 31 | `RECIPESUBCODE01` | CHAR(20) |  |  |  |  |
| 32 | `RECIPESUBCODE02` | CHAR(10) |  |  |  |  |
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
| 43 | `COLORANTRATIO` | INTEGER | NOT NULL |  |  |  |
| 44 | `BINDERFILLERRATIO` | INTEGER | NOT NULL |  |  |  |
| 45 | `PASTECONSUMPTION` | DECIMAL(15,5) |  |  |  |  |
| 46 | `PASTEUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 47 | `WASTEPERBATCH` | DECIMAL(5,2) |  |  |  |  |
| 48 | `WASTEFORRETURN` | DECIMAL(5,2) |  |  |  |  |
| 49 | `INITIALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 50 | `FINALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 51 | `COMPONENTUOMTYPE` | CHAR(2) |  |  |  |  |
| 52 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 53 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 54 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 55 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 56 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 57 | `DESIGNITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 58 | `RECIPEITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 59 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 60 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DESIGNCOMPONENT_DESIGNSCREENS` | `DESIGNCMPDESIGNCOMPANYCODE`, `DESIGNCOMPONENTDESIGNNUMBERID`, `DESIGNCOMPONENTVARIANTCODE` | [`DESIGNCOMPONENT`](../PRODUCTION/DESIGNCOMPONENT.md) | `DESIGNCOMPANYCODE`, `DESIGNNUMBERID`, `VARIANTCODE` | RESTRICT | `DESIGNSCREENS.DESIGNCMPDESIGNCOMPANYCODE = DESIGNCOMPONENT.DESIGNCOMPANYCODE AND DESIGNSCREENS.DESIGNCOMPONENTDESIGNNUMBERID = DESIGNCOMPONENT.DESIGNNUMBERID AND DESIGNSCREENS.DESIGNCOMPONENTVARIANTCODE = DESIGNCOMPONENT.VARIANTCODE` |
| `ITEMTYPE_DESIGNITEMTYPE` | `DESIGNITEMTYPECOMPANYCODE`, `DESIGNITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESIGNSCREENS.DESIGNITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND DESIGNSCREENS.DESIGNITEMTYPECODE = ITEMTYPE.CODE` |
| `ITEMTYPE_RECIPEITEMTYPE` | `RECIPEITEMTYPECOMPANYCODE`, `RECIPEITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESIGNSCREENS.RECIPEITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND DESIGNSCREENS.RECIPEITEMTYPECODE = ITEMTYPE.CODE` |
| `UNITOFMEASURE_PASTEUOM` | `PASTEUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `DESIGNSCREENS.PASTEUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DESIGNSCREENSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DESIGNCMPDESIGNCOMPANYCODE,
       t.DESIGNCOMPONENTDESIGNNUMBERID,
       t.DESIGNCOMPONENTVARIANTCODE,
       t.DESIGNITEMTYPECODE,
       t.DESIGNSUBCODE01,
       t.DESIGNSUBCODE02,
       t.DESIGNSUBCODE03,
       t.DESIGNSUBCODE04,
       t.DESIGNSUBCODE05,
       t.DESIGNSUBCODE06,
       t.DESIGNSUBCODE07,
       t.DESIGNSUBCODE08
FROM   DB2ADMIN.DESIGNSCREENS t
FETCH FIRST 100 ROWS ONLY;
```
