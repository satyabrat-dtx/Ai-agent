# DB2ADMIN.ABSDIVISIONHANDLING

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ABSCOMPANYCODE`, `ENTITYNAME`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70321

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ENTITYNAME` | CHAR(100) | NOT NULL | PK | primary_key |  |
| 2 | `DIVISIONHANDLING` | INTEGER | NOT NULL |  |  |  |
| 3 | `LOADALLOWEDDIVISIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSCOMPANY_ABSCOMPANY` | `ABSCOMPANYCODE` | [`ABSCOMPANY`](../PLATFORM/ABSCOMPANY.md) | `CODE` | RESTRICT | `ABSDIVISIONHANDLING.ABSCOMPANYCODE = ABSCOMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSDIVISIONHANDLINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSCOMPANYCODE,
       t.ENTITYNAME,
       t.DIVISIONHANDLING,
       t.LOADALLOWEDDIVISIONPOLICYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSDIVISIONHANDLING t
FETCH FIRST 100 ROWS ONLY;
```
