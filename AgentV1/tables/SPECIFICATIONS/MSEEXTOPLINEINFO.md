# DB2ADMIN.MSEEXTOPLINEINFO

- **Module**: `SPECIFICATIONS` (medium confidence — table name starts with 'MSE')
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `EXTOPLINECOMPANYCODE`, `EXTOPLINECOUNTERCODE`, `EXTOPLINECODE`, `EXTOPLINEORDERLINE`, `SUPPLIERTYPE`, `SUPPLIERCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 198143

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPLINECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EXTOPLINECOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EXTOPLINECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 5 | `SUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 6 | `CONFIRMEDDATE` | DATE |  |  |  |  |
| 7 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 8 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `TERMSOFDELIVERYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `DELIVERYDELAYINWRKDAYS` | INTEGER | NOT NULL |  |  |  |
| 11 | `DELIVERYDELAYINWEEKS` | DECIMAL(12,5) |  |  |  |  |
| 12 | `CONFIRMEDPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `TRANSACTIONPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `PRMDELIVEREDDELTAPERCENTAGE` | DECIMAL(18,3) | NOT NULL |  |  |  |
| 15 | `CLOSED` | SMALLINT | NOT NULL |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `ORDERDATE` | DATE |  |  |  |  |
| 18 | `COMPLETIONDATE` | DATE |  |  |  |  |
| 19 | `COMPLETIONDAYS` | INTEGER | NOT NULL |  |  |  |
| 20 | `COMPLETIONWRKDAYS` | INTEGER | NOT NULL |  |  |  |
| 21 | `COMPLETIONWEEKS` | DECIMAL(12,5) |  |  |  |  |
| 22 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 23 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 24 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EXTOPLINE_MSEINFO` | `EXTOPLINECOMPANYCODE`, `EXTOPLINECOUNTERCODE`, `EXTOPLINECODE`, `EXTOPLINEORDERLINE` | [`EXTOPLINE`](../SUBCONTRACTING/EXTOPLINE.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE`, `ORDERLINE` | RESTRICT | `MSEEXTOPLINEINFO.EXTOPLINECOMPANYCODE = EXTOPLINE.COMPANYCODE AND MSEEXTOPLINEINFO.EXTOPLINECOUNTERCODE = EXTOPLINE.COUNTERCODE AND MSEEXTOPLINEINFO.EXTOPLINECODE = EXTOPLINE.CODE AND MSEEXTOPLINEINFO.EXTOPLINEORDERLINE = EXTOPLINE.ORDERLINE` |
| `LOGREASON_LOGREASON` | `EXTOPLINECOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MSEEXTOPLINEINFO.EXTOPLINECOMPANYCODE = LOGREASON.COMPANYCODE AND MSEEXTOPLINEINFO.LOGREASONCODE = LOGREASON.CODE` |
| `TERMSOFDELIVERY_TERMSOFDELIVERY` | `TERMSOFDELIVERYCOMPANYCODE`, `TERMSOFDELIVERYCODE` | [`TERMSOFDELIVERY`](../CORE_MASTER/TERMSOFDELIVERY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MSEEXTOPLINEINFO.TERMSOFDELIVERYCOMPANYCODE = TERMSOFDELIVERY.COMPANYCODE AND MSEEXTOPLINEINFO.TERMSOFDELIVERYCODE = TERMSOFDELIVERY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MSEEXTOPLINEINFOUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EXTOPLINECOMPANYCODE,
       t.EXTOPLINECOUNTERCODE,
       t.EXTOPLINECODE,
       t.EXTOPLINEORDERLINE,
       t.SUPPLIERTYPE,
       t.SUPPLIERCODE,
       t.CONFIRMEDDATE,
       t.TRANSACTIONDATE,
       t.TERMSOFDELIVERYCOMPANYCODE,
       t.TERMSOFDELIVERYCODE,
       t.DELIVERYDELAYINWRKDAYS,
       t.DELIVERYDELAYINWEEKS
FROM   DB2ADMIN.MSEEXTOPLINEINFO t
FETCH FIRST 100 ROWS ONLY;
```
