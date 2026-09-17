# DB2ADMIN.EXTOPLINECHARGE

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `EXTOPLINECOMPANYCODE`, `EXTOPLINECOUNTERCODE`, `EXTOPLINECODE`, `EXTOPLINEORDERLINE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30284

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPLINECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EXTOPLINECOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EXTOPLINECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 5 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 8 | `CHARGETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `CHARGECURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 11 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 14 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 15 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 16 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 17 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CHARGECURRENCY` | `CHARGECURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `EXTOPLINECHARGE.CHARGECURRENCYCODE = CURRENCY.CODE` |
| `EXTOPLINE_CHARGE` | `EXTOPLINECOMPANYCODE`, `EXTOPLINECOUNTERCODE`, `EXTOPLINECODE`, `EXTOPLINEORDERLINE` | [`EXTOPLINE`](../SUBCONTRACTING/EXTOPLINE.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE`, `ORDERLINE` | RESTRICT | `EXTOPLINECHARGE.EXTOPLINECOMPANYCODE = EXTOPLINE.COMPANYCODE AND EXTOPLINECHARGE.EXTOPLINECOUNTERCODE = EXTOPLINE.COUNTERCODE AND EXTOPLINECHARGE.EXTOPLINECODE = EXTOPLINE.CODE AND EXTOPLINECHARGE.EXTOPLINEORDERLINE = EXTOPLINE.ORDERLINE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EXTOPLINECHARGE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND EXTOPLINECHARGE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `LOGREASON_LOGREASON` | `EXTOPLINECOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EXTOPLINECHARGE.EXTOPLINECOMPANYCODE = LOGREASON.COMPANYCODE AND EXTOPLINECHARGE.LOGREASONCODE = LOGREASON.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPLINECHARGEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EXTOPLINECOMPANYCODE,
       t.EXTOPLINECOUNTERCODE,
       t.EXTOPLINECODE,
       t.EXTOPLINEORDERLINE,
       t.NUMBERID,
       t.SEQUENCE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE,
       t.VALUE,
       t.CHARGECURRENCYCODE,
       t.SIGN
FROM   DB2ADMIN.EXTOPLINECHARGE t
FETCH FIRST 100 ROWS ONLY;
```
