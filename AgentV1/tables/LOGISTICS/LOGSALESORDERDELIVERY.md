# DB2ADMIN.LOGSALESORDERDELIVERY

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 126
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 55115

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALORDLINESALORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALORDLINESALORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `SALESORDERLINESALESORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `SALESORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `SALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `SALORDLINECOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 6 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 7 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 8 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 9 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 10 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `ORDERLINESTATUS` | CHAR(2) |  |  |  |  |
| 12 | `DELIVERYLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 13 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 14 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 15 | `DELIVERYDATE` | DATE |  |  |  |  |
| 16 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 17 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 18 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 19 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 20 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 21 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 22 | `RESERVATIONDATE` | DATE |  |  |  |  |
| 23 | `DISTRIBUTIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 24 | `SCHEDULEDDELIVERYDATE` | DATE |  |  |  |  |
| 25 | `PRODUCTIONCONFIRMEDDATE` | DATE |  |  |  |  |
| 26 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 27 | `EFFECTIVEDELIVERYDATE` | DATE |  |  |  |  |
| 28 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 29 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 30 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 31 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 32 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 41 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 42 | `SELLINGITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 43 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 44 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 45 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 46 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 47 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 48 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 49 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 50 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 51 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 52 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 54 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 56 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 58 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 60 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 62 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 67 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 68 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 69 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 70 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 71 | `TRANSFERUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 72 | `TRANSFERBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 73 | `TRANSFERUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 74 | `TRANSFERBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `TRANSFERUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `TRANSFERSTATUS` | CHAR(2) |  |  |  |  |
| 77 | `RECEIVEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 78 | `RECEIVEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `RECEIVEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 80 | `RECEIVEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 81 | `RECEIVEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 82 | `RECEIVINGSTATUS` | CHAR(2) |  |  |  |  |
| 83 | `CONSIGNMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 84 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 85 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 86 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 87 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 88 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 89 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 90 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 91 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 92 | `CONFIRMATION` | CHAR(15) |  |  |  |  |
| 93 | `CUTTINGLISTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 94 | `CUTTINGLISTCODE` | CHAR(15) |  |  |  |  |
| 95 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 96 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 97 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 98 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 99 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 100 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 101 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 102 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 103 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 104 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 105 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 106 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 107 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 108 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 109 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 110 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 111 | `DISTRIBUTIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 112 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 113 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 114 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 115 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 116 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 117 | `CONSIGNMENTWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 118 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 119 | `READYTOSHIP` | SMALLINT | NOT NULL |  |  |  |
| 120 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 121 | `SHIPPINGDATE` | DATE |  |  |  |  |
| 122 | `CUSTOMERDELIVERYDATE` | DATE |  |  |  |  |
| 123 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 124 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 125 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESORDER' + known child suffix 'DELIVERY')
  - JOIN predicate: `LOGSALESORDERDELIVERY.FATHERID = LOGSALESORDER.ABSUNIQUEID`
- child `LOGSALESORDERDELIVERYBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.SALORDLINESALORDERCOMPANYCODE,
       t.SALORDLINESALORDERCOUNTERCODE,
       t.SALESORDERLINESALESORDERCODE,
       t.SALESORDERLINEORDERLINE,
       t.SALESORDERLINEORDERSUBLINE,
       t.SALORDLINECOMPONENTORDERLINE,
       t.ABSVERSIONNUMBER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.LINETEMPLATECODE,
       t.ORDERTYPE,
       t.ORDERLINESTATUS
FROM   DB2ADMIN.LOGSALESORDERDELIVERY t
FETCH FIRST 100 ROWS ONLY;
```
