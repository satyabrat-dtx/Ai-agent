# DB2ADMIN.PROFITELEMENTFORMULA

- **Module**: `COSTING` (low confidence — FK neighbourhood: 1 of 1 related tables are COSTING)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `PROFITELEMENTCOMPANYCODE`, `PROFITELEMENTCODE`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196490

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PROFITELEMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PROFITELEMENTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ACTION` | CHAR(1) |  |  |  |  |
| 4 | `VALUEFROM` | CHAR(1) |  |  |  |  |
| 5 | `REFPROFITELEMENTCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `FIXNUMBER` | DECIMAL(10,5) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PROFITELEMENT_FORMULA` | `PROFITELEMENTCOMPANYCODE`, `PROFITELEMENTCODE` | [`PROFITELEMENT`](../COSTING/PROFITELEMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PROFITELEMENTFORMULA.PROFITELEMENTCOMPANYCODE = PROFITELEMENT.COMPANYCODE AND PROFITELEMENTFORMULA.PROFITELEMENTCODE = PROFITELEMENT.CODE` |
| `PROFITELEMENT_REFPROFITELEMENT` | `PROFITELEMENTCOMPANYCODE`, `REFPROFITELEMENTCODE` | [`PROFITELEMENT`](../COSTING/PROFITELEMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PROFITELEMENTFORMULA.PROFITELEMENTCOMPANYCODE = PROFITELEMENT.COMPANYCODE AND PROFITELEMENTFORMULA.REFPROFITELEMENTCODE = PROFITELEMENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROFITELEMENTFORMULAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PROFITELEMENTCOMPANYCODE,
       t.PROFITELEMENTCODE,
       t.SEQUENCE,
       t.ACTION,
       t.VALUEFROM,
       t.REFPROFITELEMENTCODE,
       t.FIXNUMBER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PROFITELEMENTFORMULA t
FETCH FIRST 100 ROWS ONLY;
```
