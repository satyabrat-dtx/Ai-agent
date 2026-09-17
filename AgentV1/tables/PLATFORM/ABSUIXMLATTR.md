# DB2ADMIN.ABSUIXMLATTR

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 82
- **Primary key**: `ABSUIXMLPATH`, `ABSUIXMLNAME`, `NAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 62714

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `NAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 3 | `UIXMLTYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `FIELDTYPE` | INTEGER | NOT NULL |  |  |  |
| 5 | `JAVANAME` | VARCHAR(100) |  |  |  |  |
| 6 | `SQLTYPE` | CHAR(50) |  |  |  |  |
| 7 | `DBCOLUMNNAME` | CHAR(50) |  |  |  |  |
| 8 | `DBALIASNAME` | CHAR(50) |  |  |  |  |
| 9 | `DBTABLENAME` | CHAR(50) |  |  |  |  |
| 10 | `USEABLEOB` | SMALLINT | NOT NULL |  |  |  |
| 11 | `USEABLEWC` | SMALLINT | NOT NULL |  |  |  |
| 12 | `USEABLECOL` | SMALLINT | NOT NULL |  |  |  |
| 13 | `HTMLTYPE` | CHAR(20) |  |  |  |  |
| 14 | `KEYSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 15 | `INHERITED` | SMALLINT | NOT NULL |  |  |  |
| 16 | `MULTIPLE` | SMALLINT | NOT NULL |  |  |  |
| 17 | `FIELDSET` | SMALLINT | NOT NULL |  |  |  |
| 18 | `ONCHANGE` | VARCHAR(1000) |  |  |  |  |
| 19 | `PARAMETERS` | VARCHAR(700) |  |  |  |  |
| 20 | `ACTIONFORCHECKBOX` | INTEGER | NOT NULL |  |  |  |
| 21 | `ACTIONFIELDS` | VARCHAR(1000) |  |  |  |  |
| 22 | `OPPOSITEACTIONFIELDS` | VARCHAR(1000) |  |  |  |  |
| 23 | `CALENDAR` | CHAR(50) |  |  |  |  |
| 24 | `CALENDARPARAMETERS` | VARCHAR(100) |  |  |  |  |
| 25 | `REFERENCED` | VARCHAR(100) |  |  |  |  |
| 26 | `AVOIDREPLACE` | VARCHAR(100) |  |  |  |  |
| 27 | `LINKEDATTRS` | VARCHAR(100) |  |  |  |  |
| 28 | `DECODINGCLASS` | CHAR(50) |  |  |  |  |
| 29 | `DECODINGCLASSPARAMETERS` | VARCHAR(100) |  |  |  |  |
| 30 | `LOOKUPMETHOD` | CHAR(50) |  |  |  |  |
| 31 | `LOOKUPPARAMETERS` | VARCHAR(350) |  |  |  |  |
| 32 | `TRANSACTIONAL` | SMALLINT | NOT NULL |  |  |  |
| 33 | `OBJLABEL` | VARCHAR(150) |  |  |  |  |
| 34 | `STPLABEL` | VARCHAR(150) |  |  |  |  |
| 35 | `LSTLABEL` | VARCHAR(150) |  |  |  |  |
| 36 | `HDRLABEL` | VARCHAR(150) |  |  |  |  |
| 37 | `ALTTEXT` | VARCHAR(150) |  |  |  |  |
| 38 | `ALTTEXTDET` | VARCHAR(150) |  |  |  |  |
| 39 | `TITLEFORCOLUMN` | VARCHAR(150) |  |  |  |  |
| 40 | `TABBEDPAGE` | VARCHAR(150) |  |  |  |  |
| 41 | `MANDATORY` | CHAR(1) |  |  |  |  |
| 42 | `READONLY` | CHAR(1) |  |  |  |  |
| 43 | `HIDDENONVIEW` | CHAR(1) |  |  |  |  |
| 44 | `HIDDENONCREATE` | CHAR(1) |  |  |  |  |
| 45 | `HIDDENONMODIFY` | CHAR(1) |  |  |  |  |
| 46 | `OBJSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 47 | `LSTSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 48 | `HDRSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 49 | `DESCENDING` | CHAR(1) |  |  |  |  |
| 50 | `AUTODECODE` | CHAR(1) |  |  |  |  |
| 51 | `DFTVALUE` | CHAR(50) |  |  |  |  |
| 52 | `MINLENGTH` | DECIMAL(10,0) |  |  |  |  |
| 53 | `MAXLENGTH` | DECIMAL(10,0) |  |  |  |  |
| 54 | `NBRINTEGERS` | DECIMAL(10,0) |  |  |  |  |
| 55 | `NBRDECIMALS` | DECIMAL(3,0) |  |  |  |  |
| 56 | `HTMLSIZE` | DECIMAL(5,0) |  |  |  |  |
| 57 | `HTMLROWS` | DECIMAL(3,0) |  |  |  |  |
| 58 | `EDITMASK` | CHAR(50) |  |  |  |  |
| 59 | `LISTLABELCSS` | VARCHAR(50) |  |  |  |  |
| 60 | `LISTOBJECTCSS` | VARCHAR(50) |  |  |  |  |
| 61 | `OBJECTLABELCSS` | VARCHAR(50) |  |  |  |  |
| 62 | `OBJECTCSS` | VARCHAR(50) |  |  |  |  |
| 63 | `COLUMNSIZE` | DECIMAL(5,0) |  |  |  |  |
| 64 | `OPTIONALKEY` | SMALLINT | NOT NULL |  |  |  |
| 65 | `GROUPBOXTYPE` | CHAR(1) |  |  |  |  |
| 66 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 67 | `TIMEZONETYPE` | CHAR(1) |  |  |  |  |
| 68 | `OBJECTHEADERSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 69 | `ADDITIONALJSONINFO` | VARCHAR(4000) |  |  |  |  |
| 70 | `SUBMITWHENREADONLY` | CHAR(1) |  |  |  |  |
| 71 | `NOTSUBMITABLE` | CHAR(1) |  |  |  |  |
| 72 | `MGRIDCHILDSESSIONPATH` | VARCHAR(50) |  |  |  |  |
| 73 | `MGRIDCHILDSESSIONNAME` | VARCHAR(54) |  |  |  |  |
| 74 | `MGRIDGETMETHODNAME` | VARCHAR(60) |  |  |  |  |
| 75 | `MGRIDVALIDATEMETHODNAME` | VARCHAR(60) |  |  |  |  |
| 76 | `MGRIDGHFDISABLED` | CHAR(1) |  |  |  |  |
| 77 | `MGRIDGHFCOLLAPSED` | CHAR(1) |  |  |  |  |
| 78 | `MGRIDEXPANDED` | CHAR(1) |  |  |  |  |
| 79 | `MGRIDEDITMODE` | INTEGER | NOT NULL |  |  |  |
| 80 | `MGRIDHIDDENOPENDETAILS` | CHAR(1) |  |  |  |  |
| 81 | `MGRIDDISABLESORTANDFILTER` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIXMLATTR1` (ABSUIXMLNAME, ABSUIXMLPATH)
- `ABSUIXMLATTR2` (ABSUIXMLPATH, ABSUIXMLNAME)
- `ABSUIXMLATTR3` (UIXMLTYPE, NAME)
- `ABSUIXMLATTRUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.NAME,
       t.UIXMLTYPE,
       t.FIELDTYPE,
       t.JAVANAME,
       t.SQLTYPE,
       t.DBCOLUMNNAME,
       t.DBALIASNAME,
       t.DBTABLENAME,
       t.USEABLEOB,
       t.USEABLEWC
FROM   DB2ADMIN.ABSUIXMLATTR t
FETCH FIRST 100 ROWS ONLY;
```
