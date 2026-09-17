# DB2ADMIN.LOGPURCHASERETURNDOCUMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 141
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 65163

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 5 | `RETURNDATE` | DATE | NOT NULL |  |  |  |
| 6 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `DEFINITIVECODE` | CHAR(15) |  |  |  |  |
| 8 | `DEFINITIVEDATE` | DATE |  |  |  |  |
| 9 | `PRINTEDRETURN` | SMALLINT | NOT NULL |  |  |  |
| 10 | `RETURNSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `PURDLVPURORDLINEPURORDCNTCODE` | CHAR(8) |  |  |  |  |
| 12 | `PURDLVPURORDLINEPURORDERCODE` | CHAR(15) |  |  |  |  |
| 13 | `PURDLVPURORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 14 | `PURDLVPURORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 15 | `PURCHASEDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 16 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 17 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 18 | `CLAIMREASONCODE` | CHAR(3) |  |  |  |  |
| 19 | `RETURNDESCRIPTION` | CHAR(140) |  |  |  |  |
| 20 | `RETURNSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 21 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 22 | `APPROVALDATE` | DATE |  |  |  |  |
| 23 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 24 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 25 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 26 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 27 | `CUSTOMERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 28 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 29 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 30 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 31 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 32 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 33 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 34 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 35 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 36 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 37 | `TRANSPORTZONECOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 38 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 39 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 40 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 41 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 42 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 43 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 44 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 45 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 46 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 47 | `TRUCKDRIVERCODE` | CHAR(3) |  |  |  |  |
| 48 | `NUMBERPLATE` | VARCHAR(80) |  |  |  |  |
| 49 | `TRANSPORTSTARTDATE` | DATE |  |  |  |  |
| 50 | `TRANSPORTSTARTTIME` | TIME |  |  |  |  |
| 51 | `NUMBERPARCEL` | DECIMAL(5,0) |  |  |  |  |
| 52 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 53 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 54 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 55 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 56 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 57 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 58 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 59 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 60 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 61 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 62 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 63 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 64 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 65 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 66 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 67 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 68 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 69 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 70 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 71 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 72 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 73 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 74 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 75 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 76 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 77 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 78 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 80 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 81 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 82 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 84 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 85 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 86 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 87 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 88 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 89 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 90 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 91 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 92 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 93 | `WHSLOCWHSLOCWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 94 | `WHSLOCWAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 95 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 96 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 97 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 98 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 99 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 100 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 101 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 102 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 103 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 104 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 105 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 106 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 107 | `PRICESIGN` | CHAR(2) | NOT NULL |  |  |  |
| 108 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 109 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 110 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 111 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 112 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 113 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 114 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 115 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 116 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 117 | `ABSSHAREDUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 118 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 119 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 120 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 121 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 122 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 123 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 124 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 125 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 126 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 127 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 128 | `TRUCKDRIVERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 129 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 130 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 131 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 132 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 133 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 134 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 135 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 136 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 137 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 138 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 139 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 140 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPURCHASERETURNDOCUMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LINE,
       t.RETURNDATE,
       t.ORDERTYPE,
       t.DEFINITIVECODE,
       t.DEFINITIVEDATE,
       t.PRINTEDRETURN,
       t.RETURNSTOCKTYPECODE,
       t.PURDLVPURORDLINEPURORDCNTCODE
FROM   DB2ADMIN.LOGPURCHASERETURNDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
