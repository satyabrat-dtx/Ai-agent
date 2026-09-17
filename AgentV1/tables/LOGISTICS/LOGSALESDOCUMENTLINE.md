# DB2ADMIN.LOGSALESDOCUMENTLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 170
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 54340

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALDOCPROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `SALESDOCUMENTPROVISIONALCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 5 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 7 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 8 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 9 | `COMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 10 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
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
| 29 | `SELLINGITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 30 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 31 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 32 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 33 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 34 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 36 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 37 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 38 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 40 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 41 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 44 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 48 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `CREDITUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `CREDITBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `CREDITUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 54 | `CREDITBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `CREDITUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 56 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 57 | `CONSIGNMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 58 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 59 | `LINESTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 60 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 61 | `INVOICEEVOLUTIONTYPE` | CHAR(2) |  |  |  |  |
| 62 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 63 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 64 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 65 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 66 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 67 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 68 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 69 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 70 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 71 | `QUANTITYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 72 | `PICKINGCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 73 | `PICKINGCODE` | CHAR(15) |  |  |  |  |
| 74 | `JOINEDORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 75 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 76 | `JOINEDCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 77 | `LINESOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 78 | `PREVIOUSORIGINFROM` | CHAR(2) |  |  |  |  |
| 79 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 80 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 81 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 82 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 83 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 84 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 85 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 86 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 87 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 88 | `DLVSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 89 | `DLVSALORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 90 | `DLVSALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 91 | `DLVSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 92 | `DLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 93 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 94 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 95 | `CONDITIONRETRIEVINGDATE` | DATE | NOT NULL |  |  |  |
| 96 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 97 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 98 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 99 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 100 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 101 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 102 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 103 | `PRICESIGN` | CHAR(2) | NOT NULL |  |  |  |
| 104 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 105 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 106 | `ORIGINALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 107 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 108 | `UPDATEVALUE` | SMALLINT | NOT NULL |  |  |  |
| 109 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 110 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 111 | `TAXABLEINCOMEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 112 | `NETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 113 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 114 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 115 | `CHARGECREATIONTYPE` | CHAR(1) |  |  |  |  |
| 116 | `FREEGIFTDISCOUNTTYPE` | CHAR(1) |  |  |  |  |
| 117 | `CLAIMREASONCODE` | CHAR(3) |  |  |  |  |
| 118 | `CLAIMSTATUS` | CHAR(1) |  |  |  |  |
| 119 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 120 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 121 | `AGENTCREATIONTYPE1` | CHAR(1) | NOT NULL |  |  |  |
| 122 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 123 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 124 | `AGENTCREATIONTYPE2` | CHAR(1) | NOT NULL |  |  |  |
| 125 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 126 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 127 | `AGENTCREATIONTYPE3` | CHAR(1) | NOT NULL |  |  |  |
| 128 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 129 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 130 | `AGENTCREATIONTYPE4` | CHAR(1) | NOT NULL |  |  |  |
| 131 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 132 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 133 | `AGENTCREATIONTYPE5` | CHAR(1) | NOT NULL |  |  |  |
| 134 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 135 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 136 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 137 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 138 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 139 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 140 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 141 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 142 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 143 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 144 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 145 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 146 | `CONSIGNMENTWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 147 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 148 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 149 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 150 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 151 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 152 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 153 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 154 | `MANUFACTORINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 155 | `INTRASTATBEFOREACCTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 156 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 157 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 158 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 159 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 160 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 161 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 162 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 163 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 164 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 165 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 166 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 167 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 168 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 169 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESDOCUMENT' + known child suffix 'LINE')
  - JOIN predicate: `LOGSALESDOCUMENTLINE.FATHERID = LOGSALESDOCUMENT.ABSUNIQUEID`
- child `LOGSALESDOCUMENTLINEBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESDOCUMENTLINECHARGE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESDOCUMENTLINEDISCOUNT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.SALESDOCUMENTCOMPANYCODE,
       t.SALDOCPROVISIONALCOUNTERCODE,
       t.SALESDOCUMENTPROVISIONALCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.COMPONENTORDERLINE,
       t.STOCKTYPECODE,
       t.LINETEMPLATECODE
FROM   DB2ADMIN.LOGSALESDOCUMENTLINE t
FETCH FIRST 100 ROWS ONLY;
```
