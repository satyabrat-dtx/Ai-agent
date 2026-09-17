# DB2ADMIN.ABSUIXML

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 73
- **Primary key**: `PATH`, `NAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 49768

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `NAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `UIXMLTYPE` | INTEGER | NOT NULL |  |  |  |
| 3 | `ORIGINPATH` | VARCHAR(50) |  |  |  |  |
| 4 | `ORIGINNAME` | VARCHAR(54) |  |  |  |  |
| 5 | `DESCRIPTION` | VARCHAR(250) |  |  | description |  |
| 6 | `FUNCTIONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 7 | `FUNCTIONREAD` | SMALLINT | NOT NULL |  |  |  |
| 8 | `FUNCTIONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `FUNCTIONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `FUNCTIONQUERY` | SMALLINT | NOT NULL |  |  |  |
| 11 | `FUNCTIONSUBMIT` | SMALLINT | NOT NULL |  |  |  |
| 12 | `OBJTITLE` | VARCHAR(150) |  |  |  |  |
| 13 | `COLTITLE` | VARCHAR(150) |  |  |  |  |
| 14 | `LKPTITLE` | VARCHAR(150) |  |  |  |  |
| 15 | `COLBREADCRUMB` | CHAR(20) |  |  |  |  |
| 16 | `OBJBREADCRUMB` | CHAR(20) |  |  |  |  |
| 17 | `DECODEBTN` | CHAR(1) |  |  |  |  |
| 18 | `MULTIINSERTBTN` | CHAR(1) |  |  |  |  |
| 19 | `LASTINSERTEDASDFT` | CHAR(1) |  |  |  |  |
| 20 | `OBJFORM` | VARCHAR(100) |  |  |  |  |
| 21 | `CSOBJBODY` | VARCHAR(100) |  |  |  |  |
| 22 | `OHLOGO` | VARCHAR(100) |  |  |  |  |
| 23 | `OHCODE` | VARCHAR(100) |  |  |  |  |
| 24 | `OFLOGO` | VARCHAR(100) |  |  |  |  |
| 25 | `OFCODE` | VARCHAR(100) |  |  |  |  |
| 26 | `DIALOGHEIGHT` | DECIMAL(4,0) |  |  |  |  |
| 27 | `DIALOGWIDTH` | DECIMAL(4,0) |  |  |  |  |
| 28 | `CUSTOMBOCSS` | CHAR(50) |  |  |  |  |
| 29 | `HELPFILE` | VARCHAR(100) |  |  |  |  |
| 30 | `ROWSINPAGE` | DECIMAL(5,0) |  |  |  |  |
| 31 | `AUTOINSERTIFVOID` | CHAR(1) |  |  |  |  |
| 32 | `COLFORM` | VARCHAR(100) |  |  |  |  |
| 33 | `CHLOGO` | VARCHAR(100) |  |  |  |  |
| 34 | `CHCODE` | VARCHAR(100) |  |  |  |  |
| 35 | `CFLOGO` | VARCHAR(100) |  |  |  |  |
| 36 | `CFCODE` | VARCHAR(100) |  |  |  |  |
| 37 | `CSPAGE` | VARCHAR(100) |  |  |  |  |
| 38 | `CSPROCESS` | VARCHAR(100) |  |  |  |  |
| 39 | `GHFCOLLECTION` | CHAR(1) |  |  |  |  |
| 40 | `GHFCHILDRENCOLLECTION` | CHAR(1) |  |  |  |  |
| 41 | `GHFFULLSCREEN` | CHAR(1) |  |  |  |  |
| 42 | `GHFCHOOSER` | CHAR(1) |  |  |  |  |
| 43 | `LKPFORM` | VARCHAR(100) |  |  |  |  |
| 44 | `LHLOGO` | VARCHAR(100) |  |  |  |  |
| 45 | `LHCODE` | VARCHAR(100) |  |  |  |  |
| 46 | `LFLOGO` | VARCHAR(100) |  |  |  |  |
| 47 | `LFCODE` | VARCHAR(100) |  |  |  |  |
| 48 | `GHFLOOKUP` | CHAR(1) |  |  |  |  |
| 49 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 50 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 51 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 52 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 53 | `DEFAULTVIEW` | SMALLINT | NOT NULL |  |  |  |
| 54 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 55 | `EXCELLIMIT` | DECIMAL(7,0) |  |  |  |  |
| 56 | `SHOWHEADERASOBJECT` | CHAR(1) |  |  |  |  |
| 57 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 58 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 59 | `ADDITIONALJSONINFOOBJ` | VARCHAR(4000) |  |  |  |  |
| 60 | `ADDITIONALJSONINFOCOL` | VARCHAR(4000) |  |  |  |  |
| 61 | `ADDITIONALJSONINFOLKP` | VARCHAR(4000) |  |  |  |  |
| 62 | `REOPENMODE` | INTEGER | NOT NULL |  |  |  |
| 63 | `DISABLEEXCELIMPORTEXPORT` | CHAR(1) |  |  |  |  |
| 64 | `HIDEABLEFASTSWITCHBAR` | CHAR(1) |  |  |  |  |
| 65 | `HIDEFASTSWITCHBAR` | CHAR(1) |  |  |  |  |
| 66 | `HIDEABLECOLUMNSFILTERS` | CHAR(1) |  |  |  |  |
| 67 | `HIDECOLUMNSFILTERS` | CHAR(1) |  |  |  |  |
| 68 | `HIDEABLEPAGINGBAR` | CHAR(1) |  |  |  |  |
| 69 | `HIDEPAGINGBAR` | CHAR(1) |  |  |  |  |
| 70 | `OBJECTWIDTH` | CHAR(9) |  |  |  |  |
| 71 | `HEADERHEIGHT` | CHAR(9) |  |  |  |  |
| 72 | `DISABLEADVANCEDPINTODESKTOP` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- UNIQUE `ABSUIXML1` (ORIGINPATH, ORIGINNAME, NAME, PATH)
- UNIQUE `ABSUIXML2` (NAME, PATH)
- `ABSUIXML3` (ORIGINPATH, NAME, PATH)
- `ABSUIXML4` (ORIGINNAME, ORIGINPATH, NAME, PATH)
- `ABSUIXMLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PATH,
       t.NAME,
       t.UIXMLTYPE,
       t.ORIGINPATH,
       t.ORIGINNAME,
       t.DESCRIPTION,
       t.FUNCTIONCREATE,
       t.FUNCTIONREAD,
       t.FUNCTIONUPDATE,
       t.FUNCTIONDELETE,
       t.FUNCTIONQUERY,
       t.FUNCTIONSUBMIT
FROM   DB2ADMIN.ABSUIXML t
FETCH FIRST 100 ROWS ONLY;
```
