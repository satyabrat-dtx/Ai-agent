# DB2ADMIN.ABSINSTALLEDDBFUNCTION

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `FUNCTIONNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194225

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FUNCTIONNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `FUNCTIONTEXT` | VARCHAR(1500) |  |  |  |  |
| 2 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSINSTALLEDDBFUNCTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FUNCTIONNAME,
       t.FUNCTIONTEXT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSINSTALLEDDBFUNCTION t
FETCH FIRST 100 ROWS ONLY;
```
