# DB2ADMIN.PURCHASEORDEREX

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `POCOMPANYCODE`, `POCOUNTERCODE`, `POCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 109833

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `READFLAG` | SMALLINT | NOT NULL |  |  |  |
| 1 | `SUPPLIERACCEPTANCE` | INTEGER | NOT NULL |  |  |  |
| 2 | `POCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `POCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `POCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SUPPLIERCOMMENT` | VARCHAR(140) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PURCHASEORDER_PO` | `POCOMPANYCODE`, `POCOUNTERCODE`, `POCODE` | [`PURCHASEORDER`](../PURCHASING/PURCHASEORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PURCHASEORDEREX.POCOMPANYCODE = PURCHASEORDER.COMPANYCODE AND PURCHASEORDEREX.POCOUNTERCODE = PURCHASEORDER.COUNTERCODE AND PURCHASEORDEREX.POCODE = PURCHASEORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDEREXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.READFLAG,
       t.SUPPLIERACCEPTANCE,
       t.POCOMPANYCODE,
       t.POCOUNTERCODE,
       t.POCODE,
       t.SUPPLIERCOMMENT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PURCHASEORDEREX t
FETCH FIRST 100 ROWS ONLY;
```
