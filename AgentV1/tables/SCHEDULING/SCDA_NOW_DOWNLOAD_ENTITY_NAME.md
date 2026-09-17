# DB2ADMIN.SCDA_NOW_DOWNLOAD_ENTITY_NAME

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `ND_IDENTIFIER`, `ND_ENTITY_NAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185445

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ND_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `ND_ENTITY_NAME` | VARCHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `ND_DATE` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ND_IDENTIFIER,
       t.ND_ENTITY_NAME,
       t.ND_DATE
FROM   DB2ADMIN.SCDA_NOW_DOWNLOAD_ENTITY_NAME t
FETCH FIRST 100 ROWS ONLY;
```
