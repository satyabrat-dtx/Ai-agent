# DB2ADMIN.SCDA_ITEMSSTOCKEXCEPTIONS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `ITE_IDENTIFIER`, `ITE_ITEMTYPE`, `ITE_NET_GROUP_CODE`, `ITE_ITEMCODE`, `ITE_DATE`, `ITE_FROMTIME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185246

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ITE_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `ITE_ITEMTYPE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `ITE_NET_GROUP_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `ITE_ITEMCODE` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 4 | `ITE_DATE` | TIMESTAMP | NOT NULL | PK | primary_key |  |
| 5 | `ITE_FROMTIME` | SMALLINT | NOT NULL | PK | primary_key |  |
| 6 | `ITE_TOTIME` | SMALLINT |  |  |  |  |
| 7 | `ITE_STOCKDIFFERENCE` | DECIMAL(9,2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ITE_IDENTIFIER,
       t.ITE_ITEMTYPE,
       t.ITE_NET_GROUP_CODE,
       t.ITE_ITEMCODE,
       t.ITE_DATE,
       t.ITE_FROMTIME,
       t.ITE_TOTIME,
       t.ITE_STOCKDIFFERENCE
FROM   DB2ADMIN.SCDA_ITEMSSTOCKEXCEPTIONS t
FETCH FIRST 100 ROWS ONLY;
```
