# DB2ADMIN.LOGSALESORDERLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 157
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 55375

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `SALESORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 5 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 7 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 8 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 9 | `COMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 10 | `ASSORTMENTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 11 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `SAMPLESTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `BOXMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 15 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 16 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 17 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 18 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 19 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 21 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 31 | `SELLINGITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 32 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 33 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 34 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 35 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 36 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 37 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 38 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 40 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 41 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 44 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 48 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 54 | `LINESTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 55 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 56 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 57 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 58 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 59 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 60 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 61 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 62 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 63 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 64 | `DISTRIBUTIONWAREHOUSEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 65 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 66 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 67 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 68 | `JOINEDORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 69 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 70 | `JOINEDCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 71 | `LINESOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 72 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 73 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 74 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 75 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 76 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 77 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 78 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 79 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 80 | `INTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 81 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 82 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 83 | `CONDITIONRETRIEVINGDATE` | DATE | NOT NULL |  |  |  |
| 84 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 85 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 86 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 87 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 88 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 89 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 90 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 91 | `PRICESIGN` | CHAR(2) | NOT NULL |  |  |  |
| 92 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 93 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 94 | `ORIGINALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 95 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 96 | `UPDATEVALUE` | SMALLINT | NOT NULL |  |  |  |
| 97 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 98 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 99 | `TAXABLEINCOMEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 100 | `NETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 101 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 102 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 103 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 104 | `AGENTCREATIONTYPE1` | CHAR(1) | NOT NULL |  |  |  |
| 105 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 106 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 107 | `AGENTCREATIONTYPE2` | CHAR(1) | NOT NULL |  |  |  |
| 108 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 109 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 110 | `AGENTCREATIONTYPE3` | CHAR(1) | NOT NULL |  |  |  |
| 111 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 112 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 113 | `AGENTCREATIONTYPE4` | CHAR(1) | NOT NULL |  |  |  |
| 114 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 115 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 116 | `AGENTCREATIONTYPE5` | CHAR(1) | NOT NULL |  |  |  |
| 117 | `MANUALLYINSERTFORBOX` | SMALLINT | NOT NULL |  |  |  |
| 118 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 119 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 120 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 121 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 122 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 123 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 124 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 125 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 126 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 127 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 128 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 129 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 130 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 131 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 132 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 133 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 134 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 135 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 136 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 137 | `PURORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 138 | `PURORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 139 | `POUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 140 | `POUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 141 | `POUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 142 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 143 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 144 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 145 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 146 | `SUBPROJECTCODE` | DECIMAL(5,0) |  |  |  |  |
| 147 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 148 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 149 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 150 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 151 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 152 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 153 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 154 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 155 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 156 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESORDER' + known child suffix 'LINE')
  - JOIN predicate: `LOGSALESORDERLINE.FATHERID = LOGSALESORDER.ABSUNIQUEID`
- child `LOGSALESORDERLINEBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESORDERLINECHARGE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESORDERLINECOMMISSION`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)
- child `LOGSALESORDERLINEDISCOUNT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESORDERLINEPRICE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESORDERLINETEMPLATE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.SALESORDERCOMPANYCODE,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.COMPONENTORDERLINE,
       t.ASSORTMENTNUMBERID,
       t.LINETEMPLATECODE
FROM   DB2ADMIN.LOGSALESORDERLINE t
FETCH FIRST 100 ROWS ONLY;
```
