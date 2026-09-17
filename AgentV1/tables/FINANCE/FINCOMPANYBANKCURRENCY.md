# DB2ADMIN.FINCOMPANYBANKCURRENCY

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `FINCOMPANYBANKCOMPANYCODE`, `FINCOMPANYBANKDIVISIONCODE`, `FINCOMPANYBANKCODE`, `CURRENCYCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 101496

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINCOMPANYBANKCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINCOMPANYBANKDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINCOMPANYBANKCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CURRENCYCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINCOMPANYBANK_SUPPORTEDCURRENCY` | `FINCOMPANYBANKCOMPANYCODE`, `FINCOMPANYBANKDIVISIONCODE`, `FINCOMPANYBANKCODE` | [`FINCOMPANYBANK`](../FINANCE/FINCOMPANYBANK.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `FINCOMPANYBANKCURRENCY.FINCOMPANYBANKCOMPANYCODE = FINCOMPANYBANK.COMPANYCODE AND FINCOMPANYBANKCURRENCY.FINCOMPANYBANKDIVISIONCODE = FINCOMPANYBANK.DIVISIONCODE AND FINCOMPANYBANKCURRENCY.FINCOMPANYBANKCODE = FINCOMPANYBANK.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINCOMPANYBANKCURRENCYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINCOMPANYBANKCOMPANYCODE,
       t.FINCOMPANYBANKDIVISIONCODE,
       t.FINCOMPANYBANKCODE,
       t.CURRENCYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINCOMPANYBANKCURRENCY t
FETCH FIRST 100 ROWS ONLY;
```
