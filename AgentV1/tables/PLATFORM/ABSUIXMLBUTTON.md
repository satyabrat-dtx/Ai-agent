# DB2ADMIN.ABSUIXMLBUTTON

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `ABSUIXMLPATH`, `ABSUIXMLNAME`, `NAME`, `FORM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 34397

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `NAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `FORM` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `UIXMLTYPE` | INTEGER | NOT NULL |  |  |  |
| 5 | `BUTTONTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `OPERATION` | CHAR(50) |  |  |  |  |
| 7 | `UIPROCESS` | INTEGER | NOT NULL |  |  |  |
| 8 | `ENVIRONMENT` | INTEGER | NOT NULL |  |  |  |
| 9 | `REPLACESTDBTN` | INTEGER | NOT NULL |  |  |  |
| 10 | `REPLACEMENTTYPE` | INTEGER | NOT NULL |  |  |  |
| 11 | `LABEL` | VARCHAR(150) |  |  |  |  |
| 12 | `ALTTEXT` | VARCHAR(150) |  |  |  |  |
| 13 | `TITLE` | VARCHAR(150) |  |  |  |  |
| 14 | `BREADCRUMB` | CHAR(20) |  |  |  |  |
| 15 | `HIDDENONVIEW` | CHAR(1) |  |  |  |  |
| 16 | `HIDDENONCREATE` | CHAR(1) |  |  |  |  |
| 17 | `HIDDENONMODIFY` | CHAR(1) |  |  |  |  |
| 18 | `SHOWONPOPUP` | CHAR(1) |  |  |  |  |
| 19 | `SEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 20 | `EVENTMASK` | INTEGER | NOT NULL |  |  |  |
| 21 | `EVENTKEY` | INTEGER | NOT NULL |  |  |  |
| 22 | `CUSTOMCSS` | CHAR(50) |  |  |  |  |
| 23 | `REFERENCED` | VARCHAR(100) |  |  |  |  |
| 24 | `ACTIONTODO` | VARCHAR(250) |  |  |  |  |
| 25 | `PARAMETERS` | VARCHAR(1500) |  |  |  |  |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 27 | `ICONCLS` | CHAR(30) |  |  |  |  |
| 28 | `TARGETTYPE` | INTEGER | NOT NULL |  |  |  |
| 29 | `TARGETATTRIBUTE` | VARCHAR(120) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIXMLBUTTON1` (ABSUIXMLNAME, ABSUIXMLPATH)
- `ABSUIXMLBUTTONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.NAME,
       t.FORM,
       t.UIXMLTYPE,
       t.BUTTONTYPE,
       t.OPERATION,
       t.UIPROCESS,
       t.ENVIRONMENT,
       t.REPLACESTDBTN,
       t.REPLACEMENTTYPE,
       t.LABEL
FROM   DB2ADMIN.ABSUIXMLBUTTON t
FETCH FIRST 100 ROWS ONLY;
```
