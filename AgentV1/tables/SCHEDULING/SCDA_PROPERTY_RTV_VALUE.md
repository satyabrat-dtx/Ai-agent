# DB2ADMIN.SCDA_PROPERTY_RTV_VALUE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `IDENTIFIER`, `PROPERTY`, `ITEMTYPE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184842

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 2 | `ITEMTYPE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `TABLE_NAME` | VARCHAR(50) |  |  |  |  |
| 4 | `COLUMN_NAME` | VARCHAR(50) |  |  |  |  |
| 5 | `RELATED_COLUMN_NAME` | VARCHAR(50) |  |  |  |  |
| 6 | `FROM_POSITION` | SMALLINT |  |  |  |  |
| 7 | `LENGTH_FROM_POS` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.PROPERTY,
       t.ITEMTYPE,
       t.TABLE_NAME,
       t.COLUMN_NAME,
       t.RELATED_COLUMN_NAME,
       t.FROM_POSITION,
       t.LENGTH_FROM_POS
FROM   DB2ADMIN.SCDA_PROPERTY_RTV_VALUE t
FETCH FIRST 100 ROWS ONLY;
```
