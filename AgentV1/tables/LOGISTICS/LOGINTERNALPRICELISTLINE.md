# DB2ADMIN.LOGINTERNALPRICELISTLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 69
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191713

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTPRCLISTDLTINTPRCLISTCMYCOD` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `INTPRCLISTDLTINTPRICELISTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `INTPRCLISTDETAILCOSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `INTPRCLISTDETAILITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `INTPRICELISTDETAILPLANTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 5 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 15 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 17 | `VALIDFROMDATE` | DATE | NOT NULL |  |  |  |
| 18 | `PRICE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 19 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 20 | `VALIDTODATE` | DATE |  |  |  |  |
| 21 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 22 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 23 | `PERCENTCATEGORY1` | DECIMAL(6,3) |  |  |  |  |
| 24 | `PERCENTCATEGORY2` | DECIMAL(6,3) |  |  |  |  |
| 25 | `PERCENTCATEGORY3` | DECIMAL(6,3) |  |  |  |  |
| 26 | `PERCENTCATEGORY4` | DECIMAL(6,3) |  |  |  |  |
| 27 | `PERCENTCATEGORY5` | DECIMAL(6,3) |  |  |  |  |
| 28 | `PERCENTCATEGORY6` | DECIMAL(6,3) |  |  |  |  |
| 29 | `PERCENTCATEGORY7` | DECIMAL(6,3) |  |  |  |  |
| 30 | `PERCENTCATEGORY8` | DECIMAL(6,3) |  |  |  |  |
| 31 | `PERCENTCATEGORY9` | DECIMAL(6,3) |  |  |  |  |
| 32 | `PERCENTCATEGORY10` | DECIMAL(6,3) |  |  |  |  |
| 33 | `PERCENTCATEGORY11` | DECIMAL(6,3) |  |  |  |  |
| 34 | `PERCENTCATEGORY12` | DECIMAL(6,3) |  |  |  |  |
| 35 | `PERCENTCATEGORY0` | DECIMAL(6,3) |  |  |  |  |
| 36 | `QUANTITYLIMITFROM` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 37 | `QUANTITYLIMITTO` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 38 | `SELECTPRIMORSEC` | INTEGER | NOT NULL |  |  |  |
| 39 | `PRICECHANGEOVER` | DECIMAL(5,2) |  |  |  |  |
| 40 | `EVERYQTYADD` | DECIMAL(9,0) |  |  |  |  |
| 41 | `PRICECHANGEUNDER` | DECIMAL(5,2) |  |  |  |  |
| 42 | `EVERYQTYSUB` | DECIMAL(9,0) |  |  |  |  |
| 43 | `LOWESTPRICE` | DECIMAL(18,5) |  |  |  |  |
| 44 | `PRICE1` | DECIMAL(18,5) |  |  |  |  |
| 45 | `QUANTITYLIMIT1FROM` | DECIMAL(15,5) |  |  |  |  |
| 46 | `QUANTITYLIMIT1TO` | DECIMAL(15,5) |  |  |  |  |
| 47 | `PRICE2` | DECIMAL(18,5) |  |  |  |  |
| 48 | `QUANTITYLIMIT2FROM` | DECIMAL(9,0) |  |  |  |  |
| 49 | `QUANTITYLIMIT2TO` | DECIMAL(15,5) |  |  |  |  |
| 50 | `PRICE3` | DECIMAL(18,5) |  |  |  |  |
| 51 | `QUANTITYLIMIT3FROM` | DECIMAL(9,0) |  |  |  |  |
| 52 | `QUANTITYLIMIT3TO` | DECIMAL(15,5) |  |  |  |  |
| 53 | `PRICE4` | DECIMAL(18,5) |  |  |  |  |
| 54 | `QUANTITYLIMIT4FROM` | DECIMAL(9,0) |  |  |  |  |
| 55 | `QUANTITYLIMIT4TO` | DECIMAL(15,5) |  |  |  |  |
| 56 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 57 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 58 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 59 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 60 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 61 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 62 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 63 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 64 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 65 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 66 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 67 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 68 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGINTERNALPRICELISTLINE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.INTPRCLISTDLTINTPRCLISTCMYCOD,
       t.INTPRCLISTDLTINTPRICELISTCODE,
       t.INTPRCLISTDETAILCOSTGROUPCODE,
       t.INTPRCLISTDETAILITEMTYPECODE,
       t.INTPRICELISTDETAILPLANTCODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.LOGINTERNALPRICELISTLINE t
FETCH FIRST 100 ROWS ONLY;
```
