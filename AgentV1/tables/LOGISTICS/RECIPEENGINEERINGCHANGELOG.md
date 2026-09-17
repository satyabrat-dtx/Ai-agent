# DB2ADMIN.RECIPEENGINEERINGCHANGELOG

- **Module**: `LOGISTICS` (low confidence — FK neighbourhood: 1 of 1 related tables are LOGISTICS)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `RECIPECOMPANYCODE`, `RECIPENUMBERID`, `ENGINEERINGCHANGENUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 13204

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RECIPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RECIPENUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ENGINEERINGCHANGENUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 4 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 6 | `RECIPEITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
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
| 18 | `RELEASEDATE` | DATE |  |  |  |  |
| 19 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 20 | `APPLICABLE` | SMALLINT | NOT NULL |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 26 | `RECIPEITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPEENGINEERINGCHANGELOG.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND RECIPEENGINEERINGCHANGELOG.COUNTERCODE = COUNTER.CODE` |
| `ENGINEERINGCHANGE_ENGINEERINGCHANGE` | `RECIPECOMPANYCODE`, `ENGINEERINGCHANGENUMBERID` | [`ENGINEERINGCHANGE`](../CORE_MASTER/ENGINEERINGCHANGE.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `RECIPEENGINEERINGCHANGELOG.RECIPECOMPANYCODE = ENGINEERINGCHANGE.COMPANYCODE AND RECIPEENGINEERINGCHANGELOG.ENGINEERINGCHANGENUMBERID = ENGINEERINGCHANGE.NUMBERID` |
| `ITEMTYPE_RECIPEITEMTYPE` | `RECIPEITEMTYPECOMPANYCODE`, `RECIPEITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPEENGINEERINGCHANGELOG.RECIPEITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND RECIPEENGINEERINGCHANGELOG.RECIPEITEMTYPECODE = ITEMTYPE.CODE` |
| `LOGREASON_LOGREASON` | `RECIPECOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPEENGINEERINGCHANGELOG.RECIPECOMPANYCODE = LOGREASON.COMPANYCODE AND RECIPEENGINEERINGCHANGELOG.LOGREASONCODE = LOGREASON.CODE` |
| `RECIPE_ENGINEERINGCHANGELOG` | `RECIPECOMPANYCODE`, `RECIPENUMBERID` | [`RECIPE`](../COSTING/RECIPE.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `RECIPEENGINEERINGCHANGELOG.RECIPECOMPANYCODE = RECIPE.COMPANYCODE AND RECIPEENGINEERINGCHANGELOG.RECIPENUMBERID = RECIPE.NUMBERID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECIPEENGINEERINGCHANGELOGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RECIPECOMPANYCODE,
       t.RECIPENUMBERID,
       t.ENGINEERINGCHANGENUMBERID,
       t.COUNTERCODE,
       t.CODE,
       t.LOGREASONCODE,
       t.RECIPEITEMTYPECODE,
       t.RECIPESUBCODE01,
       t.RECIPESUBCODE02,
       t.RECIPESUBCODE03,
       t.RECIPESUBCODE04,
       t.RECIPESUBCODE05
FROM   DB2ADMIN.RECIPEENGINEERINGCHANGELOG t
FETCH FIRST 100 ROWS ONLY;
```
