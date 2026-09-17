# DB2ADMIN.SALESDOCUMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `staging_mirror`
- **Columns**: 180
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 95417

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 8 | `PROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `PROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 10 | `PROVISIONALDOCUMENTDATE` | DATE |  |  |  |  |
| 11 | `RESETDOCUMENT` | SMALLINT | NOT NULL |  |  |  |
| 12 | `DEFINITIVECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 13 | `DEFINITIVECODE` | CHAR(15) |  |  |  |  |
| 14 | `DEFINITIVEDOCUMENTDATE` | DATE |  |  |  |  |
| 15 | `GOODSISSUEDATE` | DATE |  |  |  |  |
| 16 | `ORDERDATE` | DATE |  |  |  |  |
| 17 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 18 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 19 | `ORDERPARTNERBRANDCODE` | CHAR(8) |  |  |  |  |
| 20 | `DERIVATIONSTEP` | CHAR(2) |  |  |  |  |
| 21 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 22 | `FROMORDERPARTNER` | SMALLINT | NOT NULL |  |  |  |
| 23 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 24 | `OPERATION` | INTEGER | NOT NULL |  |  |  |
| 25 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 26 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 27 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 28 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 29 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 30 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 31 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 32 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 33 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 34 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 35 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 36 | `REGISTERTAXCODE` | CHAR(3) |  |  |  |  |
| 37 | `GROUPSHIPPINGSONINVOICE` | INTEGER | NOT NULL |  |  |  |
| 38 | `CONSIGNMENTTYPE` | CHAR(2) |  |  |  |  |
| 39 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 40 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 41 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 42 | `TERMSOFDELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 43 | `TERMSOFSHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 44 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 45 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 46 | `AREACODE` | CHAR(3) |  |  |  |  |
| 47 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 48 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 49 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 50 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 51 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 52 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 53 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 54 | `TRUCKDRIVERCODE` | CHAR(3) |  |  |  |  |
| 55 | `NUMBERPLATE` | VARCHAR(80) |  |  |  |  |
| 56 | `TRANSPORTSTARTDATE` | DATE |  |  |  |  |
| 57 | `TRANSPORTSTARTTIME` | TIME |  |  |  |  |
| 58 | `NUMBERPARCEL` | DECIMAL(5,0) |  |  |  |  |
| 59 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 60 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 61 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 62 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 63 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 64 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 65 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 66 | `STOCKTRANSACTIONCREATED` | SMALLINT | NOT NULL |  |  |  |
| 67 | `TRACKINGNUMBER` | CHAR(25) |  |  |  |  |
| 68 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 69 | `DISCOUNTCATEGORYCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 70 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 71 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 72 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 73 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 74 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 75 | `PRICEANDDISCOUNTDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 76 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 77 | `PAYMENTSTARTINGDATE` | DATE |  |  |  |  |
| 78 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 79 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 80 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 81 | `ONDOCUMENTTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 82 | `ONINVOICETOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 83 | `PAYMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 84 | `PAYMENTCUSTOMERUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 85 | `PAYMENTCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 86 | `MINAMOUNTACHIEVEMENTINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 87 | `BANKBOXBEGIN` | SMALLINT | NOT NULL |  |  |  |
| 88 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 89 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 90 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 91 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 92 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 93 | `COMPANYBANKBOXBEGIN` | SMALLINT | NOT NULL |  |  |  |
| 94 | `COMPANYBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 95 | `COMPANYBANKCODE` | CHAR(15) |  |  |  |  |
| 96 | `COMPANYBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 97 | `COMPANYBANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 98 | `COMPANYBANKIDIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 99 | `ACCTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 100 | `COMMISSIONTRANSACTIONCREATED` | SMALLINT | NOT NULL |  |  |  |
| 101 | `INVOICEEVOLUTIONTYPE` | CHAR(2) |  |  |  |  |
| 102 | `COMMISSIONDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 103 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 104 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 105 | `AGENTCREATIONTYPE1` | CHAR(1) |  |  |  |  |
| 106 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 107 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 108 | `AGENTCREATIONTYPE2` | CHAR(1) |  |  |  |  |
| 109 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 110 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 111 | `AGENTCREATIONTYPE3` | CHAR(1) |  |  |  |  |
| 112 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 113 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 114 | `AGENTCREATIONTYPE4` | CHAR(1) |  |  |  |  |
| 115 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 116 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 117 | `AGENTCREATIONTYPE5` | CHAR(1) |  |  |  |  |
| 118 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 119 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 120 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 121 | `PRINTEDDOCUMENT` | SMALLINT | NOT NULL |  |  |  |
| 122 | `ORDERSOURCE` | CHAR(2) |  |  |  |  |
| 123 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 124 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 125 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 126 | `SALESORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 127 | `SALESORDERCODE` | CHAR(15) |  |  |  |  |
| 128 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 129 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 130 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 131 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 132 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 133 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 134 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 135 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 136 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 137 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 138 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 139 | `DECLARATIONCODE1` | DECIMAL(23,0) |  |  |  |  |
| 140 | `DECLARATIONYEAR1` | DECIMAL(4,0) |  |  |  |  |
| 141 | `DECLARATIONVALUE1` | DECIMAL(18,5) |  |  |  |  |
| 142 | `DECLARATIONCODE2` | DECIMAL(23,0) |  |  |  |  |
| 143 | `DECLARATIONYEAR2` | DECIMAL(4,0) |  |  |  |  |
| 144 | `DECLARATIONVALUE2` | DECIMAL(18,5) |  |  |  |  |
| 145 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 146 | `KEEPENTRYEXCHANGERATECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 147 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 148 | `LEGALDOCUMENTTYPECODE` | CHAR(4) |  |  |  |  |
| 149 | `RFORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 150 | `PAYMENTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 151 | `PAIDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 152 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 153 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 154 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 155 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 156 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 157 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 158 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 159 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 160 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 161 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 162 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
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
| 177 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 178 | `EISTATUS` | CHAR(2) |  |  |  |  |
| 179 | `EITRANSMISSIONID` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESDOCUMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.FORCEDWARNING,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.PROVISIONALDOCUMENTDATE,
       t.RESETDOCUMENT
FROM   DB2ADMIN.SALESDOCUMENTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
