# DB2ADMIN.ABSWRKFILEFACTORY

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `WORKTABLENAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42328

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WORKTABLENAME` | VARCHAR(100) | NOT NULL | PK | primary_key |  |
| 1 | `DAYSTOKEEP` | INTEGER | NOT NULL |  |  |  |
| 2 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 3 | `ENTITYNAME` | VARCHAR(100) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSWRKFILEFACTORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.WORKTABLENAME,
       t.DAYSTOKEEP,
       t.ABSUNIQUEID,
       t.ENTITYNAME
FROM   DB2ADMIN.ABSWRKFILEFACTORY t
FETCH FIRST 100 ROWS ONLY;
```
