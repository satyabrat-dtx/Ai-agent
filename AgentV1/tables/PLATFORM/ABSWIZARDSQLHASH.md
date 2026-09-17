# DB2ADMIN.ABSWIZARDSQLHASH

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `HASHSHA256`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 205823

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `HASHSHA256` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `SQLSTATEMENT` | CLOB(1000000) | NOT NULL |  |  |  |
| 2 | `MODULENAME` | CHAR(20) |  |  |  |  |
| 3 | `MODULEVERSION` | CHAR(50) |  |  |  |  |
| 4 | `EXECUTIONDATE` | DATE |  |  |  |  |
| 5 | `EXECUTEDBY` | VARCHAR(100) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSWIZARDSQLHASHUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.HASHSHA256,
       t.SQLSTATEMENT,
       t.MODULENAME,
       t.MODULEVERSION,
       t.EXECUTIONDATE,
       t.EXECUTEDBY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSWIZARDSQLHASH t
FETCH FIRST 100 ROWS ONLY;
```
