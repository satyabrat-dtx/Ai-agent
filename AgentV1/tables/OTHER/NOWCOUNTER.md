# DB2ADMIN.NOWCOUNTER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `COUNTERKEY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 19677

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COUNTERKEY` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `UNIQUEID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 2 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NOWCOUNTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COUNTERKEY,
       t.UNIQUEID,
       t.ABSUNIQUEID
FROM   DB2ADMIN.NOWCOUNTER t
FETCH FIRST 100 ROWS ONLY;
```
