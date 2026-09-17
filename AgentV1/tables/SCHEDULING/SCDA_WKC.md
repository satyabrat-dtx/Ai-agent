# DB2ADMIN.SCDA_WKC

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `WC_IDENTIFIER`, `WC_WKCNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184232

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
| 7 | `WC_OVERLAP_WITH_OTHER_STEPS` | CHAR(1) |  |  |  |  |
| 8 | `WC_AD_OVERLAP_WITH_OTHER_STEPS` | VARCHAR(30) |  |  |  |  |
| 9 | `WC_HANDLEDBYMQM` | CHAR(1) |  |  |  |  |
| 10 | `WC_HANDLEDBYMCM` | CHAR(1) |  |  |  |  |
| 11 | `WC_HANDLE_LEARNINGCURVE` | CHAR(1) |  |  |  |  |
| 12 | `WC_AD_LEARNINGCURVE_CODE` | VARCHAR(30) |  |  |  |  |
| 13 | `WC_PLANT_CODE` | VARCHAR(8) |  |  |  |  |
| 14 | `WC_HANDLEGERERICPLAN` | CHAR(1) |  |  |  |  |
| 15 | `WC_RES_NUM_PLN` | SMALLINT |  |  |  |  |
| 16 | `WC_CAL` | VARCHAR(3) |  |  |  |  |
| 17 | `WC_MCM_SEQUENCE` | SMALLINT |  |  |  |  |
| 18 | `WC_WARP_HANDLE` | CHAR(1) |  |  |  |  |

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
       t.WC_OVERLAP_WITH_OTHER_STEPS,
       t.WC_AD_OVERLAP_WITH_OTHER_STEPS,
       t.WC_HANDLEDBYMQM,
       t.WC_HANDLEDBYMCM,
       t.WC_HANDLE_LEARNINGCURVE
FROM   DB2ADMIN.SCDA_WKC t
FETCH FIRST 100 ROWS ONLY;
```
