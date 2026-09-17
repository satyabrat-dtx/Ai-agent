# DB2ADMIN.SCDM_PROP_PROD

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `PP_IDENTIFIER`, `PP_PREQ_NO`, `PP_PSTEP_ID`, `PP_PROPERTY`, `PP_RSC_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186367

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PP_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PP_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `PP_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `PP_PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 4 | `PP_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `PP_VALUE` | VARCHAR(90) |  |  |  |  |
| 6 | `PP_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 7 | `PP_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PP_IDENTIFIER,
       t.PP_PREQ_NO,
       t.PP_PSTEP_ID,
       t.PP_PROPERTY,
       t.PP_RSC_CODE,
       t.PP_VALUE,
       t.PP_USR_NAMECG,
       t.PP_USR_TIMECG
FROM   DB2ADMIN.SCDM_PROP_PROD t
FETCH FIRST 100 ROWS ONLY;
```
