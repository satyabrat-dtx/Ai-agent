# DB2ADMIN.LOGEXTOPLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 176
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 213395

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `COUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 5 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 7 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `ENTRYTRANSMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `LINESOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `EXTOPLINECANCELLED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `STEPPRODEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `STEPPRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 15 | `STEPSTEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 16 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 17 | `ORDERDATE` | DATE | NOT NULL |  |  |  |
| 18 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 19 | `DLVORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 20 | `DLVORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 21 | `INVOICEADDRESSTYPE` | CHAR(2) |  |  |  |  |
| 22 | `INVOICEORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 23 | `INVOICEORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 24 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 26 | `BOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 27 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 28 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 29 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 39 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 40 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 41 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 42 | `ENTRYITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `ENTRYITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 44 | `ENTRYSUBCODE01` | CHAR(20) |  |  |  |  |
| 45 | `ENTRYSUBCODE02` | CHAR(10) |  |  |  |  |
| 46 | `ENTRYSUBCODE03` | CHAR(10) |  |  |  |  |
| 47 | `ENTRYSUBCODE04` | CHAR(10) |  |  |  |  |
| 48 | `ENTRYSUBCODE05` | CHAR(10) |  |  |  |  |
| 49 | `ENTRYSUBCODE06` | CHAR(10) |  |  |  |  |
| 50 | `ENTRYSUBCODE07` | CHAR(10) |  |  |  |  |
| 51 | `ENTRYSUBCODE08` | CHAR(10) |  |  |  |  |
| 52 | `ENTRYSUBCODE09` | CHAR(10) |  |  |  |  |
| 53 | `ENTRYSUBCODE10` | CHAR(10) |  |  |  |  |
| 54 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 55 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 56 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 57 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 59 | `ENTRYUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `ENTRYUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 61 | `ENTRYBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 62 | `ENTRYBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 63 | `ENTRYUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `ENTRYUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 65 | `ENTRYBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `ENTRYBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 67 | `ENTRYUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 68 | `ENTRYUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 69 | `PARAMETERQUANTITYTYPE` | CHAR(1) |  |  |  |  |
| 70 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 71 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 72 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 73 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 74 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `ENTEREDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `ENTEREDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 77 | `ENTEREDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 78 | `ENTEREDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `ENTEREDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 80 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 81 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 82 | `LINESTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 83 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 84 | `EXTENDEDSTATUS` | CHAR(2) |  |  |  |  |
| 85 | `SUPPLIERWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 86 | `SUPPLIERWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 87 | `PRINTED` | SMALLINT | NOT NULL |  |  |  |
| 88 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 89 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 90 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 91 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 92 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 93 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 94 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 95 | `ISSUEWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 96 | `ISSUEWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 97 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 98 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 99 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 100 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 101 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 102 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 103 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 104 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 105 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 106 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 107 | `DELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 108 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 109 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 110 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 111 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 112 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 113 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 114 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 115 | `AREACODE` | CHAR(3) |  |  |  |  |
| 116 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 117 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 118 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 119 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 120 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 121 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 122 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 123 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 124 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 125 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 126 | `CONDITIONRETRIEVINGDATE` | DATE | NOT NULL |  |  |  |
| 127 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 128 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 129 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 130 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 131 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 132 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 133 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 134 | `PRICESIGN` | CHAR(2) | NOT NULL |  |  |  |
| 135 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 136 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 137 | `ORIGINALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 138 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 139 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 140 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 141 | `TAXABLEINCOMEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 142 | `NETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 143 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 144 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 145 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 146 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 147 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 148 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 149 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 150 | `ORDPRNBANKORDPRNCSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 151 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 152 | `INVOICEADDRESSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 153 | `INVOICEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 154 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 155 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 156 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 157 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 158 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 159 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 160 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 161 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 162 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 163 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 164 | `ABSSHAREDUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 165 | `CONFIRMEDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 166 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 167 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 168 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 169 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 170 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 171 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 172 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 173 | `SUPPLIERACCEPTED` | SMALLINT | NOT NULL |  |  |  |
| 174 | `SUPPLIERACCEPTANCEDATE` | DATE |  |  |  |  |
| 175 | `PLANNEDPICKUPDATE` | DATE |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEXTOPLINE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGEXTOPLINEDISCOUNT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGEXTOPLINECHARGE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGEXTOPLINECOMMENT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGEXTOPLINESTOCKTRANSACTION`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)
- child `LOGEXTOPLINERESERVATION`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)
- child `LOGEXTOPLINEENTRYTRANSACTION`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERLINE,
       t.LINETEMPLATECODE,
       t.ENTRYTRANSMANAGEMENT,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.LINESOURCE
FROM   DB2ADMIN.LOGEXTOPLINE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
