# DB2ADMIN.ABSUIXMLCUSTOMVALUE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 59
- **Primary key**: `ABSUIXMLPATH`, `ABSUIXMLNAME`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 49920

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `DECODEBTN` | CHAR(1) |  |  |  |  |
| 5 | `MULTIINSERTBTN` | CHAR(1) |  |  |  |  |
| 6 | `LASTINSERTEDASDFT` | CHAR(1) |  |  |  |  |
| 7 | `OBJFORM` | VARCHAR(100) |  |  |  |  |
| 8 | `CSOBJBODY` | VARCHAR(100) |  |  |  |  |
| 9 | `OHLOGO` | VARCHAR(100) |  |  |  |  |
| 10 | `OHCODE` | VARCHAR(100) |  |  |  |  |
| 11 | `OFLOGO` | VARCHAR(100) |  |  |  |  |
| 12 | `OFCODE` | VARCHAR(100) |  |  |  |  |
| 13 | `DIALOGHEIGHT` | DECIMAL(4,0) |  |  |  |  |
| 14 | `DIALOGWIDTH` | DECIMAL(4,0) |  |  |  |  |
| 15 | `CUSTOMBOCSS` | CHAR(50) |  |  |  |  |
| 16 | `HELPFILE` | VARCHAR(100) |  |  |  |  |
| 17 | `ROWSINPAGE` | DECIMAL(5,0) |  |  |  |  |
| 18 | `AUTOINSERTIFVOID` | CHAR(1) |  |  |  |  |
| 19 | `COLFORM` | VARCHAR(100) |  |  |  |  |
| 20 | `CHLOGO` | VARCHAR(100) |  |  |  |  |
| 21 | `CHCODE` | VARCHAR(100) |  |  |  |  |
| 22 | `CFLOGO` | VARCHAR(100) |  |  |  |  |
| 23 | `CFCODE` | VARCHAR(100) |  |  |  |  |
| 24 | `CSPAGE` | VARCHAR(100) |  |  |  |  |
| 25 | `CSPROCESS` | VARCHAR(100) |  |  |  |  |
| 26 | `GHFCOLLECTION` | CHAR(1) |  |  |  |  |
| 27 | `GHFCHILDRENCOLLECTION` | CHAR(1) |  |  |  |  |
| 28 | `GHFFULLSCREEN` | CHAR(1) |  |  |  |  |
| 29 | `GHFCHOOSER` | CHAR(1) |  |  |  |  |
| 30 | `LKPFORM` | VARCHAR(100) |  |  |  |  |
| 31 | `LHLOGO` | VARCHAR(100) |  |  |  |  |
| 32 | `LHCODE` | VARCHAR(100) |  |  |  |  |
| 33 | `LFLOGO` | VARCHAR(100) |  |  |  |  |
| 34 | `LFCODE` | VARCHAR(100) |  |  |  |  |
| 35 | `GHFLOOKUP` | CHAR(1) |  |  |  |  |
| 36 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 37 | `EXCELLIMIT` | DECIMAL(7,0) |  |  |  |  |
| 38 | `SHOWHEADERASOBJECT` | CHAR(1) |  |  |  |  |
| 39 | `ADDITIONALJSONINFOOBJ` | VARCHAR(4000) |  |  |  |  |
| 40 | `ADDITIONALJSONINFOCOL` | VARCHAR(4000) |  |  |  |  |
| 41 | `ADDITIONALJSONINFOLKP` | VARCHAR(4000) |  |  |  |  |
| 42 | `REOPENMODE` | INTEGER | NOT NULL |  |  |  |
| 43 | `DISABLEEXCELIMPORTEXPORT` | CHAR(1) |  |  |  |  |
| 44 | `HIDEABLEFASTSWITCHBAR` | CHAR(1) |  |  |  |  |
| 45 | `HIDEFASTSWITCHBAR` | CHAR(1) |  |  |  |  |
| 46 | `HIDEABLECOLUMNSFILTERS` | CHAR(1) |  |  |  |  |
| 47 | `HIDECOLUMNSFILTERS` | CHAR(1) |  |  |  |  |
| 48 | `HIDEABLEPAGINGBAR` | CHAR(1) |  |  |  |  |
| 49 | `HIDEPAGINGBAR` | CHAR(1) |  |  |  |  |
| 50 | `OBJECTWIDTH` | CHAR(9) |  |  |  |  |
| 51 | `HEADERHEIGHT` | CHAR(9) |  |  |  |  |
| 52 | `DISABLEADVANCEDPINTODESKTOP` | CHAR(1) |  |  |  |  |
| 53 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 54 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 55 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 56 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 57 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 58 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIXMLCV1` (USERUSERID, COMPANYCODE)
- `ABSUIXMLCUSTOMVALUEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.USERUSERID,
       t.COMPANYCODE,
       t.DECODEBTN,
       t.MULTIINSERTBTN,
       t.LASTINSERTEDASDFT,
       t.OBJFORM,
       t.CSOBJBODY,
       t.OHLOGO,
       t.OHCODE,
       t.OFLOGO
FROM   DB2ADMIN.ABSUIXMLCUSTOMVALUE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
