# DB2ADMIN.PURCHASEORDERCHARGE

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 28569

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURCHASEORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PURCHASEORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 4 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 7 | `CHARGETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `CHARGECURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 10 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 13 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 15 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 16 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CHARGECURRENCY` | `CHARGECURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `PURCHASEORDERCHARGE.CHARGECURRENCYCODE = CURRENCY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEORDERCHARGE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND PURCHASEORDERCHARGE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `LOGREASON_LOGREASON` | `PURCHASEORDERCOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEORDERCHARGE.PURCHASEORDERCOMPANYCODE = LOGREASON.COMPANYCODE AND PURCHASEORDERCHARGE.LOGREASONCODE = LOGREASON.CODE` |
| `PURCHASEORDER_CHARGE` | `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE` | [`PURCHASEORDER`](../PURCHASING/PURCHASEORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PURCHASEORDERCHARGE.PURCHASEORDERCOMPANYCODE = PURCHASEORDER.COMPANYCODE AND PURCHASEORDERCHARGE.PURCHASEORDERCOUNTERCODE = PURCHASEORDER.COUNTERCODE AND PURCHASEORDERCHARGE.PURCHASEORDERCODE = PURCHASEORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDERCHARGEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PURCHASEORDERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.NUMBERID,
       t.SEQUENCE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE,
       t.VALUE,
       t.CHARGECURRENCYCODE,
       t.SIGN,
       t.CALCULATIONTYPE
FROM   DB2ADMIN.PURCHASEORDERCHARGE t
FETCH FIRST 100 ROWS ONLY;
```
