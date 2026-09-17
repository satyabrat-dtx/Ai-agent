# DB2ADMIN.SCDM_EXT_CONNECTION

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `EC_IDENTIFIER`, `EC_PREQ_NO`, `EC_CONNE_KEY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186105

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `EC_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `EC_CONNE_KEY` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 3 | `EC_NUM_LEVELS` | SMALLINT |  |  |  |  |
| 4 | `EC_CONN_CERTENT_LEVEL` | CHAR(1) |  |  |  |  |
| 5 | `EC_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 6 | `EC_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.EC_IDENTIFIER,
       t.EC_PREQ_NO,
       t.EC_CONNE_KEY,
       t.EC_NUM_LEVELS,
       t.EC_CONN_CERTENT_LEVEL,
       t.EC_USR_NAMECG,
       t.EC_USR_TIMECG
FROM   DB2ADMIN.SCDM_EXT_CONNECTION t
FETCH FIRST 100 ROWS ONLY;
```
