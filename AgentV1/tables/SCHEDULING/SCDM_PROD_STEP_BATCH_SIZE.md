# DB2ADMIN.SCDM_PROD_STEP_BATCH_SIZE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `SB_IDENTIFIER`, `SB_PREQ_NO`, `SB_PSTEP_ID`, `SB_BCH_UM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187047

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SB_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `SB_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `SB_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `SB_BCH_UM` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `SB_MULTIPILR_TO_BATCH_UM` | DECIMAL(14,4) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.SB_IDENTIFIER,
       t.SB_PREQ_NO,
       t.SB_PSTEP_ID,
       t.SB_BCH_UM,
       t.SB_MULTIPILR_TO_BATCH_UM
FROM   DB2ADMIN.SCDM_PROD_STEP_BATCH_SIZE t
FETCH FIRST 100 ROWS ONLY;
```
