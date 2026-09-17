# DB2ADMIN.LOGPURCHASEORDER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 121
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 64744

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 7 | `COUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 8 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `ORDERDATE` | DATE | NOT NULL |  |  |  |
| 10 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `INTERCOMPANYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 13 | `ALTERNATIVEADDRESSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 14 | `ALTERNATIVEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 15 | `DLVORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 16 | `DLVORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 17 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 18 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 19 | `INVOICEADDRESSTYPE` | CHAR(2) |  |  |  |  |
| 20 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 21 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 22 | `APPLICANTCODE` | CHAR(50) |  |  |  |  |
| 23 | `RELEASELEVEL` | CHAR(2) |  |  |  |  |
| 24 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 25 | `APPROVALDATE` | DATE |  |  |  |  |
| 26 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 27 | `INITIALDATE` | DATE |  |  |  |  |
| 28 | `FINALDATE` | DATE |  |  |  |  |
| 29 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 30 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 31 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 32 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 33 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 34 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 35 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 36 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 37 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 38 | `DELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 39 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 40 | `SHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 41 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 42 | `TRANSPORTREASONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 43 | `AREACODE` | CHAR(3) |  |  |  |  |
| 44 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 45 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 46 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 47 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 48 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 49 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 50 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 51 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 52 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 53 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 54 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 55 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 56 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 57 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 58 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 59 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 60 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 61 | `PRCANDDISCOUNTAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 62 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 63 | `PAYMENTSTARTINGDATE` | DATE |  |  |  |  |
| 64 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 65 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 66 | `ONORDERTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 67 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 68 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 69 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 70 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 71 | `INVOICEORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 72 | `INVOICEORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 73 | `INVOICEADDRESSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 74 | `INVOICEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 75 | `CURRENTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 76 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 77 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 78 | `PRINTSTATUS` | CHAR(2) |  |  |  |  |
| 79 | `ORDERSOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 80 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 81 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 82 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 83 | `LINESUNMATCHEDWITHBOX` | SMALLINT | NOT NULL |  |  |  |
| 84 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 85 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 86 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 87 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 88 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 89 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 90 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 91 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 92 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 93 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 94 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 95 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 96 | `BUYERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 97 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 98 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 99 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 100 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 101 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 102 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 103 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 104 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 105 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 106 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 107 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 108 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 109 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 110 | `READFLAG` | SMALLINT | NOT NULL |  |  |  |
| 111 | `SUPPLIERACCEPTANCE` | INTEGER | NOT NULL |  |  |  |
| 112 | `SUPPLIERCOMMENT` | VARCHAR(140) |  |  |  |  |
| 113 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 114 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 115 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 116 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 117 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 118 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 119 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 120 | `EXHANGERATEAPPLICATIONDOCTYPE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPURCHASEORDER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGPURCHASEORDERASSORTMENT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGPURCHASEORDERBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGPURCHASEORDERCHARGE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGPURCHASEORDERDISCOUNT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGPURCHASEORDERDELIVERY`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGPURCHASEORDERLINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGPURCHASEORDERTEMPLATE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.ABSVERSIONNUMBER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERDATE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.INTERCOMPANYREQUIRED
FROM   DB2ADMIN.LOGPURCHASEORDER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
