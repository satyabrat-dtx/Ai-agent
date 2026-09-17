# DB2ADMIN.SCDM_PROD_SCHED

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 56
- **Primary key**: `PS_IDENTIFIER`, `PS_PREQ_NO`, `PS_PSTEP_ID`, `PS_PSUBST_ID`, `PS_REPROC_NO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186568

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PS_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PS_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `PS_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `PS_PSUBST_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `PS_REPROC_NO` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `PS_VERS_NO` | SMALLINT |  |  |  |  |
| 6 | `PS_UPD_CODE` | INTEGER |  |  |  |  |
| 7 | `PS_UPD_OP` | CHAR(1) |  |  |  |  |
| 8 | `PS_TYPE_PROD` | VARCHAR(3) |  |  |  |  |
| 9 | `PS_PROD_LINE` | VARCHAR(4) |  |  |  |  |
| 10 | `PS_PROD_UM` | VARCHAR(3) |  |  |  |  |
| 11 | `PS_STEP_TYP` | CHAR(1) |  |  |  |  |
| 12 | `PS_INIT_QUENT` | DECIMAL(11,2) |  |  |  |  |
| 13 | `PS_ST_GROUP` | INTEGER |  |  |  |  |
| 14 | `PS_STEP_IS_GRPED` | CHAR(1) |  |  |  |  |
| 15 | `PS_SCHED_TYPE` | CHAR(1) |  |  |  |  |
| 16 | `PS_WKCNTER` | VARCHAR(8) |  |  |  |  |
| 17 | `PS_WKCT_PROC` | VARCHAR(8) |  |  |  |  |
| 18 | `PS_ALTERNATIVE_CODE` | VARCHAR(6) |  |  |  |  |
| 19 | `PS_RSC_CODE` | VARCHAR(8) |  |  |  |  |
| 20 | `PS_PROD_SUBLIN_RSC` | SMALLINT |  |  |  |  |
| 21 | `PS_NUM_RSC_COMPONENTS` | SMALLINT |  |  |  |  |
| 22 | `PS_QTY` | DECIMAL(11,2) |  |  |  |  |
| 23 | `PS_SUP_BASE` | DECIMAL(11,2) |  |  |  |  |
| 24 | `PS_SUP_REAL` | DECIMAL(11,2) |  |  |  |  |
| 25 | `PS_SUP_OVERLAP` | DECIMAL(11,2) |  |  |  |  |
| 26 | `PS_EXE_MIN` | DECIMAL(11,2) |  |  |  |  |
| 27 | `PS_SCH_START` | TIMESTAMP |  |  |  |  |
| 28 | `PS_SCH_END` | TIMESTAMP |  |  |  |  |
| 29 | `PS_COMMENT` | VARCHAR(30) |  |  |  |  |
| 30 | `PS_FWD_SUBSTEP` | SMALLINT |  |  |  |  |
| 31 | `PS_FWD_REPROC_SUBSTEP` | SMALLINT |  |  |  |  |
| 32 | `PS_BKW_SUBSTEP` | SMALLINT |  |  |  |  |
| 33 | `PS_BKW_REPROC_SUBSTEP` | SMALLINT |  |  |  |  |
| 34 | `PS_SAVES_AT_LEAST_ONES_FINNAL` | CHAR(1) |  |  |  |  |
| 35 | `PS_NETTED_QUANTITY` | DECIMAL(11,2) |  |  |  |  |
| 36 | `PS_CHANGED_QUANTITY` | DECIMAL(11,2) |  |  |  |  |
| 37 | `PS_MACHINE_SETUP_CODE` | VARCHAR(10) |  |  |  |  |
| 38 | `PS_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 39 | `PS_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 40 | `PS_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 41 | `PS_USR_TIMECG` | TIMESTAMP |  |  |  |  |
| 42 | `PS_PROG_OVERRIDE_TYPE` | CHAR(1) |  |  |  |  |
| 43 | `PS_WKCNTER_KEY_ST` | VARCHAR(8) |  |  |  |  |
| 44 | `PS_WC_PROCESS_KEY_ST` | VARCHAR(8) |  |  |  |  |
| 45 | `PS_RES_KEY_ST` | VARCHAR(8) |  |  |  |  |
| 46 | `PS_RES_CAT_KEY_ST` | VARCHAR(3) |  |  |  |  |
| 47 | `PS_NEW_PREQ_UNIQ_ID` | VARCHAR(10) |  |  |  |  |
| 48 | `PS_SPLITED_FAMILY` | VARCHAR(12) |  |  |  |  |
| 49 | `PS_LEARNING_CURVE_CODE` | VARCHAR(6) |  |  |  |  |
| 50 | `PS_LEARNING_CURVE_CODE_OCC_OCC` | VARCHAR(6) |  |  |  |  |
| 51 | `PS_GRP_SEQUENCE` | VARCHAR(2) |  |  |  |  |
| 52 | `PS_LAST_SCHEDULE_CHANGED` | TIMESTAMP |  |  |  |  |
| 53 | `PS_ACTUAL_START` | TIMESTAMP |  |  |  |  |
| 54 | `PS_ACTUAL_END` | TIMESTAMP |  |  |  |  |
| 55 | `PS_MQM_ENV` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PS_IDENTIFIER,
       t.PS_PREQ_NO,
       t.PS_PSTEP_ID,
       t.PS_PSUBST_ID,
       t.PS_REPROC_NO,
       t.PS_VERS_NO,
       t.PS_UPD_CODE,
       t.PS_UPD_OP,
       t.PS_TYPE_PROD,
       t.PS_PROD_LINE,
       t.PS_PROD_UM,
       t.PS_STEP_TYP
FROM   DB2ADMIN.SCDM_PROD_SCHED t
FETCH FIRST 100 ROWS ONLY;
```
