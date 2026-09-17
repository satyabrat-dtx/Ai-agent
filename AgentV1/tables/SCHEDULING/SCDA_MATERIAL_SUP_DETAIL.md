# DB2ADMIN.SCDA_MATERIAL_SUP_DETAIL

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `MD_IDENTIFIER`, `MD_WKCNTER`, `MD_WKCT_PROC`, `MD_RES_CAT_CODE`, `MD_RSC_CODE`, `MD_TYPE_PROD`, `MD_ISSUE_TRANS_MAT`, `MD_MAT_PROD_TYPE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184713

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `MD_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `MD_WKCT_PROC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `MD_RES_CAT_CODE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `MD_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `MD_TYPE_PROD` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `MD_SEARCH_BALANCE` | CHAR(1) |  |  |  |  |
| 7 | `MD_WAIT_ENTIRE_MAT` | CHAR(1) |  |  |  |  |
| 8 | `MD_ISSUE_TRANS_MAT` | VARCHAR(6) | NOT NULL | PK | primary_key |  |
| 9 | `MD_MINQTY` | DECIMAL(11,2) |  |  |  |  |
| 10 | `MD_UPD_REQ_HRS` | SMALLINT |  |  |  |  |
| 11 | `MD_MAT_PROD_TYPE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 12 | `MD_MODULERULE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.MD_IDENTIFIER,
       t.MD_WKCNTER,
       t.MD_WKCT_PROC,
       t.MD_RES_CAT_CODE,
       t.MD_RSC_CODE,
       t.MD_TYPE_PROD,
       t.MD_SEARCH_BALANCE,
       t.MD_WAIT_ENTIRE_MAT,
       t.MD_ISSUE_TRANS_MAT,
       t.MD_MINQTY,
       t.MD_UPD_REQ_HRS,
       t.MD_MAT_PROD_TYPE
FROM   DB2ADMIN.SCDA_MATERIAL_SUP_DETAIL t
FETCH FIRST 100 ROWS ONLY;
```
