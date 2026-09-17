# DB2ADMIN.PLANLISTLINEOCCUPIEDQUANTITY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANYCODE`, `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 36114

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `FORLINEPLANLISTGROUPNUMBER` | BIGINT |  |  |  |  |
| 3 | `FORLINELINE` | INTEGER |  |  |  |  |
| 4 | `FROMLINEPLANLISTGROUPNUMBER` | BIGINT |  |  |  |  |
| 5 | `FROMLINELINE` | INTEGER |  |  |  |  |
| 6 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TABLEINDEX,
       t.FORLINEPLANLISTGROUPNUMBER,
       t.FORLINELINE,
       t.FROMLINEPLANLISTGROUPNUMBER,
       t.FROMLINELINE,
       t.QUANTITY
FROM   DB2ADMIN.PLANLISTLINEOCCUPIEDQUANTITY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
