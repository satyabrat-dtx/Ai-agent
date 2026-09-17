# DB2ADMIN.ABSWIZARDHASH

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `MODULENAME`, `OBJECTNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 210033

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MODULENAME` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 1 | `OBJECTNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `HASHSHA256` | VARCHAR(64) | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSWIZARDHASHUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MODULENAME,
       t.OBJECTNAME,
       t.HASHSHA256,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSWIZARDHASH t
FETCH FIRST 100 ROWS ONLY;
```
