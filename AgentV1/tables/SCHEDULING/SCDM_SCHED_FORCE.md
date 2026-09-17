# DB2ADMIN.SCDM_SCHED_FORCE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 35
- **Primary key**: `FS_IDENTIFIER`, `FS_PREQ_NO`, `FS_PSTEP_ID`, `FS_PSUBST_ID`, `FS_REPROC_NO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186133

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FS_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `FS_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `FS_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `FS_PSUBST_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `FS_REPROC_NO` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `FS_UPD_CODE` | INTEGER | NOT NULL |  |  |  |
| 6 | `FS_TYPE_PROD` | VARCHAR(3) |  |  |  |  |
| 7 | `FS_PROD_LINE` | VARCHAR(4) |  |  |  |  |
| 8 | `FS_PROD_UM` | VARCHAR(3) |  |  |  |  |
| 9 | `FS_STEP_TYP` | CHAR(1) |  |  |  |  |
| 10 | `FS_INIT_QUENT` | DECIMAL(11,2) |  |  |  |  |
| 11 | `FS_ST_GROUP` | INTEGER |  |  |  |  |
| 12 | `FS_STEP_IS_GRPED` | CHAR(1) |  |  |  |  |
| 13 | `FS_SCHED_TYPE` | CHAR(1) |  |  |  |  |
| 14 | `FS_WKCNTER` | VARCHAR(8) |  |  |  |  |
| 15 | `FS_WKCT_PROC` | VARCHAR(8) |  |  |  |  |
| 16 | `FS_RSC_CODE` | VARCHAR(8) |  |  |  |  |
| 17 | `FS_PROD_SUBLIN_RSC` | SMALLINT |  |  |  |  |
| 18 | `FS_NUM_RSC_COMPONENTS` | SMALLINT |  |  |  |  |
| 19 | `FS_QTY` | DECIMAL(11,2) |  |  |  |  |
| 20 | `FS_SETUP_MIN` | DECIMAL(11,2) |  |  |  |  |
| 21 | `FS_EXE_MIN` | DECIMAL(11,2) |  |  |  |  |
| 22 | `FS_SCH_START` | TIMESTAMP |  |  |  |  |
| 23 | `FS_SCH_END` | TIMESTAMP |  |  |  |  |
| 24 | `FS_COMMENT` | VARCHAR(30) |  |  |  |  |
| 25 | `FS_FWD_SUBSTEP` | SMALLINT |  |  |  |  |
| 26 | `FS_FWD_REPROC_SUBSTEP` | SMALLINT |  |  |  |  |
| 27 | `FS_BKW_SUBSTEP` | SMALLINT |  |  |  |  |
| 28 | `FS_BKW_REPROC_SUBSTEP` | SMALLINT |  |  |  |  |
| 29 | `FS_SAVES_AT_LEAST_ONES_FINNAL` | CHAR(1) |  |  |  |  |
| 30 | `FS_TIME_DESCR` | VARCHAR(50) |  |  |  |  |
| 31 | `FS_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 32 | `FS_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 33 | `FS_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 34 | `FS_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.FS_IDENTIFIER,
       t.FS_PREQ_NO,
       t.FS_PSTEP_ID,
       t.FS_PSUBST_ID,
       t.FS_REPROC_NO,
       t.FS_UPD_CODE,
       t.FS_TYPE_PROD,
       t.FS_PROD_LINE,
       t.FS_PROD_UM,
       t.FS_STEP_TYP,
       t.FS_INIT_QUENT,
       t.FS_ST_GROUP
FROM   DB2ADMIN.SCDM_SCHED_FORCE t
FETCH FIRST 100 ROWS ONLY;
```
