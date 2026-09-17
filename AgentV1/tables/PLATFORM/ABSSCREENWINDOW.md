# DB2ADMIN.ABSSCREENWINDOW

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `ABSSCREENDEFINITIONFUNCTIONID`, `ABSSCREENDEFINITIONREVISION`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118044

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSSCREENDEFINITIONREVISION` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CODE` | CHAR(30) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `DESCRIPTION` | VARCHAR(250) | NOT NULL |  | description |  |
| 3 | `PRIMARYWINDOW` | SMALLINT | NOT NULL |  |  |  |
| 4 | `WIDTH` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 5 | `HEIGHT` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 6 | `POSX` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 7 | `POSY` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 8 | `TITLE` | VARCHAR(100) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 16 | `ABSSCREENDEFINITIONFUNCTIONID` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 17 | `DISABLED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `HIDDEN` | SMALLINT | NOT NULL |  |  |  |
| 19 | `JSONINFO` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSSCREENDEFINITION_WINDOW` | `ABSSCREENDEFINITIONFUNCTIONID`, `ABSSCREENDEFINITIONREVISION` | [`ABSSCREENDEFINITION`](../PLATFORM/ABSSCREENDEFINITION.md) | `FUNCTIONID`, `REVISION` | RESTRICT | `ABSSCREENWINDOW.ABSSCREENDEFINITIONFUNCTIONID = ABSSCREENDEFINITION.FUNCTIONID AND ABSSCREENWINDOW.ABSSCREENDEFINITIONREVISION = ABSSCREENDEFINITION.REVISION` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSSCREENWINDOW_WINDOW` | [`ABSSCREENCOMPONENT`](../PLATFORM/ABSSCREENCOMPONENT.md) | `ABSSCREENDEFINITIONFUNCTIONID`, `ABSSCREENDEFINITIONREVISION`, `WINDOWCODE` | `ABSSCREENCOMPONENT.ABSSCREENDEFINITIONFUNCTIONID = ABSSCREENWINDOW.ABSSCREENDEFINITIONFUNCTIONID AND ABSSCREENCOMPONENT.ABSSCREENDEFINITIONREVISION = ABSSCREENWINDOW.ABSSCREENDEFINITIONREVISION AND ABSSCREENCOMPONENT.WINDOWCODE = ABSSCREENWINDOW.CODE` |

## Implicit links (NOT declared in the DDL — inferred)

- child `ABSSCREENWINDOWLANGUAGE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Indexes

- `ABSSCREENWINDOWUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSSCREENDEFINITIONREVISION,
       t.CODE,
       t.DESCRIPTION,
       t.PRIMARYWINDOW,
       t.WIDTH,
       t.HEIGHT,
       t.POSX,
       t.POSY,
       t.TITLE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.ABSSCREENWINDOW t
FETCH FIRST 100 ROWS ONLY;
```
