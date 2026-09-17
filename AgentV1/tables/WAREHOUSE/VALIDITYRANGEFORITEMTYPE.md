# DB2ADMIN.VALIDITYRANGEFORITEMTYPE

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `LOGICALWAREHOUSECOMPANYCODE`, `LOGICALWAREHOUSECODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 79233

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `INITIALDATE` | DATE | NOT NULL |  |  |  |
| 4 | `FINALDATE` | DATE | NOT NULL |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `LOGICALWAREHOUSE_VALIDITYRANGE` | `LOGICALWAREHOUSECOMPANYCODE`, `LOGICALWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `VALIDITYRANGEFORITEMTYPE.LOGICALWAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND VALIDITYRANGEFORITEMTYPE.LOGICALWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `VALIDITYRANGEFORITEMTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LOGICALWAREHOUSECOMPANYCODE,
       t.LOGICALWAREHOUSECODE,
       t.ITEMTYPECODE,
       t.INITIALDATE,
       t.FINALDATE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.VALIDITYRANGEFORITEMTYPE t
FETCH FIRST 100 ROWS ONLY;
```
