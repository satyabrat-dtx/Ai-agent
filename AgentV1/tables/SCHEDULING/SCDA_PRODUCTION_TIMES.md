# DB2ADMIN.SCDA_PRODUCTION_TIMES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `IDENTIFIER`, `INDEX_FLD`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185068

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `INDEX_FLD` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `WORK_CENTER` | VARCHAR(8) |  |  |  |  |
| 3 | `OPERATION` | VARCHAR(8) |  |  |  |  |
| 4 | `PRODUCT_TYPE` | VARCHAR(3) |  |  |  |  |
| 5 | `TBLNAME1_COL_NAME1_VAL` | VARCHAR(30) |  |  |  |  |
| 6 | `TBLNAME1_COL_NAME2_VAL` | VARCHAR(30) |  |  |  |  |
| 7 | `TBLNAME1_COL_NAME3_VAL` | VARCHAR(30) |  |  |  |  |
| 8 | `TBLNAME1_COL_NAME4_VAL` | VARCHAR(30) |  |  |  |  |
| 9 | `TBLNAME1_COL_NAME5_VAL` | VARCHAR(30) |  |  |  |  |
| 10 | `TBLNAME1_COL_NAME6_VAL` | VARCHAR(30) |  |  |  |  |
| 11 | `TBLNAME1_COL_NAME7_VAL` | VARCHAR(30) |  |  |  |  |
| 12 | `TBLNAME1_COL_NAME8_VAL` | VARCHAR(30) |  |  |  |  |
| 13 | `TBLNAME1_COL_NAME9_VAL` | VARCHAR(30) |  |  |  |  |
| 14 | `TBLNAME1_COL_NAME10_VAL` | VARCHAR(30) |  |  |  |  |
| 15 | `RES_CATEGORY` | VARCHAR(3) |  |  |  |  |
| 16 | `RES` | VARCHAR(8) |  |  |  |  |
| 17 | `SETUP_TIME` | DECIMAL(9,2) |  |  |  |  |
| 18 | `BATCH_TIME` | DECIMAL(12,5) |  |  |  |  |
| 19 | `CONTINUOUS_TIME` | DECIMAL(12,5) |  |  |  |  |
| 20 | `CONTINUOUS_OPERATION_UM` | VARCHAR(3) |  |  |  |  |
| 21 | `CONSIDER_STEP_EFFICIENCY` | CHAR(1) |  |  |  |  |
| 22 | `CODE` | VARCHAR(20) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 23 | `SETUP_TIME_MULTIPLIER` | DECIMAL(14,4) |  |  |  |  |
| 24 | `OPERATION_TIME_MULTIPLIER` | DECIMAL(14,4) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.INDEX_FLD,
       t.WORK_CENTER,
       t.OPERATION,
       t.PRODUCT_TYPE,
       t.TBLNAME1_COL_NAME1_VAL,
       t.TBLNAME1_COL_NAME2_VAL,
       t.TBLNAME1_COL_NAME3_VAL,
       t.TBLNAME1_COL_NAME4_VAL,
       t.TBLNAME1_COL_NAME5_VAL,
       t.TBLNAME1_COL_NAME6_VAL,
       t.TBLNAME1_COL_NAME7_VAL
FROM   DB2ADMIN.SCDA_PRODUCTION_TIMES t
FETCH FIRST 100 ROWS ONLY;
```
