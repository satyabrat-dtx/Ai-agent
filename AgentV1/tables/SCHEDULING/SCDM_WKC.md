# DB2ADMIN.SCDM_WKC

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `WC_IDENTIFIER`, `WC_WKCNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187243

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WC_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `WC_WK_CNTER_GROUP` | VARCHAR(4) |  |  |  |  |
| 3 | `WC_S_DESCR` | VARCHAR(28) |  |  |  |  |
| 4 | `WC_L_DESCR` | VARCHAR(60) |  |  |  |  |
| 5 | `WC_TYP_OPRATION` | CHAR(1) |  |  |  |  |
| 6 | `WC_TYP_PROCESS` | CHAR(1) |  |  |  |  |
| 7 | `WC_RES_NUM_PLN` | DECIMAL(9,3) |  |  |  |  |
| 8 | `WC_CAL` | VARCHAR(3) |  |  |  |  |
| 9 | `WC_PLANT_CODE` | VARCHAR(8) |  |  |  |  |
| 10 | `WC_MCM_SEQUENCE` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.WC_IDENTIFIER,
       t.WC_WKCNTER,
       t.WC_WK_CNTER_GROUP,
       t.WC_S_DESCR,
       t.WC_L_DESCR,
       t.WC_TYP_OPRATION,
       t.WC_TYP_PROCESS,
       t.WC_RES_NUM_PLN,
       t.WC_CAL,
       t.WC_PLANT_CODE,
       t.WC_MCM_SEQUENCE
FROM   DB2ADMIN.SCDM_WKC t
FETCH FIRST 100 ROWS ONLY;
```
