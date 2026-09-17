# DB2ADMIN.WAREHOUSEITEMPERIODSTDCOST

- **Module**: `WAREHOUSE` (high confidence — table name starts with 'WAREHOUSE')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COSTIDENTIFIER`, `ENDDATE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 80808

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COSTIDENTIFIER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 1 | `ENDDATE` | DATE | NOT NULL | PK | primary_key |  |
| 2 | `STANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 3 | `DEVALUEDSTANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 4 | `SECONDSTANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 5 | `DEVALUEDSECONDSTANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WAREHOUSEITEMPERIODSTDCOSTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COSTIDENTIFIER,
       t.ENDDATE,
       t.STANDARDCOST,
       t.DEVALUEDSTANDARDCOST,
       t.SECONDSTANDARDCOST,
       t.DEVALUEDSECONDSTANDARDCOST,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WAREHOUSEITEMPERIODSTDCOST t
FETCH FIRST 100 ROWS ONLY;
```
