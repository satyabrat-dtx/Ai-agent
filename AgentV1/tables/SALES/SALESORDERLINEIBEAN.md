# DB2ADMIN.SALESORDERLINEIBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 250
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 149191

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `FORCEVALUESFROMIMPORT` | SMALLINT | NOT NULL |  |  |  |
| 5 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 6 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 7 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 8 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 10 | `DERIVATIONSTEP` | CHAR(2) |  |  |  |  |
| 11 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `COMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 13 | `LOADFROMDELIVERYEXECUTED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `FROMORDERPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 15 | `ASSORTMENTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 16 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 17 | `SAMPLESTYPE` | CHAR(2) |  |  |  |  |
| 18 | `BOXMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 19 | `PURORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 20 | `PURORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 21 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 22 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 23 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 24 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 25 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 26 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 27 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 28 | `ORDERITEMCODE` | VARCHAR(120) |  |  |  |  |
| 29 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
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
| 43 | `SUBSTITUTECRITERIA` | CHAR(2) |  |  |  |  |
| 44 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 45 | `SELLINGITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 46 | `PRDSERIALNOCODE` | CHAR(10) |  |  |  |  |
| 47 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 48 | `ITEMBARCODE` | VARCHAR(50) |  |  |  |  |
| 49 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 50 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 51 | `BOXHIDEUOM` | SMALLINT | NOT NULL |  |  |  |
| 52 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 53 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 54 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 55 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 56 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 57 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 59 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 61 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 62 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 67 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 68 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 69 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 70 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 71 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 72 | `POUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 73 | `POUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 74 | `POUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `SUBCODE01DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 76 | `SUBCODE02DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 77 | `SUBCODE03DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 78 | `SUBCODE04DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 79 | `SUBCODE05DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 80 | `SUBCODE06DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 81 | `SUBCODE07DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 82 | `SUBCODE08DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 83 | `SUBCODE09DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 84 | `SUBCODE10DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 85 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 86 | `LINESTATUS` | CHAR(2) |  |  |  |  |
| 87 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 88 | `READYTOSHIP` | SMALLINT | NOT NULL |  |  |  |
| 89 | `RELATEDENTITYSTATUS` | CHAR(90) |  |  |  |  |
| 90 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 91 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 92 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 93 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 94 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 95 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 96 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 97 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 98 | `DISTRIBUTIONWAREHOUSEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 99 | `CARRIERTYPE` | CHAR(1) |  |  |  |  |
| 100 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 101 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 102 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 103 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 104 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 105 | `CONFIRMEDDELIVERYDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 106 | `SHIPPINGDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 107 | `CUSTOMERDELIVERYDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 108 | `SHIPPINGDATE` | DATE |  |  |  |  |
| 109 | `CUSTOMERDELIVERYDATE` | DATE |  |  |  |  |
| 110 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 111 | `CONSIGNMENTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 112 | `CONSIGNMENTTYPE` | CHAR(2) |  |  |  |  |
| 113 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 114 | `JOINEDORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 115 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 116 | `JOINEDCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 117 | `LINESOURCE` | CHAR(2) |  |  |  |  |
| 118 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 119 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 120 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 121 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 122 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 123 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 124 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 125 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 126 | `INTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 127 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 128 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 129 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 130 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 131 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 132 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 133 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 134 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 135 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 136 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 137 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 138 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 139 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 140 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 141 | `ORIGINALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 142 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 143 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 144 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 145 | `TAXABLEINCOMEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 146 | `NETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 147 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 148 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 149 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 150 | `AGENTCREATIONTYPE1` | CHAR(1) |  |  |  |  |
| 151 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 152 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 153 | `AGENTCREATIONTYPE2` | CHAR(1) |  |  |  |  |
| 154 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 155 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 156 | `AGENTCREATIONTYPE3` | CHAR(1) |  |  |  |  |
| 157 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 158 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 159 | `AGENTCREATIONTYPE4` | CHAR(1) |  |  |  |  |
| 160 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 161 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 162 | `AGENTCREATIONTYPE5` | CHAR(1) |  |  |  |  |
| 163 | `MANUALLYINSERTFORBOX` | SMALLINT | NOT NULL |  |  |  |
| 164 | `SDICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 165 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 166 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 167 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 168 | `INVOICEIMAGE` | CHAR(65) |  |  |  |  |
| 169 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 170 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 171 | `SHIPMENTARTICLECODE` | CHAR(5) |  |  |  |  |
| 172 | `SCHEMECODE` | CHAR(3) |  |  |  |  |
| 173 | `AGAINSTFORM` | CHAR(1) |  |  |  |  |
| 174 | `FORMCODE` | CHAR(3) |  |  |  |  |
| 175 | `IPPOLICYNO` | CHAR(30) |  |  |  |  |
| 176 | `IPPOLICYDATE` | DATE |  |  |  |  |
| 177 | `POLICYEXPIRYDATE` | DATE |  |  |  |  |
| 178 | `INSURANCECOMPANY` | CHAR(60) |  |  |  |  |
| 179 | `POLICYPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 180 | `CUSTOMERPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 181 | `INSURANCEMARKUP` | DECIMAL(9,5) |  |  |  |  |
| 182 | `ARTICLERATE1` | DECIMAL(18,5) |  |  |  |  |
| 183 | `ARTICLERATE2` | DECIMAL(18,5) |  |  |  |  |
| 184 | `ARTICLERATE3` | DECIMAL(18,5) |  |  |  |  |
| 185 | `JOBRATE1` | DECIMAL(18,5) |  |  |  |  |
| 186 | `JOBRATE2` | DECIMAL(18,5) |  |  |  |  |
| 187 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 188 | `GROSSVALUEEXT` | DECIMAL(18,5) |  |  |  |  |
| 189 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 190 | `PRODUCTIONTOLERANCEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 191 | `ORDERSUBCODE01` | CHAR(20) |  |  |  |  |
| 192 | `ORDERSUBCODE02` | CHAR(10) |  |  |  |  |
| 193 | `ORDERSUBCODE03` | CHAR(10) |  |  |  |  |
| 194 | `ORDERSUBCODE04` | CHAR(10) |  |  |  |  |
| 195 | `ORDERSUBCODE05` | CHAR(10) |  |  |  |  |
| 196 | `ORDERSUBCODE06` | CHAR(10) |  |  |  |  |
| 197 | `ORDERSUBCODE07` | CHAR(10) |  |  |  |  |
| 198 | `ORDERSUBCODE08` | CHAR(10) |  |  |  |  |
| 199 | `ORDERSUBCODE09` | CHAR(10) |  |  |  |  |
| 200 | `ORDERSUBCODE10` | CHAR(10) |  |  |  |  |
| 201 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 202 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 203 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 204 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 205 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 206 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 207 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 208 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 209 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 210 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 211 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 212 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 213 | `EXTERNALITEMRESET` | SMALLINT | NOT NULL |  |  |  |
| 214 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 215 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 216 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 217 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 218 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 219 | `RESIDUALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 220 | `RESIDUALBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 221 | `RESIDUALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 222 | `RESIDUALBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 223 | `RESIDUALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 224 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 225 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 226 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 227 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 228 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 229 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 230 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 231 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 232 | `PRDSERIALNOUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 233 | `READYTOSHIPCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 234 | `FORCESUBPROJECTCODE` | SMALLINT | NOT NULL |  |  |  |
| 235 | `SUBPROJECTCODE` | DECIMAL(5,0) |  |  |  |  |
| 236 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 237 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 238 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 239 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 240 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 241 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 242 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 243 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 244 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 245 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 246 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 247 | `OVERDUEAMOUNTFORCED` | SMALLINT | NOT NULL |  |  |  |
| 248 | `EIOTHERDATALOADED` | SMALLINT | NOT NULL |  |  |  |
| 249 | `NOTDELETELINK` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `SALESORDERLINEIBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `SALESORDERLINEIBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.FORCEVALUESFROMIMPORT,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.SESSIONSTEP,
       t.DERIVATIONSTEP,
       t.INITIALIZEREQUIRED
FROM   DB2ADMIN.SALESORDERLINEIBEAN t
FETCH FIRST 100 ROWS ONLY;
```
