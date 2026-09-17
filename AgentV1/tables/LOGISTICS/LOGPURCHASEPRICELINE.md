# DB2ADMIN.LOGPURCHASEPRICELINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 46
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 116866

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURCHASEPRICELISTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PURCHASEPRICELISTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `LINEID` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 3 | `TEMPLATEDEFINITIONTYPE` | CHAR(1) |  |  |  |  |
| 4 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 18 | `BREAKDOWNTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 19 | `DISCOUNTBREAKDOWNTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 20 | `CHARGEBREAKDOWNTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 21 | `DISCOUNTLIMITCALCULATIONMODE` | CHAR(2) | NOT NULL |  |  |  |
| 22 | `CHARGELIMITCALCULATIONMODE` | CHAR(2) | NOT NULL |  |  |  |
| 23 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 24 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 25 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 26 | `MINIMUMBATCHQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `MINIMUMBATCHUOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `PRIORITY` | INTEGER | NOT NULL |  |  |  |
| 29 | `INITIALDATE` | DATE |  |  |  |  |
| 30 | `FINALDATE` | DATE |  |  |  |  |
| 31 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 32 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 33 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 34 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 36 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 37 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 38 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 39 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 40 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 41 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 42 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 43 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 44 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 45 | `PROTOTYPEMANAGED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPURCHASEPRICELINE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.PURCHASEPRICELISTCOMPANYCODE,
       t.PURCHASEPRICELISTCODE,
       t.LINEID,
       t.TEMPLATEDEFINITIONTYPE,
       t.TEMPLATECODE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.LOGPURCHASEPRICELINE t
FETCH FIRST 100 ROWS ONLY;
```
