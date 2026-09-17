# DB2ADMIN.FINIMPFCPAYMENTDETAILS

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `FINIMPORTFCPAYMENTCOMPANYCODE`, `FINIMPORTFCPAYMENTCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 177165

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINIMPORTFCPAYMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINIMPORTFCPAYMENTCODE` | CHAR(5) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `BANKREFERENCENUMBER` | CHAR(50) |  |  |  |  |
| 4 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 5 | `DUEDATEFROM` | DATE |  |  |  |  |
| 6 | `FCRATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 7 | `UTILISEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `ADJUSTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `FCNOCODE` | CHAR(5) |  | FK | foreign_key |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `FINIMPFCPAYMENTDETAILS.CURRENCYCODE = CURRENCY.CODE` |
| `FINIMPORTFCPAYMENT_LINE` | `FINIMPORTFCPAYMENTCOMPANYCODE`, `FINIMPORTFCPAYMENTCODE` | [`FINIMPORTFCPAYMENT`](../FINANCE/FINIMPORTFCPAYMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINIMPFCPAYMENTDETAILS.FINIMPORTFCPAYMENTCOMPANYCODE = FINIMPORTFCPAYMENT.COMPANYCODE AND FINIMPFCPAYMENTDETAILS.FINIMPORTFCPAYMENTCODE = FINIMPORTFCPAYMENT.CODE` |
| `FINIMPORTFC_FCNO` | `FINIMPORTFCPAYMENTCOMPANYCODE`, `FCNOCODE` | [`FINIMPORTFC`](../FINANCE/FINIMPORTFC.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINIMPFCPAYMENTDETAILS.FINIMPORTFCPAYMENTCOMPANYCODE = FINIMPORTFC.COMPANYCODE AND FINIMPFCPAYMENTDETAILS.FCNOCODE = FINIMPORTFC.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINIMPFCPAYMENTDETAILSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINIMPORTFCPAYMENTCOMPANYCODE,
       t.FINIMPORTFCPAYMENTCODE,
       t.LINENO,
       t.BANKREFERENCENUMBER,
       t.CURRENCYCODE,
       t.DUEDATEFROM,
       t.FCRATE,
       t.UTILISEDVALUE,
       t.VALUE,
       t.ADJUSTEDAMOUNT,
       t.FCNOCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINIMPFCPAYMENTDETAILS t
FETCH FIRST 100 ROWS ONLY;
```
