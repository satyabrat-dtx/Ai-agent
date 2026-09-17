# DB2ADMIN.ABSINSTALLEDMODULEVERSION

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `APPLICATIONNAME`, `MODULENAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 3859

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `APPLICATIONNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `MODULENAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `DESCRIPTION` | CHAR(50) | NOT NULL |  | description |  |
| 3 | `VERSION` | CHAR(20) | NOT NULL |  |  |  |
| 4 | `RELEASEDATE` | DATE | NOT NULL |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSINSTALLEDMODULEVERSIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.APPLICATIONNAME,
       t.MODULENAME,
       t.DESCRIPTION,
       t.VERSION,
       t.RELEASEDATE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSINSTALLEDMODULEVERSION t
FETCH FIRST 100 ROWS ONLY;
```
