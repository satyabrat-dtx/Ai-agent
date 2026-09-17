# DB2ADMIN.TREPURCHASEORDEREXT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `UNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 69426

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `SALESORDERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 2 | `SALESORDERCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 3 | `SALESORDERCODE` | CHAR(15) |  | FK | foreign_key |  |
| 4 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 5 | `PURCHASEORDERCODE` | CHAR(15) |  | FK | foreign_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PURCHASEORDER_PURCHASEORDER` | `SALESORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE` | [`PURCHASEORDER`](../PURCHASING/PURCHASEORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `TREPURCHASEORDEREXT.SALESORDERCOMPANYCODE = PURCHASEORDER.COMPANYCODE AND TREPURCHASEORDEREXT.PURCHASEORDERCOUNTERCODE = PURCHASEORDER.COUNTERCODE AND TREPURCHASEORDEREXT.PURCHASEORDERCODE = PURCHASEORDER.CODE` |
| `SALESORDER_SALESORDER` | `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE` | [`SALESORDER`](../SALES/SALESORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `TREPURCHASEORDEREXT.SALESORDERCOMPANYCODE = SALESORDER.COMPANYCODE AND TREPURCHASEORDEREXT.SALESORDERCOUNTERCODE = SALESORDER.COUNTERCODE AND TREPURCHASEORDEREXT.SALESORDERCODE = SALESORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TREPURCHASEORDEREXTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.SALESORDERCOMPANYCODE,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TREPURCHASEORDEREXT t
FETCH FIRST 100 ROWS ONLY;
```
