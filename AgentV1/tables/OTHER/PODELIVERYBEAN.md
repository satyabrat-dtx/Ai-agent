# DB2ADMIN.PODELIVERYBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 173
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 109963

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
| 18 | `ORDERLINE` | DECIMAL(5,0) |  |  |  |  |
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
| 36 | `EFFECTIVEDELIVERYDATE` | DATE |  |  |  |  |
| 37 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 38 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 39 | `ITEMLEVEL` | INTEGER | NOT NULL |  |  |  |
| 40 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 41 | `QUALITYCRITERIA` | CHAR(2) |  |  |  |  |
| 42 | `ORDERITEMCODE` | VARCHAR(120) |  |  |  |  |
| 43 | `ORDERSUBCODE01` | CHAR(20) |  |  |  |  |
| 44 | `ORDERSUBCODE02` | CHAR(10) |  |  |  |  |
| 45 | `ORDERSUBCODE03` | CHAR(10) |  |  |  |  |
| 46 | `ORDERSUBCODE04` | CHAR(10) |  |  |  |  |
| 47 | `ORDERSUBCODE05` | CHAR(10) |  |  |  |  |
| 48 | `ORDERSUBCODE06` | CHAR(10) |  |  |  |  |
| 49 | `ORDERSUBCODE07` | CHAR(10) |  |  |  |  |
| 50 | `ORDERSUBCODE08` | CHAR(10) |  |  |  |  |
| 51 | `ORDERSUBCODE09` | CHAR(10) |  |  |  |  |
| 52 | `ORDERSUBCODE10` | CHAR(10) |  |  |  |  |
| 53 | `SUBCODE01DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 54 | `SUBCODE02DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 55 | `SUBCODE03DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 56 | `SUBCODE04DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 57 | `SUBCODE05DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 58 | `SUBCODE06DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 59 | `SUBCODE07DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 60 | `SUBCODE08DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 61 | `SUBCODE09DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 62 | `SUBCODE10DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 63 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 64 | `PREVIOUSQUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 65 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 66 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 67 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 68 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 69 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 70 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 71 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 72 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 73 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 74 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 75 | `ITEMDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 76 | `VIRTUALITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 77 | `VIRTUALITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 78 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 79 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 80 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 81 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 82 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 83 | `PREVIOUSSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 84 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 85 | `PREVIOUSCOLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 86 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 87 | `PREVIOUSPROJECTCODE` | CHAR(20) |  |  |  |  |
| 88 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 89 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 90 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 91 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 92 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 93 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 94 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 95 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 96 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 97 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 98 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 99 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 100 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 101 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 102 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 103 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 104 | `PREVIOUSBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 105 | `PREVIOUSBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 106 | `PREVIOUSBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 107 | `PREVIOUSBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 108 | `PREVIOUSUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 109 | `PREVIOUSUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 110 | `PREVIOUSUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 111 | `PREVIOUSUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 112 | `PREVIOUSUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 113 | `PREVIOUSUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 114 | `USERPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 115 | `BASEPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 116 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 117 | `USERSECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 118 | `BASESECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 119 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 120 | `USERPACKAGINGUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 121 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 122 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 123 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 124 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 125 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 126 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 127 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 128 | `ALLOCATIONTODELETE` | SMALLINT | NOT NULL |  |  |  |
| 129 | `BOXHIDEUOM` | SMALLINT | NOT NULL |  |  |  |
| 130 | `RELATEDENTITYSTATUS` | CHAR(90) |  |  |  |  |
| 131 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 132 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 133 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 134 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 135 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 136 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 137 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 138 | `CONFIRMATION` | CHAR(15) |  |  |  |  |
| 139 | `REMINDERCOMMENTCODE` | CHAR(12) |  |  |  |  |
| 140 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 141 | `PREVIOUSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 142 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 143 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 144 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 145 | `PREVIOUSUSEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 146 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 147 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 148 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 149 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 150 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 151 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 152 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 153 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 154 | `STOPUPDATEFATHER` | SMALLINT | NOT NULL |  |  |  |
| 155 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 156 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 157 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 158 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 159 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 160 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 161 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 162 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 163 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 164 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 165 | `ORIGCONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 166 | `PREVIOUSCUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 167 | `PREVIOUSCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 168 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 169 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 170 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 171 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 172 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

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
FROM   DB2ADMIN.PODELIVERYBEAN t
FETCH FIRST 100 ROWS ONLY;
```
