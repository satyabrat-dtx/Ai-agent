# DB2ADMIN.NETCOUNTER

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `COUNTERKEY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 122715

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COUNTERKEY` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 2 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETCOUNTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COUNTERKEY,
       t.UNIQUEID,
       t.ABSUNIQUEID
FROM   DB2ADMIN.NETCOUNTER t
FETCH FIRST 100 ROWS ONLY;
```
