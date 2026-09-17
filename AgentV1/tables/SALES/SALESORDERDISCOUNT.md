# DB2ADMIN.SALESORDERDISCOUNT

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 25912

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SALESORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 4 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `DISCOUNTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 7 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 8 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `TAXAPPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 12 | `EXCLUDEDINCMSCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 13 | `EXCLUDEDINCOMMISSIONRETRIEVING` | SMALLINT | NOT NULL |  |  |  |
| 14 | `DISCOUNTGROUPCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `PAYMENTDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 17 | `DEFSALDSCDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 18 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 19 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 20 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 21 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_DISCOUNTCURRENCY` | `DISCOUNTCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `SALESORDERDISCOUNT.DISCOUNTCURRENCYCODE = CURRENCY.CODE` |
| `DISCOUNTGROUP_DISCOUNTGROUP` | `SALESORDERCOMPANYCODE`, `DISCOUNTGROUPCODE` | [`DISCOUNTGROUP`](../SALES/DISCOUNTGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESORDERDISCOUNT.SALESORDERCOMPANYCODE = DISCOUNTGROUP.COMPANYCODE AND SALESORDERDISCOUNT.DISCOUNTGROUPCODE = DISCOUNTGROUP.CODE` |
| `LOGREASON_LOGREASON` | `SALESORDERCOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESORDERDISCOUNT.SALESORDERCOMPANYCODE = LOGREASON.COMPANYCODE AND SALESORDERDISCOUNT.LOGREASONCODE = LOGREASON.CODE` |
| `SALESORDER_DISCOUNT` | `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE` | [`SALESORDER`](../SALES/SALESORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `SALESORDERDISCOUNT.SALESORDERCOMPANYCODE = SALESORDER.COMPANYCODE AND SALESORDERDISCOUNT.SALESORDERCOUNTERCODE = SALESORDER.COUNTERCODE AND SALESORDERDISCOUNT.SALESORDERCODE = SALESORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESORDERDISCOUNTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESORDERCOMPANYCODE,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.NUMBERID,
       t.SEQUENCE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN,
       t.TAXAPPLICATIONTYPE,
       t.CALCULATIONTYPE,
       t.AMOUNTCALCULATIONTYPE
FROM   DB2ADMIN.SALESORDERDISCOUNT t
FETCH FIRST 100 ROWS ONLY;
```
