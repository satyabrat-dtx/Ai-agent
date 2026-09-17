# DB2ADMIN.SCDM_ALTERNATIVEWAREHOUSE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `IDENTIFIER`, `WKCNTER`, `ALTERN_WC`, `NET_GROUP_CODE`, `ISSUE_ITEM_TYPE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185676

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `ALTERN_WC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `NET_GROUP_CODE` | VARCHAR(16) | NOT NULL | PK | primary_key |  |
| 4 | `ISSUE_ITEM_TYPE` | VARCHAR(16) | NOT NULL | PK | primary_key |  |
| 5 | `ALTERN_NET_GROUP_CODE` | VARCHAR(120) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.WKCNTER,
       t.ALTERN_WC,
       t.NET_GROUP_CODE,
       t.ISSUE_ITEM_TYPE,
       t.ALTERN_NET_GROUP_CODE
FROM   DB2ADMIN.SCDM_ALTERNATIVEWAREHOUSE t
FETCH FIRST 100 ROWS ONLY;
```
