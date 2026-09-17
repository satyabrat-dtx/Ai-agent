# DB2ADMIN.SCDC_CLR_JOB_MAT_WRN

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `JM_IDENTIFIER`, `JM_WKST_CODE`, `JM_VALUE_FROM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189231

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `JM_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `JM_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `JM_VALUE_FROM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `JM_INT_COLOR` | INTEGER |  |  |  |  |
| 4 | `JM_BDR_COLOR` | INTEGER |  |  |  |  |
| 5 | `JM_TXT_COLOR` | INTEGER |  |  |  |  |
| 6 | `JM_TXT_DESCRIPTION` | VARCHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.JM_IDENTIFIER,
       t.JM_WKST_CODE,
       t.JM_VALUE_FROM,
       t.JM_INT_COLOR,
       t.JM_BDR_COLOR,
       t.JM_TXT_COLOR,
       t.JM_TXT_DESCRIPTION
FROM   DB2ADMIN.SCDC_CLR_JOB_MAT_WRN t
FETCH FIRST 100 ROWS ONLY;
```
