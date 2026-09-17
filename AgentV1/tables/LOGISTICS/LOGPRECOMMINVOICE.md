# DB2ADMIN.LOGPRECOMMINVOICE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 192
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 217825

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `STEP` | CHAR(1) |  |  |  |  |
| 3 | `INVOICETYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `INVOICEDATE` | DATE |  |  |  |  |
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
| 36 | `AGENT1ONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `AGENT1ONCODE` | CHAR(3) |  |  |  |  |
| 38 | `AGENT1CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 39 | `AGENT1AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 40 | `AGENT1COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 41 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 42 | `AGENT2ONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `AGENT2ONCODE` | CHAR(3) |  |  |  |  |
| 44 | `AGENT2CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 45 | `AGENT2AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 46 | `AGENT2COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 47 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 48 | `AGENT3ONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 49 | `AGENT3ONCODE` | CHAR(3) |  |  |  |  |
| 50 | `AGENT3CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 51 | `AGENT3AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 52 | `AGENT3COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 53 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 54 | `AGENT4ONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 55 | `AGENT4ONCODE` | CHAR(3) |  |  |  |  |
| 56 | `AGENT4CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 57 | `AGENT4AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 58 | `AGENT4COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 59 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 60 | `AGENT5ONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 61 | `AGENT5ONCODE` | CHAR(3) |  |  |  |  |
| 62 | `AGENT5CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 63 | `AGENT5AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 64 | `AGENT5COMMISSIONPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 65 | `BOTTLESEALNO` | CHAR(15) |  |  |  |  |
| 66 | `CUSTOMERBOTTLESEALNO` | CHAR(15) |  |  |  |  |
| 67 | `COMPANYSEALNO` | CHAR(15) |  |  |  |  |
| 68 | `GOODSORIGINCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 69 | `DESTINATIONCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 70 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 71 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 72 | `PRECARRIAGEBY` | CHAR(15) |  |  |  |  |
| 73 | `PLACEOFRECEIPTBYPRECARRIAGE` | CHAR(10) |  |  |  |  |
| 74 | `VESSELFLIGHTNO` | CHAR(30) |  |  |  |  |
| 75 | `PORTOFLOADINGCODE` | CHAR(10) |  |  |  |  |
| 76 | `PORTOFDISCHARGECODE` | CHAR(10) |  |  |  |  |
| 77 | `FINALDESTINATIONCODE` | CHAR(3) |  |  |  |  |
| 78 | `WEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 79 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 80 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 81 | `TOTALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 82 | `TOTALNUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 83 | `PACKDIMENSIONIN` | CHAR(15) |  |  |  |  |
| 84 | `PACKINGLISTNO` | CHAR(15) |  |  |  |  |
| 85 | `PACKINGLISTDATE` | DATE |  |  |  |  |
| 86 | `SHIPLINECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 87 | `SHIPLINECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 88 | `CHACUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 89 | `CHACUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 90 | `FORWARDERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 91 | `FORWARDERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 92 | `ETADATE` | DATE |  |  |  |  |
| 93 | `ETDDATE` | DATE |  |  |  |  |
| 94 | `EXWORKDATE` | DATE |  |  |  |  |
| 95 | `LCLFCL` | INTEGER | NOT NULL |  |  |  |
| 96 | `CHALLANNO` | CHAR(15) |  |  |  |  |
| 97 | `CHALLANDATE` | DATE |  |  |  |  |
| 98 | `LRNO` | CHAR(15) |  |  |  |  |
| 99 | `LRDATE` | DATE |  |  |  |  |
| 100 | `TRANSPORTERCODCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 101 | `TRANSPORTERCODCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 102 | `TRUCKNO` | VARCHAR(80) |  |  |  |  |
| 103 | `CONTAINERNO` | CHAR(30) |  |  |  |  |
| 104 | `CATEGORY` | CHAR(30) |  |  |  |  |
| 105 | `ITEMDESCRIPTION` | CHAR(30) |  |  |  |  |
| 106 | `SHIPPINGMARKS1` | VARCHAR(1000) |  |  |  |  |
| 107 | `SHIPPINGMARKS2` | VARCHAR(250) |  |  |  |  |
| 108 | `SHIPPINGMARKS3` | VARCHAR(250) |  |  |  |  |
| 109 | `SHIPPINGMARKS4` | VARCHAR(250) |  |  |  |  |
| 110 | `AR3CODE` | CHAR(20) |  |  |  |  |
| 111 | `AR3EXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 112 | `AR3EXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 113 | `AR3DATE` | DATE |  |  |  |  |
| 114 | `AR4CODE` | CHAR(20) |  |  |  |  |
| 115 | `AR4EXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 116 | `AR4EXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 117 | `AR4DATE` | DATE |  |  |  |  |
| 118 | `SEALINGOPTION` | INTEGER | NOT NULL |  |  |  |
| 119 | `EXAMINATIONAT` | INTEGER | NOT NULL |  |  |  |
| 120 | `UNDERREBATE` | INTEGER | NOT NULL |  |  |  |
| 121 | `TIMEOFREMOVALOFGOODS` | DATE |  |  |  |  |
| 122 | `INVOICEISSUETIME` | TIMESTAMP |  |  |  |  |
| 123 | `FOOTERLINES` | CHAR(100) |  |  |  |  |
| 124 | `IPPOLICYNO` | CHAR(30) |  |  |  |  |
| 125 | `IPPOLICYDATE` | DATE |  |  |  |  |
| 126 | `INSURANCECOMPANY` | CHAR(60) |  |  |  |  |
| 127 | `POLICYPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 128 | `CUSTOMERPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 129 | `INSURANCEMARKUP` | DECIMAL(9,5) |  |  |  |  |
| 130 | `MARINEINSURANCEMICNO` | CHAR(12) |  |  |  |  |
| 131 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 132 | `ALCODE` | CHAR(30) |  |  |  |  |
| 133 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 134 | `ADVANCELICENSENO` | CHAR(15) |  |  |  |  |
| 135 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 136 | `EPCGEPCGAPPLICATIONCODE` | CHAR(30) |  |  |  |  |
| 137 | `EPCGAPPLICATIONDATE` | DATE |  |  |  |  |
| 138 | `EPCGLICENSENO` | CHAR(30) |  |  |  |  |
| 139 | `EPCGLICENSEDATE` | DATE |  |  |  |  |
| 140 | `ADVANCELICENSEFILENO` | CHAR(15) |  |  |  |  |
| 141 | `ADVANCELICENSEFILEDATE` | DATE |  |  |  |  |
| 142 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 143 | `ORDERCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 144 | `EXCHANGERATEOFCONTRACT` | DECIMAL(28,15) |  |  |  |  |
| 145 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 146 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 147 | `TERMSOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 148 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 149 | `LCLCNO` | CHAR(35) |  |  |  |  |
| 150 | `LCLCDATE` | DATE |  |  |  |  |
| 151 | `BCFORMOFRS` | DECIMAL(18,5) |  |  |  |  |
| 152 | `PRICELISTORDERTYPE` | CHAR(1) |  |  |  |  |
| 153 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 154 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 155 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 156 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 157 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 158 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 159 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 160 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 161 | `USEDCOUNTER` | INTEGER | NOT NULL |  |  |  |
| 162 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 163 | `PRINTDATEANDTIME` | TIMESTAMP |  |  |  |  |
| 164 | `PRINTUSER` | CHAR(50) |  |  |  |  |
| 165 | `REPRINTDATEANDTIME` | TIMESTAMP |  |  |  |  |
| 166 | `REPRINTUSER` | CHAR(50) |  |  |  |  |
| 167 | `INVOICERATEOPTION` | CHAR(2) |  |  |  |  |
| 168 | `INVOICECREATIONFROM` | CHAR(2) |  |  |  |  |
| 169 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 170 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 171 | `FLAG` | CHAR(15) |  |  |  |  |
| 172 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 173 | `DOMEXCISEFLAG` | CHAR(15) |  |  |  |  |
| 174 | `DOMEXCISESAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 175 | `EXCISEFLAG` | CHAR(15) |  |  |  |  |
| 176 | `EXCISESAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 177 | `SALINVPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 178 | `SALESINVOICEPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 179 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 180 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 181 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 182 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 183 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 184 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 185 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 186 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 187 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 188 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 189 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 190 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 191 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPRECOMMINVOICE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGPRECOMMINVOICELINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.STEP,
       t.INVOICETYPECODE,
       t.CODE,
       t.INVOICEDATE,
       t.FIRMCODE,
       t.FIRMBANKBANKCOUNTRYCODE,
       t.FIRMBANKCODE,
       t.FIRMBANKBRANCHCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE
FROM   DB2ADMIN.LOGPRECOMMINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
