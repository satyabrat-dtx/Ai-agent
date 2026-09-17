# DB2ADMIN.SALESORDERDELIVERYBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 150
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 67727

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 6 | `ORDERLINESTATUS` | CHAR(2) |  |  |  |  |
| 7 | `DELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 9 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 10 | `DELIVERYDATE` | DATE |  |  |  |  |
| 11 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 12 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 13 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 14 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 15 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 16 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 18 | `RESERVATIONDATE` | DATE |  |  |  |  |
| 19 | `DISTRIBUTIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 20 | `SCHEDULEDDELIVERYDATE` | DATE |  |  |  |  |
| 21 | `PRODUCTIONCONFIRMEDDATE` | DATE |  |  |  |  |
| 22 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 23 | `EFFECTIVEDELIVERYDATE` | DATE |  |  |  |  |
| 24 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 25 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 26 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
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
| 37 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 38 | `SELLINGITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 39 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 40 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 41 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 42 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 43 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 44 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 45 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 46 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 47 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 48 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 52 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 54 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 56 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 62 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 67 | `TRANSFERUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 68 | `TRANSFERBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 69 | `TRANSFERUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 70 | `TRANSFERBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 71 | `TRANSFERUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 72 | `TRANSFERSTATUS` | CHAR(2) |  |  |  |  |
| 73 | `RECEIVEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 74 | `RECEIVEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `RECEIVEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `RECEIVEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 77 | `RECEIVEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 78 | `RECEIVINGSTATUS` | CHAR(2) |  |  |  |  |
| 79 | `CONSIGNMENTTYPE` | CHAR(2) |  |  |  |  |
| 80 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 81 | `SELORDERITEMCODE` | VARCHAR(120) |  |  |  |  |
| 82 | `SELORDERSUBCODE01` | CHAR(20) |  |  |  |  |
| 83 | `SELORDERSUBCODE02` | CHAR(10) |  |  |  |  |
| 84 | `SELORDERSUBCODE03` | CHAR(10) |  |  |  |  |
| 85 | `SELORDERSUBCODE04` | CHAR(10) |  |  |  |  |
| 86 | `SELORDERSUBCODE05` | CHAR(10) |  |  |  |  |
| 87 | `SELORDERSUBCODE06` | CHAR(10) |  |  |  |  |
| 88 | `SELORDERSUBCODE07` | CHAR(10) |  |  |  |  |
| 89 | `SELORDERSUBCODE08` | CHAR(10) |  |  |  |  |
| 90 | `SELORDERSUBCODE09` | CHAR(10) |  |  |  |  |
| 91 | `SELORDERSUBCODE10` | CHAR(10) |  |  |  |  |
| 92 | `SELSUBCODE01DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 93 | `SELSUBCODE02DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 94 | `SELSUBCODE03DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 95 | `SELSUBCODE04DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 96 | `SELSUBCODE05DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 97 | `SELSUBCODE06DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 98 | `SELSUBCODE07DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 99 | `SELSUBCODE08DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 100 | `SELSUBCODE09DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 101 | `SELSUBCODE10DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 102 | `BOXHIDEUOM` | SMALLINT | NOT NULL |  |  |  |
| 103 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 104 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 105 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 106 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 107 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 108 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 109 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 110 | `CONFIRMATION` | CHAR(15) |  |  |  |  |
| 111 | `CUTTINGLISTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 112 | `CUTTINGLISTCODE` | CHAR(15) |  |  |  |  |
| 113 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 114 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 115 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 116 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 117 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 118 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 119 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 120 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 121 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 122 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 123 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 124 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 125 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 126 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 127 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 128 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 129 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 130 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 131 | `READYTOSHIP` | SMALLINT | NOT NULL |  |  |  |
| 132 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 133 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 134 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 135 | `SHIPPINGDATE` | DATE |  |  |  |  |
| 136 | `CUSTOMERDELIVERYDATE` | DATE |  |  |  |  |
| 137 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 138 | `FORCEVALUESFROMIMPORT` | SMALLINT | NOT NULL |  |  |  |
| 139 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 140 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 141 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 142 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 143 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 144 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 145 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 146 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 147 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 148 | `NOTDELETELINK` | SMALLINT | NOT NULL |  |  |  |
| 149 | `OVERDUEAMOUNTFORCED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESORDER**.`ABSUNIQUEID` (high confidence — name = 'SALESORDER' + known child suffix 'DELIVERY')
  - JOIN predicate: `SALESORDERDELIVERYBEAN.FATHERID = SALESORDER.ABSUNIQUEID`

## Indexes

- `SALESORDERDELIVERYBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.LINETEMPLATECODE,
       t.ORDERTYPE,
       t.ORDERLINESTATUS,
       t.DELIVERYLINE,
       t.DELIVERYPOINTUNIQUEID,
       t.DELIVERYPOINTCODE,
       t.DELIVERYDATE,
       t.PROGRESSSTATUS
FROM   DB2ADMIN.SALESORDERDELIVERYBEAN t
FETCH FIRST 100 ROWS ONLY;
```
