# DB2ADMIN.PURCHASEDISCOUNTHEADER

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `PURCHASEPRICELISTCOMPANYCODE`, `PURCHASEPRICELISTCODE`, `LINEID`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 283

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURCHASEPRICELISTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PURCHASEPRICELISTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINEID` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 3 | `INITIALDATE` | DATE |  |  |  |  |
| 4 | `FINALDATE` | DATE |  |  |  |  |
| 5 | `PAYMENTMETHODCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `DISCOUNTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 8 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 9 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `TAXAPPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_DISCOUNTCURRENCY` | `DISCOUNTCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `PURCHASEDISCOUNTHEADER.DISCOUNTCURRENCYCODE = CURRENCY.CODE` |
| `PAYMENTMETHOD_PAYMENTMETHOD` | `PAYMENTMETHODCOMPANYCODE`, `PAYMENTMETHODCODE` | [`PAYMENTMETHOD`](../CORE_MASTER/PAYMENTMETHOD.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEDISCOUNTHEADER.PAYMENTMETHODCOMPANYCODE = PAYMENTMETHOD.COMPANYCODE AND PURCHASEDISCOUNTHEADER.PAYMENTMETHODCODE = PAYMENTMETHOD.CODE` |
| `PURCHASEPRICELIST_DISCOUNTHEADER` | `PURCHASEPRICELISTCOMPANYCODE`, `PURCHASEPRICELISTCODE` | [`PURCHASEPRICELIST`](../PURCHASING/PURCHASEPRICELIST.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEDISCOUNTHEADER.PURCHASEPRICELISTCOMPANYCODE = PURCHASEPRICELIST.COMPANYCODE AND PURCHASEDISCOUNTHEADER.PURCHASEPRICELISTCODE = PURCHASEPRICELIST.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEDISCOUNTHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PURCHASEPRICELISTCOMPANYCODE,
       t.PURCHASEPRICELISTCODE,
       t.LINEID,
       t.INITIALDATE,
       t.FINALDATE,
       t.PAYMENTMETHODCODE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN,
       t.TAXAPPLICATIONTYPE,
       t.CALCULATIONTYPE
FROM   DB2ADMIN.PURCHASEDISCOUNTHEADER t
FETCH FIRST 100 ROWS ONLY;
```
