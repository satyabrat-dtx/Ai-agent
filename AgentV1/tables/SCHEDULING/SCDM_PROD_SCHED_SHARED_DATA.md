# DB2ADMIN.SCDM_PROD_SCHED_SHARED_DATA

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `PSD_IDENTIFIER`, `PSD_PREQ_NO`, `PSD_PSTEP_ID`, `PSD_PSUBST_ID`, `PSD_REPROC_NO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186726

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PSD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PSD_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `PSD_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `PSD_PSUBST_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `PSD_REPROC_NO` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `PSD_COMMENT` | VARCHAR(30) |  |  |  |  |
| 6 | `PSD_UPD_CODE` | INTEGER |  |  |  |  |
| 7 | `PSD_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 8 | `PSD_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 9 | `PSD_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 10 | `PSD_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PSD_IDENTIFIER,
       t.PSD_PREQ_NO,
       t.PSD_PSTEP_ID,
       t.PSD_PSUBST_ID,
       t.PSD_REPROC_NO,
       t.PSD_COMMENT,
       t.PSD_UPD_CODE,
       t.PSD_USR_NAMECR,
       t.PSD_USR_TIMECR,
       t.PSD_USR_NAMECG,
       t.PSD_USR_TIMECG
FROM   DB2ADMIN.SCDM_PROD_SCHED_SHARED_DATA t
FETCH FIRST 100 ROWS ONLY;
```
