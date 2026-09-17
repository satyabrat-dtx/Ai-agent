# DB2ADMIN.SCDC_CLR_RES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `RC_IDENTIFIER`, `RC_WKST_CODE`, `RC_VALUE_FROM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189339

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `RC_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `RC_VALUE_FROM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `RC_INT_COLOR` | INTEGER |  |  |  |  |
| 4 | `RC_BDR_COLOR` | INTEGER |  |  |  |  |
| 5 | `RC_TXT_COLOR` | INTEGER |  |  |  |  |
| 6 | `RC_TXT_DESCRIPTION` | VARCHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.RC_IDENTIFIER,
       t.RC_WKST_CODE,
       t.RC_VALUE_FROM,
       t.RC_INT_COLOR,
       t.RC_BDR_COLOR,
       t.RC_TXT_COLOR,
       t.RC_TXT_DESCRIPTION
FROM   DB2ADMIN.SCDC_CLR_RES t
FETCH FIRST 100 ROWS ONLY;
```
