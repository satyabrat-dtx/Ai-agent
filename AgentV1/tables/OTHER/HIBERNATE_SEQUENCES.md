# DB2ADMIN.HIBERNATE_SEQUENCES

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `no_primary_key`
- **Columns**: 2
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 109270

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SEQUENCE_NAME` | VARCHAR(255) |  |  |  |  |
| 1 | `SEQUENCE_NEXT_HI_VALUE` | INTEGER |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.SEQUENCE_NAME,
       t.SEQUENCE_NEXT_HI_VALUE
FROM   DB2ADMIN.HIBERNATE_SEQUENCES t
FETCH FIRST 100 ROWS ONLY;
```
