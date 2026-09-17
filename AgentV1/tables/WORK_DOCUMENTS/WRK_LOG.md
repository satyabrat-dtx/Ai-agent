# DB2ADMIN.WRK_LOG

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `no_primary_key`
- **Columns**: 5
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181770

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT |  |  | audit |  |
| 1 | `SERIALNO` | DECIMAL(3,0) |  |  |  |  |
| 2 | `LOGITEM` | VARCHAR(2000) |  |  |  |  |
| 3 | `LOGVALUE1` | VARCHAR(2000) |  |  |  |  |
| 4 | `LOGVALUE2` | VARCHAR(2000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.SERIALNO,
       t.LOGITEM,
       t.LOGVALUE1,
       t.LOGVALUE2
FROM   DB2ADMIN.WRK_LOG t
FETCH FIRST 100 ROWS ONLY;
```
