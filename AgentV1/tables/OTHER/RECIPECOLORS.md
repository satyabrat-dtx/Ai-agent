# DB2ADMIN.RECIPECOLORS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `COLOR`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 383

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COLOR` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 1 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 2 | `SVGCOLOR` | CHAR(30) |  |  |  |  |
| 3 | `PREVIEW` | CHAR(30) |  |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RECIPECOLORS_EXPLOSIONLINECOLOR` | [`RECIPETEMPLATE`](../OTHER/RECIPETEMPLATE.md) | `EXPLOSIONLINECOLORCOLOR` | `RECIPETEMPLATE.EXPLOSIONLINECOLORCOLOR = RECIPECOLORS.COLOR` |
| `RECIPECOLORS_TOTALLINECOLOR` | [`RECIPETEMPLATE`](../OTHER/RECIPETEMPLATE.md) | `TOTALLINECOLORCOLOR` | `RECIPETEMPLATE.TOTALLINECOLORCOLOR = RECIPECOLORS.COLOR` |

## Indexes

- `RECIPECOLORSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COLOR,
       t.DESCRIPTION,
       t.SVGCOLOR,
       t.PREVIEW,
       t.ABSUNIQUEID
FROM   DB2ADMIN.RECIPECOLORS t
FETCH FIRST 100 ROWS ONLY;
```
