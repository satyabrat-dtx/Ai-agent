# DB2ADMIN.SCDM_PROD_SCHED_PROGRESS_OVRD

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `SPO_IDENTIFIER`, `SPO_PREQ_NO`, `SPO_PSTEP_ID`, `SPO_PSUBST_ID`, `SPO_REPROC_NO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187156

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SPO_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `SPO_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `SPO_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `SPO_PSUBST_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `SPO_REPROC_NO` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `SPO_LAST_PROG_TYPE` | CHAR(1) |  |  |  |  |
| 6 | `SPO_RSC_CODE` | VARCHAR(8) |  |  |  |  |
| 7 | `SPO_PROGRESED_GROUP` | INTEGER |  |  |  |  |
| 8 | `SPO_PROGRSTART` | TIMESTAMP |  |  |  |  |
| 9 | `SPO_CURR_PRG_DATE` | TIMESTAMP |  |  |  |  |
| 10 | `SPO_PROGREND` | TIMESTAMP |  |  |  |  |
| 11 | `SPO_QTY` | DECIMAL(11,2) |  |  |  |  |
| 12 | `SPO_REMAIN_TIME` | DECIMAL(11,2) |  |  |  |  |
| 13 | `SPO_PROG_OVERRIDE_TYPE` | CHAR(1) |  |  |  |  |
| 14 | `SPO_START_QTY` | DECIMAL(11,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.SPO_IDENTIFIER,
       t.SPO_PREQ_NO,
       t.SPO_PSTEP_ID,
       t.SPO_PSUBST_ID,
       t.SPO_REPROC_NO,
       t.SPO_LAST_PROG_TYPE,
       t.SPO_RSC_CODE,
       t.SPO_PROGRESED_GROUP,
       t.SPO_PROGRSTART,
       t.SPO_CURR_PRG_DATE,
       t.SPO_PROGREND,
       t.SPO_QTY
FROM   DB2ADMIN.SCDM_PROD_SCHED_PROGRESS_OVRD t
FETCH FIRST 100 ROWS ONLY;
```
