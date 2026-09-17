# DB2ADMIN.PERIODDETAIL

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `PERPERIODIZEDCALENDARTYPECODE`, `PERIODPERIODIZEDCALENDARYEAR`, `PERIODCODE`, `NUMBERDATE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 4678

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PERPERIODIZEDCALENDARTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PERIODPERIODIZEDCALENDARYEAR` | DECIMAL(4,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PERIODCODE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `NUMBERDATE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `DATEINPERIOD` | DATE | NOT NULL |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PERIOD_PERIODDETAIL` | `PERPERIODIZEDCALENDARTYPECODE`, `PERIODPERIODIZEDCALENDARYEAR`, `PERIODCODE` | [`PERIOD`](../WAREHOUSE/PERIOD.md) | `PERIODIZEDCALENDARTYPECODE`, `PERIODIZEDCALENDARYEAR`, `CODE` | RESTRICT | `PERIODDETAIL.PERPERIODIZEDCALENDARTYPECODE = PERIOD.PERIODIZEDCALENDARTYPECODE AND PERIODDETAIL.PERIODPERIODIZEDCALENDARYEAR = PERIOD.PERIODIZEDCALENDARYEAR AND PERIODDETAIL.PERIODCODE = PERIOD.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PERIODDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PERPERIODIZEDCALENDARTYPECODE,
       t.PERIODPERIODIZEDCALENDARYEAR,
       t.PERIODCODE,
       t.NUMBERDATE,
       t.DATEINPERIOD,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PERIODDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
