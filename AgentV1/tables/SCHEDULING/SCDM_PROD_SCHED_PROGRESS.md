# DB2ADMIN.SCDM_PROD_SCHED_PROGRESS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `SP_IDENTIFIER`, `SP_PREQ_NO`, `SP_PSTEP_ID`, `SP_PSUBST_ID`, `SP_REPROC_NO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187112

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SP_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `SP_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `SP_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `SP_PSUBST_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `SP_REPROC_NO` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `SP_LAST_PROG_TYPE` | CHAR(1) |  |  |  |  |
| 6 | `SP_RSC_CODE` | VARCHAR(8) |  |  |  |  |
| 7 | `SP_PROGRESED_GROUP` | INTEGER |  |  |  |  |
| 8 | `SP_PROGRSTART` | TIMESTAMP |  |  |  |  |
| 9 | `SP_CURR_PRG_DATE` | TIMESTAMP |  |  |  |  |
| 10 | `SP_PROGREND` | TIMESTAMP |  |  |  |  |
| 11 | `SP_QTY` | DECIMAL(11,2) |  |  |  |  |
| 12 | `SP_REMAIN_TIME` | DECIMAL(11,2) |  |  |  |  |
| 13 | `SP_LAST_PROG_TYPE_HOST` | CHAR(1) |  |  |  |  |
| 14 | `SP_RSC_CODE_HOST` | VARCHAR(8) |  |  |  |  |
| 15 | `SP_PROGRSTART_HOST` | TIMESTAMP |  |  |  |  |
| 16 | `SP_CURR_PRG_DATE_HOST` | TIMESTAMP |  |  |  |  |
| 17 | `SP_PROGREND_HOST` | TIMESTAMP |  |  |  |  |
| 18 | `SP_QTY_HOST` | DECIMAL(11,2) |  |  |  |  |
| 19 | `SP_REMAIN_TIME_HOST` | DECIMAL(11,2) |  |  |  |  |
| 20 | `SP_START_QTY` | DECIMAL(11,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.SP_IDENTIFIER,
       t.SP_PREQ_NO,
       t.SP_PSTEP_ID,
       t.SP_PSUBST_ID,
       t.SP_REPROC_NO,
       t.SP_LAST_PROG_TYPE,
       t.SP_RSC_CODE,
       t.SP_PROGRESED_GROUP,
       t.SP_PROGRSTART,
       t.SP_CURR_PRG_DATE,
       t.SP_PROGREND,
       t.SP_QTY
FROM   DB2ADMIN.SCDM_PROD_SCHED_PROGRESS t
FETCH FIRST 100 ROWS ONLY;
```
