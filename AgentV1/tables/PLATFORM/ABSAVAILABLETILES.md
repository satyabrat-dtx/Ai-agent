# DB2ADMIN.ABSAVAILABLETILES

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `CODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 82134

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | BIGINT | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `DESCRIPTION` | CHAR(50) | NOT NULL |  | description |  |
| 2 | `TILETEXT` | CHAR(50) |  |  |  |  |
| 3 | `BACKGROUNDCOLOR` | CHAR(20) |  |  |  |  |
| 4 | `FOREGROUNDCOLOR` | CHAR(20) |  |  |  |  |
| 5 | `TYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `SVGFONT` | VARCHAR(250) |  | FK | foreign_key |  |
| 7 | `SVGHEXCHAR` | CHAR(20) |  |  |  |  |
| 8 | `CONTENTTYPE` | CHAR(30) |  |  |  |  |
| 9 | `IMAGEDATA` | BLOB(1000000000) |  |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `TILEVERSION` | INTEGER | NOT NULL |  |  |  |
| 12 | `MODULENAME` | CHAR(50) |  |  |  |  |
| 13 | `TAGCOLOR` | CHAR(20) |  |  |  |  |
| 14 | `TEXTCOLOR` | CHAR(20) |  |  |  |  |
| 15 | `TEXTBACKGROUNDCOLOR` | CHAR(20) |  |  |  |  |
| 16 | `BORDERCOLOR` | CHAR(20) |  |  |  |  |
| 17 | `CSSCLASS` | CHAR(150) |  |  |  |  |
| 18 | `STYLE` | VARCHAR(500) |  |  |  |  |
| 19 | `WRAPTEXT` | INTEGER | NOT NULL |  |  |  |
| 20 | `TEMPLATECODE` | CHAR(20) |  | FK | foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSSVGFONTS_SVGFONT` | `SVGFONT` | [`ABSSVGFONTS`](../PLATFORM/ABSSVGFONTS.md) | `CODE` | RESTRICT | `ABSAVAILABLETILES.SVGFONT = ABSSVGFONTS.CODE` |
| `ABSTILETEMPLATE_TEMPLATE` | `TEMPLATECODE` | [`ABSTILETEMPLATE`](../PLATFORM/ABSTILETEMPLATE.md) | `CODE` | RESTRICT | `ABSAVAILABLETILES.TEMPLATECODE = ABSTILETEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- child `ABSAVAILABLETILESDESCRIPTIONS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Indexes

- `ABSAVAILABLETILESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.DESCRIPTION,
       t.TILETEXT,
       t.BACKGROUNDCOLOR,
       t.FOREGROUNDCOLOR,
       t.TYPE,
       t.SVGFONT,
       t.SVGHEXCHAR,
       t.CONTENTTYPE,
       t.IMAGEDATA,
       t.ABSUNIQUEID,
       t.TILEVERSION
FROM   DB2ADMIN.ABSAVAILABLETILES t
FETCH FIRST 100 ROWS ONLY;
```
