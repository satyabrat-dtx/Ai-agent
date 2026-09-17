# DB2ADMIN.ABSUIXMLATTRCUSTOMVALUE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 50
- **Primary key**: `ABSUIXMLATTRABSUIXMLPATH`, `ABSUIXMLATTRABSUIXMLNAME`, `ABSUIXMLATTRNAME`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 32210

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLATTRABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLATTRABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `ABSUIXMLATTRNAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 3 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `MANDATORY` | CHAR(1) |  |  |  |  |
| 6 | `READONLY` | CHAR(1) |  |  |  |  |
| 7 | `HIDDENONVIEW` | CHAR(1) |  |  |  |  |
| 8 | `HIDDENONCREATE` | CHAR(1) |  |  |  |  |
| 9 | `HIDDENONMODIFY` | CHAR(1) |  |  |  |  |
| 10 | `OBJSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 11 | `LSTSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 12 | `HDRSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 13 | `DESCENDING` | CHAR(1) |  |  |  |  |
| 14 | `AUTODECODE` | CHAR(1) |  |  |  |  |
| 15 | `DFTVALUE` | CHAR(50) |  |  |  |  |
| 16 | `MINLENGTH` | DECIMAL(10,0) |  |  |  |  |
| 17 | `MAXLENGTH` | DECIMAL(10,0) |  |  |  |  |
| 18 | `NBRINTEGERS` | DECIMAL(10,0) |  |  |  |  |
| 19 | `NBRDECIMALS` | DECIMAL(3,0) |  |  |  |  |
| 20 | `HTMLSIZE` | DECIMAL(5,0) |  |  |  |  |
| 21 | `HTMLROWS` | DECIMAL(3,0) |  |  |  |  |
| 22 | `EDITMASK` | CHAR(50) |  |  |  |  |
| 23 | `LISTLABELCSS` | VARCHAR(50) |  |  |  |  |
| 24 | `LISTOBJECTCSS` | VARCHAR(50) |  |  |  |  |
| 25 | `OBJECTLABELCSS` | VARCHAR(50) |  |  |  |  |
| 26 | `OBJECTCSS` | VARCHAR(50) |  |  |  |  |
| 27 | `COLUMNSIZE` | DECIMAL(5,0) |  |  |  |  |
| 28 | `GROUPBOXTYPE` | CHAR(1) |  |  |  |  |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 30 | `OBJECTHEADERSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 31 | `ADDITIONALJSONINFO` | VARCHAR(4000) |  |  |  |  |
| 32 | `SUBMITWHENREADONLY` | CHAR(1) |  |  |  |  |
| 33 | `NOTSUBMITABLE` | CHAR(1) |  |  |  |  |
| 34 | `MGRIDCHILDSESSIONPATH` | VARCHAR(50) |  |  |  |  |
| 35 | `MGRIDCHILDSESSIONNAME` | VARCHAR(54) |  |  |  |  |
| 36 | `MGRIDGETMETHODNAME` | VARCHAR(60) |  |  |  |  |
| 37 | `MGRIDVALIDATEMETHODNAME` | VARCHAR(60) |  |  |  |  |
| 38 | `MGRIDGHFDISABLED` | CHAR(1) |  |  |  |  |
| 39 | `MGRIDGHFCOLLAPSED` | CHAR(1) |  |  |  |  |
| 40 | `MGRIDEXPANDED` | CHAR(1) |  |  |  |  |
| 41 | `MGRIDEDITMODE` | INTEGER | NOT NULL |  |  |  |
| 42 | `MGRIDHIDDENOPENDETAILS` | CHAR(1) |  |  |  |  |
| 43 | `MGRIDDISABLESORTANDFILTER` | CHAR(1) |  |  |  |  |
| 44 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 45 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 46 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 47 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 48 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 49 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIXMLATTCUS1` (ABSUIXMLATTRABSUIXMLNAME, ABSUIXMLATTRABSUIXMLPATH, ABSUIXMLATTRNAME)
- `ABSUIXMLATTRCUSTOMVALUEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLATTRABSUIXMLPATH,
       t.ABSUIXMLATTRABSUIXMLNAME,
       t.ABSUIXMLATTRNAME,
       t.USERUSERID,
       t.COMPANYCODE,
       t.MANDATORY,
       t.READONLY,
       t.HIDDENONVIEW,
       t.HIDDENONCREATE,
       t.HIDDENONMODIFY,
       t.OBJSEQUENCE,
       t.LSTSEQUENCE
FROM   DB2ADMIN.ABSUIXMLATTRCUSTOMVALUE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
