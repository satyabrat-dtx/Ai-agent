# DB2ADMIN.SCDM_PROD_SCHED_MCM

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 56
- **Primary key**: `MS_IDENTIFIER`, `MS_PREQ_NO`, `MS_PSTEP_ID`, `MS_PSUBST_ID`, `MS_REPROC_NO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186647

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MS_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `MS_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `MS_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `MS_PSUBST_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `MS_REPROC_NO` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `MS_VERS_NO` | SMALLINT |  |  |  |  |
| 6 | `MS_UPD_CODE` | INTEGER |  |  |  |  |
| 7 | `MS_UPD_OP` | CHAR(1) |  |  |  |  |
| 8 | `MS_TYPE_PROD` | VARCHAR(3) |  |  |  |  |
| 9 | `MS_PROD_LINE` | VARCHAR(4) |  |  |  |  |
| 10 | `MS_PROD_UM` | VARCHAR(3) |  |  |  |  |
| 11 | `MS_STEP_TYP` | CHAR(1) |  |  |  |  |
| 12 | `MS_INIT_QUENT` | DECIMAL(11,2) |  |  |  |  |
| 13 | `MS_ST_GROUP` | INTEGER |  |  |  |  |
| 14 | `MS_STEP_IS_GRPED` | CHAR(1) |  |  |  |  |
| 15 | `MS_SCHED_TYPE` | CHAR(1) |  |  |  |  |
| 16 | `MS_WKCNTER` | VARCHAR(8) |  |  |  |  |
| 17 | `MS_WKCT_PROC` | VARCHAR(8) |  |  |  |  |
| 18 | `MS_ALTERNATIVE_CODE` | VARCHAR(6) |  |  |  |  |
| 19 | `MS_RSC_CODE` | VARCHAR(8) |  |  |  |  |
| 20 | `MS_PROD_SUBLIN_RSC` | SMALLINT |  |  |  |  |
| 21 | `MS_NUM_RSC_COMPONENTS` | SMALLINT |  |  |  |  |
| 22 | `MS_QTY` | DECIMAL(11,2) |  |  |  |  |
| 23 | `MS_SUP_BASE` | DECIMAL(11,2) |  |  |  |  |
| 24 | `MS_SUP_REAL` | DECIMAL(11,2) |  |  |  |  |
| 25 | `MS_SUP_OVERLAP` | DECIMAL(11,2) |  |  |  |  |
| 26 | `MS_EXE_MIN` | DECIMAL(11,2) |  |  |  |  |
| 27 | `MS_SCH_START` | TIMESTAMP |  |  |  |  |
| 28 | `MS_SCH_END` | TIMESTAMP |  |  |  |  |
| 29 | `MS_COMMENT` | VARCHAR(30) |  |  |  |  |
| 30 | `MS_FWD_SUBSTEP` | SMALLINT |  |  |  |  |
| 31 | `MS_FWD_REPROC_SUBSTEP` | SMALLINT |  |  |  |  |
| 32 | `MS_BKW_SUBSTEP` | SMALLINT |  |  |  |  |
| 33 | `MS_BKW_REPROC_SUBSTEP` | SMALLINT |  |  |  |  |
| 34 | `MS_SAVES_AT_LEAST_ONES_FINNAL` | CHAR(1) |  |  |  |  |
| 35 | `MS_NETTED_QUANTITY` | DECIMAL(11,2) |  |  |  |  |
| 36 | `MS_CHANGED_QUANTITY` | DECIMAL(11,2) |  |  |  |  |
| 37 | `MS_MACHINE_SETUP_CODE` | VARCHAR(10) |  |  |  |  |
| 38 | `MS_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 39 | `MS_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 40 | `MS_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 41 | `MS_USR_TIMECG` | TIMESTAMP |  |  |  |  |
| 42 | `MS_PROG_OVERRIDE_TYPE` | CHAR(1) |  |  |  |  |
| 43 | `MS_WKCNTER_KEY_ST` | VARCHAR(8) |  |  |  |  |
| 44 | `MS_WC_PROCESS_KEY_ST` | VARCHAR(8) |  |  |  |  |
| 45 | `MS_RES_KEY_ST` | VARCHAR(8) |  |  |  |  |
| 46 | `MS_RES_CAT_KEY_ST` | VARCHAR(3) |  |  |  |  |
| 47 | `MS_NEW_PREQ_UNIQ_ID` | VARCHAR(10) |  |  |  |  |
| 48 | `MS_SPLITED_FAMILY` | VARCHAR(12) |  |  |  |  |
| 49 | `MS_LEARNING_CURVE_CODE` | VARCHAR(6) |  |  |  |  |
| 50 | `MS_LEARNING_CURVE_CODE_OCC_OCC` | VARCHAR(6) |  |  |  |  |
| 51 | `MS_GRP_SEQUENCE` | VARCHAR(2) |  |  |  |  |
| 52 | `MS_LAST_SCHEDULE_CHANGED` | TIMESTAMP |  |  |  |  |
| 53 | `MS_ACTUAL_START` | TIMESTAMP |  |  |  |  |
| 54 | `MS_ACTUAL_END` | TIMESTAMP |  |  |  |  |
| 55 | `MS_MQM_ENV` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.MS_IDENTIFIER,
       t.MS_PREQ_NO,
       t.MS_PSTEP_ID,
       t.MS_PSUBST_ID,
       t.MS_REPROC_NO,
       t.MS_VERS_NO,
       t.MS_UPD_CODE,
       t.MS_UPD_OP,
       t.MS_TYPE_PROD,
       t.MS_PROD_LINE,
       t.MS_PROD_UM,
       t.MS_STEP_TYP
FROM   DB2ADMIN.SCDM_PROD_SCHED_MCM t
FETCH FIRST 100 ROWS ONLY;
```
