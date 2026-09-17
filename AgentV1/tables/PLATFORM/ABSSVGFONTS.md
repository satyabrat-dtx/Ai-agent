# DB2ADMIN.ABSSVGFONTS

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `CODE`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 82328

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | VARCHAR(250) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `FONT` | CLOB(2000000) | NOT NULL |  |  |  |
| 2 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 3 | `MODULENAME` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSSVGFONTS_SVGFONT` | [`ABSAVAILABLETILES`](../PLATFORM/ABSAVAILABLETILES.md) | `SVGFONT` | `ABSAVAILABLETILES.SVGFONT = ABSSVGFONTS.CODE` |
| `ABSSVGFONTS_TEMPLATESVGFONT` | [`ABSTILETEMPLATE`](../PLATFORM/ABSTILETEMPLATE.md) | `TEMPLATESVGFONTCODE` | `ABSTILETEMPLATE.TEMPLATESVGFONTCODE = ABSSVGFONTS.CODE` |

## Indexes

- `ABSSVGFONTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.FONT,
       t.ABSUNIQUEID,
       t.MODULENAME
FROM   DB2ADMIN.ABSSVGFONTS t
FETCH FIRST 100 ROWS ONLY;
```
