# DB2ADMIN.DATAACCESSRECOVERY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 2
- **Primary key**: `SERNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 60

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SERNAME` | VARCHAR(400) | NOT NULL | PK | primary_key |  |
| 1 | `STATUS` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.SERNAME,
       t.STATUS
FROM   DB2ADMIN.DATAACCESSRECOVERY t
FETCH FIRST 100 ROWS ONLY;
```
