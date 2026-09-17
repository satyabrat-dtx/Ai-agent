# DB2ADMIN.EXTOPLINEDISCOUNT

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `EXTOPLINECOMPANYCODE`, `EXTOPLINECOUNTERCODE`, `EXTOPLINECODE`, `EXTOPLINEORDERLINE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30397

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPLINECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EXTOPLINECOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EXTOPLINECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 5 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 6 | `DISCOUNTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 8 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 9 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `TAXAPPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
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
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_DISCOUNTCURRENCY` | `DISCOUNTCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `EXTOPLINEDISCOUNT.DISCOUNTCURRENCYCODE = CURRENCY.CODE` |
| `EXTOPLINE_DISCOUNTS` | `EXTOPLINECOMPANYCODE`, `EXTOPLINECOUNTERCODE`, `EXTOPLINECODE`, `EXTOPLINEORDERLINE` | [`EXTOPLINE`](../SUBCONTRACTING/EXTOPLINE.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE`, `ORDERLINE` | RESTRICT | `EXTOPLINEDISCOUNT.EXTOPLINECOMPANYCODE = EXTOPLINE.COMPANYCODE AND EXTOPLINEDISCOUNT.EXTOPLINECOUNTERCODE = EXTOPLINE.COUNTERCODE AND EXTOPLINEDISCOUNT.EXTOPLINECODE = EXTOPLINE.CODE AND EXTOPLINEDISCOUNT.EXTOPLINEORDERLINE = EXTOPLINE.ORDERLINE` |
| `LOGREASON_LOGREASON` | `EXTOPLINECOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EXTOPLINEDISCOUNT.EXTOPLINECOMPANYCODE = LOGREASON.COMPANYCODE AND EXTOPLINEDISCOUNT.LOGREASONCODE = LOGREASON.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPLINEDISCOUNTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EXTOPLINECOMPANYCODE,
       t.EXTOPLINECOUNTERCODE,
       t.EXTOPLINECODE,
       t.EXTOPLINEORDERLINE,
       t.NUMBERID,
       t.SEQUENCE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN,
       t.TAXAPPLICATIONTYPE,
       t.CALCULATIONTYPE
FROM   DB2ADMIN.EXTOPLINEDISCOUNT t
FETCH FIRST 100 ROWS ONLY;
```
