# DB2ADMIN.EXTOPERATIONCHARGEDETAIL

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOPERATION')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `EXTOPPRCEXTOPPRCLISTCMYCODE`, `EXTOPPRICEEXTOPPRICELISTCODE`, `EXTOPPRICELINEID`, `LINEID`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30125

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
| 8 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
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
| 21 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CHARGECURRENCY` | `CHARGECURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `EXTOPERATIONCHARGEDETAIL.CHARGECURRENCYCODE = CURRENCY.CODE` |
| `EXTOPPRICE_CHARGESDETAIL` | `EXTOPPRCEXTOPPRCLISTCMYCODE`, `EXTOPPRICEEXTOPPRICELISTCODE`, `EXTOPPRICELINEID` | [`EXTOPPRICE`](../SUBCONTRACTING/EXTOPPRICE.md) | `EXTOPPRICELISTCOMPANYCODE`, `EXTOPPRICELISTCODE`, `LINEID` | RESTRICT | `EXTOPERATIONCHARGEDETAIL.EXTOPPRCEXTOPPRCLISTCMYCODE = EXTOPPRICE.EXTOPPRICELISTCOMPANYCODE AND EXTOPERATIONCHARGEDETAIL.EXTOPPRICEEXTOPPRICELISTCODE = EXTOPPRICE.EXTOPPRICELISTCODE AND EXTOPERATIONCHARGEDETAIL.EXTOPPRICELINEID = EXTOPPRICE.LINEID` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EXTOPERATIONCHARGEDETAIL.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND EXTOPERATIONCHARGEDETAIL.ITEMTYPECODE = ITEMTYPE.CODE` |
| `PAYMENTMETHOD_PAYMENTMETHOD` | `PAYMENTMETHODCOMPANYCODE`, `PAYMENTMETHODCODE` | [`PAYMENTMETHOD`](../CORE_MASTER/PAYMENTMETHOD.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EXTOPERATIONCHARGEDETAIL.PAYMENTMETHODCOMPANYCODE = PAYMENTMETHOD.COMPANYCODE AND EXTOPERATIONCHARGEDETAIL.PAYMENTMETHODCODE = PAYMENTMETHOD.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPERATIONCHARGEDETAILUID` (ABSUNIQUEID)

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
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE,
       t.VALUE
FROM   DB2ADMIN.EXTOPERATIONCHARGEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
