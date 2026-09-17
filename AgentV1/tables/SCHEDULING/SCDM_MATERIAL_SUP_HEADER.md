# DB2ADMIN.SCDM_MATERIAL_SUP_HEADER

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `MH_IDENTIFIER`, `MH_WKCNTER`, `MH_WKCT_PROC`, `MH_RES_CAT_CODE`, `MH_RSC_CODE`, `MH_TYPE_PROD`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187725

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MH_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `MH_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `MH_WKCT_PROC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `MH_RES_CAT_CODE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `MH_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `MH_TYPE_PROD` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `MH_WAIT_PREV_QTY` | CHAR(1) |  |  |  |  |
| 7 | `MH_MIN_QTY_PASS_NXT` | DECIMAL(11,2) |  |  |  |  |
| 8 | `MH_MIN_QTY_PREV_STP` | DECIMAL(11,2) |  |  |  |  |
| 9 | `MH_MIN_DEL_WAIT_DAYS` | SMALLINT |  |  |  |  |
| 10 | `MH_MIN_DEL_WAIT_HRS` | SMALLINT |  |  |  |  |
| 11 | `MH_MIN_DEL_WAIT_MIN` | SMALLINT |  |  |  |  |
| 12 | `MH_MAX_DEL_WAIT_DAYS` | SMALLINT |  |  |  |  |
| 13 | `MH_MAX_DEL_WAIT_HRS` | SMALLINT |  |  |  |  |
| 14 | `MH_MAX_DEL_WAIT_MIN` | SMALLINT |  |  |  |  |
| 15 | `MH_PART_DEL` | CHAR(1) |  |  |  |  |
| 16 | `MH_UPD_BAL_HRS` | SMALLINT |  |  |  |  |
| 17 | `MH_UPD_BAL_QTY` | DECIMAL(11,2) |  |  |  |  |
| 18 | `MH_UPD_REQ_PREV_STP_HRS` | SMALLINT |  |  |  |  |
| 19 | `MH_MODULERULE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.MH_IDENTIFIER,
       t.MH_WKCNTER,
       t.MH_WKCT_PROC,
       t.MH_RES_CAT_CODE,
       t.MH_RSC_CODE,
       t.MH_TYPE_PROD,
       t.MH_WAIT_PREV_QTY,
       t.MH_MIN_QTY_PASS_NXT,
       t.MH_MIN_QTY_PREV_STP,
       t.MH_MIN_DEL_WAIT_DAYS,
       t.MH_MIN_DEL_WAIT_HRS,
       t.MH_MIN_DEL_WAIT_MIN
FROM   DB2ADMIN.SCDM_MATERIAL_SUP_HEADER t
FETCH FIRST 100 ROWS ONLY;
```
