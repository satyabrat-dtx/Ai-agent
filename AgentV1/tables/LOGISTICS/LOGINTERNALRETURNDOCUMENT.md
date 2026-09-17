# DB2ADMIN.LOGINTERNALRETURNDOCUMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 129
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 52325

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
| 11 | `INTDOCLINEINTDOCPRVCNTCODE` | CHAR(8) |  |  |  |  |
| 12 | `INTDOCLINEINTDOCPRVCODE` | CHAR(15) |  |  |  |  |
| 13 | `INTERNALDOCUMENTLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 14 | `INTDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 15 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 16 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 17 | `CLAIMREASONCODE` | CHAR(3) |  |  |  |  |
| 18 | `RETURNDESCRIPTION` | CHAR(140) |  |  |  |  |
| 19 | `DESTINATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `RETURNSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 21 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 22 | `APPROVALDATE` | DATE |  |  |  |  |
| 23 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 24 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 25 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 26 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 27 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 28 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 29 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 30 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 31 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 32 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 33 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 34 | `TRANSPORTZONECOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 35 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 36 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 37 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 38 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 39 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 40 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 41 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 42 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 43 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 44 | `TRUCKDRIVERCODE` | CHAR(3) |  |  |  |  |
| 45 | `NUMBERPLATE` | VARCHAR(80) |  |  |  |  |
| 46 | `TRANSPORTSTARTDATE` | DATE |  |  |  |  |
| 47 | `TRANSPORTSTARTTIME` | TIME |  |  |  |  |
| 48 | `NUMBERPARCEL` | DECIMAL(5,0) |  |  |  |  |
| 49 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 50 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 51 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 52 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 53 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 54 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 55 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 56 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 57 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 58 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 59 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 60 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 61 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 62 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 63 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 64 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 65 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 66 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 67 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 68 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 69 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 70 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 71 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 72 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 73 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 74 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 76 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 77 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 78 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 80 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 81 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 82 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 84 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 85 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 86 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 87 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 88 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 89 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 90 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 91 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 92 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 93 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 94 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 95 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 96 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 97 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 98 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 99 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 100 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 101 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 102 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 103 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 104 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 105 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 106 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 107 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 108 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 109 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 110 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 111 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 112 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 113 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 114 | `TRUCKDRIVERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 115 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 116 | `QUALITYITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 117 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 118 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 119 | `WHSLOCWHSZONEPHYWHSCMYCODE` | CHAR(3) |  |  |  |  |
| 120 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 121 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 122 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 123 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 124 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 125 | `ABSSHAREDUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 126 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 127 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 128 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGINTERNALRETURNDOCUMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

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
       t.INTDOCLINEINTDOCPRVCNTCODE
FROM   DB2ADMIN.LOGINTERNALRETURNDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
