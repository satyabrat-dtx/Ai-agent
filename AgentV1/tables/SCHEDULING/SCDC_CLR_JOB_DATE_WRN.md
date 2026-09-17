# DB2ADMIN.SCDC_CLR_JOB_DATE_WRN

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `JD_IDENTIFIER`, `JD_WKST_CODE`, `JD_VALUE_FROM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189203

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `JD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `JD_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `JD_VALUE_FROM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `JD_INT_COLOR` | INTEGER |  |  |  |  |
| 4 | `JD_BDR_COLOR` | INTEGER |  |  |  |  |
| 5 | `JD_TXT_COLOR` | INTEGER |  |  |  |  |
| 6 | `JD_TXT_DESCRIPTION` | VARCHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.JD_IDENTIFIER,
       t.JD_WKST_CODE,
       t.JD_VALUE_FROM,
       t.JD_INT_COLOR,
       t.JD_BDR_COLOR,
       t.JD_TXT_COLOR,
       t.JD_TXT_DESCRIPTION
FROM   DB2ADMIN.SCDC_CLR_JOB_DATE_WRN t
FETCH FIRST 100 ROWS ONLY;
```
