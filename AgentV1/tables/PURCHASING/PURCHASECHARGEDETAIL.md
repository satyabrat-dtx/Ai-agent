# DB2ADMIN.PURCHASECHARGEDETAIL

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `PURPRCLINEPURPRCLISTCMYCODE`, `PURPRCLINEPURPRICELISTCODE`, `PURCHASEPRICELINELINEID`, `LINEID`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 27645

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURPRCLINEPURPRCLISTCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PURPRCLINEPURPRICELISTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PURCHASEPRICELINELINEID` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINEID` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `BREAKDOWNLIMIT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 5 | `INITIALDATE` | DATE |  |  |  |  |
| 6 | `FINALDATE` | DATE |  |  |  |  |
| 7 | `PAYMENTMETHODCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 10 | `CHARGETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 12 | `CHARGECURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 13 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 15 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CHARGECURRENCY` | `CHARGECURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `PURCHASECHARGEDETAIL.CHARGECURRENCYCODE = CURRENCY.CODE` |
| `PAYMENTMETHOD_PAYMENTMETHOD` | `PAYMENTMETHODCOMPANYCODE`, `PAYMENTMETHODCODE` | [`PAYMENTMETHOD`](../CORE_MASTER/PAYMENTMETHOD.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASECHARGEDETAIL.PAYMENTMETHODCOMPANYCODE = PAYMENTMETHOD.COMPANYCODE AND PURCHASECHARGEDETAIL.PAYMENTMETHODCODE = PAYMENTMETHOD.CODE` |
| `PURCHASEPRICELINE_CHARGESDETAIL` | `PURPRCLINEPURPRCLISTCMYCODE`, `PURPRCLINEPURPRICELISTCODE`, `PURCHASEPRICELINELINEID` | [`PURCHASEPRICELINE`](../PURCHASING/PURCHASEPRICELINE.md) | `PURCHASEPRICELISTCOMPANYCODE`, `PURCHASEPRICELISTCODE`, `LINEID` | RESTRICT | `PURCHASECHARGEDETAIL.PURPRCLINEPURPRCLISTCMYCODE = PURCHASEPRICELINE.PURCHASEPRICELISTCOMPANYCODE AND PURCHASECHARGEDETAIL.PURPRCLINEPURPRICELISTCODE = PURCHASEPRICELINE.PURCHASEPRICELISTCODE AND PURCHASECHARGEDETAIL.PURCHASEPRICELINELINEID = PURCHASEPRICELINE.LINEID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASECHARGEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PURPRCLINEPURPRCLISTCMYCODE,
       t.PURPRCLINEPURPRICELISTCODE,
       t.PURCHASEPRICELINELINEID,
       t.LINEID,
       t.BREAKDOWNLIMIT,
       t.INITIALDATE,
       t.FINALDATE,
       t.PAYMENTMETHODCODE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE,
       t.VALUE
FROM   DB2ADMIN.PURCHASECHARGEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
