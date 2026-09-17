# DB2ADMIN.SCDM_PROD_REQCONN

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `IC_IDENTIFIER`, `IC_PREQ_NO`, `IC_PREV_PREQ_NO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186223

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `IC_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `IC_PREV_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 3 | `IC_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 4 | `IC_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IC_IDENTIFIER,
       t.IC_PREQ_NO,
       t.IC_PREV_PREQ_NO,
       t.IC_USR_NAMECG,
       t.IC_USR_TIMECG
FROM   DB2ADMIN.SCDM_PROD_REQCONN t
FETCH FIRST 100 ROWS ONLY;
```
