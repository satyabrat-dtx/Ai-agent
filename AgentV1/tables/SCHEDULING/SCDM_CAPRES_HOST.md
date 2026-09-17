# DB2ADMIN.SCDM_CAPRES_HOST

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `CH_IDENTIFIER`, `CH_CAPACTY_RESRV`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185827

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CH_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CH_CAPACTY_RESRV` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CH_RSC_CODE` | VARCHAR(8) |  |  |  |  |
| 3 | `CH_PROD_SUBLIN_RSC` | SMALLINT |  |  |  |  |
| 4 | `CH_WC_PROCESS` | VARCHAR(8) |  |  |  |  |
| 5 | `CH_CAPACITY_TYPE` | CHAR(1) |  |  |  |  |
| 6 | `CH_CAPACITY_TO_JOB` | VARCHAR(2) |  |  |  |  |
| 7 | `CH_COMMENT` | VARCHAR(30) |  |  |  |  |
| 8 | `CH_SCH_START` | TIMESTAMP |  |  |  |  |
| 9 | `CH_SCH_END` | TIMESTAMP |  |  |  |  |
| 10 | `CH_COLOR_INDEX` | SMALLINT |  |  |  |  |
| 11 | `CH_UPD_CODE` | INTEGER |  |  |  |  |
| 12 | `CH_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 13 | `CH_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 14 | `CH_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 15 | `CH_USR_TIMECG` | TIMESTAMP |  |  |  |  |
| 16 | `CH_EXE_MIN` | DECIMAL(11,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CH_IDENTIFIER,
       t.CH_CAPACTY_RESRV,
       t.CH_RSC_CODE,
       t.CH_PROD_SUBLIN_RSC,
       t.CH_WC_PROCESS,
       t.CH_CAPACITY_TYPE,
       t.CH_CAPACITY_TO_JOB,
       t.CH_COMMENT,
       t.CH_SCH_START,
       t.CH_SCH_END,
       t.CH_COLOR_INDEX,
       t.CH_UPD_CODE
FROM   DB2ADMIN.SCDM_CAPRES_HOST t
FETCH FIRST 100 ROWS ONLY;
```
