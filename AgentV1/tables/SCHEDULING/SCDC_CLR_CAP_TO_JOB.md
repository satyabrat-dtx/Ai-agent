# DB2ADMIN.SCDC_CLR_CAP_TO_JOB

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CJ_IDENTIFIER`, `CJ_WKST_CODE`, `CJ_VALUE_FROM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188644

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CJ_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CJ_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `CJ_VALUE_FROM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `CJ_INT_COLOR` | INTEGER |  |  |  |  |
| 4 | `CJ_BDR_COLOR` | INTEGER |  |  |  |  |
| 5 | `CJ_TXT_COLOR` | INTEGER |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CJ_IDENTIFIER,
       t.CJ_WKST_CODE,
       t.CJ_VALUE_FROM,
       t.CJ_INT_COLOR,
       t.CJ_BDR_COLOR,
       t.CJ_TXT_COLOR
FROM   DB2ADMIN.SCDC_CLR_CAP_TO_JOB t
FETCH FIRST 100 ROWS ONLY;
```
