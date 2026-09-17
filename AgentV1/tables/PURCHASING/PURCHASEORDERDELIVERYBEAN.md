# DB2ADMIN.PURCHASEORDERDELIVERYBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 125
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 59299

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
| 19 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 20 | `EFFECTIVEDELIVERYDATE` | DATE |  |  |  |  |
| 21 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 22 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 23 | `ORDERITEMCODE` | VARCHAR(120) |  |  |  |  |
| 24 | `ORDERSUBCODE01` | CHAR(20) |  |  |  |  |
| 25 | `ORDERSUBCODE02` | CHAR(10) |  |  |  |  |
| 26 | `ORDERSUBCODE03` | CHAR(10) |  |  |  |  |
| 27 | `ORDERSUBCODE04` | CHAR(10) |  |  |  |  |
| 28 | `ORDERSUBCODE05` | CHAR(10) |  |  |  |  |
| 29 | `ORDERSUBCODE06` | CHAR(10) |  |  |  |  |
| 30 | `ORDERSUBCODE07` | CHAR(10) |  |  |  |  |
| 31 | `ORDERSUBCODE08` | CHAR(10) |  |  |  |  |
| 32 | `ORDERSUBCODE09` | CHAR(10) |  |  |  |  |
| 33 | `ORDERSUBCODE10` | CHAR(10) |  |  |  |  |
| 34 | `SUBCODE01DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 35 | `SUBCODE02DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 36 | `SUBCODE03DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 37 | `SUBCODE04DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 38 | `SUBCODE05DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 39 | `SUBCODE06DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 40 | `SUBCODE07DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 41 | `SUBCODE08DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 42 | `SUBCODE09DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 43 | `SUBCODE10DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 44 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 45 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 46 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 47 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 48 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 49 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 50 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 51 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 52 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 53 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 54 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 55 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 56 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 57 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 58 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 59 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 60 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 61 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 62 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 63 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 64 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 66 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 67 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 68 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 69 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 70 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 71 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 72 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 73 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 74 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 77 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 78 | `PREVIOUSUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 80 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 81 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 82 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 84 | `BOXHIDEUOM` | SMALLINT | NOT NULL |  |  |  |
| 85 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 86 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 87 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 88 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 89 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 90 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 91 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 92 | `CONFIRMATION` | CHAR(15) |  |  |  |  |
| 93 | `REMINDERCOMMENTCODE` | CHAR(12) |  |  |  |  |
| 94 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 95 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 96 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 97 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 98 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 99 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 100 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 101 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 102 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 103 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 104 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 105 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 106 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 107 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 108 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 109 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 110 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 111 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 112 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 113 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 114 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 115 | `ORIGCONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 116 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 117 | `PREVIOUSCUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 118 | `PREVIOUSCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 119 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 120 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 121 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 122 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 123 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 124 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **PURCHASEORDER**.`ABSUNIQUEID` (high confidence — name = 'PURCHASEORDER' + known child suffix 'DELIVERY')
  - JOIN predicate: `PURCHASEORDERDELIVERYBEAN.FATHERID = PURCHASEORDER.ABSUNIQUEID`

## Indexes

- `PURCHASEORDERDELIVERYBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.PURCHASEORDERDELIVERYBEAN t
FETCH FIRST 100 ROWS ONLY;
```
