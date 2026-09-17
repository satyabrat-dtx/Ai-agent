# DB2ADMIN.SALESORDERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `staging_mirror`
- **Columns**: 163
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 62315

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
| 7 | `INTERCOMPANYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `INTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 11 | `ORDERDATE` | DATE |  |  |  |  |
| 12 | `SOURCEDOCUMENTORDERTYPE` | CHAR(1) |  |  |  |  |
| 13 | `SOURCEDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 14 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 15 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 16 | `ORDERPARTNERBRANDCODE` | CHAR(8) |  |  |  |  |
| 17 | `DERIVATIONSTEP` | CHAR(2) |  |  |  |  |
| 18 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 19 | `FROMORDERPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 20 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 21 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 22 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 23 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 24 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 25 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 26 | `INITIALDATE` | DATE |  |  |  |  |
| 27 | `FINALDATE` | DATE |  |  |  |  |
| 28 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 29 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 30 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 31 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 32 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 33 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 34 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 35 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 36 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 37 | `GROUPORDERSONSHIPPING` | INTEGER | NOT NULL |  |  |  |
| 38 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 39 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 40 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 41 | `AREACODE` | CHAR(3) |  |  |  |  |
| 42 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 43 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 44 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 45 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 46 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 47 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 48 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 49 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 50 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 51 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 52 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 53 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 54 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 55 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 56 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 57 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 58 | `PRICEANDDISCOUNTDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 59 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 60 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 61 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 62 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 63 | `ONORDERTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 64 | `PAYMENTCUSTOMERUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 65 | `PAYMENTCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 66 | `MINAMOUNTACHIEVEMENTINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 67 | `BANKBOXBEGIN` | SMALLINT | NOT NULL |  |  |  |
| 68 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 69 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 70 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 71 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 72 | `COMPANYBANKBOXBEGIN` | SMALLINT | NOT NULL |  |  |  |
| 73 | `COMPANYBANKCODE` | CHAR(15) |  |  |  |  |
| 74 | `COMPANYBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 75 | `COMPANYBANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 76 | `COMPANYBANKIDIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 77 | `THIRDPARTYBILLING` | SMALLINT | NOT NULL |  |  |  |
| 78 | `COMMISSIONDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 79 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 80 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 81 | `AGENTCREATIONTYPE1` | CHAR(1) |  |  |  |  |
| 82 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 83 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 84 | `AGENTCREATIONTYPE2` | CHAR(1) |  |  |  |  |
| 85 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 86 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 87 | `AGENTCREATIONTYPE3` | CHAR(1) |  |  |  |  |
| 88 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 89 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 90 | `AGENTCREATIONTYPE4` | CHAR(1) |  |  |  |  |
| 91 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 92 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 93 | `AGENTCREATIONTYPE5` | CHAR(1) |  |  |  |  |
| 94 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 95 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 96 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 97 | `ORDERSOURCE` | CHAR(2) |  |  |  |  |
| 98 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 99 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 100 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 101 | `PRINTEDCONFIRMATION` | SMALLINT | NOT NULL |  |  |  |
| 102 | `LINESUNMATCHEDWITHBOX` | SMALLINT | NOT NULL |  |  |  |
| 103 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 104 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 105 | `FULLSCREEN` | SMALLINT | NOT NULL |  |  |  |
| 106 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 107 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 108 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 109 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 110 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 111 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 112 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 113 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 114 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 115 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 116 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 117 | `CREDITCHECKFORCED` | SMALLINT | NOT NULL |  |  |  |
| 118 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 119 | `COMPANYBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 120 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 121 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 122 | `PURORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 123 | `PURORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 124 | `REQUIREDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 125 | `CONFIRMEDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 126 | `KEEPENTRYEXCHANGERATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 127 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 128 | `PURORDERGENERATEDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 129 | `PURCHASEORDERGENERATEDCODE` | CHAR(15) |  |  |  |  |
| 130 | `RFORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 131 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 132 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 133 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 134 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 135 | `PURORDERCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 136 | `PLANNINGGROUPINGCODE` | CHAR(3) |  |  |  |  |
| 137 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 138 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 139 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 140 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 141 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 142 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 143 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 144 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 145 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 146 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 147 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 148 | `OVERDUEAMOUNTFORCED` | SMALLINT | NOT NULL |  |  |  |
| 149 | `TNAHEADERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 150 | `TNAHEADERCODE` | CHAR(10) |  |  |  |  |
| 151 | `ACTIVITYDATE` | TIMESTAMP |  |  |  |  |
| 152 | `TNASTARTDATE` | TIMESTAMP |  |  |  |  |
| 153 | `TNAENDDATE` | TIMESTAMP |  |  |  |  |
| 154 | `TNARECALCULATIONENDDATE` | TIMESTAMP |  |  |  |  |
| 155 | `TNASTATUS` | INTEGER | NOT NULL |  |  |  |
| 156 | `REALIGNTNA` | SMALLINT | NOT NULL |  |  |  |
| 157 | `GANTTMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 158 | `TNAGANTTRESOURCEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 159 | `TNAGANTTMARKERREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 160 | `TNAGANTTLINKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 161 | `TNAGANTTSUBTASKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 162 | `TNAACTIVITYGANTT` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESORDERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.INTERCOMPANYREQUIRED,
       t.INTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERDATE
FROM   DB2ADMIN.SALESORDERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
