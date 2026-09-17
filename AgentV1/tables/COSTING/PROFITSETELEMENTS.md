# DB2ADMIN.PROFITSETELEMENTS

- **Module**: `COSTING` (low confidence — FK neighbourhood: 1 of 1 related tables are COSTING)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `PROFITSETCOMPANYCODE`, `PROFITSETCODE`, `PROFITELEMENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196568

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PROFITSETCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PROFITSETCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PROFITELEMENTCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 4 | `FINALPRICECONTRIBUTION` | CHAR(1) |  |  |  |  |
| 5 | `DISPLAYSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 6 | `MANUALVALUE` | DECIMAL(10,5) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PROFITSET_ELEMENTS` | `PROFITSETCOMPANYCODE`, `PROFITSETCODE` | [`PROFITSET`](../COSTING/PROFITSET.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PROFITSETELEMENTS.PROFITSETCOMPANYCODE = PROFITSET.COMPANYCODE AND PROFITSETELEMENTS.PROFITSETCODE = PROFITSET.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROFITSETELEMENTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PROFITSETCOMPANYCODE,
       t.PROFITSETCODE,
       t.PROFITELEMENTCODE,
       t.SEQUENCE,
       t.FINALPRICECONTRIBUTION,
       t.DISPLAYSEQUENCE,
       t.MANUALVALUE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PROFITSETELEMENTS t
FETCH FIRST 100 ROWS ONLY;
```
