# DB2ADMIN.SCDA_ITEMSSTOCK

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `IDENTIFIER`, `ITEMTYPE`, `NET_GROUP_CODE`, `ITEMCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185187

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `ITEMTYPE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `NET_GROUP_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `ITEMCODE` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 4 | `STOCK` | DECIMAL(9,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.ITEMTYPE,
       t.NET_GROUP_CODE,
       t.ITEMCODE,
       t.STOCK
FROM   DB2ADMIN.SCDA_ITEMSSTOCK t
FETCH FIRST 100 ROWS ONLY;
```
