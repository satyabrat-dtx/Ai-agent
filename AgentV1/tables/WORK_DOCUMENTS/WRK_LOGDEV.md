# DB2ADMIN.WRK_LOGDEV

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `no_primary_key`
- **Columns**: 7
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181789

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT |  |  | audit |  |
| 1 | `LINENO` | DECIMAL(10,0) |  |  |  |  |
| 2 | `LOGITEM` | VARCHAR(2000) |  |  |  |  |
| 3 | `INTEGERVALUE` | DECIMAL(10,0) |  |  |  |  |
| 4 | `DECIMALVALUE` | DECIMAL(15,5) |  |  |  |  |
| 5 | `STRINGVALUE` | VARCHAR(2000) |  |  |  |  |
| 6 | `DATEVALUE` | DATE |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.LOGITEM,
       t.INTEGERVALUE,
       t.DECIMALVALUE,
       t.STRINGVALUE,
       t.DATEVALUE
FROM   DB2ADMIN.WRK_LOGDEV t
FETCH FIRST 100 ROWS ONLY;
```
