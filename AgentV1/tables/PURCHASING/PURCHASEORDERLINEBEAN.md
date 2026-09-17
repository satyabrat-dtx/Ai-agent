# DB2ADMIN.PURCHASEORDERLINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 182
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 68999

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `CREATIONPHASE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 6 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 7 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 8 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 10 | `DERIVATIONSTEP` | CHAR(2) |  |  |  |  |
| 11 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `LOADFROMDELIVERYEXECUTED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `FROMORDERPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 14 | `ASSORTMENTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 15 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 16 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 17 | `EXTERNALOPERATIONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `BOXMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 19 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 20 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 21 | `ORDERITEMCODE` | VARCHAR(120) |  |  |  |  |
| 22 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 23 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 24 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBSTITUTESUBCODESEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 34 | `AVAILABILITYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 35 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 36 | `SUBSTITUTECRITERIA` | CHAR(2) |  |  |  |  |
| 37 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 38 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 39 | `ITEMBARCODE` | VARCHAR(50) |  |  |  |  |
| 40 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 41 | `BOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
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
| 53 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 54 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 56 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `SUBCODE01DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 62 | `SUBCODE02DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 63 | `SUBCODE03DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 64 | `SUBCODE04DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 65 | `SUBCODE05DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 66 | `SUBCODE06DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 67 | `SUBCODE07DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 68 | `SUBCODE08DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 69 | `SUBCODE09DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 70 | `SUBCODE10DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 71 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 72 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 73 | `LINESTATUS` | CHAR(2) |  |  |  |  |
| 74 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 75 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 76 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 77 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 78 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 79 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 80 | `ISSUEWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 81 | `SUBCONTRACTORWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 82 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 83 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 84 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 85 | `DELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 86 | `SHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 87 | `THIRDCARRIERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 88 | `TRANSPORTREASONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 89 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 90 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 91 | `DATEPERIODTYPECODE` | CHAR(3) |  |  |  |  |
| 92 | `JOINEDORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 93 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 94 | `LINESOURCE` | CHAR(2) |  |  |  |  |
| 95 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 96 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 97 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 98 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 99 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 100 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 101 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 102 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 103 | `SENDTOSUPPLIER` | SMALLINT | NOT NULL |  |  |  |
| 104 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 105 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 106 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 107 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 108 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 109 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 110 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 111 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 112 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 113 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 114 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 115 | `ORIGINALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 116 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 117 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 118 | `PREVIOUSFREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 119 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 120 | `TAXABLEINCOMEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 121 | `NETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 122 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 123 | `MANUALLYINSERTFORBOX` | SMALLINT | NOT NULL |  |  |  |
| 124 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 125 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 126 | `ORDERSUBCODE01` | CHAR(20) |  |  |  |  |
| 127 | `ORDERSUBCODE02` | CHAR(10) |  |  |  |  |
| 128 | `ORDERSUBCODE03` | CHAR(10) |  |  |  |  |
| 129 | `ORDERSUBCODE04` | CHAR(10) |  |  |  |  |
| 130 | `ORDERSUBCODE05` | CHAR(10) |  |  |  |  |
| 131 | `ORDERSUBCODE06` | CHAR(10) |  |  |  |  |
| 132 | `ORDERSUBCODE07` | CHAR(10) |  |  |  |  |
| 133 | `ORDERSUBCODE08` | CHAR(10) |  |  |  |  |
| 134 | `ORDERSUBCODE09` | CHAR(10) |  |  |  |  |
| 135 | `ORDERSUBCODE10` | CHAR(10) |  |  |  |  |
| 136 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 137 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 138 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 139 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 140 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 141 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 142 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 143 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 144 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 145 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 146 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 147 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 148 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 149 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 150 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 151 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 152 | `ORIGCONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 153 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 154 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 155 | `CUSTOMERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 156 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 157 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 158 | `EXTERNALITEMRESET` | SMALLINT | NOT NULL |  |  |  |
| 159 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 160 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 161 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 162 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 163 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 164 | `PREVIOUSPROJECTCODE` | CHAR(20) |  |  |  |  |
| 165 | `PREVIOUSCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 166 | `PREVIOUSENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 167 | `CURRENCYPOOLCOMPANY` | CHAR(3) |  |  |  |  |
| 168 | `CURRENCYPOOLCODE` | CHAR(15) |  |  |  |  |
| 169 | `CURRENCYPOOLLINENR` | DECIMAL(5,0) |  |  |  |  |
| 170 | `CURRENCYPOOLEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 171 | `CURRENCYPOOLFOREIGNAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 172 | `CURRENCYPOOLRESIDUALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 173 | `CURRENCYPOOLSELECTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 174 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 175 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 176 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 177 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 178 | `SUMSELECTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 179 | `DIFFSUMANDTAXINC` | DECIMAL(18,5) |  |  |  |  |
| 180 | `PREVIOUSCURPOOLSELECTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 181 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **PURCHASEORDER**.`ABSUNIQUEID` (high confidence — name = 'PURCHASEORDER' + known child suffix 'LINE')
  - JOIN predicate: `PURCHASEORDERLINEBEAN.FATHERID = PURCHASEORDER.ABSUNIQUEID`

## Indexes

- `PURCHASEORDERLINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CREATIONPHASE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.SESSIONSTEP,
       t.DERIVATIONSTEP,
       t.INITIALIZEREQUIRED
FROM   DB2ADMIN.PURCHASEORDERLINEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
