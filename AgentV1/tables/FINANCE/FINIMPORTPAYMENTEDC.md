# DB2ADMIN.FINIMPORTPAYMENTEDC

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `FINIMPORTEDCHARGESCOMPANYCODE`, `FINIMPORTEDCHARGESCODE`, `IMPORTPAYMENT`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 177469

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINIMPORTEDCHARGESCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINIMPORTEDCHARGESCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `BANKREFERENCENUMBER` | CHAR(50) |  |  |  |  |
| 4 | `DUEDATEFROM` | DATE |  |  |  |  |
| 5 | `FCNO` | CHAR(3) |  |  |  |  |
| 6 | `RATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 7 | `ADJUSTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `UTILISEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `RATEDIFF` | DECIMAL(18,5) |  |  |  |  |
| 11 | `IMPORTPAYMENT` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 12 | `BANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 13 | `POSTED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINIMPORTEDCHARGES_IMPORTPAYMENT` | `FINIMPORTEDCHARGESCOMPANYCODE`, `FINIMPORTEDCHARGESCODE` | [`FINIMPORTEDCHARGES`](../FINANCE/FINIMPORTEDCHARGES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINIMPORTPAYMENTEDC.FINIMPORTEDCHARGESCOMPANYCODE = FINIMPORTEDCHARGES.COMPANYCODE AND FINIMPORTPAYMENTEDC.FINIMPORTEDCHARGESCODE = FINIMPORTEDCHARGES.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINIMPORTPAYMENTEDCUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINIMPORTEDCHARGESCOMPANYCODE,
       t.FINIMPORTEDCHARGESCODE,
       t.LINENO,
       t.BANKREFERENCENUMBER,
       t.DUEDATEFROM,
       t.FCNO,
       t.RATE,
       t.ADJUSTEDAMOUNT,
       t.UTILISEDVALUE,
       t.VALUE,
       t.RATEDIFF,
       t.IMPORTPAYMENT
FROM   DB2ADMIN.FINIMPORTPAYMENTEDC t
FETCH FIRST 100 ROWS ONLY;
```
