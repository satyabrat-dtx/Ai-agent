# DB2ADMIN.PURCHASEORDERLINEIBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 192
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 148758

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
| 19 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 20 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 21 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 22 | `ORDERITEMCODE` | VARCHAR(120) |  |  |  |  |
| 23 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 24 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 25 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBSTITUTESUBCODESEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 35 | `AVAILABILITYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 36 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 37 | `SUBSTITUTECRITERIA` | CHAR(2) |  |  |  |  |
| 38 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 39 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 40 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 41 | `ITEMBARCODE` | VARCHAR(50) |  |  |  |  |
| 42 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 43 | `BOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 44 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 45 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 46 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 48 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 52 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 54 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 56 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 61 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 62 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `SUBCODE01DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 66 | `SUBCODE02DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 67 | `SUBCODE03DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 68 | `SUBCODE04DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 69 | `SUBCODE05DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 70 | `SUBCODE06DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 71 | `SUBCODE07DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 72 | `SUBCODE08DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 73 | `SUBCODE09DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 74 | `SUBCODE10DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 75 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 76 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 77 | `LINESTATUS` | CHAR(2) |  |  |  |  |
| 78 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 79 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 80 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 81 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 82 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 83 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 84 | `CUSTOMERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 85 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 86 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 87 | `ISSUEWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 88 | `SUBCONTRACTORWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 89 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 90 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 91 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 92 | `DELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 93 | `SHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 94 | `THIRDCARRIERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 95 | `TRANSPORTREASONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 96 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 97 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 98 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 99 | `CONFIRMEDDELIVERYDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 100 | `ORIGCONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 101 | `REQUIREDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 102 | `DATEPERIODTYPECODE` | CHAR(3) |  |  |  |  |
| 103 | `JOINEDORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 104 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 105 | `LINESOURCE` | CHAR(2) |  |  |  |  |
| 106 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 107 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 108 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 109 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 110 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 111 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 112 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 113 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 114 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 115 | `SENDTOSUPPLIER` | SMALLINT | NOT NULL |  |  |  |
| 116 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 117 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 118 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 119 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 120 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 121 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 122 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 123 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 124 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 125 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 126 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 127 | `ORIGINALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 128 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 129 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 130 | `PREVIOUSFREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 131 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 132 | `TAXABLEINCOMEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 133 | `NETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 134 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 135 | `MANUALLYINSERTFORBOX` | SMALLINT | NOT NULL |  |  |  |
| 136 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 137 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 138 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 139 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 140 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 141 | `CT3FORMNO` | CHAR(20) |  |  |  |  |
| 142 | `CT3DATE` | DATE |  |  |  |  |
| 143 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 144 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 145 | `GROSSVALUEEXT` | DECIMAL(18,5) |  |  |  |  |
| 146 | `ORDERSUBCODE01` | CHAR(20) |  |  |  |  |
| 147 | `ORDERSUBCODE02` | CHAR(10) |  |  |  |  |
| 148 | `ORDERSUBCODE03` | CHAR(10) |  |  |  |  |
| 149 | `ORDERSUBCODE04` | CHAR(10) |  |  |  |  |
| 150 | `ORDERSUBCODE05` | CHAR(10) |  |  |  |  |
| 151 | `ORDERSUBCODE06` | CHAR(10) |  |  |  |  |
| 152 | `ORDERSUBCODE07` | CHAR(10) |  |  |  |  |
| 153 | `ORDERSUBCODE08` | CHAR(10) |  |  |  |  |
| 154 | `ORDERSUBCODE09` | CHAR(10) |  |  |  |  |
| 155 | `ORDERSUBCODE10` | CHAR(10) |  |  |  |  |
| 156 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 157 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 158 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 159 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 160 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 161 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 162 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 163 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 164 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 165 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 166 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 167 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 168 | `EXTERNALITEMRESET` | SMALLINT | NOT NULL |  |  |  |
| 169 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 170 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 171 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 172 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 173 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 174 | `PREVIOUSPROJECTCODE` | CHAR(20) |  |  |  |  |
| 175 | `PREVIOUSCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 176 | `PREVIOUSENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 177 | `CURRENCYPOOLCOMPANY` | CHAR(3) |  |  |  |  |
| 178 | `CURRENCYPOOLCODE` | CHAR(15) |  |  |  |  |
| 179 | `CURRENCYPOOLLINENR` | DECIMAL(5,0) |  |  |  |  |
| 180 | `CURRENCYPOOLEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 181 | `CURRENCYPOOLFOREIGNAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 182 | `CURRENCYPOOLRESIDUALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 183 | `CURRENCYPOOLSELECTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 184 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 185 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 186 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 187 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 188 | `SUMSELECTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 189 | `DIFFSUMANDTAXINC` | DECIMAL(18,5) |  |  |  |  |
| 190 | `PREVIOUSCURPOOLSELECTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 191 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PURCHASEORDERLINEIBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PURCHASEORDERLINEIBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.PURCHASEORDERLINEIBEAN t
FETCH FIRST 100 ROWS ONLY;
```
