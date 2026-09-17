# DB2ADMIN.SCDM_ARTICLE_TYPE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `AT_IDENTIFIER`, `AT_ART_TYPE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185705

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AT_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `AT_ART_TYPE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `AT_S_DESCR` | VARCHAR(28) |  |  |  |  |
| 3 | `AT_L_DESCR` | VARCHAR(60) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.AT_IDENTIFIER,
       t.AT_ART_TYPE,
       t.AT_S_DESCR,
       t.AT_L_DESCR
FROM   DB2ADMIN.SCDM_ARTICLE_TYPE t
FETCH FIRST 100 ROWS ONLY;
```
