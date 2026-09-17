# DB2ADMIN.PURCHASEORDEREXTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`
- **Columns**: 182
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 112073

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PREVIOUSALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 5 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 6 | `CUSTOMERDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 7 | `PROGRESSSTATUSDESC` | CHAR(20) |  |  |  |  |
| 8 | `APPROVEDSTATUS` | INTEGER | NOT NULL |  |  |  |
| 9 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 10 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 11 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 12 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 13 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 14 | `ORDERDATE` | DATE |  |  |  |  |
| 15 | `SOURCEDOCUMENTORDERTYPE` | CHAR(1) |  |  |  |  |
| 16 | `SOURCEDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 17 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 18 | `ORDERPARTNERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 19 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 20 | `DERIVATIONSTEP` | CHAR(2) |  |  |  |  |
| 21 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 22 | `FROMORDERPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 23 | `INTERCOMPANYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 25 | `ALTERNATIVEADDRESSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 26 | `ALTERNATIVEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 27 | `DLVORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 28 | `DLVORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 29 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 30 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 31 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 32 | `INVOICEADDRESSTYPE` | CHAR(2) |  |  |  |  |
| 33 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 34 | `DELIVERYPOINTCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 35 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 36 | `APPLICANTCODE` | CHAR(50) |  |  |  |  |
| 37 | `APPROVED` | SMALLINT | NOT NULL |  |  |  |
| 38 | `REJECTED` | SMALLINT | NOT NULL |  |  |  |
| 39 | `REOPENLEVEL` | CHAR(2) |  |  |  |  |
| 40 | `RELEASELEVEL` | CHAR(2) |  |  |  |  |
| 41 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 42 | `APPROVALDATE` | DATE |  |  |  |  |
| 43 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 44 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 45 | `INITIALDATE` | DATE |  |  |  |  |
| 46 | `FINALDATE` | DATE |  |  |  |  |
| 47 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 48 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 49 | `EXTERNALREFERENCECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 50 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 51 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 52 | `INTERNALREFERENCECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 53 | `DIVISIONCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 54 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 55 | `STATISTICALGROUPCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 56 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 57 | `COLLECTIONGROUPCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 58 | `STATUSFLAG` | CHAR(1) |  |  |  |  |
| 59 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 60 | `PROJECTCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 61 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 62 | `LANGUAGECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 63 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 64 | `TERMSOFDELIVERYCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 65 | `DELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 66 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 67 | `TERMSOFSHIPPINGCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 68 | `SHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 69 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 70 | `TRANSPORTREASONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 71 | `TRANSPORTREASONCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 72 | `AREACODE` | CHAR(3) |  |  |  |  |
| 73 | `AREACHANGED` | SMALLINT | NOT NULL |  |  |  |
| 74 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 75 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 76 | `FIRSTCARRIERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 77 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 78 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 79 | `SECONDCARRIERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 80 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 81 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 82 | `THIRDCARRIERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 83 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 84 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 85 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 86 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 87 | `WAREHOUSECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 88 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 89 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 90 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 91 | `RELEASETYPECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 92 | `POACCEPTANCEREQUIRED` | CHAR(1) |  |  |  |  |
| 93 | `ENTRYEXCHANGERATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 94 | `CONDITIONRETRIEVINGDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 95 | `PAYMENTMETHODCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 96 | `DISCOUNTCATEGORYCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 97 | `TAXCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 98 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 99 | `ORDERCATEGORYCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 100 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 101 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 102 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 103 | `PRCANDDISCOUNTAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 104 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 105 | `PAYMENTSTARTINGDATE` | DATE |  |  |  |  |
| 106 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 107 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 108 | `ONORDERTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 109 | `BANKBOXBEGIN` | SMALLINT | NOT NULL |  |  |  |
| 110 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 111 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 112 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 113 | `BANKCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 114 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 115 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 116 | `INVOICEORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 117 | `INVOICEORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 118 | `INVOICEADDRESSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 119 | `INVOICEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 120 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 121 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 122 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 123 | `PROGRESSSTATUSCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 124 | `RUNMANUALCLOSURE` | SMALLINT | NOT NULL |  |  |  |
| 125 | `RELATEDENTITYSTATUS` | CHAR(90) |  |  |  |  |
| 126 | `SALESORDERGENERATEDCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 127 | `SALESORDERGENERATEDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 128 | `SALESORDERGENERATEDCODE` | CHAR(15) |  |  |  |  |
| 129 | `PRINTSTATUS` | CHAR(2) |  |  |  |  |
| 130 | `READFLAG` | SMALLINT | NOT NULL |  |  |  |
| 131 | `SUPPLIERACCEPTANCE` | INTEGER | NOT NULL |  |  |  |
| 132 | `SUPPLIERCOMMENT` | VARCHAR(140) |  |  |  |  |
| 133 | `ORDERSOURCE` | CHAR(2) |  |  |  |  |
| 134 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 135 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 136 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 137 | `LINESUNMATCHEDWITHBOX` | SMALLINT | NOT NULL |  |  |  |
| 138 | `HIERARCHICQUERY` | SMALLINT | NOT NULL |  |  |  |
| 139 | `IMAGE` | CHAR(65) |  |  |  |  |
| 140 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 141 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 142 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 143 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 144 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 145 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 146 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 147 | `FULLSCREEN` | SMALLINT | NOT NULL |  |  |  |
| 148 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 149 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 150 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 151 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 152 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 153 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 154 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 155 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 156 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 157 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 158 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 159 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 160 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 161 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 162 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 163 | `CUSTOMERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 164 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 165 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 166 | `REQUIREDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 167 | `CONFIRMEDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 168 | `ADDITIONALDATA` | BLOB(1000000) |  |  |  |  |
| 169 | `KEEPENTRYEXCHANGERATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 170 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 171 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 172 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 173 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 174 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 175 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 176 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 177 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 178 | `PREVIOUSDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 179 | `PREVIOUSORDERDATE` | DATE |  |  |  |  |
| 180 | `EXHANGERATEAPPLICATIONDOCTYPE` | CHAR(3) |  |  |  |  |
| 181 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDEREXTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.PREVIOUSALLOWEDDIVISIONS,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.FORCEDWARNING,
       t.COMPANYCODE,
       t.CUSTOMERDESCRIPTION,
       t.PROGRESSSTATUSDESC,
       t.APPROVEDSTATUS,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE
FROM   DB2ADMIN.PURCHASEORDEREXTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
