# DB2ADMIN.LOGSALESCLAIMLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 234
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 53679

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 6 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `CLAIMDATE` | DATE | NOT NULL |  |  |  |
| 8 | `CLAIMUSERCODE` | CHAR(50) |  |  |  |  |
| 9 | `CLAIMTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 10 | `CLAIMLINESOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `INVOICEDEFINITIVECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 12 | `INVOICEDEFINITIVECODE` | CHAR(15) |  |  |  |  |
| 13 | `INVOICEDEFINITIVEDATE` | DATE |  |  |  |  |
| 14 | `INVOICELINESALDOCPRVCNTCODE` | CHAR(8) |  |  |  |  |
| 15 | `INVOICELINESALDOCPRVCODE` | CHAR(15) |  |  |  |  |
| 16 | `INVOICELINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 17 | `INVOICELINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 18 | `INVOICELINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 19 | `INVOICEPROVISIONALDATE` | DATE |  |  |  |  |
| 20 | `CLAIMREASONCODE` | CHAR(3) |  |  |  |  |
| 21 | `CLAIMTYPECODE` | CHAR(3) |  |  |  |  |
| 22 | `CLAIMDESCRIPTION` | CHAR(140) |  |  |  |  |
| 23 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 24 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 25 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 26 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 27 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 28 | `CUSTOMERADDRESS` | CHAR(100) |  |  |  |  |
| 29 | `CUSTOMERPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 30 | `CUSTOMERCONTACT` | CHAR(30) |  |  |  |  |
| 31 | `CLAIMTERMSCODE` | CHAR(3) |  |  |  |  |
| 32 | `CLAIMSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 33 | `CLAIMSTATUSDATE` | DATE | NOT NULL |  |  |  |
| 34 | `APPROVALUSERCODE` | CHAR(50) |  |  |  |  |
| 35 | `APPROVALDATE` | DATE |  |  |  |  |
| 36 | `DECLINATIONUSERCODE` | CHAR(50) |  |  |  |  |
| 37 | `DECLINATIONDATE` | DATE |  |  |  |  |
| 38 | `RETURNAUTHEXPDATE` | DATE |  |  |  |  |
| 39 | `PRINTEDCLAIM` | SMALLINT | NOT NULL |  |  |  |
| 40 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 41 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 42 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 43 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 44 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 45 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 46 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 47 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 48 | `AREACODE` | CHAR(3) |  |  |  |  |
| 49 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 50 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 51 | `AGENTCREATIONTYPE1` | CHAR(1) | NOT NULL |  |  |  |
| 52 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 53 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 54 | `AGENTCREATIONTYPE2` | CHAR(1) | NOT NULL |  |  |  |
| 55 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 56 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 57 | `AGENTCREATIONTYPE3` | CHAR(1) | NOT NULL |  |  |  |
| 58 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 59 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 60 | `AGENTCREATIONTYPE4` | CHAR(1) | NOT NULL |  |  |  |
| 61 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 62 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 63 | `AGENTCREATIONTYPE5` | CHAR(1) | NOT NULL |  |  |  |
| 64 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 65 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 66 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 67 | `CONSIGNMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 68 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 69 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 70 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 71 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 72 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 73 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 74 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 75 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 76 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 77 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 78 | `BILLLINESALDOCPRVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 79 | `BILLLINESALDOCPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 80 | `BILLLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 81 | `BILLLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 82 | `BILLLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 83 | `BILLPROVISIONALDATE` | DATE |  |  |  |  |
| 84 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 85 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 86 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 87 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 88 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 89 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 90 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 91 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 92 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 93 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 94 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 95 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 96 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 97 | `SELLINGITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 98 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 99 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 100 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 101 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 102 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 103 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 104 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 105 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 106 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 107 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 108 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 109 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 110 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 111 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 112 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 113 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 114 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 115 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 116 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 117 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 118 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 119 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 120 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 121 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 122 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 123 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 124 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 125 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 126 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 127 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 128 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 129 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 130 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 131 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 132 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 133 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 134 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 135 | `INSPECTIONCODE` | CHAR(10) |  |  |  |  |
| 136 | `INSPECTIONDATE` | DATE |  |  |  |  |
| 137 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 138 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 139 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 140 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 141 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 142 | `INVOICELINENETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 143 | `INVOICEDPRICE` | DECIMAL(18,5) |  |  |  |  |
| 144 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 145 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 146 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 147 | `PRICESIGN` | CHAR(2) | NOT NULL |  |  |  |
| 148 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 149 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 150 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 151 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 152 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 153 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 154 | `PAYMENTCUSTOMERUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 155 | `PAYMENTCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 156 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 157 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 158 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 159 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 160 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 161 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 162 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 163 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 164 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 165 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 166 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 167 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 168 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 169 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 170 | `CLAIMUSERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 171 | `INVOICEDEFINITIVECNTCMYCODE` | CHAR(3) |  |  |  |  |
| 172 | `CLAIMTERMSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 173 | `APPROVALUSERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 174 | `DECLINATIONUSERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 175 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 176 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 177 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 178 | `CONSIGNMENTWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 179 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 180 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 181 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 182 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 183 | `QUALITYREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 184 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 185 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 186 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 187 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 188 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 189 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 190 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 191 | `ENTRYCSMWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 192 | `ENTRYCUSTOMERWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 193 | `CLAIMPROGRESSSTATUSCODE` | CHAR(3) |  |  |  |  |
| 194 | `HEADERDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 195 | `ENTEREDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 196 | `ENTEREDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 197 | `ENTEREDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 198 | `ENTEREDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 199 | `ENTEREDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 200 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 201 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 202 | `CREDITUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 203 | `CREDITBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 204 | `CREDITUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 205 | `CREDITBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 206 | `CREDITUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 207 | `SALESORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 208 | `SALESORDERCODE` | CHAR(15) |  |  |  |  |
| 209 | `ORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 210 | `ORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 211 | `ORDERLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 212 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 213 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 214 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 215 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 216 | `ABSSHAREDUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 217 | `CREDITNOTEUSERPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 218 | `CREDITNOTEBASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 219 | `CREDITNOTEUSERSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 220 | `CREDITNOTEBASESECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 221 | `CREDITNOTEUSERPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 222 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 223 | `RFORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 224 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 225 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 226 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 227 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 228 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 229 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 230 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 231 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 232 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 233 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGSALESCLAIMLINE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGSALESCLAIMLINEDISCOUNT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.ABSVERSIONNUMBER,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LINE,
       t.ORDERTYPE,
       t.CLAIMDATE,
       t.CLAIMUSERCODE,
       t.CLAIMTEMPLATECODE,
       t.CLAIMLINESOURCE,
       t.INVOICEDEFINITIVECOUNTERCODE
FROM   DB2ADMIN.LOGSALESCLAIMLINE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
