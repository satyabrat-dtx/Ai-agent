# DB2ADMIN.CONSTRAINTDECODE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `TABLENAME`, `CONSTRAINTNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 82404

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TABLENAME` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 1 | `CONSTRAINTNAME` | CHAR(140) | NOT NULL | PK | primary_key |  |
| 2 | `DBCONSTRAINTNAME` | CHAR(30) |  |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- UNIQUE `CONSTRAINTDECODEI1` (TABLENAME, DBCONSTRAINTNAME)
- `CONSTRAINTDECODEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TABLENAME,
       t.CONSTRAINTNAME,
       t.DBCONSTRAINTNAME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.CONSTRAINTDECODE t
FETCH FIRST 100 ROWS ONLY;
```
