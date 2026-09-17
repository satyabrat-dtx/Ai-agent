# DB2ADMIN.PROPROGRESSQUANTITYPERDEMAND

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `PRODUCTIONPROGRESSCOMPANYCODE`, `PROPROGRESSPROGRESSNUMBER`, `DEMANDCOUNTERCODE`, `DEMANDCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 192195

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PRODUCTIONPROGRESSCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PROPROGRESSPROGRESSNUMBER` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DEMANDCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `DEMANDCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `SELECTED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 6 | `SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 7 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PRODUCTIONPROGRESS_QUANTITYPERDEMAND` | `PRODUCTIONPROGRESSCOMPANYCODE`, `PROPROGRESSPROGRESSNUMBER` | [`PRODUCTIONPROGRESS`](../PRODUCTION/PRODUCTIONPROGRESS.md) | `COMPANYCODE`, `PROGRESSNUMBER` | RESTRICT | `PROPROGRESSQUANTITYPERDEMAND.PRODUCTIONPROGRESSCOMPANYCODE = PRODUCTIONPROGRESS.COMPANYCODE AND PROPROGRESSQUANTITYPERDEMAND.PROPROGRESSPROGRESSNUMBER = PRODUCTIONPROGRESS.PROGRESSNUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROGRESSQUANTITYPERDEMANDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PRODUCTIONPROGRESSCOMPANYCODE,
       t.PROPROGRESSPROGRESSNUMBER,
       t.DEMANDCOUNTERCODE,
       t.DEMANDCODE,
       t.SELECTED,
       t.PRIMARYQUANTITY,
       t.SECONDARYQUANTITY,
       t.PACKAGINGQUANTITY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PROPROGRESSQUANTITYPERDEMAND t
FETCH FIRST 100 ROWS ONLY;
```
