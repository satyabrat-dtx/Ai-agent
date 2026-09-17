# DB2ADMIN.PURCHASEORDERDISCOUNT

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 23550

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURCHASEORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PURCHASEORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 4 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `DISCOUNTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 7 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 8 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `TAXAPPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 12 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 14 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 15 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_DISCOUNTCURRENCY` | `DISCOUNTCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `PURCHASEORDERDISCOUNT.DISCOUNTCURRENCYCODE = CURRENCY.CODE` |
| `LOGREASON_LOGREASON` | `PURCHASEORDERCOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEORDERDISCOUNT.PURCHASEORDERCOMPANYCODE = LOGREASON.COMPANYCODE AND PURCHASEORDERDISCOUNT.LOGREASONCODE = LOGREASON.CODE` |
| `PURCHASEORDER_DISCOUNT` | `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE` | [`PURCHASEORDER`](../PURCHASING/PURCHASEORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PURCHASEORDERDISCOUNT.PURCHASEORDERCOMPANYCODE = PURCHASEORDER.COMPANYCODE AND PURCHASEORDERDISCOUNT.PURCHASEORDERCOUNTERCODE = PURCHASEORDER.COUNTERCODE AND PURCHASEORDERDISCOUNT.PURCHASEORDERCODE = PURCHASEORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDERDISCOUNTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PURCHASEORDERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.NUMBERID,
       t.SEQUENCE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN,
       t.TAXAPPLICATIONTYPE,
       t.CALCULATIONTYPE,
       t.AMOUNTCALCULATIONTYPE
FROM   DB2ADMIN.PURCHASEORDERDISCOUNT t
FETCH FIRST 100 ROWS ONLY;
```
