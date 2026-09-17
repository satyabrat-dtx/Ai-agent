# DB2ADMIN.BILLOFLADINGDETAIL

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `BILLOFLADINGCOMPANYCODE`, `BILLOFLADINGDIVISIONCODE`, `BILLOFLADINGCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 135198

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BILLOFLADINGCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `BILLOFLADINGDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `BILLOFLADINGCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `INVOICETYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `INVOICENO` | CHAR(15) | NOT NULL |  |  |  |
| 6 | `INVOICEDATE` | DATE | NOT NULL |  |  |  |
| 7 | `GROSSWEIGHT` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 8 | `NETWEIGHT` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 9 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `PRIMARYUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `SECONDARYUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `PACKINGUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 16 | `VALUEINCURRENCY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 17 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 18 | `VALUEINCOMPANYCURRENCY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BILLOFLADING_DETAIL` | `BILLOFLADINGCOMPANYCODE`, `BILLOFLADINGDIVISIONCODE`, `BILLOFLADINGCODE` | [`BILLOFLADING`](../OTHER/BILLOFLADING.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `BILLOFLADINGDETAIL.BILLOFLADINGCOMPANYCODE = BILLOFLADING.COMPANYCODE AND BILLOFLADINGDETAIL.BILLOFLADINGDIVISIONCODE = BILLOFLADING.DIVISIONCODE AND BILLOFLADINGDETAIL.BILLOFLADINGCODE = BILLOFLADING.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `BILLOFLADINGDETAIL.CURRENCYCODE = CURRENCY.CODE` |
| `INVOICETYPE_INVOICETYPE` | `BILLOFLADINGCOMPANYCODE`, `BILLOFLADINGDIVISIONCODE`, `INVOICETYPECODE` | [`INVOICETYPE`](../SALES/INVOICETYPE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `BILLOFLADINGDETAIL.BILLOFLADINGCOMPANYCODE = INVOICETYPE.COMPANYCODE AND BILLOFLADINGDETAIL.BILLOFLADINGDIVISIONCODE = INVOICETYPE.DIVISIONCODE AND BILLOFLADINGDETAIL.INVOICETYPECODE = INVOICETYPE.CODE` |
| `UNITOFMEASURE_PACKINGUM` | `PACKINGUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `BILLOFLADINGDETAIL.PACKINGUMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_PRIMARYUM` | `PRIMARYUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `BILLOFLADINGDETAIL.PRIMARYUMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_SECONDARYUM` | `SECONDARYUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `BILLOFLADINGDETAIL.SECONDARYUMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BILLOFLADINGDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BILLOFLADINGCOMPANYCODE,
       t.BILLOFLADINGDIVISIONCODE,
       t.BILLOFLADINGCODE,
       t.LINENO,
       t.INVOICETYPECODE,
       t.INVOICENO,
       t.INVOICEDATE,
       t.GROSSWEIGHT,
       t.NETWEIGHT,
       t.PRIMARYQTY,
       t.PRIMARYUMCODE,
       t.SECONDARYQTY
FROM   DB2ADMIN.BILLOFLADINGDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
