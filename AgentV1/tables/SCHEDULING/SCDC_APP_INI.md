# DB2ADMIN.SCDC_APP_INI

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `AI_IDENTIFIER`, `AI_WKST_CODE`, `AI_FIELDNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188347

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AI_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `AI_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `AI_FIELDNAME` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 3 | `AI_VALUE` | VARCHAR(120) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.AI_IDENTIFIER,
       t.AI_WKST_CODE,
       t.AI_FIELDNAME,
       t.AI_VALUE
FROM   DB2ADMIN.SCDC_APP_INI t
FETCH FIRST 100 ROWS ONLY;
```
