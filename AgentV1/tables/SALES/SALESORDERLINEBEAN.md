# DB2ADMIN.SALESORDERLINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 227
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 80949

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 5 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 6 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 9 | `DERIVATIONSTEP` | CHAR(2) |  |  |  |  |
| 10 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `COMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 12 | `LOADFROMDELIVERYEXECUTED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `FROMORDERPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 14 | `ASSORTMENTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 15 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 16 | `SAMPLESTYPE` | CHAR(2) |  |  |  |  |
| 17 | `BOXMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 19 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 20 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 21 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 22 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 23 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 24 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 25 | `ORDERITEMCODE` | VARCHAR(120) |  |  |  |  |
| 26 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 27 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 28 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBSTITUTESUBCODESEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 38 | `AVAILABILITYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 39 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 40 | `SUBSTITUTECRITERIA` | CHAR(2) |  |  |  |  |
| 41 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 42 | `SELLINGITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 43 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 44 | `ITEMBARCODE` | VARCHAR(50) |  |  |  |  |
| 45 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 46 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 47 | `BOXHIDEUOM` | SMALLINT | NOT NULL |  |  |  |
| 48 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 49 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 51 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 53 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 54 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 55 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 56 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 57 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 62 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `SUBCODE01DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 67 | `SUBCODE02DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 68 | `SUBCODE03DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 69 | `SUBCODE04DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 70 | `SUBCODE05DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 71 | `SUBCODE06DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 72 | `SUBCODE07DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 73 | `SUBCODE08DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 74 | `SUBCODE09DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 75 | `SUBCODE10DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 76 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 77 | `LINESTATUS` | CHAR(2) |  |  |  |  |
| 78 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 79 | `RELATEDENTITYSTATUS` | CHAR(90) |  |  |  |  |
| 80 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 81 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 82 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 83 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 84 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 85 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 86 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 87 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 88 | `DISTRIBUTIONWAREHOUSEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 89 | `CARRIERTYPE` | CHAR(1) |  |  |  |  |
| 90 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 91 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 92 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 93 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 94 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 95 | `CONFIRMEDDELIVERYDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 96 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 97 | `CONSIGNMENTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 98 | `CONSIGNMENTTYPE` | CHAR(2) |  |  |  |  |
| 99 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 100 | `JOINEDORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 101 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 102 | `JOINEDCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 103 | `LINESOURCE` | CHAR(2) |  |  |  |  |
| 104 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 105 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 106 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 107 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 108 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 109 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 110 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 111 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 112 | `INTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 113 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 114 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 115 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 116 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 117 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 118 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 119 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 120 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 121 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 122 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 123 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 124 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 125 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 126 | `ORIGINALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 127 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 128 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 129 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 130 | `TAXABLEINCOMEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 131 | `NETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 132 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 133 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 134 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 135 | `AGENTCREATIONTYPE1` | CHAR(1) |  |  |  |  |
| 136 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 137 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 138 | `AGENTCREATIONTYPE2` | CHAR(1) |  |  |  |  |
| 139 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 140 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 141 | `AGENTCREATIONTYPE3` | CHAR(1) |  |  |  |  |
| 142 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 143 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 144 | `AGENTCREATIONTYPE4` | CHAR(1) |  |  |  |  |
| 145 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 146 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 147 | `AGENTCREATIONTYPE5` | CHAR(1) |  |  |  |  |
| 148 | `MANUALLYINSERTFORBOX` | SMALLINT | NOT NULL |  |  |  |
| 149 | `SDICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 150 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 151 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 152 | `INVOICEIMAGE` | CHAR(65) |  |  |  |  |
| 153 | `ORDERSUBCODE01` | CHAR(20) |  |  |  |  |
| 154 | `ORDERSUBCODE02` | CHAR(10) |  |  |  |  |
| 155 | `ORDERSUBCODE03` | CHAR(10) |  |  |  |  |
| 156 | `ORDERSUBCODE04` | CHAR(10) |  |  |  |  |
| 157 | `ORDERSUBCODE05` | CHAR(10) |  |  |  |  |
| 158 | `ORDERSUBCODE06` | CHAR(10) |  |  |  |  |
| 159 | `ORDERSUBCODE07` | CHAR(10) |  |  |  |  |
| 160 | `ORDERSUBCODE08` | CHAR(10) |  |  |  |  |
| 161 | `ORDERSUBCODE09` | CHAR(10) |  |  |  |  |
| 162 | `ORDERSUBCODE10` | CHAR(10) |  |  |  |  |
| 163 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 164 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 165 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 166 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 167 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 168 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 169 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 170 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 171 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 172 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 173 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 174 | `READYTOSHIP` | SMALLINT | NOT NULL |  |  |  |
| 175 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 176 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 177 | `SHIPPINGDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 178 | `CUSTOMERDELIVERYDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 179 | `SHIPPINGDATE` | DATE |  |  |  |  |
| 180 | `CUSTOMERDELIVERYDATE` | DATE |  |  |  |  |
| 181 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 182 | `FORCEVALUESFROMIMPORT` | SMALLINT | NOT NULL |  |  |  |
| 183 | `PRODUCTIONCONFIRMEDDATE` | DATE |  |  |  |  |
| 184 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 185 | `PURORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 186 | `PURORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 187 | `POUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 188 | `POUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 189 | `POUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 190 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 191 | `EXTERNALITEMRESET` | SMALLINT | NOT NULL |  |  |  |
| 192 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 193 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 194 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 195 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 196 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 197 | `RESIDUALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 198 | `RESIDUALBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 199 | `RESIDUALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 200 | `RESIDUALBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 201 | `RESIDUALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 202 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 203 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 204 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 205 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 206 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 207 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 208 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 209 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 210 | `READYTOSHIPCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 211 | `FORCESUBPROJECTCODE` | SMALLINT | NOT NULL |  |  |  |
| 212 | `SUBPROJECTCODE` | DECIMAL(5,0) |  |  |  |  |
| 213 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 214 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 215 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 216 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 217 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 218 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 219 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 220 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 221 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 222 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 223 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 224 | `OVERDUEAMOUNTFORCED` | SMALLINT | NOT NULL |  |  |  |
| 225 | `EIOTHERDATALOADED` | SMALLINT | NOT NULL |  |  |  |
| 226 | `NOTDELETELINK` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESORDER**.`ABSUNIQUEID` (high confidence — name = 'SALESORDER' + known child suffix 'LINE')
  - JOIN predicate: `SALESORDERLINEBEAN.FATHERID = SALESORDER.ABSUNIQUEID`

## Indexes

- `SALESORDERLINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.SESSIONSTEP,
       t.DERIVATIONSTEP,
       t.INITIALIZEREQUIRED,
       t.COMPONENTORDERLINE
FROM   DB2ADMIN.SALESORDERLINEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
