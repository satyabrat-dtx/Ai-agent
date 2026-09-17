# DB2ADMIN.ABSHELP

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `LANGUAGE`, `COUNTRY`, `ABSUIXMLPATH`, `ABSUIXMLNAME`, `NAME`, `HELPTYPE`, `RECORDTYPE`, `FORM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 35748

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LANGUAGE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 1 | `COUNTRY` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 4 | `NAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 5 | `HELPTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `RECORDTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 7 | `FORM` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `HELPTEXT` | CLOB(2000000) |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSHELPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LANGUAGE,
       t.COUNTRY,
       t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.NAME,
       t.HELPTYPE,
       t.RECORDTYPE,
       t.FORM,
       t.HELPTEXT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSHELP t
FETCH FIRST 100 ROWS ONLY;
```
