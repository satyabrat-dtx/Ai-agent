# DB2ADMIN.LOGPURCHASEORDERDELIVERY

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 105
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 64886

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURORDLINEPURORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PURORDLINEPURORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `PURORDERLINEPURCHASEORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `PURCHASEORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `PURCHASEORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 6 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 7 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 8 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 9 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `ORDERLINESTATUS` | CHAR(2) |  |  |  |  |
| 11 | `DELIVERYLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 12 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 13 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 14 | `DELIVERYDATE` | DATE |  |  |  |  |
| 15 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 16 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 17 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 18 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 19 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 21 | `RESERVATIONDATE` | DATE |  |  |  |  |
| 22 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 23 | `EFFECTIVEDELIVERYDATE` | DATE |  |  |  |  |
| 24 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 25 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 26 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 27 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 28 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 38 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 39 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 40 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 41 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 42 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 43 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 44 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 45 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 46 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 48 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 52 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 54 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 56 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 62 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 66 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 67 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 68 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 69 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 70 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 71 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 72 | `CONFIRMATION` | CHAR(15) |  |  |  |  |
| 73 | `REMINDERCOMMENTCODE` | CHAR(12) |  |  |  |  |
| 74 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 75 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 76 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 77 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 78 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 79 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 80 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 81 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 82 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 83 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 84 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 85 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 86 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 87 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 88 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 89 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 90 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 91 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 92 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 93 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 94 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 95 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 96 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 97 | `REMINDERCOMMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 98 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 99 | `ORIGCONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 100 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 101 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 102 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 103 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 104 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGPURCHASEORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGPURCHASEORDER' + known child suffix 'DELIVERY')
  - JOIN predicate: `LOGPURCHASEORDERDELIVERY.FATHERID = LOGPURCHASEORDER.ABSUNIQUEID`

## Starter query

```sql
SELECT t.PURORDLINEPURORDERCOMPANYCODE,
       t.PURORDLINEPURORDERCOUNTERCODE,
       t.PURORDERLINEPURCHASEORDERCODE,
       t.PURCHASEORDERLINEORDERLINE,
       t.PURCHASEORDERLINEORDERSUBLINE,
       t.ABSVERSIONNUMBER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.LINETEMPLATECODE,
       t.ORDERTYPE,
       t.ORDERLINESTATUS,
       t.DELIVERYLINE
FROM   DB2ADMIN.LOGPURCHASEORDERDELIVERY t
FETCH FIRST 100 ROWS ONLY;
```
