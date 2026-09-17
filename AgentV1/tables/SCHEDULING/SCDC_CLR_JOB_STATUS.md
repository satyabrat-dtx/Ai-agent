# DB2ADMIN.SCDC_CLR_JOB_STATUS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `JS_IDENTIFIER`, `JS_WKST_CODE`, `JS_VALUE_FROM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189175

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `JS_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `JS_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `JS_VALUE_FROM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `JS_INT_COLOR` | INTEGER |  |  |  |  |
| 4 | `JS_BDR_COLOR` | INTEGER |  |  |  |  |
| 5 | `JS_TXT_COLOR` | INTEGER |  |  |  |  |
| 6 | `JS_TXT_DESCRIPTION` | VARCHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.JS_IDENTIFIER,
       t.JS_WKST_CODE,
       t.JS_VALUE_FROM,
       t.JS_INT_COLOR,
       t.JS_BDR_COLOR,
       t.JS_TXT_COLOR,
       t.JS_TXT_DESCRIPTION
FROM   DB2ADMIN.SCDC_CLR_JOB_STATUS t
FETCH FIRST 100 ROWS ONLY;
```
