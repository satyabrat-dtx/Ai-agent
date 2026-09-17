# DB2ADMIN.SCDC_CLR_JOB_TO_RES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `JR_IDENTIFIER`, `JR_WKST_CODE`, `JR_VALUE_FROM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189259

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `JR_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `JR_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `JR_VALUE_FROM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `JR_INT_COLOR` | INTEGER |  |  |  |  |
| 4 | `JR_BDR_COLOR` | INTEGER |  |  |  |  |
| 5 | `JR_TXT_COLOR` | INTEGER |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.JR_IDENTIFIER,
       t.JR_WKST_CODE,
       t.JR_VALUE_FROM,
       t.JR_INT_COLOR,
       t.JR_BDR_COLOR,
       t.JR_TXT_COLOR
FROM   DB2ADMIN.SCDC_CLR_JOB_TO_RES t
FETCH FIRST 100 ROWS ONLY;
```
