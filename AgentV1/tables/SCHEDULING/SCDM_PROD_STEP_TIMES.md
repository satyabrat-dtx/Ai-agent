# DB2ADMIN.SCDM_PROD_STEP_TIMES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `ST_IDENTIFIER`, `ST_PREQ_NO`, `ST_PSTEP_ID`, `ST_WKCNTER`, `ST_WKCT_PROC`, `ST_RES_CATEGORY`, `ST_RSC_CODE`, `ST_MACHINE_SETUP_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187074

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ST_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `ST_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `ST_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `ST_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `ST_WKCT_PROC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `ST_RES_CATEGORY` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `ST_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 7 | `ST_MACHINE_SETUP_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `ST_SETUP_TIME_JOB` | DECIMAL(11,3) |  |  |  |  |
| 9 | `ST_EXC_TIME_INIT_QTY` | DECIMAL(11,3) |  |  |  |  |
| 10 | `ST_CAPUSED` | DECIMAL(11,3) |  |  |  |  |
| 11 | `ST_CONFLEV` | INTEGER |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ST_IDENTIFIER,
       t.ST_PREQ_NO,
       t.ST_PSTEP_ID,
       t.ST_WKCNTER,
       t.ST_WKCT_PROC,
       t.ST_RES_CATEGORY,
       t.ST_RSC_CODE,
       t.ST_MACHINE_SETUP_CODE,
       t.ST_SETUP_TIME_JOB,
       t.ST_EXC_TIME_INIT_QTY,
       t.ST_CAPUSED,
       t.ST_CONFLEV
FROM   DB2ADMIN.SCDM_PROD_STEP_TIMES t
FETCH FIRST 100 ROWS ONLY;
```
