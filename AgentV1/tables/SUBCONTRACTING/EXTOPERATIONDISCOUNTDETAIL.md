# DB2ADMIN.EXTOPERATIONDISCOUNTDETAIL

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOPERATION')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `EXTOPPRCEXTOPPRCLISTCMYCODE`, `EXTOPPRICEEXTOPPRICELISTCODE`, `EXTOPPRICELINEID`, `LINEID`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30182

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPPRCEXTOPPRCLISTCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EXTOPPRICEEXTOPPRICELISTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EXTOPPRICELINEID` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINEID` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `BREAKDOWNLIMIT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 5 | `INITIALDATE` | DATE |  |  |  |  |
| 6 | `FINALDATE` | DATE |  |  |  |  |
| 7 | `PAYMENTMETHODCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `DISCOUNTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 11 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `TAXAPPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_DISCOUNTCURRENCY` | `DISCOUNTCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `EXTOPERATIONDISCOUNTDETAIL.DISCOUNTCURRENCYCODE = CURRENCY.CODE` |
| `EXTOPPRICE_DISCOUNTDETAIL` | `EXTOPPRCEXTOPPRCLISTCMYCODE`, `EXTOPPRICEEXTOPPRICELISTCODE`, `EXTOPPRICELINEID` | [`EXTOPPRICE`](../SUBCONTRACTING/EXTOPPRICE.md) | `EXTOPPRICELISTCOMPANYCODE`, `EXTOPPRICELISTCODE`, `LINEID` | RESTRICT | `EXTOPERATIONDISCOUNTDETAIL.EXTOPPRCEXTOPPRCLISTCMYCODE = EXTOPPRICE.EXTOPPRICELISTCOMPANYCODE AND EXTOPERATIONDISCOUNTDETAIL.EXTOPPRICEEXTOPPRICELISTCODE = EXTOPPRICE.EXTOPPRICELISTCODE AND EXTOPERATIONDISCOUNTDETAIL.EXTOPPRICELINEID = EXTOPPRICE.LINEID` |
| `PAYMENTMETHOD_PAYMENTMETHOD` | `PAYMENTMETHODCOMPANYCODE`, `PAYMENTMETHODCODE` | [`PAYMENTMETHOD`](../CORE_MASTER/PAYMENTMETHOD.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EXTOPERATIONDISCOUNTDETAIL.PAYMENTMETHODCOMPANYCODE = PAYMENTMETHOD.COMPANYCODE AND EXTOPERATIONDISCOUNTDETAIL.PAYMENTMETHODCODE = PAYMENTMETHOD.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPERATIONDISCOUNTDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EXTOPPRCEXTOPPRCLISTCMYCODE,
       t.EXTOPPRICEEXTOPPRICELISTCODE,
       t.EXTOPPRICELINEID,
       t.LINEID,
       t.BREAKDOWNLIMIT,
       t.INITIALDATE,
       t.FINALDATE,
       t.PAYMENTMETHODCODE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN
FROM   DB2ADMIN.EXTOPERATIONDISCOUNTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
