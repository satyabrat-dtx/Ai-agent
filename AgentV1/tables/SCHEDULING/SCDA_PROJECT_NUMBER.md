# DB2ADMIN.SCDA_PROJECT_NUMBER

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `IDENTIFIER`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185164

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CODE` | VARCHAR(20) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `PROJECT_NUMBER` | INTEGER |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.CODE,
       t.PROJECT_NUMBER
FROM   DB2ADMIN.SCDA_PROJECT_NUMBER t
FETCH FIRST 100 ROWS ONLY;
```
