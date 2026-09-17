# DB2ADMIN.PRIMROSEADDRESSKEY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `NUMBERID`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 10703

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NUMBERID` | DECIMAL(8,0) | NOT NULL | PK | primary_key |  |
| 1 | `CODE` | CHAR(8) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `ANICD` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRIMROSEADDRESSKEYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.NUMBERID,
       t.CODE,
       t.ANICD,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PRIMROSEADDRESSKEY t
FETCH FIRST 100 ROWS ONLY;
```
