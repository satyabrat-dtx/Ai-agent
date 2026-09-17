# DB2ADMIN.POHEADERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 166
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 110155

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PREVIOUSALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 5 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 6 | `CUSTOMERDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 7 | `APPROVEDSTATUS` | INTEGER | NOT NULL |  |  |  |
| 8 | `PROGRESSSTATUSDESC` | CHAR(20) |  |  |  |  |
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
| 25 | `ALTERNATIVEADDRESSUNIQUEID` | BIGINT |  |  |  |  |
| 26 | `ALTERNATIVEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 27 | `DLVORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 28 | `DLVORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 29 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 30 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 31 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 32 | `INVOICEADDRESSTYPE` | CHAR(2) |  |  |  |  |
| 33 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 34 | `DELIVERYPOINTCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 35 | `BUYERCODE` | CHAR(25) |  |  |  |  |
| 36 | `APPLICANTCODE` | CHAR(25) |  |  |  |  |
| 37 | `APPROVED` | SMALLINT | NOT NULL |  |  |  |
| 38 | `REJECTED` | SMALLINT | NOT NULL |  |  |  |
| 39 | `REOPENLEVEL` | CHAR(2) |  |  |  |  |
| 40 | `RELEASELEVEL` | CHAR(2) |  |  |  |  |
| 41 | `APPROVALUSER` | CHAR(25) |  |  |  |  |
| 42 | `APPROVALDATE` | DATE |  |  |  |  |
| 43 | `DESCRIPTION` | VARCHAR(100) |  |  | description |  |
| 44 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 45 | `INITIALDATE` | DATE |  |  |  |  |
| 46 | `FINALDATE` | DATE |  |  |  |  |
| 47 | `EXTERNALREFERENCE` | VARCHAR(100) |  |  |  |  |
| 48 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 49 | `EXTERNALREFERENCECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 50 | `INTERNALREFERENCE` | VARCHAR(100) |  |  |  |  |
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
| 65 | `DELIVERYDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 66 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 67 | `TERMSOFSHIPPINGCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 68 | `SHIPPINGDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 69 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 70 | `TRANSPORTREASONDESCRIPTION` | VARCHAR(100) |  |  |  |  |
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
| 93 | `READFLAG` | SMALLINT | NOT NULL |  |  |  |
| 94 | `ENTRYEXCHANGERATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 95 | `CONDITIONRETRIEVINGDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 96 | `PAYMENTMETHODCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 97 | `DISCOUNTCATEGORYCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 98 | `TAXCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 99 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 100 | `ORDERCATEGORYCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 101 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 102 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 103 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 104 | `PRCANDDISCOUNTAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 105 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 106 | `PAYMENTSTARTINGDATE` | DATE |  |  |  |  |
| 107 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 108 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 109 | `ONORDERTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 110 | `BANKBOXBEGIN` | SMALLINT | NOT NULL |  |  |  |
| 111 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 112 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 113 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 114 | `BANKCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 115 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 116 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 117 | `INVOICEORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 118 | `INVOICEORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 119 | `INVOICEADDRESSUNIQUEID` | BIGINT |  |  |  |  |
| 120 | `INVOICEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 121 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 122 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 123 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 124 | `PROGRESSSTATUSCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 125 | `RUNMANUALCLOSURE` | SMALLINT | NOT NULL |  |  |  |
| 126 | `RELATEDENTITYSTATUS` | CHAR(90) |  |  |  |  |
| 127 | `SALESORDERGENERATEDCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 128 | `SALESORDERGENERATEDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 129 | `SALESORDERGENERATEDCODE` | CHAR(15) |  |  |  |  |
| 130 | `PRINTSTATUS` | CHAR(2) |  |  |  |  |
| 131 | `ORDERSOURCE` | CHAR(2) |  |  |  |  |
| 132 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 133 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 134 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 135 | `LINESUNMATCHEDWITHBOX` | SMALLINT | NOT NULL |  |  |  |
| 136 | `HIERARCHICQUERY` | SMALLINT | NOT NULL |  |  |  |
| 137 | `IMAGE` | CHAR(65) |  |  |  |  |
| 138 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 139 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 140 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 141 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 142 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 143 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 144 | `FULLSCREEN` | SMALLINT | NOT NULL |  |  |  |
| 145 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 146 | `WFMSTATUSREASONCODE` | CHAR(9) |  |  |  |  |
| 147 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 148 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 149 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 150 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 151 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 152 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 153 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 154 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 155 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 156 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 157 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 158 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 159 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 160 | `CUSTOMERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 161 | `SUPPLIERACCEPTANCE` | INTEGER | NOT NULL |  |  |  |
| 162 | `SUPPLIERCOMMENT` | VARCHAR(140) |  |  |  |  |
| 163 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 164 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 165 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PREVIOUSALLOWEDDIVISIONS,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.FORCEDWARNING,
       t.COMPANYCODE,
       t.CUSTOMERDESCRIPTION,
       t.APPROVEDSTATUS,
       t.PROGRESSSTATUSDESC,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE
FROM   DB2ADMIN.POHEADERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
