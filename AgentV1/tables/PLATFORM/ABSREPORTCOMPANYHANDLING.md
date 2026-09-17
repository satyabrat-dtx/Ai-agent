# DB2ADMIN.ABSREPORTCOMPANYHANDLING

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `TABLENAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70440

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TABLENAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYLEVELHANDLING` | INTEGER | NOT NULL |  |  |  |
| 2 | `ENTITYNAME` | CHAR(100) | NOT NULL |  |  |  |
| 3 | `COMPANYATTRIBUTENAME` | CHAR(50) | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSREPORTCOMPANYHANDLINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TABLENAME,
       t.COMPANYLEVELHANDLING,
       t.ENTITYNAME,
       t.COMPANYATTRIBUTENAME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSREPORTCOMPANYHANDLING t
FETCH FIRST 100 ROWS ONLY;
```
