# DB2ADMIN.SALESDOCUMENTLINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 177
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 96009

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
| 10 | `FIRSTISSUEDONE` | CHAR(2) |  |  |  |  |
| 11 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `COMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 13 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 14 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 15 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 16 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 17 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 18 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 19 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 20 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 21 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 22 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 23 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBSTITUTESUBCODESEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 33 | `AVAILABILITYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 34 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 35 | `SUBSTITUTECRITERIA` | CHAR(2) |  |  |  |  |
| 36 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 37 | `SELLINGITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 38 | `BARCODE` | VARCHAR(50) |  |  |  |  |
| 39 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 40 | `ITEMBARCODE` | VARCHAR(50) |  |  |  |  |
| 41 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 42 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 43 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 44 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 46 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 48 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 52 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 54 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 56 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `CREDITUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 62 | `CREDITBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `CREDITUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `CREDITBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `CREDITUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 67 | `CONSIGNMENTTYPE` | CHAR(2) |  |  |  |  |
| 68 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 69 | `LINESTATUS` | CHAR(2) |  |  |  |  |
| 70 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 71 | `INVOICEEVOLUTIONTYPE` | CHAR(2) |  |  |  |  |
| 72 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 73 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 74 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 75 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 76 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 77 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 78 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 79 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 80 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 81 | `QUANTITYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 82 | `PICKINGCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 83 | `PICKINGCODE` | CHAR(15) |  |  |  |  |
| 84 | `JOINEDORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 85 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 86 | `JOINEDCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 87 | `LINESOURCE` | CHAR(2) |  |  |  |  |
| 88 | `PREVIOUSORIGINFROM` | CHAR(2) |  |  |  |  |
| 89 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 90 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 91 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 92 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 93 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 94 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 95 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 96 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 97 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 98 | `DLVSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 99 | `DLVSALORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 100 | `DLVSALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 101 | `DLVSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 102 | `DLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 103 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 104 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 105 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 106 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 107 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 108 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 109 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 110 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 111 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 112 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 113 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 114 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 115 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 116 | `ORIGINALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 117 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 118 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 119 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 120 | `TAXABLEINCOMEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 121 | `NETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 122 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 123 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 124 | `CHARGECREATIONTYPE` | CHAR(1) |  |  |  |  |
| 125 | `FREEGIFTDISCOUNTTYPE` | CHAR(1) |  |  |  |  |
| 126 | `CLAIMREASONCODE` | CHAR(3) |  |  |  |  |
| 127 | `CLAIMSTATUS` | CHAR(1) |  |  |  |  |
| 128 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 129 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 130 | `AGENTCREATIONTYPE1` | CHAR(1) |  |  |  |  |
| 131 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 132 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 133 | `AGENTCREATIONTYPE2` | CHAR(1) |  |  |  |  |
| 134 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 135 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 136 | `AGENTCREATIONTYPE3` | CHAR(1) |  |  |  |  |
| 137 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 138 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 139 | `AGENTCREATIONTYPE4` | CHAR(1) |  |  |  |  |
| 140 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 141 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 142 | `AGENTCREATIONTYPE5` | CHAR(1) |  |  |  |  |
| 143 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 144 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 145 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 146 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 147 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 148 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 149 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 150 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 151 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 152 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 153 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 154 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 155 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 156 | `MANUFACTORINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 157 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 158 | `INTRASTATBEFOREACCTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 159 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 160 | `CONSIDERBASEQUANTITIES` | SMALLINT | NOT NULL |  |  |  |
| 161 | `EXTERNALITEMRESET` | SMALLINT | NOT NULL |  |  |  |
| 162 | `CREDITCHECKFORCED` | SMALLINT | NOT NULL |  |  |  |
| 163 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 164 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 165 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 166 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 167 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 168 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 169 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 170 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 171 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 172 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 173 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 174 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 175 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 176 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'SALESDOCUMENT' + known child suffix 'LINE')
  - JOIN predicate: `SALESDOCUMENTLINEBEAN.FATHERID = SALESDOCUMENT.ABSUNIQUEID`

## Indexes

- `SALESDOCUMENTLINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
       t.FIRSTISSUEDONE,
       t.INITIALIZEREQUIRED
FROM   DB2ADMIN.SALESDOCUMENTLINEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
