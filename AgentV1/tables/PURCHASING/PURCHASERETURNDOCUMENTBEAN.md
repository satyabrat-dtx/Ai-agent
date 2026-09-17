# DB2ADMIN.PURCHASERETURNDOCUMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`
- **Columns**: 153
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 116059

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 5 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `LINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `RETURNDATE` | DATE |  |  |  |  |
| 8 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `RUNDEFINITIVE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `RUNDEFINITIVEPREVIOUS` | SMALLINT | NOT NULL |  |  |  |
| 11 | `DEFINITIVECODE` | CHAR(15) |  |  |  |  |
| 12 | `DEFINITIVEDATE` | DATE |  |  |  |  |
| 13 | `PRINTEDRETURN` | SMALLINT | NOT NULL |  |  |  |
| 14 | `RETURNSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 15 | `PURDLVPURORDLINEPURORDCNTCODE` | CHAR(8) |  |  |  |  |
| 16 | `PURDLVPURORDLINEPURORDERCODE` | CHAR(15) |  |  |  |  |
| 17 | `PURDLVPURORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 18 | `PURDLVPURORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 19 | `PURCHASEDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 20 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 21 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 22 | `CLAIMREASONCODE` | CHAR(3) |  |  |  |  |
| 23 | `RETURNDESCRIPTION` | CHAR(140) |  |  |  |  |
| 24 | `RETURNSTATUS` | CHAR(2) |  |  |  |  |
| 25 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 26 | `APPROVALDATE` | DATE |  |  |  |  |
| 27 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 28 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 29 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 30 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 31 | `CUSTOMERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 32 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 33 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 34 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 35 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 36 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 37 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 38 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 39 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 40 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 41 | `TRANSPORTZONECOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 42 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 43 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 44 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 45 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 46 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 47 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 48 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 49 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 50 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 51 | `TRUCKDRIVERCODE` | CHAR(3) |  |  |  |  |
| 52 | `NUMBERPLATE` | VARCHAR(80) |  |  |  |  |
| 53 | `TRANSPORTSTARTDATE` | DATE |  |  |  |  |
| 54 | `TRANSPORTSTARTTIME` | TIME |  |  |  |  |
| 55 | `NUMBERPARCEL` | DECIMAL(5,0) |  |  |  |  |
| 56 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 57 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 58 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 59 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 60 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 61 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 62 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 63 | `RUNAPPROVE` | SMALLINT | NOT NULL |  |  |  |
| 64 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
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
| 75 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 76 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 77 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 78 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 79 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 80 | `BOXHIDEUOM` | SMALLINT | NOT NULL |  |  |  |
| 81 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 82 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 84 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 85 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 86 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 87 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 88 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 89 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 90 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 91 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 92 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 93 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 94 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 95 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 96 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 97 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 98 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 99 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 100 | `WHSLOCWHSLOCWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 101 | `WHSLOCWAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 102 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 103 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 104 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 105 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 106 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 107 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 108 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 109 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 110 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 111 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 112 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 113 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 114 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 115 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 116 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 117 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 118 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 119 | `AUTOMATICCREATION` | SMALLINT | NOT NULL |  |  |  |
| 120 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 121 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 122 | `FIRSTISSUEDONE` | CHAR(2) |  |  |  |  |
| 123 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 124 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 125 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 126 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 127 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 128 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 129 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 130 | `ABSSHAREDUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 131 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 132 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 133 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 134 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 135 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 136 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 137 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 138 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 139 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 140 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 141 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 142 | `EVENTCOMPONENT` | CHAR(20) |  |  |  |  |
| 143 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 144 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 145 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 146 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 147 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 148 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 149 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 150 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 151 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 152 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASERETURNDOCUMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.FORCEDWARNING,
       t.CODE,
       t.LINE,
       t.RETURNDATE,
       t.ORDERTYPE,
       t.RUNDEFINITIVE,
       t.RUNDEFINITIVEPREVIOUS,
       t.DEFINITIVECODE
FROM   DB2ADMIN.PURCHASERETURNDOCUMENTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
