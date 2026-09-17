# DB2ADMIN.SCDM_OVERRIDE_STEP_PARAMETERS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `PDO_IDENTIFIER`, `PDO_PREQ_NO`, `PDO_PSTEP_ID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189728

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PDO_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PDO_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `PDO_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `PDO_SPEED` | DECIMAL(9,4) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PDO_IDENTIFIER,
       t.PDO_PREQ_NO,
       t.PDO_PSTEP_ID,
       t.PDO_SPEED
FROM   DB2ADMIN.SCDM_OVERRIDE_STEP_PARAMETERS t
FETCH FIRST 100 ROWS ONLY;
```
