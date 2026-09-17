# DB2ADMIN.PURCHASEORDERIBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`
- **Columns**: 151
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 148575

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 5 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `ORDERTYPEE` | INTEGER | NOT NULL |  |  |  |
| 7 | `DDPAYABLEAT` | CHAR(30) |  |  |  |  |
| 8 | `DDCHARGESPAYBYE` | INTEGER | NOT NULL |  |  |  |
| 9 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 12 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 13 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 15 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 16 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 18 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 19 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 20 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 21 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 22 | `SELECTIONDATE` | DATE |  |  |  |  |
| 23 | `EXCISEINCLUSIVE` | CHAR(3) |  |  |  |  |
| 24 | `ADVANCEOPTION` | INTEGER | NOT NULL |  |  |  |
| 25 | `ORDERDATE` | DATE |  |  |  |  |
| 26 | `SOURCEDOCUMENTORDERTYPE` | CHAR(1) |  |  |  |  |
| 27 | `SOURCEDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 28 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 29 | `ORDERPARTNERSUPPLYSTATECODE` | CHAR(3) |  |  |  |  |
| 30 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 31 | `DERIVATIONSTEP` | CHAR(2) |  |  |  |  |
| 32 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 33 | `FROMORDERPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 34 | `INTERCOMPANYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 35 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 36 | `ALTERNATIVEADDRESSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 37 | `ALTERNATIVEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 38 | `DLVORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 39 | `DLVORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 40 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 41 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 42 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 43 | `INVOICEADDRESSTYPE` | CHAR(2) |  |  |  |  |
| 44 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 45 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 46 | `APPLICANTCODE` | CHAR(50) |  |  |  |  |
| 47 | `APPROVED` | SMALLINT | NOT NULL |  |  |  |
| 48 | `RELEASELEVEL` | CHAR(2) |  |  |  |  |
| 49 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 50 | `APPROVALDATE` | DATE |  |  |  |  |
| 51 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 52 | `INITIALDATE` | DATE |  |  |  |  |
| 53 | `FINALDATE` | DATE |  |  |  |  |
| 54 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 55 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 56 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 57 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 58 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 59 | `STATISTICALGROUPCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 60 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 61 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 62 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 63 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 64 | `CUSTOMERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 65 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 66 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 67 | `DELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 68 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 69 | `TERMSOFSHIPPINGCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 70 | `SHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 71 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 72 | `TRANSPORTREASONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 73 | `AREACODE` | CHAR(3) |  |  |  |  |
| 74 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 75 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 76 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 77 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 78 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 79 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 80 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 81 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 82 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 83 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 84 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 85 | `REQUIREDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 86 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 87 | `CONFIRMEDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 88 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 89 | `KEEPENTRYEXCHANGERATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 90 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 91 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 92 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 93 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 94 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 95 | `PRCANDDISCOUNTAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 96 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 97 | `PAYMENTSTARTINGDATE` | DATE |  |  |  |  |
| 98 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 99 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 100 | `ONORDERTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 101 | `BANKBOXBEGIN` | SMALLINT | NOT NULL |  |  |  |
| 102 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 103 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 104 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 105 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 106 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 107 | `INVOICEORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 108 | `INVOICEORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 109 | `INVOICEADDRESSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 110 | `INVOICEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 111 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 112 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 113 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 114 | `SALESORDERGENERATEDCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 115 | `SALESORDERGENERATEDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 116 | `SALESORDERGENERATEDCODE` | CHAR(15) |  |  |  |  |
| 117 | `PRINTSTATUS` | CHAR(2) |  |  |  |  |
| 118 | `READFLAG` | SMALLINT | NOT NULL |  |  |  |
| 119 | `SUPPLIERACCEPTANCE` | INTEGER | NOT NULL |  |  |  |
| 120 | `SUPPLIERCOMMENT` | VARCHAR(140) |  |  |  |  |
| 121 | `ORDERSOURCE` | CHAR(2) |  |  |  |  |
| 122 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 123 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 124 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 125 | `LINESUNMATCHEDWITHBOX` | SMALLINT | NOT NULL |  |  |  |
| 126 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 127 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 128 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 129 | `FULLSCREEN` | SMALLINT | NOT NULL |  |  |  |
| 130 | `MATRIXINPUT` | SMALLINT | NOT NULL |  |  |  |
| 131 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 132 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 133 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 134 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 135 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 136 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 137 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 138 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 139 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 140 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 141 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 142 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 143 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 144 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 145 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 146 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 147 | `PREVIOUSDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 148 | `PREVIOUSORDERDATE` | DATE |  |  |  |  |
| 149 | `EXHANGERATEAPPLICATIONDOCTYPE` | CHAR(3) |  |  |  |  |
| 150 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDERIBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.ORDERTYPEE,
       t.DDPAYABLEAT,
       t.DDCHARGESPAYBYE,
       t.SCHEMETYPECODE,
       t.TEMPLATECODE,
       t.ORDERTYPE
FROM   DB2ADMIN.PURCHASEORDERIBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
