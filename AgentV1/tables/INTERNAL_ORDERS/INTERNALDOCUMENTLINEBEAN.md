# DB2ADMIN.INTERNALDOCUMENTLINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 204
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 67049

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `CREATIONPHASE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `DELETIONPHASE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `EXTERNALUPDATEPHASE` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 8 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 9 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 10 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 11 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 12 | `FIRSTISSUEDONE` | CHAR(2) |  |  |  |  |
| 13 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 15 | `RECEIVINGSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 17 | `PRECEDINGLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 18 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 19 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 20 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 21 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 22 | `PREVIOUSSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 23 | `PREVIOUSCOLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 24 | `PREVIOUSPROJECTCODE` | CHAR(20) |  |  |  |  |
| 25 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 26 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 27 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 28 | `VIRTUALITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `VIRTUALITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 30 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 31 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `SUBSTITUTESUBCODESEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 41 | `AVAILABILITYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 42 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 43 | `ITEMCHANGEDLEVEL` | INTEGER | NOT NULL |  |  |  |
| 44 | `SUBSTITUTECRITERIA` | CHAR(2) |  |  |  |  |
| 45 | `ITEMLEVEL` | INTEGER | NOT NULL |  |  |  |
| 46 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 47 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 48 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 49 | `EXTERNALITEMCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 50 | `ITEMBARCODE` | VARCHAR(50) |  |  |  |  |
| 51 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 52 | `ITEMDESCRIPTIONCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 53 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 54 | `BOXHIDEUOM` | SMALLINT | NOT NULL |  |  |  |
| 55 | `PREVIOUSBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 56 | `PREVIOUSBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `PREVIOUSBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 58 | `PREVIOUSBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `PREVIOUSUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 60 | `PREVIOUSUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `PREVIOUSUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 62 | `PREVIOUSUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `PREVIOUSUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 64 | `PREVIOUSUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 66 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 67 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 68 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 69 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 70 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 71 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 72 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 73 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 74 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 77 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 78 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 80 | `RECEIVEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 81 | `RECEIVEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 82 | `RECEIVEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `RECEIVEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 84 | `RECEIVEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 85 | `AVAILABLEUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 86 | `AVAILABLEUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 87 | `AVAILABLEUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 88 | `USERPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 89 | `BASEPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 90 | `USERSECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 91 | `BASESECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 92 | `USERPACKAGINGUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 93 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 94 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 95 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 96 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 97 | `PREVIOUSQUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 98 | `QUALITYCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 99 | `QUALITYCONTROLALLOCATION` | SMALLINT | NOT NULL |  |  |  |
| 100 | `QUALITYCRITERIA` | CHAR(2) |  |  |  |  |
| 101 | `DESTINATIONTYPE` | CHAR(1) |  |  |  |  |
| 102 | `TERMOFSHIPPINGANDRECEIVINGTYPE` | CHAR(2) |  |  |  |  |
| 103 | `DESTINATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 104 | `DESTINATIONWAREHOUSECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 105 | `PREVIOUSDESTINATIONWHSCODE` | CHAR(8) |  |  |  |  |
| 106 | `RECEIVINGDATE` | DATE |  |  |  |  |
| 107 | `LINESTATUS` | CHAR(2) |  |  |  |  |
| 108 | `LINESTATUSCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 109 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 110 | `PROGRESSSTATUSCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 111 | `PREVIOUSRECEIVINGSTATUS` | CHAR(2) |  |  |  |  |
| 112 | `RUNMANUALREOPEN` | SMALLINT | NOT NULL |  |  |  |
| 113 | `RUNMANUALCLOSURE` | SMALLINT | NOT NULL |  |  |  |
| 114 | `RECEIVINGSTATUS` | CHAR(2) |  |  |  |  |
| 115 | `RELATEDENTITYSTATUS` | CHAR(90) |  |  |  |  |
| 116 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 117 | `STATISTICALGROUPCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 118 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 119 | `COLLECTIONGROUPCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 120 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 121 | `PROJECTCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 122 | `PROJECTUPDATEALLOCATION` | SMALLINT | NOT NULL |  |  |  |
| 123 | `STCGROUPUPDATEALLOCATION` | SMALLINT | NOT NULL |  |  |  |
| 124 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 125 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 126 | `PREVIOUSWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 127 | `WAREHOUSECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 128 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 129 | `UPDATEWHSAVAILABILITYCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 130 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 131 | `COSTCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 132 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 133 | `COSTCENTERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 134 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 135 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 136 | `DELIVERYPOINTCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 137 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 138 | `TERMSOFDELIVERYCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 139 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 140 | `TERMSOFSHIPPINGCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 141 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 142 | `LEFTOVERLOSSCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 143 | `QUANTITYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 144 | `PICKINGCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 145 | `PICKINGCODE` | CHAR(15) |  |  |  |  |
| 146 | `JOINEDORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 147 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 148 | `LINESOURCE` | CHAR(2) |  |  |  |  |
| 149 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 150 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 151 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 152 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 153 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 154 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 155 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 156 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 157 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 158 | `DLVINTORDLINEINTORDCNTCODE` | CHAR(8) |  |  |  |  |
| 159 | `DLVINTORDLINEINTORDERCODE` | CHAR(15) |  |  |  |  |
| 160 | `DLVINTERNALORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 161 | `DLVINTORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 162 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 163 | `ORIGINTYPE` | CHAR(2) |  |  |  |  |
| 164 | `ORIGINORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 165 | `ORIGINORDERCODE` | CHAR(15) |  |  |  |  |
| 166 | `ORIGINLINE` | DECIMAL(7,0) |  |  |  |  |
| 167 | `ORIGINDETAILLINE` | DECIMAL(3,0) |  |  |  |  |
| 168 | `ALLOCATIONTODELETE` | SMALLINT | NOT NULL |  |  |  |
| 169 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 170 | `STOPUPDATEFATHER` | SMALLINT | NOT NULL |  |  |  |
| 171 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 172 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 173 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 174 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 175 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 176 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 177 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 178 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 179 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 180 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 181 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 182 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 183 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 184 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 185 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 186 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 187 | `PMWORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 188 | `PMWORKORDERCODE` | CHAR(15) |  |  |  |  |
| 189 | `PMMACHINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 190 | `PMMACHINECODE` | CHAR(15) |  |  |  |  |
| 191 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 192 | `EXTERNALITEMRESET` | SMALLINT | NOT NULL |  |  |  |
| 193 | `NORECEIVEUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 194 | `NORECEIVEBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 195 | `NORECEIVEUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 196 | `NORECEIVEBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 197 | `NORECEIVEUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 198 | `DESTPHYSWHSCODE` | CHAR(8) |  |  |  |  |
| 199 | `DESTZONECODE` | CHAR(3) |  |  |  |  |
| 200 | `DESTLOCATIONCODE` | CHAR(10) |  |  |  |  |
| 201 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 202 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 203 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **INTERNALDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'INTERNALDOCUMENT' + known child suffix 'LINE')
  - JOIN predicate: `INTERNALDOCUMENTLINEBEAN.FATHERID = INTERNALDOCUMENT.ABSUNIQUEID`

## Indexes

- `INTERNALDOCUMENTLINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CREATIONPHASE,
       t.DELETIONPHASE,
       t.EXTERNALUPDATEPHASE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.SESSIONSTEP
FROM   DB2ADMIN.INTERNALDOCUMENTLINEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
