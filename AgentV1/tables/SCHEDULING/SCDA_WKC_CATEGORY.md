# DB2ADMIN.SCDA_WKC_CATEGORY

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `CA_IDENTIFIER`, `CA_WKCNTER`, `CA_CATEGORY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184871

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CA_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CA_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `CA_CATEGORY` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `CA_CAL` | VARCHAR(3) |  |  |  |  |
| 4 | `CA_PROCES_TYPE` | CHAR(1) |  |  |  |  |
| 5 | `CA_REAL_NUM_MACHINE_TO_CREATE` | SMALLINT |  |  |  |  |
| 6 | `CA_NUM_MX_OVR_FINIT_MC_CAP_CR` | SMALLINT |  |  |  |  |
| 7 | `CA_NUM_MAX_INFINITE_MC_CAP_CR` | SMALLINT |  |  |  |  |
| 8 | `CA_NUMBER_ID` | VARCHAR(4) |  |  |  |  |
| 9 | `CA_STANDRD_BCH_SIZE` | DECIMAL(7,2) |  |  |  |  |
| 10 | `CA_MIN_BCH_SIZE` | DECIMAL(7,2) |  |  |  |  |
| 11 | `CA_MAX_BCH_SIZE` | DECIMAL(7,2) |  |  |  |  |
| 12 | `CA_NUM_RSC_COMP` | DECIMAL(5,0) |  |  |  |  |
| 13 | `CA_BCH_UM` | VARCHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CA_IDENTIFIER,
       t.CA_WKCNTER,
       t.CA_CATEGORY,
       t.CA_CAL,
       t.CA_PROCES_TYPE,
       t.CA_REAL_NUM_MACHINE_TO_CREATE,
       t.CA_NUM_MX_OVR_FINIT_MC_CAP_CR,
       t.CA_NUM_MAX_INFINITE_MC_CAP_CR,
       t.CA_NUMBER_ID,
       t.CA_STANDRD_BCH_SIZE,
       t.CA_MIN_BCH_SIZE,
       t.CA_MAX_BCH_SIZE
FROM   DB2ADMIN.SCDA_WKC_CATEGORY t
FETCH FIRST 100 ROWS ONLY;
```
