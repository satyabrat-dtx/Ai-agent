# DB2ADMIN.ABSUIXMLATTRLANGDESCR

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ABSUIXMLATTRABSUIXMLPATH`, `ABSUIXMLATTRABSUIXMLNAME`, `ABSUIXMLATTRNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 9920

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLATTRABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLATTRABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `ABSUIXMLATTRNAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 3 | `OBJLABEL` | VARCHAR(150) |  |  |  |  |
| 4 | `STPLABEL` | VARCHAR(150) |  |  |  |  |
| 5 | `LSTLABEL` | VARCHAR(150) |  |  |  |  |
| 6 | `HDRLABEL` | VARCHAR(150) |  |  |  |  |
| 7 | `ALTTEXT` | VARCHAR(150) |  |  |  |  |
| 8 | `ALTTEXTDET` | VARCHAR(150) |  |  |  |  |
| 9 | `TITLEFORCOLUMN` | VARCHAR(150) |  |  |  |  |
| 10 | `TABBEDPAGE` | VARCHAR(150) |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `TRANSLATEDOPTIONS` | VARCHAR(2000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIXMLATTRLANGDESCRUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLATTRABSUIXMLPATH,
       t.ABSUIXMLATTRABSUIXMLNAME,
       t.ABSUIXMLATTRNAME,
       t.OBJLABEL,
       t.STPLABEL,
       t.LSTLABEL,
       t.HDRLABEL,
       t.ALTTEXT,
       t.ALTTEXTDET,
       t.TITLEFORCOLUMN,
       t.TABBEDPAGE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSUIXMLATTRLANGDESCR t
FETCH FIRST 100 ROWS ONLY;
```
