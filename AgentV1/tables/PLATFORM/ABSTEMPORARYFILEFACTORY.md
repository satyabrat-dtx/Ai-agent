# DB2ADMIN.ABSTEMPORARYFILEFACTORY

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `TEMPORARYFILENAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 10339

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TEMPORARYFILENAME` | VARCHAR(100) | NOT NULL | PK | primary_key |  |
| 1 | `OVERRIDECLASSNAME` | VARCHAR(100) | NOT NULL |  |  |  |
| 2 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSTEMPORARYFILEFACTORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TEMPORARYFILENAME,
       t.OVERRIDECLASSNAME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSTEMPORARYFILEFACTORY t
FETCH FIRST 100 ROWS ONLY;
```
