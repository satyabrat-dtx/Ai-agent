# DB2ADMIN.SCDM_RES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `RS_IDENTIFIER`, `RS_RSC_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186833

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RS_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `RS_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `RS_S_DESCR` | VARCHAR(28) |  |  |  |  |
| 3 | `RS_L_DESCR` | VARCHAR(60) |  |  |  |  |
| 4 | `RS_PROCES_TYPE` | CHAR(1) |  |  |  |  |
| 5 | `RS_WKCNTER` | VARCHAR(8) |  |  |  |  |
| 6 | `RS_RES_CATEGORY` | VARCHAR(3) |  |  |  |  |
| 7 | `RS_STANDRD_BCH_SIZE` | DECIMAL(7,2) |  |  |  |  |
| 8 | `RS_BCH_UM` | VARCHAR(3) |  |  |  |  |
| 9 | `RS_CAL` | VARCHAR(3) |  |  |  |  |
| 10 | `RS_RSC_TYPE` | CHAR(1) |  |  |  |  |
| 11 | `RS_NUM_RSC_COMP` | DECIMAL(5,0) |  |  |  |  |
| 12 | `RS_MIN_BCH_SIZE` | DECIMAL(7,2) |  |  |  |  |
| 13 | `RS_MAX_BCH_SIZE` | DECIMAL(7,2) |  |  |  |  |
| 14 | `RS_TEXT1` | VARCHAR(12) |  |  |  |  |
| 15 | `RS_TEXT2` | VARCHAR(12) |  |  |  |  |
| 16 | `RS_ONE_BATCH_MACHINE_GRP_CODE` | VARCHAR(12) |  |  |  |  |
| 17 | `RS_RSC_PLAN_TYPE` | CHAR(1) |  |  |  |  |
| 18 | `RS_ONE_BATCH_MACHINE_GRP_TYPE` | CHAR(1) |  |  |  |  |
| 19 | `RS_LINE_WITHIN_PLANT` | VARCHAR(3) |  |  |  |  |
| 20 | `RS_OPTIMUMMAXMULTIPLIER` | VARCHAR(5) |  |  |  |  |
| 21 | `RS_FORCE_OUTSIDE_LIMIT_QTY` | CHAR(1) |  |  |  |  |
| 22 | `RS_FORCE_OCC_TO_RES_CASE_99` | CHAR(1) |  |  |  |  |
| 23 | `RS_MINMULTIPLIER` | VARCHAR(5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.RS_IDENTIFIER,
       t.RS_RSC_CODE,
       t.RS_S_DESCR,
       t.RS_L_DESCR,
       t.RS_PROCES_TYPE,
       t.RS_WKCNTER,
       t.RS_RES_CATEGORY,
       t.RS_STANDRD_BCH_SIZE,
       t.RS_BCH_UM,
       t.RS_CAL,
       t.RS_RSC_TYPE,
       t.RS_NUM_RSC_COMP
FROM   DB2ADMIN.SCDM_RES t
FETCH FIRST 100 ROWS ONLY;
```
