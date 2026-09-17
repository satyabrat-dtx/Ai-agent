# DB2ADMIN.SALESORDERIBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `staging_mirror`
- **Columns**: 177
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 148982

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 5 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `TYPEOFINVOICE` | INTEGER | NOT NULL |  |  |  |
| 7 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `PCNUMBER` | CHAR(20) |  |  |  |  |
| 9 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 11 | `INTERCOMPANYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `INTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 15 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 16 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 18 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 19 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 20 | `ORDERDATE` | DATE |  |  |  |  |
| 21 | `SOURCEDOCUMENTORDERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `SOURCEDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 23 | `PURORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 24 | `PURORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 25 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 26 | `OURSUPPLYSTATECODE` | CHAR(3) |  |  |  |  |
| 27 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 28 | `ORDERPARTNERBRANDCODE` | CHAR(8) |  |  |  |  |
| 29 | `DERIVATIONSTEP` | CHAR(2) |  |  |  |  |
| 30 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 31 | `FROMORDERPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 32 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 33 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 34 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 35 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 36 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 37 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 38 | `INITIALDATE` | DATE |  |  |  |  |
| 39 | `FINALDATE` | DATE |  |  |  |  |
| 40 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 41 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 42 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 43 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 44 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 45 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 46 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 47 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 48 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 49 | `GROUPORDERSONSHIPPING` | INTEGER | NOT NULL |  |  |  |
| 50 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 51 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 52 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 53 | `AREACODE` | CHAR(3) |  |  |  |  |
| 54 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 55 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 56 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 57 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 58 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 59 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 60 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 61 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 62 | `REQUIREDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 63 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 64 | `CONFIRMEDDUEDATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 65 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 66 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 67 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 68 | `KEEPENTRYEXCHANGERATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 69 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 70 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 71 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 72 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 73 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 74 | `PRICEANDDISCOUNTDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 75 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 76 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 77 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 78 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 79 | `ONORDERTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 80 | `PAYMENTCUSTOMERUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 81 | `PAYMENTCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 82 | `MINAMOUNTACHIEVEMENTINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 83 | `BANKBOXBEGIN` | SMALLINT | NOT NULL |  |  |  |
| 84 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 85 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 86 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 87 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 88 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 89 | `COMPANYBANKBOXBEGIN` | SMALLINT | NOT NULL |  |  |  |
| 90 | `COMPANYBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 91 | `COMPANYBANKCODE` | CHAR(15) |  |  |  |  |
| 92 | `COMPANYBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 93 | `COMPANYBANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 94 | `COMPANYBANKIDIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 95 | `THIRDPARTYBILLING` | SMALLINT | NOT NULL |  |  |  |
| 96 | `COMMISSIONDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 97 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 98 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 99 | `AGENTCREATIONTYPE1` | CHAR(1) |  |  |  |  |
| 100 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 101 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 102 | `AGENTCREATIONTYPE2` | CHAR(1) |  |  |  |  |
| 103 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 104 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 105 | `AGENTCREATIONTYPE3` | CHAR(1) |  |  |  |  |
| 106 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 107 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 108 | `AGENTCREATIONTYPE4` | CHAR(1) |  |  |  |  |
| 109 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 110 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 111 | `AGENTCREATIONTYPE5` | CHAR(1) |  |  |  |  |
| 112 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 113 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 114 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 115 | `PURORDERGENERATEDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 116 | `PURCHASEORDERGENERATEDCODE` | CHAR(15) |  |  |  |  |
| 117 | `ORDERSOURCE` | CHAR(2) |  |  |  |  |
| 118 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 119 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 120 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 121 | `PRINTEDCONFIRMATION` | SMALLINT | NOT NULL |  |  |  |
| 122 | `LINESUNMATCHEDWITHBOX` | SMALLINT | NOT NULL |  |  |  |
| 123 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 124 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 125 | `STOPUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 126 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 127 | `ALCODE` | CHAR(30) |  |  |  |  |
| 128 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 129 | `ADVANCELICENSENO` | CHAR(15) |  |  |  |  |
| 130 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 131 | `FULLSCREEN` | SMALLINT | NOT NULL |  |  |  |
| 132 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 133 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 134 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 135 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 136 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 137 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 138 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 139 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 140 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 141 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 142 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 143 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 144 | `RFORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 145 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 146 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 147 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 148 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 149 | `PURORDERCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 150 | `PLANNINGGROUPINGCODE` | CHAR(3) |  |  |  |  |
| 151 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 152 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 153 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 154 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 155 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 156 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 157 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 158 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 159 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 160 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 161 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 162 | `OVERDUEAMOUNTFORCED` | SMALLINT | NOT NULL |  |  |  |
| 163 | `TNAHEADERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 164 | `TNAHEADERCODE` | CHAR(10) |  |  |  |  |
| 165 | `ACTIVITYDATE` | TIMESTAMP |  |  |  |  |
| 166 | `TNASTARTDATE` | TIMESTAMP |  |  |  |  |
| 167 | `TNAENDDATE` | TIMESTAMP |  |  |  |  |
| 168 | `TNARECALCULATIONENDDATE` | TIMESTAMP |  |  |  |  |
| 169 | `TNASTATUS` | INTEGER | NOT NULL |  |  |  |
| 170 | `REALIGNTNA` | SMALLINT | NOT NULL |  |  |  |
| 171 | `GANTTMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 172 | `TNAGANTTRESOURCEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 173 | `TNAGANTTMARKERREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 174 | `TNAGANTTLINKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 175 | `TNAGANTTSUBTASKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 176 | `TNAACTIVITYGANTT` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESORDERIBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.TYPEOFINVOICE,
       t.TEMPLATECODE,
       t.PCNUMBER,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.INTERCOMPANYREQUIRED
FROM   DB2ADMIN.SALESORDERIBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
