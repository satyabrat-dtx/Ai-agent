# DB2ADMIN.CUSTOMINVOICESHIPPINMARKDLT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CUSTOMINVOICECOMPANYCODE`, `CUSTOMINVOICEDIVISIONCODE`, `CUSTOMINVOICECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 136549

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CUSTOMINVOICECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CUSTOMINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CUSTOMINVOICECODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `SHIPPINGMARK` | VARCHAR(1000) | NOT NULL |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CUSTOMINVOICE_SHIPPINGLINE` | `CUSTOMINVOICECOMPANYCODE`, `CUSTOMINVOICEDIVISIONCODE`, `CUSTOMINVOICECODE` | [`CUSTOMINVOICE`](../CORE_MASTER/CUSTOMINVOICE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `CUSTOMINVOICESHIPPINMARKDLT.CUSTOMINVOICECOMPANYCODE = CUSTOMINVOICE.COMPANYCODE AND CUSTOMINVOICESHIPPINMARKDLT.CUSTOMINVOICEDIVISIONCODE = CUSTOMINVOICE.DIVISIONCODE AND CUSTOMINVOICESHIPPINMARKDLT.CUSTOMINVOICECODE = CUSTOMINVOICE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TOMINVOICESHIPPINMARKDLTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CUSTOMINVOICECOMPANYCODE,
       t.CUSTOMINVOICEDIVISIONCODE,
       t.CUSTOMINVOICECODE,
       t.LINENO,
       t.SHIPPINGMARK,
       t.ABSUNIQUEID
FROM   DB2ADMIN.CUSTOMINVOICESHIPPINMARKDLT t
FETCH FIRST 100 ROWS ONLY;
```
