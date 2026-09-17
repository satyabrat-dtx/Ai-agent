# DB2ADMIN.SCDM_CAPRES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `CR_IDENTIFIER`, `CR_CAPACTY_RESRV`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185789

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CR_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CR_CAPACTY_RESRV` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CR_RSC_CODE` | VARCHAR(8) |  |  |  |  |
| 3 | `CR_PROD_SUBLIN_RSC` | SMALLINT |  |  |  |  |
| 4 | `CR_WC_PROCESS` | VARCHAR(8) |  |  |  |  |
| 5 | `CR_CAPACITY_TYPE` | CHAR(1) |  |  |  |  |
| 6 | `CR_CAPACITY_TO_JOB` | VARCHAR(2) |  |  |  |  |
| 7 | `CR_COMMENT` | VARCHAR(30) |  |  |  |  |
| 8 | `CR_SCH_START` | TIMESTAMP |  |  |  |  |
| 9 | `CR_SCH_END` | TIMESTAMP |  |  |  |  |
| 10 | `CR_COLOR_INDEX` | SMALLINT |  |  |  |  |
| 11 | `CR_UPD_CODE` | INTEGER |  |  |  |  |
| 12 | `CR_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 13 | `CR_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 14 | `CR_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 15 | `CR_USR_TIMECG` | TIMESTAMP |  |  |  |  |
| 16 | `CR_EXE_MIN` | DECIMAL(11,2) |  |  |  |  |
| 17 | `CR_STATUS` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CR_IDENTIFIER,
       t.CR_CAPACTY_RESRV,
       t.CR_RSC_CODE,
       t.CR_PROD_SUBLIN_RSC,
       t.CR_WC_PROCESS,
       t.CR_CAPACITY_TYPE,
       t.CR_CAPACITY_TO_JOB,
       t.CR_COMMENT,
       t.CR_SCH_START,
       t.CR_SCH_END,
       t.CR_COLOR_INDEX,
       t.CR_UPD_CODE
FROM   DB2ADMIN.SCDM_CAPRES t
FETCH FIRST 100 ROWS ONLY;
```
