# DB2ADMIN.ABSSCREENDEFINITION

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `FUNCTIONID`, `REVISION`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 117983

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REVISION` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 1 | `UIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 2 | `UIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 3 | `DESCRIPTION` | VARCHAR(250) | NOT NULL |  | description |  |
| 4 | `ENABLED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `FUNCTIONID` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 13 | `CUSTOMIZEDUIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 14 | `CUSTOMIZEDUIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 15 | `CUSTOMIZEDSCREENMETHOD` | VARCHAR(100) |  |  |  |  |
| 16 | `LAYOUT` | INTEGER | NOT NULL |  |  |  |
| 17 | `DOCKINGCONFIG` | CLOB(1000000) |  |  |  |  |
| 18 | `JSONINFO` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSSCREENDEFINITION_COMPONENT` | [`ABSSCREENCOMPONENT`](../PLATFORM/ABSSCREENCOMPONENT.md) | `ABSSCREENDEFINITIONFUNCTIONID`, `ABSSCREENDEFINITIONREVISION` | `ABSSCREENCOMPONENT.ABSSCREENDEFINITIONFUNCTIONID = ABSSCREENDEFINITION.FUNCTIONID AND ABSSCREENCOMPONENT.ABSSCREENDEFINITIONREVISION = ABSSCREENDEFINITION.REVISION` |
| `ABSSCREENDEFINITION_WINDOW` | [`ABSSCREENWINDOW`](../PLATFORM/ABSSCREENWINDOW.md) | `ABSSCREENDEFINITIONFUNCTIONID`, `ABSSCREENDEFINITIONREVISION` | `ABSSCREENWINDOW.ABSSCREENDEFINITIONFUNCTIONID = ABSSCREENDEFINITION.FUNCTIONID AND ABSSCREENWINDOW.ABSSCREENDEFINITIONREVISION = ABSSCREENDEFINITION.REVISION` |

## Indexes

- `ABSSCREENDEFINITIONUID` (ABSUNIQUEID)
- `UIXML` (FUNCTIONID, UIXMLPATH, UIXMLNAME)

## Starter query

```sql
SELECT t.REVISION,
       t.UIXMLPATH,
       t.UIXMLNAME,
       t.DESCRIPTION,
       t.ENABLED,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSSCREENDEFINITION t
FETCH FIRST 100 ROWS ONLY;
```
