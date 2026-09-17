# DB2ADMIN.SCDC_CLR_JOB_TO_JOB

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `JJ_IDENTIFIER`, `JJ_WKST_CODE`, `JJ_VALUE_FROM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189286

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `JJ_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `JJ_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `JJ_VALUE_FROM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `JJ_INT_COLOR` | INTEGER |  |  |  |  |
| 4 | `JJ_BDR_COLOR` | INTEGER |  |  |  |  |
| 5 | `JJ_TXT_COLOR` | INTEGER |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.JJ_IDENTIFIER,
       t.JJ_WKST_CODE,
       t.JJ_VALUE_FROM,
       t.JJ_INT_COLOR,
       t.JJ_BDR_COLOR,
       t.JJ_TXT_COLOR
FROM   DB2ADMIN.SCDC_CLR_JOB_TO_JOB t
FETCH FIRST 100 ROWS ONLY;
```
