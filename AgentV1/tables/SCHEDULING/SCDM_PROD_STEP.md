# DB2ADMIN.SCDM_PROD_STEP

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 66
- **Primary key**: `PD_IDENTIFIER`, `PD_PREQ_NO`, `PD_PSTEP_ID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186428

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PD_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `PD_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `PD_UPD_CODE` | INTEGER | NOT NULL |  |  |  |
| 4 | `PD_TO_SCHED` | CHAR(1) |  |  |  |  |
| 5 | `PD_PRV_STEP_SCHED_MQM` | SMALLINT |  |  |  |  |
| 6 | `PD_PRV_STEP_TRUE` | SMALLINT |  |  |  |  |
| 7 | `PD_NEX_STEP_SCHED_MQM` | SMALLINT |  |  |  |  |
| 8 | `PD_NEX_STEP_TRUE` | SMALLINT |  |  |  |  |
| 9 | `PD_STEP_TYP` | CHAR(1) |  |  |  |  |
| 10 | `PD_MAT_ARRV_DATE` | TIMESTAMP |  |  |  |  |
| 11 | `PD_FRC_MAT_DATE` | CHAR(1) |  |  |  |  |
| 12 | `PD_PLAN_START` | TIMESTAMP |  |  |  |  |
| 13 | `PD_LOW_LIMIT_TIME_STRT` | TIMESTAMP |  |  |  |  |
| 14 | `PD_FRC_LOW_DATE` | CHAR(1) |  |  |  |  |
| 15 | `PD_PLAN_END` | TIMESTAMP |  |  |  |  |
| 16 | `PD_HIGH_LIMIT_TIMEND` | TIMESTAMP |  |  |  |  |
| 17 | `PD_FRC_HIGH_DATE` | CHAR(1) |  |  |  |  |
| 18 | `PD_INI_PLAN_SCHED_DATE_TIME` | TIMESTAMP |  |  |  |  |
| 19 | `PD_FIN_PLAN_SCHED_DATE_TIME` | TIMESTAMP |  |  |  |  |
| 20 | `PD_WKCNTER` | VARCHAR(8) |  |  |  |  |
| 21 | `PD_WKCT_PROC` | VARCHAR(8) |  |  |  |  |
| 22 | `PD_INIT_QUENT` | DECIMAL(11,2) |  |  |  |  |
| 23 | `PD_FIN_QUENT` | DECIMAL(11,2) |  |  |  |  |
| 24 | `PD_WEIGHT` | INTEGER |  |  |  |  |
| 25 | `PD_DESC_UM` | VARCHAR(3) |  |  |  |  |
| 26 | `PD_CAL` | VARCHAR(3) |  |  |  |  |
| 27 | `PD_SETUP_TIME_STP` | DECIMAL(11,2) |  |  |  |  |
| 28 | `PD_EXC_TIME_STP` | DECIMAL(11,2) |  |  |  |  |
| 29 | `PD_RES_NUM_PLN` | DECIMAL(9,3) |  |  |  |  |
| 30 | `PD_ALLOW_SPLIT` | CHAR(1) |  |  |  |  |
| 31 | `PD_STEP_HANDLE_REPROCES` | CHAR(1) |  |  |  |  |
| 32 | `PD_STEP_PART_GEN_PLAN` | CHAR(1) |  |  |  |  |
| 33 | `PD_STEP_CAN_GROUP` | CHAR(1) |  |  |  |  |
| 34 | `PD_FORCED_GRP_NO` | INTEGER |  |  |  |  |
| 35 | `PD_CONN_TYPE_PREV_STEP_SPLIT` | CHAR(1) |  |  |  |  |
| 36 | `PD_FRC_OVERLAPP` | CHAR(1) |  |  |  |  |
| 37 | `PD_STEP_CLOSED` | CHAR(1) |  |  |  |  |
| 38 | `PD_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 39 | `PD_USR_TIMECG` | TIMESTAMP |  |  |  |  |
| 40 | `PD_SCHDULE_BY_MCM` | CHAR(1) |  |  |  |  |
| 41 | `PD_SCHDULE_BY_MQM` | CHAR(1) |  |  |  |  |
| 42 | `PD_SPLITED_FAMILY` | VARCHAR(12) |  |  |  |  |
| 43 | `PD_LEARNING_CURVE_CODE` | VARCHAR(6) |  |  |  |  |
| 44 | `PD_LEARNING_CURVE_TYPE` | CHAR(1) |  |  |  |  |
| 45 | `PD_APPROVAL_DATE` | TIMESTAMP |  |  |  |  |
| 46 | `PD_GRP_SEQUENCE` | VARCHAR(2) |  |  |  |  |
| 47 | `PD_PREV_LEAD_TIME_MQM` | DECIMAL(11,2) |  |  |  |  |
| 48 | `PD_NEXT_LEAD_TIME_MQM` | DECIMAL(11,2) |  |  |  |  |
| 49 | `PD_PREV_LEAD_TIME_BATCH_MQM` | DECIMAL(11,2) |  |  |  |  |
| 50 | `PD_NEXT_LEAD_TIME_BATCH_MQM` | DECIMAL(11,2) |  |  |  |  |
| 51 | `PD_BATCH_SIZE_PER_STEP` | CHAR(1) |  |  |  |  |
| 52 | `PD_MIN_BATCH_SIZE` | DECIMAL(11,2) |  |  |  |  |
| 53 | `PD_OPTIMUM_BATCH_SIZE` | DECIMAL(11,2) |  |  |  |  |
| 54 | `PD_MAX_BATCH_SIZE` | DECIMAL(11,2) |  |  |  |  |
| 55 | `PD_OVERLAP_WITH_OTHER_STEPS` | CHAR(1) |  |  |  |  |
| 56 | `PD_PRV_STEP_SCHED_MCM` | SMALLINT |  |  |  |  |
| 57 | `PD_NEX_STEP_SCHED_MCM` | SMALLINT |  |  |  |  |
| 58 | `PD_PREV_LEAD_TIME_MCM` | DECIMAL(11,2) |  |  |  |  |
| 59 | `PD_NEXT_LEAD_TIME_MCM` | DECIMAL(11,2) |  |  |  |  |
| 60 | `PD_PREV_LEAD_TIME_BATCH_MCM` | DECIMAL(11,2) |  |  |  |  |
| 61 | `PD_NEXT_LEAD_TIME_BATCH_MCM` | DECIMAL(11,2) |  |  |  |  |
| 62 | `PD_NUM_RSC_COMPONENTS` | SMALLINT |  |  |  |  |
| 63 | `PD_MAX_STARTDATE_AUTOSEQ` | TIMESTAMP |  |  |  |  |
| 64 | `PD_ALTERNATIVEQTY` | DECIMAL(11,2) |  |  |  |  |
| 65 | `PD_ALTERNATIVEUM` | VARCHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PD_IDENTIFIER,
       t.PD_PREQ_NO,
       t.PD_PSTEP_ID,
       t.PD_UPD_CODE,
       t.PD_TO_SCHED,
       t.PD_PRV_STEP_SCHED_MQM,
       t.PD_PRV_STEP_TRUE,
       t.PD_NEX_STEP_SCHED_MQM,
       t.PD_NEX_STEP_TRUE,
       t.PD_STEP_TYP,
       t.PD_MAT_ARRV_DATE,
       t.PD_FRC_MAT_DATE
FROM   DB2ADMIN.SCDM_PROD_STEP t
FETCH FIRST 100 ROWS ONLY;
```
