# DB2ADMIN.AVAILABILITYFORMULADETAIL

- **Module**: `INVENTORY` (low confidence — FK neighbourhood: 1 of 1 related tables are INVENTORY)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `AVAILABILITYFORMULACOMPANYCODE`, `AVAILABILITYFORMULACODE`, `STOCKTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 25276

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AVAILABILITYFORMULACOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `AVAILABILITYFORMULACODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `STOCKTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DUMMY` | INTEGER | NOT NULL |  |  |  |
| 4 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AVAILABILITYFORMULA_AVAILABILITYFORMULADETAIL` | `AVAILABILITYFORMULACOMPANYCODE`, `AVAILABILITYFORMULACODE` | [`AVAILABILITYFORMULA`](../CORE_MASTER/AVAILABILITYFORMULA.md) | `COMPANYCODE`, `CODE` | RESTRICT | `AVAILABILITYFORMULADETAIL.AVAILABILITYFORMULACOMPANYCODE = AVAILABILITYFORMULA.COMPANYCODE AND AVAILABILITYFORMULADETAIL.AVAILABILITYFORMULACODE = AVAILABILITYFORMULA.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `AVAILABILITYFORMULADETAIL.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `STOCKTYPE_STOCKTYPE` | `STOCKTYPECODE` | [`STOCKTYPE`](../INVENTORY/STOCKTYPE.md) | `CODE` | RESTRICT | `AVAILABILITYFORMULADETAIL.STOCKTYPECODE = STOCKTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `AVAILABILITYFORMULADETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.AVAILABILITYFORMULACOMPANYCODE,
       t.AVAILABILITYFORMULACODE,
       t.STOCKTYPECODE,
       t.DUMMY,
       t.OWNINGCOMPANYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.AVAILABILITYFORMULADETAIL t
FETCH FIRST 100 ROWS ONLY;
```
