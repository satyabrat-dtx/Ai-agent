# DB2ADMIN.ITEMSSTOCKCHANGES

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `ITC_IDENTIFIER`, `ITC_ITEMTYPE`, `ITC_NET_GROUP_CODE`, `ITC_ITEMCODE`, `ITC_DAYINWEEK`, `ITC_FROMTIME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188050

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ITC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `ITC_ITEMTYPE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `ITC_NET_GROUP_CODE` | VARCHAR(16) | NOT NULL | PK | primary_key |  |
| 3 | `ITC_ITEMCODE` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 4 | `ITC_DAYINWEEK` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 5 | `ITC_FROMTIME` | SMALLINT | NOT NULL | PK | primary_key |  |
| 6 | `ITC_TOTIME` | SMALLINT |  |  |  |  |
| 7 | `ITC_STOCKDIFFERENCE` | DECIMAL(11,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ITC_IDENTIFIER,
       t.ITC_ITEMTYPE,
       t.ITC_NET_GROUP_CODE,
       t.ITC_ITEMCODE,
       t.ITC_DAYINWEEK,
       t.ITC_FROMTIME,
       t.ITC_TOTIME,
       t.ITC_STOCKDIFFERENCE
FROM   DB2ADMIN.ITEMSSTOCKCHANGES t
FETCH FIRST 100 ROWS ONLY;
```
