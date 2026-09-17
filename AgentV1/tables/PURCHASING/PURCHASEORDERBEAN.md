# DB2ADMIN.PURCHASEORDERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`
- **Columns**: 133
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 62150

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 6 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 7 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `ORDERDATE` | DATE |  |  |  |  |
| 10 | `SOURCEDOCUMENTORDERTYPE` | CHAR(1) |  |  |  |  |
| 11 | `SOURCEDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 12 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 13 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 14 | `DERIVATIONSTEP` | CHAR(2) |  |  |  |  |
| 15 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 16 | `FROMORDERPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 17 | `INTERCOMPANYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 19 | `ALTERNATIVEADDRESSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 20 | `ALTERNATIVEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 21 | `DLVORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `DLVORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 23 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 24 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 25 | `INVOICEADDRESSTYPE` | CHAR(2) |  |  |  |  |
| 26 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 27 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 28 | `APPLICANTCODE` | CHAR(50) |  |  |  |  |
| 29 | `APPROVED` | SMALLINT | NOT NULL |  |  |  |
| 30 | `RELEASELEVEL` | CHAR(2) |  |  |  |  |
| 31 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 32 | `APPROVALDATE` | DATE |  |  |  |  |
| 33 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 34 | `INITIALDATE` | DATE |  |  |  |  |
| 35 | `FINALDATE` | DATE |  |  |  |  |
| 36 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 37 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 38 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 39 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 40 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 41 | `STATISTICALGROUPCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 42 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 43 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 44 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 45 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 46 | `DELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 47 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 48 | `TERMSOFSHIPPINGCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 49 | `SHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 50 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 51 | `TRANSPORTREASONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 52 | `AREACODE` | CHAR(3) |  |  |  |  |
| 53 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 54 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 55 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 56 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 57 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 58 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 59 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 60 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 61 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 62 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 63 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 64 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 65 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 66 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 67 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 68 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 69 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 70 | `PRCANDDISCOUNTAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 71 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 72 | `PAYMENTSTARTINGDATE` | DATE |  |  |  |  |
| 73 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 74 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 75 | `ONORDERTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 76 | `BANKBOXBEGIN` | SMALLINT | NOT NULL |  |  |  |
| 77 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 78 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 79 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 80 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 81 | `INVOICEORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 82 | `INVOICEORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 83 | `INVOICEADDRESSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 84 | `INVOICEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 85 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 86 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 87 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 88 | `SALESORDERGENERATEDCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 89 | `SALESORDERGENERATEDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 90 | `SALESORDERGENERATEDCODE` | CHAR(15) |  |  |  |  |
| 91 | `PRINTSTATUS` | CHAR(2) |  |  |  |  |
| 92 | `ORDERSOURCE` | CHAR(2) |  |  |  |  |
| 93 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 94 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 95 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 96 | `LINESUNMATCHEDWITHBOX` | SMALLINT | NOT NULL |  |  |  |
| 97 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 98 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 99 | `FULLSCREEN` | SMALLINT | NOT NULL |  |  |  |
| 100 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 101 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 102 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 103 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 104 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 105 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 106 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 107 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 108 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 109 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 110 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 111 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 112 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 113 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 114 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 115 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 116 | `READFLAG` | SMALLINT | NOT NULL |  |  |  |
| 117 | `SUPPLIERACCEPTANCE` | INTEGER | NOT NULL |  |  |  |
| 118 | `SUPPLIERCOMMENT` | VARCHAR(140) |  |  |  |  |
| 119 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 120 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 121 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 122 | `CUSTOMERCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 123 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 124 | `REQUIREDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 125 | `CONFIRMEDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 126 | `KEEPENTRYEXCHANGERATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 127 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 128 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 129 | `PREVIOUSDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 130 | `PREVIOUSORDERDATE` | DATE |  |  |  |  |
| 131 | `EXHANGERATEAPPLICATIONDOCTYPE` | CHAR(3) |  |  |  |  |
| 132 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERDATE,
       t.SOURCEDOCUMENTORDERTYPE,
       t.SOURCEDOCUMENTTYPE
FROM   DB2ADMIN.PURCHASEORDERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
