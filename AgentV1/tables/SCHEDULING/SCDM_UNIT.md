# DB2ADMIN.SCDM_UNIT

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `UM_IDENTIFIER`, `UM_UM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187194

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UM_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `UM_UM` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `UM_S_DESCR` | VARCHAR(28) |  |  |  |  |
| 3 | `UM_L_DESCR` | VARCHAR(60) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.UM_IDENTIFIER,
       t.UM_UM,
       t.UM_S_DESCR,
       t.UM_L_DESCR
FROM   DB2ADMIN.SCDM_UNIT t
FETCH FIRST 100 ROWS ONLY;
```
