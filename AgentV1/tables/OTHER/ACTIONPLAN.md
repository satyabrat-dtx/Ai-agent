# DB2ADMIN.ACTIONPLAN

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `ACTIONPLANKEY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 18799

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ACTIONPLANKEY` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 1 | `DATETOSTART` | DATE |  |  |  |  |
| 2 | `PRODUCTTYPE` | CHAR(10) |  |  |  |  |
| 3 | `PRODUCT` | CHAR(20) |  |  |  |  |
| 4 | `QUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 5 | `UM` | CHAR(3) |  |  |  |  |
| 6 | `DELIVERYDATE` | DATE | NOT NULL |  |  |  |
| 7 | `PROPOSALTYPE` | CHAR(15) |  |  |  |  |
| 8 | `CUSTOMER` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ACTIONPLANKEY,
       t.DATETOSTART,
       t.PRODUCTTYPE,
       t.PRODUCT,
       t.QUANTITY,
       t.UM,
       t.DELIVERYDATE,
       t.PROPOSALTYPE,
       t.CUSTOMER
FROM   DB2ADMIN.ACTIONPLAN t
FETCH FIRST 100 ROWS ONLY;
```
