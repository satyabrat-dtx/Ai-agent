# DB2ADMIN.LOGPLANTINVOICE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 230
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 141301

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `INVOICETYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `INVOICEDATE` | DATE |  |  |  |  |
| 5 | `CREATIONDATE` | DATE |  |  |  |  |
| 6 | `FIRMCODE` | CHAR(3) |  |  |  |  |
| 7 | `FIRMBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 8 | `FIRMBANKCODE` | CHAR(15) |  |  |  |  |
| 9 | `FIRMBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 10 | `FACTORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 12 | `CONTRACTNOCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 13 | `CONTRACTNOCODE` | CHAR(15) |  |  |  |  |
| 14 | `CONTRACTDATE` | DATE |  |  |  |  |
| 15 | `EXPORTERREFNO` | CHAR(15) |  |  |  |  |
| 16 | `BUYERSPOREFNO` | VARCHAR(200) |  |  |  |  |
| 17 | `PSINVOICECODE` | CHAR(15) |  |  |  |  |
| 18 | `CUSTOMINVOICECODE` | CHAR(20) |  |  |  |  |
| 19 | `CUSTOMINVOICETYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `COMMERCIALINVOICECODE` | CHAR(20) |  |  |  |  |
| 21 | `COMMERCIALINVOICETYPECODE` | CHAR(3) |  |  |  |  |
| 22 | `MRNHEADERCODE` | DECIMAL(11,0) |  |  |  |  |
| 23 | `MRNHEADERMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 24 | `SALESINVOICEPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 25 | `CONSIGNEECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 26 | `CONSIGNEECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 27 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 28 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 29 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 30 | `BUYERIFOTCCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 31 | `BUYERIFOTCCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 32 | `PLANTINVOICEDATE` | DATE |  |  |  |  |
| 33 | `NOTIFYPARTYCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 34 | `NOTIFYPARTYCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 35 | `BUYERSBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 36 | `BUYERSBANKCODE` | CHAR(15) |  |  |  |  |
| 37 | `BUYERSBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 38 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 39 | `AGENT1ONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 40 | `AGENT1ONCODE` | CHAR(3) |  |  |  |  |
| 41 | `AGENT1CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 42 | `AGENT1AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 43 | `AGENT1COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 44 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 45 | `AGENT2ONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 46 | `AGENT2ONCODE` | CHAR(3) |  |  |  |  |
| 47 | `AGENT2CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 48 | `AGENT2AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 49 | `AGENT2COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 50 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 51 | `AGENT3ONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 52 | `AGENT3ONCODE` | CHAR(3) |  |  |  |  |
| 53 | `AGENT3CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 54 | `AGENT3AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 55 | `AGENT3COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 56 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 57 | `AGENT4ONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 58 | `AGENT4ONCODE` | CHAR(3) |  |  |  |  |
| 59 | `AGENT4CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 60 | `AGENT4AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 61 | `AGENT4COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 62 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 63 | `AGENT5ONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 64 | `AGENT5ONCODE` | CHAR(3) |  |  |  |  |
| 65 | `AGENT5CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 66 | `AGENT5AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 67 | `AGENT5COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 68 | `BOTTLESEALNO` | CHAR(15) |  |  |  |  |
| 69 | `CUSTOMERBOTTLESEALNO` | CHAR(25) |  |  |  |  |
| 70 | `COMPANYSEALNO` | CHAR(15) |  |  |  |  |
| 71 | `GOODSORIGINCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 72 | `DESTINATIONCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 73 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 74 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 75 | `PRECARRIAGEBY` | CHAR(15) |  |  |  |  |
| 76 | `PLACEOFRECEIPTBYPRECARRIAGE` | CHAR(10) |  |  |  |  |
| 77 | `VESSELFLIGHTNO` | CHAR(30) |  |  |  |  |
| 78 | `PORTOFLOADINGCODE` | CHAR(10) |  |  |  |  |
| 79 | `PORTOFDISCHARGECODE` | CHAR(10) |  |  |  |  |
| 80 | `FINALDESTINATIONCODE` | CHAR(3) |  |  |  |  |
| 81 | `WEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 82 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 83 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 84 | `TOTALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 85 | `TOTALNUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 86 | `PACKDIMENSIONIN` | CHAR(15) |  |  |  |  |
| 87 | `PACKINGLISTNO` | CHAR(15) |  |  |  |  |
| 88 | `PACKINGLISTDATE` | DATE |  |  |  |  |
| 89 | `SHIPLINECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 90 | `SHIPLINECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 91 | `CHACUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 92 | `CHACUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 93 | `FORWARDERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 94 | `FORWARDERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 95 | `ETADATE` | DATE |  |  |  |  |
| 96 | `ETDDATE` | DATE |  |  |  |  |
| 97 | `EXWORKDATE` | DATE |  |  |  |  |
| 98 | `LCLFCL` | INTEGER | NOT NULL |  |  |  |
| 99 | `CHALLANNO` | CHAR(15) |  |  |  |  |
| 100 | `CHALLANDATE` | DATE |  |  |  |  |
| 101 | `LRNO` | CHAR(15) |  |  |  |  |
| 102 | `LRDATE` | DATE |  |  |  |  |
| 103 | `HOUSEAWBBILLNO` | CHAR(15) |  |  |  |  |
| 104 | `HOUSEAWBBILLDATE` | DATE |  |  |  |  |
| 105 | `BLDATE` | DATE |  |  |  |  |
| 106 | `BLNUMBER` | CHAR(25) |  |  |  |  |
| 107 | `TRANSPORTERCODCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 108 | `TRANSPORTERCODCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 109 | `TRUCKNO` | VARCHAR(80) |  |  |  |  |
| 110 | `CONTAINERNO` | CHAR(100) |  |  |  |  |
| 111 | `CONTAINERSIZE` | CHAR(15) |  |  |  |  |
| 112 | `CATEGORY` | CHAR(30) |  |  |  |  |
| 113 | `ITEMDESCRIPTION` | CHAR(30) |  |  |  |  |
| 114 | `SHIPPINGMARKS1` | VARCHAR(250) |  |  |  |  |
| 115 | `SHIPPINGMARKS2` | VARCHAR(250) |  |  |  |  |
| 116 | `SHIPPINGMARKS3` | VARCHAR(250) |  |  |  |  |
| 117 | `SHIPPINGMARKS4` | VARCHAR(250) |  |  |  |  |
| 118 | `AR3CODE` | CHAR(20) |  |  |  |  |
| 119 | `AR3EXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 120 | `AR3EXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 121 | `AR3DATE` | DATE |  |  |  |  |
| 122 | `AR4CODE` | CHAR(20) |  |  |  |  |
| 123 | `AR4EXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 124 | `AR4EXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 125 | `AR4DATE` | DATE |  |  |  |  |
| 126 | `SEALINGOPTION` | INTEGER | NOT NULL |  |  |  |
| 127 | `EXAMINATIONAT` | INTEGER | NOT NULL |  |  |  |
| 128 | `UNDERREBATE` | INTEGER | NOT NULL |  |  |  |
| 129 | `TIMEOFREMOVALOFGOODS` | DATE |  |  |  |  |
| 130 | `INVOICEISSUETIME` | TIMESTAMP |  |  |  |  |
| 131 | `FOOTERLINES` | CHAR(100) |  |  |  |  |
| 132 | `IPPOLICYNO` | CHAR(30) |  |  |  |  |
| 133 | `IPPOLICYDATE` | DATE |  |  |  |  |
| 134 | `INSURANCECOMPANY` | CHAR(60) |  |  |  |  |
| 135 | `POLICYPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 136 | `CUSTOMERPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 137 | `INSURANCEMARKUP` | DECIMAL(9,5) |  |  |  |  |
| 138 | `MARINEINSURANCEMICNO` | CHAR(12) |  |  |  |  |
| 139 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 140 | `ALADVANCELICENSECODE` | CHAR(30) |  |  |  |  |
| 141 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 142 | `ADVANCELICENSENO` | CHAR(15) |  |  |  |  |
| 143 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 144 | `EPCGEPCGAPPLICATIONCODE` | CHAR(30) |  |  |  |  |
| 145 | `EPCGAPPLICATIONDATE` | DATE |  |  |  |  |
| 146 | `EPCGLICENSENO` | CHAR(30) |  |  |  |  |
| 147 | `EPCGLICENSEDATE` | DATE |  |  |  |  |
| 148 | `ADVANCELICENSEFILENO` | CHAR(15) |  |  |  |  |
| 149 | `ADVANCELICENSEFILEDATE` | DATE |  |  |  |  |
| 150 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 151 | `ORDERCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 152 | `EXCHANGERATEOFCONTRACT` | DECIMAL(28,15) |  |  |  |  |
| 153 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 154 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 155 | `TERMSOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 156 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 157 | `LCLCNO` | CHAR(35) |  |  |  |  |
| 158 | `LCLCDATE` | DATE |  |  |  |  |
| 159 | `BCFORMOFRS` | DECIMAL(18,5) |  |  |  |  |
| 160 | `PRICELISTORDERTYPE` | CHAR(1) |  |  |  |  |
| 161 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 162 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 163 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 164 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 165 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 166 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 167 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 168 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 169 | `USEDCOUNTER` | INTEGER | NOT NULL |  |  |  |
| 170 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 171 | `PRINTDATEANDTIME` | TIMESTAMP |  |  |  |  |
| 172 | `PRINTUSER` | CHAR(50) |  |  |  |  |
| 173 | `REPRINTDATEANDTIME` | TIMESTAMP |  |  |  |  |
| 174 | `REPRINTUSER` | CHAR(50) |  |  |  |  |
| 175 | `INVOICERATEOPTION` | CHAR(2) |  |  |  |  |
| 176 | `INVOICECREATIONFROM` | CHAR(2) |  |  |  |  |
| 177 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 178 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 179 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 180 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 181 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 182 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 183 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 184 | `FLAG` | CHAR(15) |  |  |  |  |
| 185 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 186 | `DOMEXCISEFLAG` | CHAR(15) |  |  |  |  |
| 187 | `DOMEXCISESAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 188 | `EXCISEFLAG` | CHAR(15) |  |  |  |  |
| 189 | `EXCISESAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 190 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 191 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 192 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 193 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 194 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 195 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 196 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 197 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 198 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 199 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 200 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 201 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 202 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 203 | `PRECOMMINVOICECODE` | CHAR(15) |  |  |  |  |
| 204 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |
| 205 | `TYPEFOREINVOICE` | CHAR(1) |  |  |  |  |
| 206 | `STATUS` | CHAR(100) |  |  |  |  |
| 207 | `EINVOICEQRCODE` | LONG VARCHAR |  |  |  |  |
| 208 | `ACKNO` | BIGINT | NOT NULL |  |  |  |
| 209 | `ACKDT` | CHAR(29) |  |  |  |  |
| 210 | `IRN` | CHAR(160) |  |  |  |  |
| 211 | `SIGNEDQRCODE` | LONG VARCHAR |  |  |  |  |
| 212 | `EWBNO` | CHAR(120) |  |  |  |  |
| 213 | `EWBDT` | CHAR(29) |  |  |  |  |
| 214 | `EWBVALIDTILL` | VARCHAR(1000) |  |  |  |  |
| 215 | `CANCLEDATE` | CHAR(100) |  |  |  |  |
| 216 | `INTERCOMPNYMRNCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 217 | `INTERCOMPNYMRNDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 218 | `INTERCOMPNYMRNMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 219 | `INTERCOMPNYMRNCODE` | DECIMAL(11,0) |  |  |  |  |
| 220 | `SALINVPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 221 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 222 | `VOLUMEUOMCODE` | CHAR(3) |  |  |  |  |
| 223 | `EXPORTSHIPPINGBILLNUMBER` | CHAR(15) |  |  |  |  |
| 224 | `EXPORTSHIPPINGBILLDATE` | DATE |  |  |  |  |
| 225 | `EXPORTPORTCODE` | CHAR(10) |  |  |  |  |
| 226 | `IRNCANCELREASON` | CHAR(1) |  |  |  |  |
| 227 | `IRNCANCELREMARKS` | CHAR(50) |  |  |  |  |
| 228 | `EWBCANCELREASON` | CHAR(1) |  |  |  |  |
| 229 | `EWBCANCELREMARKS` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPLANTINVOICE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGPLANTINVOICELINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.INVOICETYPECODE,
       t.CODE,
       t.INVOICEDATE,
       t.CREATIONDATE,
       t.FIRMCODE,
       t.FIRMBANKBANKCOUNTRYCODE,
       t.FIRMBANKCODE,
       t.FIRMBANKBRANCHCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE
FROM   DB2ADMIN.LOGPLANTINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
