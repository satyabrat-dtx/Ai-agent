# DB2ADMIN.SCDM_DOWNLOAD_TIME

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 2
- **Primary key**: `DD_IDENTIFIER`, `DD_DOWNLOAD_DATE_TIME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187924

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `DD_DOWNLOAD_DATE_TIME` | TIMESTAMP | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.DD_IDENTIFIER,
       t.DD_DOWNLOAD_DATE_TIME
FROM   DB2ADMIN.SCDM_DOWNLOAD_TIME t
FETCH FIRST 100 ROWS ONLY;
```
