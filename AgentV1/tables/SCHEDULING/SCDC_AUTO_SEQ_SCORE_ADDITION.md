# DB2ADMIN.SCDC_AUTO_SEQ_SCORE_ADDITION

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `AU_IDENTIFIER`, `AU_WKST_CODE`, `AU_CFGNAME`, `AU_SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189644

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AU_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `AU_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `AU_CFGNAME` | VARCHAR(14) | NOT NULL | PK | primary_key |  |
| 3 | `AU_SEQUENCE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `AU_FROM_JOB_TO_PRIOR_JOB_CASE` | SMALLINT |  |  |  |  |
| 5 | `AU_TO_JOB_TO_PRIOR_JOB_CASE` | SMALLINT |  |  |  |  |
| 6 | `AU_FROM_JOB_TO_FOLLOW_JOB_CASE` | SMALLINT |  |  |  |  |
| 7 | `AU_TO_JOB_TO_FOLLOW_JOB_CASE` | SMALLINT |  |  |  |  |
| 8 | `AU_FROM_JOB_TO_RESOURCE_CASE` | SMALLINT |  |  |  |  |
| 9 | `AU_TO_JOB_TO_RESOURCE_CASE` | SMALLINT |  |  |  |  |
| 10 | `AU_FROM_NUMBER_OF_DAYS_DELAY` | SMALLINT |  |  |  |  |
| 11 | `AU_TO_NUMBER_OF_DAYS_DELAY` | SMALLINT |  |  |  |  |
| 12 | `AU_FROM_NUMBER_OF_DAYS_EARLY` | SMALLINT |  |  |  |  |
| 13 | `AU_TO_NUMBER_OF_DAYS_EARLY` | SMALLINT |  |  |  |  |
| 14 | `AU_FROM_NUMBER_MINTS_SETUP_ADD` | SMALLINT |  |  |  |  |
| 15 | `AU_TO_NUMBER_MINTS_SETUP_ADD` | SMALLINT |  |  |  |  |
| 16 | `AU_ADD_TO_SCORE` | SMALLINT |  |  |  |  |
| 17 | `AU_DOUBLE_DIRECTION` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.AU_IDENTIFIER,
       t.AU_WKST_CODE,
       t.AU_CFGNAME,
       t.AU_SEQUENCE,
       t.AU_FROM_JOB_TO_PRIOR_JOB_CASE,
       t.AU_TO_JOB_TO_PRIOR_JOB_CASE,
       t.AU_FROM_JOB_TO_FOLLOW_JOB_CASE,
       t.AU_TO_JOB_TO_FOLLOW_JOB_CASE,
       t.AU_FROM_JOB_TO_RESOURCE_CASE,
       t.AU_TO_JOB_TO_RESOURCE_CASE,
       t.AU_FROM_NUMBER_OF_DAYS_DELAY,
       t.AU_TO_NUMBER_OF_DAYS_DELAY
FROM   DB2ADMIN.SCDC_AUTO_SEQ_SCORE_ADDITION t
FETCH FIRST 100 ROWS ONLY;
```
