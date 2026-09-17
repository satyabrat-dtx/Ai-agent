# DB2ADMIN.LOGSALESRELEASELINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 182
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 55848

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 6 | `SUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 7 | `COMPONENTRELEASELINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 8 | `RELEASEDATE` | DATE | NOT NULL |  |  |  |
| 9 | `DLVSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 10 | `DLVSALORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 11 | `DLVSALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 12 | `DLVSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 13 | `DLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 14 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 15 | `CURRENTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 16 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 17 | `PICKINGCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 18 | `PICKINGCODE` | CHAR(15) |  |  |  |  |
| 19 | `RELEASELINESOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 20 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 21 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 22 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 23 | `ORDERDATE` | DATE | NOT NULL |  |  |  |
| 24 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 25 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 26 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 27 | `ORDERPARTNERBRANDCODE` | CHAR(8) |  |  |  |  |
| 28 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 29 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 30 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 31 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 32 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 33 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 34 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 35 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 36 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 37 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 38 | `DISTRIBUTIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 39 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 40 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 41 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 42 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 43 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 44 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 45 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 46 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 47 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 48 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 49 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 50 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 51 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 52 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 53 | `SELLINGITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 54 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 55 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 56 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 57 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 58 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 59 | `CONSIGNMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 60 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 61 | `RELEASEUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 62 | `RELEASEUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 63 | `RELEASEBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `RELEASEBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 65 | `RELEASEUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `RELEASEUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 67 | `RELEASEBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 68 | `RELEASEBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 69 | `RELEASEUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 70 | `RELEASEUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 71 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 72 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 73 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 74 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `TRANSFERUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 77 | `TRANSFERBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 78 | `TRANSFERUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `TRANSFERBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 80 | `TRANSFERUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 81 | `TRANSFERSTATUS` | CHAR(2) |  |  |  |  |
| 82 | `RECEIVEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `RECEIVEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 84 | `RECEIVEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 85 | `RECEIVEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 86 | `RECEIVEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 87 | `RECEIVINGSTATUS` | CHAR(2) |  |  |  |  |
| 88 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 89 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 90 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 91 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 92 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 93 | `AREACODE` | CHAR(3) |  |  |  |  |
| 94 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 95 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 96 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 97 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 98 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 99 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 100 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 101 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 102 | `CONDITIONRETRIEVINGDATE` | DATE | NOT NULL |  |  |  |
| 103 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 104 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 105 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 106 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 107 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 108 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 109 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 110 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 111 | `PRICESIGN` | CHAR(2) | NOT NULL |  |  |  |
| 112 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 113 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 114 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 115 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 116 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 117 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 118 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 119 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 120 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 121 | `AGENTCREATIONTYPE1` | CHAR(1) | NOT NULL |  |  |  |
| 122 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 123 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 124 | `AGENTCREATIONTYPE2` | CHAR(1) | NOT NULL |  |  |  |
| 125 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 126 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 127 | `AGENTCREATIONTYPE3` | CHAR(1) | NOT NULL |  |  |  |
| 128 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 129 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 130 | `AGENTCREATIONTYPE4` | CHAR(1) | NOT NULL |  |  |  |
| 131 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 132 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 133 | `AGENTCREATIONTYPE5` | CHAR(1) | NOT NULL |  |  |  |
| 134 | `PAYMENTCUSTOMERUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 135 | `PAYMENTCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 136 | `MINAMOUNTACHIEVEMENTINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 137 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 138 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 139 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 140 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 141 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 142 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 143 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 144 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 145 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 146 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 147 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 148 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 149 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 150 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 151 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 152 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 153 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 154 | `DISTRIBUTIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 155 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 156 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 157 | `CONSIGNMENTWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 158 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 159 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 160 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 161 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 162 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 163 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 164 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 165 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 166 | `MANUFACTORINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 167 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 168 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 169 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 170 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 171 | `RFORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 172 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 173 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 174 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 175 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 176 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 177 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 178 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 179 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 180 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 181 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGSALESRELEASELINE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGSALESRELEASELINEBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESRELEASELINECHARGE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESRELEASELINECOMMISSION`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)
- child `LOGSALESRELEASELINEDISCOUNT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.ABSVERSIONNUMBER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.CODE,
       t.LINE,
       t.SUBLINE,
       t.COMPONENTRELEASELINE,
       t.RELEASEDATE,
       t.DLVSALORDLINESALORDCNTCODE,
       t.DLVSALORDERLINESALESORDERCODE,
       t.DLVSALESORDERLINEORDERLINE
FROM   DB2ADMIN.LOGSALESRELEASELINE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
