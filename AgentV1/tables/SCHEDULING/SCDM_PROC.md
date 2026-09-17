# DB2ADMIN.SCDM_PROC

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `PR_IDENTIFIER`, `PR_WKCT_PROC`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187471

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PR_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PR_WKCT_PROC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `PR_S_DESCR` | VARCHAR(28) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PR_IDENTIFIER,
       t.PR_WKCT_PROC,
       t.PR_S_DESCR
FROM   DB2ADMIN.SCDM_PROC t
FETCH FIRST 100 ROWS ONLY;
```
