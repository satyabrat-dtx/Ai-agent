# DB2ADMIN.ABSUIXMLEXT

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 43
- **Primary key**: `PATH`, `NAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70722

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `NAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `PATTERN` | CHAR(50) |  |  |  |  |
| 3 | `MANAGEDCLASSTYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `JNDINAME` | CHAR(100) |  |  |  |  |
| 5 | `DEPENDENTCLASS` | VARCHAR(100) |  |  |  |  |
| 6 | `TABLENAME` | CHAR(50) |  |  |  |  |
| 7 | `SINGLEINSTANCE` | SMALLINT | NOT NULL |  |  |  |
| 8 | `MPRECREATE` | CHAR(50) |  |  |  |  |
| 9 | `MUICOMMIT` | CHAR(50) |  |  |  |  |
| 10 | `MUIROLLBACK` | CHAR(50) |  |  |  |  |
| 11 | `FMONCREATE` | CHAR(50) |  |  |  |  |
| 12 | `FMONUPDATE` | CHAR(50) |  |  |  |  |
| 13 | `FMONDELETE` | CHAR(50) |  |  |  |  |
| 14 | `FIRSTINDEXKEY` | INTEGER | NOT NULL |  |  |  |
| 15 | `NODECODE` | SMALLINT | NOT NULL |  |  |  |
| 16 | `HTMLFORMENCTYPE` | INTEGER | NOT NULL |  |  |  |
| 17 | `CMOBJECT` | CHAR(50) |  |  |  |  |
| 18 | `OBJONLOAD` | VARCHAR(1000) |  |  |  |  |
| 19 | `OBJONLOADARGS` | VARCHAR(250) |  |  |  |  |
| 20 | `OBJONUNLOAD` | VARCHAR(1000) |  |  |  |  |
| 21 | `OBJONUNLOADARGS` | VARCHAR(250) |  |  |  |  |
| 22 | `OBJONSUBMIT` | VARCHAR(1000) |  |  |  |  |
| 23 | `OBJONSUBMITARGS` | VARCHAR(250) |  |  |  |  |
| 24 | `CMCOLLECTION` | CHAR(50) |  |  |  |  |
| 25 | `CMSETUPCOLLECTION` | CHAR(50) |  |  |  |  |
| 26 | `COLONLOAD` | VARCHAR(1000) |  |  |  |  |
| 27 | `COLONLOADARGS` | VARCHAR(250) |  |  |  |  |
| 28 | `COLONUNLOAD` | VARCHAR(1000) |  |  |  |  |
| 29 | `COLONUNLOADARGS` | VARCHAR(250) |  |  |  |  |
| 30 | `CMLOOKUP` | CHAR(50) |  |  |  |  |
| 31 | `CMSETUPLOOKUP` | CHAR(50) |  |  |  |  |
| 32 | `LKPONLOAD` | VARCHAR(1000) |  |  |  |  |
| 33 | `LKPONLOADARGS` | VARCHAR(250) |  |  |  |  |
| 34 | `LKPONUNLOAD` | VARCHAR(100) |  |  |  |  |
| 35 | `LKPONUNLOADARGS` | VARCHAR(250) |  |  |  |  |
| 36 | `CMHEADER` | CHAR(50) |  |  |  |  |
| 37 | `HDRONLOAD` | VARCHAR(1000) |  |  |  |  |
| 38 | `HDRONLOADARGS` | VARCHAR(100) |  |  |  |  |
| 39 | `HDRONUNLOAD` | VARCHAR(1000) |  |  |  |  |
| 40 | `HDRONUNLOADARGS` | VARCHAR(100) |  |  |  |  |
| 41 | `REFERENCEDENTITY` | CHAR(50) |  |  |  |  |
| 42 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- UNIQUE `ABSUIXMLEXT1` (NAME, PATH)
- UNIQUE `ABSUIXMLEXT2` (NAME, PATH)
- `ABSUIXMLEXTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PATH,
       t.NAME,
       t.PATTERN,
       t.MANAGEDCLASSTYPE,
       t.JNDINAME,
       t.DEPENDENTCLASS,
       t.TABLENAME,
       t.SINGLEINSTANCE,
       t.MPRECREATE,
       t.MUICOMMIT,
       t.MUIROLLBACK,
       t.FMONCREATE
FROM   DB2ADMIN.ABSUIXMLEXT t
FETCH FIRST 100 ROWS ONLY;
```
