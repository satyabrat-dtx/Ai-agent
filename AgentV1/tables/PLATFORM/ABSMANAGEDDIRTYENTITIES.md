# DB2ADMIN.ABSMANAGEDDIRTYENTITIES

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `CLASSFULLNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 115778

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CLASSFULLNAME` | VARCHAR(100) | NOT NULL | PK | primary_key |  |
| 1 | `ENABLED` | SMALLINT | NOT NULL |  |  |  |
| 2 | `DONOTRESETONFLUSH` | SMALLINT | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSMANAGEDDIRTYENTITIESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CLASSFULLNAME,
       t.ENABLED,
       t.DONOTRESETONFLUSH,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSMANAGEDDIRTYENTITIES t
FETCH FIRST 100 ROWS ONLY;
```
