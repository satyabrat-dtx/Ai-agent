# DB2ADMIN.DATAACCESSERROR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `no_primary_key`
- **Columns**: 5
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 41

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TABLENAME` | CHAR(30) |  |  |  |  |
| 1 | `RECORDKEY` | VARCHAR(1000) |  |  |  |  |
| 2 | `STACKTRACE` | VARCHAR(10000) |  |  |  |  |
| 3 | `ERRORCODE` | CHAR(10) |  |  |  |  |
| 4 | `SQLSTATE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.TABLENAME,
       t.RECORDKEY,
       t.STACKTRACE,
       t.ERRORCODE,
       t.SQLSTATE
FROM   DB2ADMIN.DATAACCESSERROR t
FETCH FIRST 100 ROWS ONLY;
```
