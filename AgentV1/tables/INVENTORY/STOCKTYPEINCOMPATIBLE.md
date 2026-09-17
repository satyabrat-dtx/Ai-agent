# DB2ADMIN.STOCKTYPEINCOMPATIBLE

- **Module**: `INVENTORY` (high confidence — table name starts with 'STOCK')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `STOCKTYPECODE`, `STOCKTYPEREFERENCECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 21851

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `STOCKTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `STOCKTYPEREFERENCECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DUMMY` | INTEGER | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `STOCKTYPE_STOCKTYPEINCOMPATIBLE` | `STOCKTYPECODE` | [`STOCKTYPE`](../INVENTORY/STOCKTYPE.md) | `CODE` | RESTRICT | `STOCKTYPEINCOMPATIBLE.STOCKTYPECODE = STOCKTYPE.CODE` |
| `STOCKTYPE_STOCKTYPEREFERENCE` | `STOCKTYPEREFERENCECODE` | [`STOCKTYPE`](../INVENTORY/STOCKTYPE.md) | `CODE` | RESTRICT | `STOCKTYPEINCOMPATIBLE.STOCKTYPEREFERENCECODE = STOCKTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STOCKTYPEINCOMPATIBLEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.STOCKTYPECODE,
       t.STOCKTYPEREFERENCECODE,
       t.DUMMY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.STOCKTYPEINCOMPATIBLE t
FETCH FIRST 100 ROWS ONLY;
```
