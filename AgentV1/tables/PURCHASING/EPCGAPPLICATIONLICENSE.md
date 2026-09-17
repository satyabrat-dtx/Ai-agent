# DB2ADMIN.EPCGAPPLICATIONLICENSE

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `EPCGAPPLICATIONCOMPANYCODE`, `EPCGAPPLICATIONCODE`, `LICENSENO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 138146

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EPCGAPPLICATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EPCGAPPLICATIONCODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LICENSENO` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 3 | `LICENSEDATE` | DATE |  |  |  |  |
| 4 | `CIFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 5 | `CIFCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 6 | `EOFIXEDINFCC` | DECIMAL(18,5) |  |  |  |  |
| 7 | `BG_LUT` | SMALLINT | NOT NULL |  |  |  |
| 8 | `EOFULFILLEDPERC` | DECIMAL(5,2) |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CIFCURRENCY` | `CIFCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `EPCGAPPLICATIONLICENSE.CIFCURRENCYCODE = CURRENCY.CODE` |
| `EPCGAPPLICATION_LICENSELINE` | `EPCGAPPLICATIONCOMPANYCODE`, `EPCGAPPLICATIONCODE` | [`EPCGAPPLICATION`](../PURCHASING/EPCGAPPLICATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EPCGAPPLICATIONLICENSE.EPCGAPPLICATIONCOMPANYCODE = EPCGAPPLICATION.COMPANYCODE AND EPCGAPPLICATIONLICENSE.EPCGAPPLICATIONCODE = EPCGAPPLICATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EPCGAPPLICATIONLICENSEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EPCGAPPLICATIONCOMPANYCODE,
       t.EPCGAPPLICATIONCODE,
       t.LICENSENO,
       t.LICENSEDATE,
       t.CIFVALUE,
       t.CIFCURRENCYCODE,
       t.EOFIXEDINFCC,
       t.BG_LUT,
       t.EOFULFILLEDPERC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.EPCGAPPLICATIONLICENSE t
FETCH FIRST 100 ROWS ONLY;
```
