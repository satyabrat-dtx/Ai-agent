# DB2ADMIN.PRECOMMINVOICEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 196
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 221899

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `STEP` | CHAR(1) |  |  |  |  |
| 4 | `INVOICETYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `INVOICEDATE` | DATE |  |  |  |  |
| 7 | `FIRMCODE` | CHAR(3) |  |  |  |  |
| 8 | `FIRMBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 9 | `FIRMBANKCODE` | CHAR(15) |  |  |  |  |
| 10 | `FIRMBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 11 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 12 | `CONTRACTNOCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 13 | `CONTRACTNOCODE` | CHAR(15) |  |  |  |  |
| 14 | `CONTRACTDATE` | DATE |  |  |  |  |
| 15 | `EXPORTERREFNO` | CHAR(15) |  |  |  |  |
| 16 | `CUSTOMINVOICECODE` | CHAR(20) |  |  |  |  |
| 17 | `CUSTOMINVOICETYPECODE` | CHAR(3) |  |  |  |  |
| 18 | `COMMERCIALINVOICECODE` | CHAR(20) |  |  |  |  |
| 19 | `COMMERCIALINVOICETYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `CUSTOMINVOICECREATED` | CHAR(1) |  |  |  |  |
| 21 | `CONSIGNEECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `CONSIGNEECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 23 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 24 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 25 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 26 | `BUYERIFOTCCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 27 | `BUYERIFOTCCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 28 | `NOTIFYPARTYCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 29 | `NOTIFYPARTYCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 30 | `NOTIFYPARTY2CSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 31 | `NOTIFYPARTY2CSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 32 | `BUYERSBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 33 | `BUYERSBANKCODE` | CHAR(15) |  |  |  |  |
| 34 | `BUYERSBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 35 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 36 | `AGENT1ONCODE` | CHAR(3) |  |  |  |  |
| 37 | `AGENT1CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 38 | `AGENT1AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 39 | `AGENT1COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 40 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 41 | `AGENT2ONCODE` | CHAR(3) |  |  |  |  |
| 42 | `AGENT2CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 43 | `AGENT2AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 44 | `AGENT2COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 45 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 46 | `AGENT3ONCODE` | CHAR(3) |  |  |  |  |
| 47 | `AGENT3CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 48 | `AGENT3AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 49 | `AGENT3COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 50 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 51 | `AGENT4ONCODE` | CHAR(3) |  |  |  |  |
| 52 | `AGENT4CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 53 | `AGENT4AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 54 | `AGENT4COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 55 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 56 | `AGENT5ONCODE` | CHAR(3) |  |  |  |  |
| 57 | `AGENT5CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 58 | `AGENT5AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 59 | `AGENT5COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 60 | `BOTTLESEALNO` | CHAR(15) |  |  |  |  |
| 61 | `CUSTOMERBOTTLESEALNO` | CHAR(15) |  |  |  |  |
| 62 | `COMPANYSEALNO` | CHAR(15) |  |  |  |  |
| 63 | `GOODSORIGINCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 64 | `DESTINATIONCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 65 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 66 | `PRECARRIAGEBY` | CHAR(15) |  |  |  |  |
| 67 | `PLACEOFRECEIPTBYPRECARRIAGE` | CHAR(10) |  |  |  |  |
| 68 | `VESSELFLIGHTNO` | CHAR(30) |  |  |  |  |
| 69 | `PORTOFLOADINGCODE` | CHAR(10) |  |  |  |  |
| 70 | `PORTOFDISCHARGECODE` | CHAR(10) |  |  |  |  |
| 71 | `FINALDESTINATIONCODE` | CHAR(3) |  |  |  |  |
| 72 | `WEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 73 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 74 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 75 | `TOTALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `TOTALNUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 77 | `PACKDIMENSIONIN` | CHAR(15) |  |  |  |  |
| 78 | `PACKINGLISTNO` | CHAR(15) |  |  |  |  |
| 79 | `PACKINGLISTDATE` | DATE |  |  |  |  |
| 80 | `SHIPLINECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 81 | `SHIPLINECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 82 | `CHACUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 83 | `CHACUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 84 | `FORWARDERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 85 | `FORWARDERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 86 | `ETADATE` | DATE |  |  |  |  |
| 87 | `ETDDATE` | DATE |  |  |  |  |
| 88 | `EXWORKDATE` | DATE |  |  |  |  |
| 89 | `LCLFCL` | INTEGER | NOT NULL |  |  |  |
| 90 | `CHALLANNO` | CHAR(15) |  |  |  |  |
| 91 | `CHALLANDATE` | DATE |  |  |  |  |
| 92 | `LRNO` | CHAR(15) |  |  |  |  |
| 93 | `LRDATE` | DATE |  |  |  |  |
| 94 | `TRANSPORTERCODCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 95 | `TRANSPORTERCODCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 96 | `TRUCKNO` | VARCHAR(80) |  |  |  |  |
| 97 | `CONTAINERNO` | CHAR(30) |  |  |  |  |
| 98 | `CATEGORY` | CHAR(30) |  |  |  |  |
| 99 | `ITEMDESCRIPTION` | CHAR(30) |  |  |  |  |
| 100 | `SHIPPINGMARKS1` | VARCHAR(1000) |  |  |  |  |
| 101 | `SHIPPINGMARKS2` | VARCHAR(250) |  |  |  |  |
| 102 | `SHIPPINGMARKS3` | VARCHAR(250) |  |  |  |  |
| 103 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 104 | `SHIPPINGMARKS4` | VARCHAR(250) |  |  |  |  |
| 105 | `AR3CODE` | CHAR(20) |  |  |  |  |
| 106 | `AR3EXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 107 | `AR3EXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 108 | `AR3DATE` | DATE |  |  |  |  |
| 109 | `AR4CODE` | CHAR(20) |  |  |  |  |
| 110 | `AR4EXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 111 | `AR4EXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 112 | `AR4DATE` | DATE |  |  |  |  |
| 113 | `SEALINGOPTION` | INTEGER | NOT NULL |  |  |  |
| 114 | `EXAMINATIONAT` | INTEGER | NOT NULL |  |  |  |
| 115 | `UNDERREBATE` | INTEGER | NOT NULL |  |  |  |
| 116 | `TIMEOFREMOVALOFGOODS` | DATE |  |  |  |  |
| 117 | `INVOICEISSUETIME` | TIMESTAMP |  |  |  |  |
| 118 | `FOOTERLINES` | CHAR(100) |  |  |  |  |
| 119 | `IPPOLICYNO` | CHAR(30) |  |  |  |  |
| 120 | `IPPOLICYDATE` | DATE |  |  |  |  |
| 121 | `INSURANCECOMPANY` | CHAR(60) |  |  |  |  |
| 122 | `POLICYPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 123 | `CUSTOMERPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 124 | `INSURANCEMARKUP` | DECIMAL(9,5) |  |  |  |  |
| 125 | `MARINEINSURANCEMICNO` | CHAR(12) |  |  |  |  |
| 126 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 127 | `ALCODE` | CHAR(30) |  |  |  |  |
| 128 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 129 | `ADVANCELICENSENO` | CHAR(15) |  |  |  |  |
| 130 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 131 | `EPCGEPCGAPPLICATIONCODE` | CHAR(30) |  |  |  |  |
| 132 | `EPCGAPPLICATIONDATE` | DATE |  |  |  |  |
| 133 | `EPCGLICENSENO` | CHAR(30) |  |  |  |  |
| 134 | `EPCGLICENSEDATE` | DATE |  |  |  |  |
| 135 | `ADVANCELICENSEFILENO` | CHAR(15) |  |  |  |  |
| 136 | `ADVANCELICENSEFILEDATE` | DATE |  |  |  |  |
| 137 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 138 | `ORDERCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 139 | `EXCHANGERATEOFCONTRACT` | DECIMAL(28,15) |  |  |  |  |
| 140 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 141 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 142 | `LCLCNO` | CHAR(35) |  |  |  |  |
| 143 | `LCLCDATE` | DATE |  |  |  |  |
| 144 | `BCFORMOFRS` | DECIMAL(18,5) |  |  |  |  |
| 145 | `PRICELISTORDERTYPE` | CHAR(1) |  |  |  |  |
| 146 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 147 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 148 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 149 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 150 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 151 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 152 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 153 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 154 | `USEDCOUNTER` | INTEGER | NOT NULL |  |  |  |
| 155 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 156 | `PRINTDATEANDTIME` | TIMESTAMP |  |  |  |  |
| 157 | `PRINTUSER` | CHAR(50) |  |  |  |  |
| 158 | `REPRINTDATEANDTIME` | TIMESTAMP |  |  |  |  |
| 159 | `REPRINTUSER` | CHAR(50) |  |  |  |  |
| 160 | `INVOICERATEOPTION` | CHAR(2) |  |  |  |  |
| 161 | `INVOICECREATIONFROM` | CHAR(2) |  |  |  |  |
| 162 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 163 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 164 | `FLAG` | CHAR(15) |  |  |  |  |
| 165 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 166 | `DOMEXCISEFLAG` | CHAR(15) |  |  |  |  |
| 167 | `DOMEXCISESAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 168 | `EXCISEFLAG` | CHAR(15) |  |  |  |  |
| 169 | `EXCISESAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 170 | `SALINVPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 171 | `SALESINVOICEPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 172 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 173 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 174 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 175 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 176 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 177 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 178 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 179 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 180 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 181 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 182 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 183 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 184 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 185 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 186 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 187 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 188 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 189 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 190 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 191 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 192 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 193 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 194 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 195 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRECOMMINVOICEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.STEP,
       t.INVOICETYPECODE,
       t.CODE,
       t.INVOICEDATE,
       t.FIRMCODE,
       t.FIRMBANKBANKCOUNTRYCODE,
       t.FIRMBANKCODE,
       t.FIRMBANKBRANCHCODE,
       t.FACTORYCODE
FROM   DB2ADMIN.PRECOMMINVOICEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
