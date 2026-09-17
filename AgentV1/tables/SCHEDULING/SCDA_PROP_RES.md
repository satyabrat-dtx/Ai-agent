# DB2ADMIN.SCDA_PROP_RES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `RP_IDENTIFIER`, `RP_WKCNTER`, `RP_RES_CATEGORY`, `RP_WC_PROCESS`, `RP_RSC_CODE`, `RP_PROPERTY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183931

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RP_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `RP_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `RP_RES_CATEGORY` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `RP_WC_PROCESS` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `RP_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `RP_PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 6 | `RP_PROPTY_VALUE` | VARCHAR(90) |  |  |  |  |
| 7 | `RP_PROPTY_VALUE_CALC` | VARCHAR(90) |  |  |  |  |
| 8 | `RP_ADD_RSC_OCC` | VARCHAR(5) |  |  |  |  |
| 9 | `RP_VAL_ADDED` | DECIMAL(14,4) |  |  |  |  |
| 10 | `RP_VAL_TAKE_FOR_GROUP` | CHAR(1) |  |  |  |  |
| 11 | `RP_DFT_CASE_RSC_OCC_RULS` | VARCHAR(2) |  |  |  |  |
| 12 | `RP_DFT_CASE_OCC_OCC_RULS` | VARCHAR(2) |  |  |  |  |
| 13 | `RP_DFT_SAME_GRP_OCC_OCC_RULS` | CHAR(1) |  |  |  |  |
| 14 | `RP_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 15 | `RP_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 16 | `RP_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 17 | `RP_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.RP_IDENTIFIER,
       t.RP_WKCNTER,
       t.RP_RES_CATEGORY,
       t.RP_WC_PROCESS,
       t.RP_RSC_CODE,
       t.RP_PROPERTY,
       t.RP_PROPTY_VALUE,
       t.RP_PROPTY_VALUE_CALC,
       t.RP_ADD_RSC_OCC,
       t.RP_VAL_ADDED,
       t.RP_VAL_TAKE_FOR_GROUP,
       t.RP_DFT_CASE_RSC_OCC_RULS
FROM   DB2ADMIN.SCDA_PROP_RES t
FETCH FIRST 100 ROWS ONLY;
```
