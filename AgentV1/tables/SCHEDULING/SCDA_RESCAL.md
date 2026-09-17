# DB2ADMIN.SCDA_RESCAL

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `RCA_IDENTIFIER`, `RCA_CAL`, `RCA_CAL_DATE`, `RCA_RSC_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194155

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RCA_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `RCA_CAL` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `RCA_CAL_DATE` | TIMESTAMP | NOT NULL | PK | primary_key |  |
| 3 | `RCA_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `RCA_PROG_WRK_HR` | DECIMAL(9,2) |  |  |  |  |
| 5 | `RCA_SH1_START` | SMALLINT |  |  |  |  |
| 6 | `RCA_SH1_END` | SMALLINT |  |  |  |  |
| 7 | `RCA_SH2_START` | SMALLINT |  |  |  |  |
| 8 | `RCA_SH2_END` | SMALLINT |  |  |  |  |
| 9 | `RCA_SH3_START` | SMALLINT |  |  |  |  |
| 10 | `RCA_SH3_END` | SMALLINT |  |  |  |  |
| 11 | `RCA_SH4_START` | SMALLINT |  |  |  |  |
| 12 | `RCA_SH4_END` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.RCA_IDENTIFIER,
       t.RCA_CAL,
       t.RCA_CAL_DATE,
       t.RCA_RSC_CODE,
       t.RCA_PROG_WRK_HR,
       t.RCA_SH1_START,
       t.RCA_SH1_END,
       t.RCA_SH2_START,
       t.RCA_SH2_END,
       t.RCA_SH3_START,
       t.RCA_SH3_END,
       t.RCA_SH4_START
FROM   DB2ADMIN.SCDA_RESCAL t
FETCH FIRST 100 ROWS ONLY;
```
