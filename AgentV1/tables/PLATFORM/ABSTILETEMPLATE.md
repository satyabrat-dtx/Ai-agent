# DB2ADMIN.ABSTILETEMPLATE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `CODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 215937

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(20) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `DESCRIPTION` | CHAR(50) | NOT NULL |  | description |  |
| 2 | `MODULENAME` | CHAR(50) |  |  |  |  |
| 3 | `TEMPLATETYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `TEMPLATEBACKGROUNDCOLOR` | CHAR(20) |  |  |  |  |
| 5 | `TEMPLATEFOREGROUNDCOLOR` | CHAR(20) |  |  |  |  |
| 6 | `TEMPLATETAGCOLOR` | CHAR(20) |  |  |  |  |
| 7 | `TEMPLATETEXTCOLOR` | CHAR(20) |  |  |  |  |
| 8 | `TEMPLATETEXTBACKGROUNDCOLOR` | CHAR(20) |  |  |  |  |
| 9 | `TEMPLATEBORDERCOLOR` | CHAR(20) |  |  |  |  |
| 10 | `TEMPLATECSSCLASS` | CHAR(150) |  |  |  |  |
| 11 | `TEMPLATESTYLE` | VARCHAR(500) |  |  |  |  |
| 12 | `TEMPLATESVGFONTCODE` | VARCHAR(250) |  | FK | foreign_key |  |
| 13 | `TEMPLATEHEXCHAR` | CHAR(20) |  |  |  |  |
| 14 | `TEMPLATEWRAPTEXT` | INTEGER | NOT NULL |  |  |  |
| 15 | `CONTENTTYPE` | CHAR(30) |  |  |  |  |
| 16 | `IMAGEDATA` | BLOB(1000000000) |  |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSSVGFONTS_TEMPLATESVGFONT` | `TEMPLATESVGFONTCODE` | [`ABSSVGFONTS`](../PLATFORM/ABSSVGFONTS.md) | `CODE` | RESTRICT | `ABSTILETEMPLATE.TEMPLATESVGFONTCODE = ABSSVGFONTS.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSTILETEMPLATE_TEMPLATE` | [`ABSAVAILABLETILES`](../PLATFORM/ABSAVAILABLETILES.md) | `TEMPLATECODE` | `ABSAVAILABLETILES.TEMPLATECODE = ABSTILETEMPLATE.CODE` |

## Implicit links (NOT declared in the DDL — inferred)

- child `ABSTILETEMPLATEDESCRIPTIONS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Indexes

- `ABSTILETEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.DESCRIPTION,
       t.MODULENAME,
       t.TEMPLATETYPE,
       t.TEMPLATEBACKGROUNDCOLOR,
       t.TEMPLATEFOREGROUNDCOLOR,
       t.TEMPLATETAGCOLOR,
       t.TEMPLATETEXTCOLOR,
       t.TEMPLATETEXTBACKGROUNDCOLOR,
       t.TEMPLATEBORDERCOLOR,
       t.TEMPLATECSSCLASS,
       t.TEMPLATESTYLE
FROM   DB2ADMIN.ABSTILETEMPLATE t
FETCH FIRST 100 ROWS ONLY;
```
