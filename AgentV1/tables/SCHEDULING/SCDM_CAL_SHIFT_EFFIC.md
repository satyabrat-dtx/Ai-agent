# DB2ADMIN.SCDM_CAL_SHIFT_EFFIC

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `CSE_IDENTIFIER`, `CSE_CAL`, `CSE_RSC_CODE`, `CSE_START_DATE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186013

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CSE_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CSE_CAL` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `CSE_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `CSE_START_DATE` | TIMESTAMP | NOT NULL | PK | primary_key |  |
| 4 | `CSE_END_DATE` | TIMESTAMP |  |  |  |  |
| 5 | `CSE_SH1_START` | SMALLINT |  |  |  |  |
| 6 | `CSE_SH1_END` | SMALLINT |  |  |  |  |
| 7 | `CSE_SH1_EFFIC` | SMALLINT |  |  |  |  |
| 8 | `CSE_SH2_START` | SMALLINT |  |  |  |  |
| 9 | `CSE_SH2_END` | SMALLINT |  |  |  |  |
| 10 | `CSE_SH2_EFFIC` | SMALLINT |  |  |  |  |
| 11 | `CSE_SH3_START` | SMALLINT |  |  |  |  |
| 12 | `CSE_SH3_END` | SMALLINT |  |  |  |  |
| 13 | `CSE_SH3_EFFIC` | SMALLINT |  |  |  |  |
| 14 | `CSE_SH4_START` | SMALLINT |  |  |  |  |
| 15 | `CSE_SH4_END` | SMALLINT |  |  |  |  |
| 16 | `CSE_SH4_EFFIC` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CSE_IDENTIFIER,
       t.CSE_CAL,
       t.CSE_RSC_CODE,
       t.CSE_START_DATE,
       t.CSE_END_DATE,
       t.CSE_SH1_START,
       t.CSE_SH1_END,
       t.CSE_SH1_EFFIC,
       t.CSE_SH2_START,
       t.CSE_SH2_END,
       t.CSE_SH2_EFFIC,
       t.CSE_SH3_START
FROM   DB2ADMIN.SCDM_CAL_SHIFT_EFFIC t
FETCH FIRST 100 ROWS ONLY;
```
