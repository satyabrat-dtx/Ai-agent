# DB2ADMIN.LOGINTERNALDOCUMENTLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 134
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 51552

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTERNALDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `INTDOCPROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `INTDOCUMENTPROVISIONALCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 5 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 7 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 8 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 9 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `RECEIVINGSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 13 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 14 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 15 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 16 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 17 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 18 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 19 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 29 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 30 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
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
| 42 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 44 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `RECEIVEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 48 | `RECEIVEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `RECEIVEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `RECEIVEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `RECEIVEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 54 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 56 | `DESTINATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 57 | `TERMOFSHIPPINGANDRECEIVINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 58 | `DESTINATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 59 | `RECEIVINGDATE` | DATE |  |  |  |  |
| 60 | `LINESTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 61 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 62 | `RECEIVINGSTATUS` | CHAR(2) |  |  |  |  |
| 63 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 64 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 65 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 66 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 67 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 68 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 69 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 70 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 71 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 72 | `QUANTITYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 73 | `PICKINGCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 74 | `PICKINGCODE` | CHAR(15) |  |  |  |  |
| 75 | `JOINEDORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 76 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 77 | `LINESOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 78 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 79 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 80 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 81 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 82 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 83 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 84 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 85 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 86 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 87 | `DLVINTORDLINEINTORDCNTCODE` | CHAR(8) |  |  |  |  |
| 88 | `DLVINTORDLINEINTORDERCODE` | CHAR(15) |  |  |  |  |
| 89 | `DLVINTERNALORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 90 | `DLVINTORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 91 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 92 | `ORIGINTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 93 | `ORIGINORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 94 | `ORIGINORDERCODE` | CHAR(15) |  |  |  |  |
| 95 | `ORIGINLINE` | DECIMAL(7,0) |  |  |  |  |
| 96 | `ORIGINDETAILLINE` | DECIMAL(3,0) |  |  |  |  |
| 97 | `CONDITIONRETRIEVINGDATE` | DATE | NOT NULL |  |  |  |
| 98 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 99 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 100 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 101 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 102 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 103 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 104 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 105 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 106 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 107 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 108 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 109 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 110 | `DESTINATIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 111 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 112 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 113 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 114 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 115 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 116 | `ORIGINORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 117 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 118 | `PMWORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 119 | `PMWORKORDERCODE` | CHAR(15) |  |  |  |  |
| 120 | `PMMACHINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 121 | `PMMACHINECODE` | CHAR(15) |  |  |  |  |
| 122 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 123 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 124 | `NORECEIVEUSERPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 125 | `NORECEIVEBASEPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 126 | `NORECEIVEUSERSECONDARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 127 | `NORECEIVEBASESECONDARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 128 | `NORECEIVEUSERPACKAGINGQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 129 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 130 | `DESTPHYSWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 131 | `DESTPHYSWHSCODE` | CHAR(8) |  |  |  |  |
| 132 | `DESTZONECODE` | CHAR(3) |  |  |  |  |
| 133 | `DESTLOCATIONCODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGINTERNALDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'LOGINTERNALDOCUMENT' + known child suffix 'LINE')
  - JOIN predicate: `LOGINTERNALDOCUMENTLINE.FATHERID = LOGINTERNALDOCUMENT.ABSUNIQUEID`
- child `LOGINTERNALDOCUMENTLINEBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.INTERNALDOCUMENTCOMPANYCODE,
       t.INTDOCPROVISIONALCOUNTERCODE,
       t.INTDOCUMENTPROVISIONALCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.STOCKTYPECODE,
       t.RECEIVINGSTOCKTYPECODE,
       t.LINETEMPLATECODE
FROM   DB2ADMIN.LOGINTERNALDOCUMENTLINE t
FETCH FIRST 100 ROWS ONLY;
```
