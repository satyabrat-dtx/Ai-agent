# DB2ADMIN.SCDC_TABLES_UPLOAD_HOST

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `TH_IDENTIFIER`, `TH_TABLE_LOCAL_NAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188242

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TH_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `TH_TABLE_LOCAL_NAME` | VARCHAR(20) | NOT NULL | PK | primary_key |  |
| 2 | `TH_TABLE_HOST_NAME` | VARCHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.TH_IDENTIFIER,
       t.TH_TABLE_LOCAL_NAME,
       t.TH_TABLE_HOST_NAME
FROM   DB2ADMIN.SCDC_TABLES_UPLOAD_HOST t
FETCH FIRST 100 ROWS ONLY;
```
