# DB2ADMIN.SCDA_PROPERTY_UPLOAD

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `PU_IDENTIFIER`, `PU_PREQ_NO`, `PU_PSTEP_ID`, `PU_PROPERTY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185278

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PU_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PU_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `PU_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `PU_PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 4 | `PU_VALUE` | VARCHAR(20) |  |  |  |  |
| 5 | `PU_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 6 | `PU_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PU_IDENTIFIER,
       t.PU_PREQ_NO,
       t.PU_PSTEP_ID,
       t.PU_PROPERTY,
       t.PU_VALUE,
       t.PU_USR_NAMECG,
       t.PU_USR_TIMECG
FROM   DB2ADMIN.SCDA_PROPERTY_UPLOAD t
FETCH FIRST 100 ROWS ONLY;
```
