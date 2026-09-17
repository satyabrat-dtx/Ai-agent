# DB2ADMIN.APPROVALREQUESTDETAILRECIPE

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANY`, `CODE`, `VERSION`, `LINE`, `RECIPEITEMTYPECODE`, `RECIPESUBCODE01`, `RECIPESUBCODE02`, `RECIPESUBCODE03`, `RECIPESUBCODE04`, `RECIPESUBCODE05`, `RECIPESUBCODE06`, `RECIPESUBCODE07`, `RECIPESUBCODE08`, `RECIPESUBCODE09`, `RECIPESUBCODE10`, `RECIPESUFFIXCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 213635

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANY` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `VERSION` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `RECIPEITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `RECIPESUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `RECIPESUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `RECIPESUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `RECIPESUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `RECIPESUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `RECIPESUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `RECIPESUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `RECIPESUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `RECIPESUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `RECIPESUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `RECIPESUFFIXCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 16 | `CHECKDETAILRECIPE` | SMALLINT | NOT NULL |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPROVALREQUESTDETAIL_RECIPE` | `COMPANY`, `CODE`, `VERSION`, `LINE` | [`APPROVALREQUESTDETAIL`](../PLATFORM/APPROVALREQUESTDETAIL.md) | `APPROVALREQUESTCOMPANYCODE`, `APPROVALREQUESTREQUESTCODE`, `APPROVALREQUESTVERSION`, `LINENR` | RESTRICT | `APPROVALREQUESTDETAILRECIPE.COMPANY = APPROVALREQUESTDETAIL.APPROVALREQUESTCOMPANYCODE AND APPROVALREQUESTDETAILRECIPE.CODE = APPROVALREQUESTDETAIL.APPROVALREQUESTREQUESTCODE AND APPROVALREQUESTDETAILRECIPE.VERSION = APPROVALREQUESTDETAIL.APPROVALREQUESTVERSION AND APPROVALREQUESTDETAILRECIPE.LINE = APPROVALREQUESTDETAIL.LINENR` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPROVALREQUESTDLTRECIPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANY,
       t.CODE,
       t.VERSION,
       t.LINE,
       t.RECIPEITEMTYPECODE,
       t.RECIPESUBCODE01,
       t.RECIPESUBCODE02,
       t.RECIPESUBCODE03,
       t.RECIPESUBCODE04,
       t.RECIPESUBCODE05,
       t.RECIPESUBCODE06,
       t.RECIPESUBCODE07
FROM   DB2ADMIN.APPROVALREQUESTDETAILRECIPE t
FETCH FIRST 100 ROWS ONLY;
```
