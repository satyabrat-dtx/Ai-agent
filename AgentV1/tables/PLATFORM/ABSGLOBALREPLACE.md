# DB2ADMIN.ABSGLOBALREPLACE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `CLASSNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 82184

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CLASSNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 1 | `JARNAME` | VARCHAR(60) | NOT NULL |  |  |  |
| 2 | `HOMENAME` | VARCHAR(100) | NOT NULL |  |  |  |
| 3 | `APPLICATIONNAME` | VARCHAR(60) | NOT NULL |  |  |  |
| 4 | `OVERRIDECLASSNAME` | VARCHAR(54) |  |  |  |  |
| 5 | `OVERRIDEJARNAME` | VARCHAR(60) |  |  |  |  |
| 6 | `OVERRIDEHOMENAME` | VARCHAR(100) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `PATTERNTYPE` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSGLOBALREPLACEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CLASSNAME,
       t.JARNAME,
       t.HOMENAME,
       t.APPLICATIONNAME,
       t.OVERRIDECLASSNAME,
       t.OVERRIDEJARNAME,
       t.OVERRIDEHOMENAME,
       t.ABSUNIQUEID,
       t.PATTERNTYPE
FROM   DB2ADMIN.ABSGLOBALREPLACE t
FETCH FIRST 100 ROWS ONLY;
```
