# DB2ADMIN.ABSJNDIREF

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `SYMBOLICNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 14679

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SYMBOLICNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `TRANSLATEDNAME` | CHAR(105) | NOT NULL |  |  |  |
| 2 | `DESCRIPTION` | VARCHAR(1000) |  |  | description |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSJNDIREFUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SYMBOLICNAME,
       t.TRANSLATEDNAME,
       t.DESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSJNDIREF t
FETCH FIRST 100 ROWS ONLY;
```
