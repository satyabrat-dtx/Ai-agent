# DB2ADMIN.DEPBFINYEARTURNOVEREXPORT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `DEPBDEFAULTCOMPANYCODE`, `DEPBDEFAULTDIVISIONCODE`, `FISCALYEARYEAR`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 137323

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DEPBDEFAULTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DEPBDEFAULTDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FISCALYEARYEAR` | DECIMAL(4,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TURNOVERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 4 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `DEPBFINYEARTURNOVEREXPORT.CURRENCYCODE = CURRENCY.CODE` |
| `DEPBDEFAULT_DETAIL1` | `DEPBDEFAULTCOMPANYCODE`, `DEPBDEFAULTDIVISIONCODE` | [`DEPBDEFAULT`](../SALES/DEPBDEFAULT.md) | `COMPANYCODE`, `DIVISIONCODE` | RESTRICT | `DEPBFINYEARTURNOVEREXPORT.DEPBDEFAULTCOMPANYCODE = DEPBDEFAULT.COMPANYCODE AND DEPBFINYEARTURNOVEREXPORT.DEPBDEFAULTDIVISIONCODE = DEPBDEFAULT.DIVISIONCODE` |
| `LIFOYEAR_FISCALYEAR` | `DEPBDEFAULTCOMPANYCODE`, `FISCALYEARYEAR` | [`LIFOYEAR`](../OTHER/LIFOYEAR.md) | `COMPANYCODE`, `YEAR` | RESTRICT | `DEPBFINYEARTURNOVEREXPORT.DEPBDEFAULTCOMPANYCODE = LIFOYEAR.COMPANYCODE AND DEPBFINYEARTURNOVEREXPORT.FISCALYEARYEAR = LIFOYEAR.YEAR` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DEPBFINYEARTURNOVEREXPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DEPBDEFAULTCOMPANYCODE,
       t.DEPBDEFAULTDIVISIONCODE,
       t.FISCALYEARYEAR,
       t.TURNOVERVALUE,
       t.CURRENCYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DEPBFINYEARTURNOVEREXPORT t
FETCH FIRST 100 ROWS ONLY;
```
