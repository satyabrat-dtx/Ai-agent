# DB2ADMIN.SCDM_GENERATE_NUM

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `GN_IDENTIFIER`, `GN_GENCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185601

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `GN_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `GN_GENCODE` | VARCHAR(12) | NOT NULL | PK | primary_key |  |
| 2 | `GN_GENNUMBER` | INTEGER |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.GN_IDENTIFIER,
       t.GN_GENCODE,
       t.GN_GENNUMBER
FROM   DB2ADMIN.SCDM_GENERATE_NUM t
FETCH FIRST 100 ROWS ONLY;
```
