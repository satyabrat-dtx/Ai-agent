# DB2ADMIN.PURCHASEORDERDELIVERYEXTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`
- **Columns**: 187
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 111854

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `AUTOMATICGENERATION` | SMALLINT | NOT NULL |  |  |  |
| 4 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 5 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `CREATIONPHASE` | SMALLINT | NOT NULL |  |  |  |
| 7 | `DELETIONPHASE` | SMALLINT | NOT NULL |  |  |  |
| 8 | `EXTERNALUPDATEPHASE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `ORDERDATE` | DATE |  |  |  |  |
| 11 | `PROGRESSSTATUSDESC` | CHAR(20) |  |  |  |  |
| 12 | `UOMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 13 | `PAYMENTMETHODDESC` | CHAR(100) |  |  |  |  |
| 14 | `DELIVERYTERMDESC` | CHAR(100) |  |  |  |  |
| 15 | `SHIPMENTTERMDESC` | CHAR(100) |  |  |  |  |
| 16 | `ORDERLINESTATUS` | CHAR(2) |  |  |  |  |
| 17 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 18 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 19 | `DELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 20 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 21 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 22 | `DELIVERYDATE` | DATE |  |  |  |  |
| 23 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 24 | `PROGRESSSTATUSCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 25 | `RUNMANUALCLOSURE` | SMALLINT | NOT NULL |  |  |  |
| 26 | `RUNMANUALREOPEN` | SMALLINT | NOT NULL |  |  |  |
| 27 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 28 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 29 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 30 | `PREVIOUSWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 31 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 32 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 33 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 34 | `RESERVATIONDATE` | DATE |  |  |  |  |
| 35 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 36 | `ORIGCONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 37 | `EFFECTIVEDELIVERYDATE` | DATE |  |  |  |  |
| 38 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 39 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 40 | `ITEMLEVEL` | INTEGER | NOT NULL |  |  |  |
| 41 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 42 | `QUALITYCRITERIA` | CHAR(2) |  |  |  |  |
| 43 | `ORDERITEMCODE` | VARCHAR(120) |  |  |  |  |
| 44 | `ORDERSUBCODE01` | CHAR(20) |  |  |  |  |
| 45 | `ORDERSUBCODE02` | CHAR(10) |  |  |  |  |
| 46 | `ORDERSUBCODE03` | CHAR(10) |  |  |  |  |
| 47 | `ORDERSUBCODE04` | CHAR(10) |  |  |  |  |
| 48 | `ORDERSUBCODE05` | CHAR(10) |  |  |  |  |
| 49 | `ORDERSUBCODE06` | CHAR(10) |  |  |  |  |
| 50 | `ORDERSUBCODE07` | CHAR(10) |  |  |  |  |
| 51 | `ORDERSUBCODE08` | CHAR(10) |  |  |  |  |
| 52 | `ORDERSUBCODE09` | CHAR(10) |  |  |  |  |
| 53 | `ORDERSUBCODE10` | CHAR(10) |  |  |  |  |
| 54 | `SUBCODE01DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 55 | `SUBCODE02DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 56 | `SUBCODE03DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 57 | `SUBCODE04DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 58 | `SUBCODE05DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 59 | `SUBCODE06DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 60 | `SUBCODE07DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 61 | `SUBCODE08DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 62 | `SUBCODE09DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 63 | `SUBCODE10DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 64 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 65 | `PREVIOUSQUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 66 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 67 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 68 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 69 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 70 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 71 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 72 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 73 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 74 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 75 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 76 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 77 | `VIRTUALITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 78 | `VIRTUALITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 79 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 80 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 81 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 82 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 83 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 84 | `PREVIOUSSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 85 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 86 | `PREVIOUSCOLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 87 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 88 | `PREVIOUSPROJECTCODE` | CHAR(20) |  |  |  |  |
| 89 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 90 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 91 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 92 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 93 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 94 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 95 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 96 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 97 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 98 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 99 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 100 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 101 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 102 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 103 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 104 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 105 | `PREVIOUSBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 106 | `PREVIOUSBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 107 | `PREVIOUSBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 108 | `PREVIOUSBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 109 | `PREVIOUSUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 110 | `PREVIOUSUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 111 | `PREVIOUSUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 112 | `PREVIOUSUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 113 | `PREVIOUSUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 114 | `PREVIOUSUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 115 | `USERPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 116 | `BASEPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 117 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 118 | `USERSECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 119 | `BASESECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 120 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 121 | `USERPACKAGINGUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 122 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 123 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 124 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 125 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 126 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 127 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 128 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 129 | `ALLOCATIONTODELETE` | SMALLINT | NOT NULL |  |  |  |
| 130 | `BOXHIDEUOM` | SMALLINT | NOT NULL |  |  |  |
| 131 | `RELATEDENTITYSTATUS` | CHAR(90) |  |  |  |  |
| 132 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 133 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 134 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 135 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 136 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 137 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 138 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 139 | `CONFIRMATION` | CHAR(15) |  |  |  |  |
| 140 | `REMINDERCOMMENTCODE` | CHAR(12) |  |  |  |  |
| 141 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 142 | `PREVIOUSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 143 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 144 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 145 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 146 | `PREVIOUSUSEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 147 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 148 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 149 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 150 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 151 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 152 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 153 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 154 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 155 | `STOPUPDATEFATHER` | SMALLINT | NOT NULL |  |  |  |
| 156 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 157 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 158 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 159 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 160 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 161 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 162 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 163 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 164 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 165 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 166 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 167 | `PREVIOUSCUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 168 | `PREVIOUSCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 169 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 170 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 171 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 172 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 173 | `ADDITIONALDATA` | BLOB(1000000) |  |  |  |  |
| 174 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 175 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 176 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 177 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 178 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 179 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 180 | `USERPACKAGINGNETQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 181 | `USERPACKAGINGUOMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 182 | `USERSECONDARYNETQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 183 | `USERSECONDARYUOMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 184 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 185 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 186 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURORDERDELIVERYEXTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.AUTOMATICGENERATION,
       t.FORCEDWARNING,
       t.LINETEMPLATECODE,
       t.CREATIONPHASE,
       t.DELETIONPHASE,
       t.EXTERNALUPDATEPHASE,
       t.ORDERTYPE,
       t.ORDERDATE,
       t.PROGRESSSTATUSDESC
FROM   DB2ADMIN.PURCHASEORDERDELIVERYEXTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
