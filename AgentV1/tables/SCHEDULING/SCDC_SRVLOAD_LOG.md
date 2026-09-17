# DB2ADMIN.SCDC_SRVLOAD_LOG

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `no_primary_key`
- **Columns**: 4
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188786

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SLO_IDENTIFIER` | SMALLINT |  |  |  |  |
| 1 | `SLO_CURRDTTIME` | TIMESTAMP |  |  |  |  |
| 2 | `SLO_OPERATION` | VARCHAR(14) |  |  |  |  |
| 3 | `SLO_TEXT` | VARCHAR(250) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.SLO_IDENTIFIER,
       t.SLO_CURRDTTIME,
       t.SLO_OPERATION,
       t.SLO_TEXT
FROM   DB2ADMIN.SCDC_SRVLOAD_LOG t
FETCH FIRST 100 ROWS ONLY;
```
