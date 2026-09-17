# DB2ADMIN.LOGPURCHASEORDERLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 130
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 65012

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURCHASEORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `PURCHASEORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 6 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 8 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 9 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 10 | `ASSORTMENTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 11 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 13 | `EXTERNALOPERATIONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `BOXMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 16 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 17 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 18 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 28 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 29 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 30 | `BOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 31 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 32 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 33 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 34 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 35 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 37 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 39 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 41 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 42 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 44 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 48 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 51 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 52 | `LINESTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 53 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 54 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 55 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 56 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 57 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 58 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 59 | `ISSUEWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 60 | `SUBCONTRACTORWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 61 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 62 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 63 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 64 | `DELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 65 | `SHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 66 | `TRANSPORTREASONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 67 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 68 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 69 | `JOINEDORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 70 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 71 | `LINESOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 72 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 73 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 74 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 75 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 76 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 77 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 78 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 79 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 80 | `SENDTOSUPPLIER` | SMALLINT | NOT NULL |  |  |  |
| 81 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 82 | `CONDITIONRETRIEVINGDATE` | DATE | NOT NULL |  |  |  |
| 83 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 84 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 85 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 86 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 87 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 88 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 89 | `PRICESIGN` | CHAR(2) | NOT NULL |  |  |  |
| 90 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 91 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 92 | `ORIGINALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 93 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 94 | `UPDATEVALUE` | SMALLINT | NOT NULL |  |  |  |
| 95 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 96 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 97 | `TAXABLEINCOMEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 98 | `NETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 99 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 100 | `MANUALLYINSERTFORBOX` | SMALLINT | NOT NULL |  |  |  |
| 101 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 102 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 103 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 104 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 105 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 106 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 107 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 108 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 109 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 110 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 111 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 112 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 113 | `BUYERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 114 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 115 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 116 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 117 | `ISSUEWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 118 | `SBCWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 119 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 120 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 121 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 122 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 123 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 124 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 125 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 126 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 127 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 128 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 129 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGPURCHASEORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGPURCHASEORDER' + known child suffix 'LINE')
  - JOIN predicate: `LOGPURCHASEORDERLINE.FATHERID = LOGPURCHASEORDER.ABSUNIQUEID`
- child `LOGPURCHASEORDERLINEBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGPURCHASEORDERLINECHARGE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGPURCHASEORDERLINEDISCOUNT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGPURCHASEORDERLINETEMPLATE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.PURCHASEORDERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.ABSVERSIONNUMBER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.ASSORTMENTNUMBERID,
       t.LINETEMPLATECODE
FROM   DB2ADMIN.LOGPURCHASEORDERLINE t
FETCH FIRST 100 ROWS ONLY;
```
