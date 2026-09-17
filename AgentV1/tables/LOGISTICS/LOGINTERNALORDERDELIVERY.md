# DB2ADMIN.LOGINTERNALORDERDELIVERY

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 101
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 51980

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTORDLINEINTORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `INTORDLINEINTORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `INTORDERLINEINTERNALORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `INTERNALORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `INTERNALORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 6 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 7 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `ORDERLINESTATUS` | CHAR(2) |  |  |  |  |
| 10 | `DELIVERYLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 11 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 12 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 13 | `DELIVERYDATE` | DATE |  |  |  |  |
| 14 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 15 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 16 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 17 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 18 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 19 | `RESERVATIONSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 21 | `RESERVATIONDATE` | DATE |  |  |  |  |
| 22 | `SCHEDULEDDELIVERYDATE` | DATE |  |  |  |  |
| 23 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 24 | `EFFECTIVEDELIVERYDATE` | DATE |  |  |  |  |
| 25 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 26 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 27 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 28 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 29 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 39 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 40 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 41 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 42 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 43 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 44 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 45 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 46 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 47 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 48 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 49 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 51 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 53 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 54 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 55 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 56 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 62 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `DESTINATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 67 | `TERMOFSHIPPINGANDRECEIVINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 68 | `DESTINATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 69 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 70 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 71 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 72 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 73 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 74 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 75 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 76 | `CONFIRMATION` | CHAR(15) |  |  |  |  |
| 77 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 78 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 79 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 80 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 81 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 82 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 83 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 84 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 85 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 86 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 87 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 88 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 89 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 90 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 91 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 92 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 93 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 94 | `DESTINATIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 95 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 96 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 97 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 98 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 99 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 100 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGINTERNALORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGINTERNALORDER' + known child suffix 'DELIVERY')
  - JOIN predicate: `LOGINTERNALORDERDELIVERY.FATHERID = LOGINTERNALORDER.ABSUNIQUEID`

## Starter query

```sql
SELECT t.INTORDLINEINTORDERCOMPANYCODE,
       t.INTORDLINEINTORDERCOUNTERCODE,
       t.INTORDERLINEINTERNALORDERCODE,
       t.INTERNALORDERLINEORDERLINE,
       t.INTERNALORDERLINEORDERSUBLINE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.LINETEMPLATECODE,
       t.ORDERTYPE,
       t.ORDERLINESTATUS,
       t.DELIVERYLINE,
       t.DELIVERYPOINTUNIQUEID
FROM   DB2ADMIN.LOGINTERNALORDERDELIVERY t
FETCH FIRST 100 ROWS ONLY;
```
