# DB2ADMIN.SCDM_PROD_REQ

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `PR_IDENTIFIER`, `PR_PREQ_NO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186398

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PR_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PR_DIV_CODE` | VARCHAR(3) |  |  |  |  |
| 2 | `PR_DSP_CODE` | VARCHAR(6) |  |  |  |  |
| 3 | `PR_BCH_CODE` | VARCHAR(2) |  |  |  |  |
| 4 | `PR_REPROC_NO` | SMALLINT |  |  |  |  |
| 5 | `PR_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 6 | `PR_HISTORICAL_REQ` | CHAR(1) |  |  |  |  |
| 7 | `PR_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 8 | `PR_USR_TIMECG` | TIMESTAMP |  |  |  |  |
| 9 | `PR_MODULEHANDLE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PR_IDENTIFIER,
       t.PR_DIV_CODE,
       t.PR_DSP_CODE,
       t.PR_BCH_CODE,
       t.PR_REPROC_NO,
       t.PR_PREQ_NO,
       t.PR_HISTORICAL_REQ,
       t.PR_USR_NAMECG,
       t.PR_USR_TIMECG,
       t.PR_MODULEHANDLE
FROM   DB2ADMIN.SCDM_PROD_REQ t
FETCH FIRST 100 ROWS ONLY;
```
