# DB2ADMIN.FULLORDERPARTNERIBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 250
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 148293

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 2 | `CUSTOMERSUPPLIERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 3 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 4 | `CUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 5 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 6 | `ORDERBUSINESSPARTNERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 7 | `ORDERLOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 8 | `ORIGININFORMATIONTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `ENDDATE` | DATE |  |  |  |  |
| 10 | `SUBSTITUTEBPNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 11 | `LEGALNAME1` | VARCHAR(270) |  |  |  |  |
| 12 | `LEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 13 | `SHORTNAME` | VARCHAR(80) |  |  |  |  |
| 14 | `SEARCHNAME` | VARCHAR(120) |  |  |  |  |
| 15 | `GROUPBPNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 16 | `SUNDRY` | SMALLINT | NOT NULL |  |  |  |
| 17 | `FISCALTYPECODE` | CHAR(2) |  |  |  |  |
| 18 | `FISCALCODE` | CHAR(16) |  |  |  |  |
| 19 | `TAXREGISTRATIONNUMBER` | CHAR(15) |  |  |  |  |
| 20 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 21 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 22 | `REPRESENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `INTERCOMPANYDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 24 | `COMPANYSUPPLIERCODE` | CHAR(10) |  |  |  |  |
| 25 | `TAXSTAMPREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 26 | `TAXSTAMPREQUIREDFORCREDIT` | SMALLINT | NOT NULL |  |  |  |
| 27 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 28 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 29 | `FINANCIALPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 30 | `FINANCIALPARTNERCODE` | CHAR(8) |  |  |  |  |
| 31 | `COMPANYBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 32 | `ACKNOWLEDGEMENTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 33 | `ACKNOWLEDGEMENTTYPE` | CHAR(2) |  |  |  |  |
| 34 | `CREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 35 | `ENDDATECREDITLIMIT` | DATE |  |  |  |  |
| 36 | `INSURANCECREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 37 | `INSURANCECMYCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 38 | `INSURANCECMYCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 39 | `ENDDATEINSURANCECREDITLIMIT` | DATE |  |  |  |  |
| 40 | `RISKCATEGORYSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 41 | `RISKCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 42 | `RISKNUMBER` | CHAR(30) |  |  |  |  |
| 43 | `TYPEOFINSURANCESYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 44 | `TYPEOFINSURANCECODE` | CHAR(10) |  |  |  |  |
| 45 | `CREDITREPORTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 46 | `CREDITREPORTCODE` | CHAR(10) |  |  |  |  |
| 47 | `CREDITREQUEST` | SMALLINT | NOT NULL |  |  |  |
| 48 | `CREDITREQUESTDATE` | DATE |  |  |  |  |
| 49 | `AREACODE` | CHAR(3) |  |  |  |  |
| 50 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 51 | `ORDERALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 52 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 53 | `BLOCKCONTROLREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 54 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 55 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 56 | `WORKINGCALENDARCODE` | CHAR(3) |  |  |  |  |
| 57 | `DATECALCULATIONCODE` | CHAR(3) |  |  |  |  |
| 58 | `COMPANYLIABLEINITIALSCODE` | CHAR(50) |  |  |  |  |
| 59 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 60 | `MINIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 61 | `MAXIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 62 | `MINIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 63 | `MAXIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 64 | `MINIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 65 | `MAXIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 66 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 67 | `GROUPORDERSONSHIPPING` | INTEGER | NOT NULL |  |  |  |
| 68 | `GROUPSHIPPINGSONINVOICE` | INTEGER | NOT NULL |  |  |  |
| 69 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 70 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 71 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 72 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 73 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 74 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 75 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 76 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 77 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 78 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 79 | `AGTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 80 | `AGENTGRPCODE` | CHAR(3) |  |  |  |  |
| 81 | `ASSORTGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 82 | `ASSORTGRPCODE` | CHAR(3) |  |  |  |  |
| 83 | `EXSGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 84 | `EXCLUSIVEGRPCODE` | CHAR(3) |  |  |  |  |
| 85 | `BLOCKGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 86 | `BLOCKGRPCODE` | CHAR(3) |  |  |  |  |
| 87 | `PRCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 88 | `PRICEGRPCODE` | CHAR(3) |  |  |  |  |
| 89 | `DSCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 90 | `DISCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 91 | `CHARGEGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 92 | `CHARGEGRPCODE` | CHAR(3) |  |  |  |  |
| 93 | `RESTRICGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 94 | `RESTRICGRPCODE` | CHAR(3) |  |  |  |  |
| 95 | `CMTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 96 | `COMMENTGRPCODE` | CHAR(3) |  |  |  |  |
| 97 | `TAXGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 98 | `TAXGRPCODE` | CHAR(3) |  |  |  |  |
| 99 | `MNGACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 100 | `MANAGEMENTACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 101 | `FNCACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 102 | `FINANCIALACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 103 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 104 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 105 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 106 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 107 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 108 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 109 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 110 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 111 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 112 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 113 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 114 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 115 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 116 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 117 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 118 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 119 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 120 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 121 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 122 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 123 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 124 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 125 | `PERSON` | VARCHAR(200) |  |  |  |  |
| 126 | `ROLEINTHECOMPANY` | VARCHAR(200) |  |  |  |  |
| 127 | `PHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 128 | `FAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 129 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 130 | `BOOKLINE01` | VARCHAR(200) |  |  |  |  |
| 131 | `BOOKLINE02` | VARCHAR(200) |  |  |  |  |
| 132 | `BOOKLINE03` | VARCHAR(200) |  |  |  |  |
| 133 | `BOOKLINE04` | VARCHAR(200) |  |  |  |  |
| 134 | `BOOKLINE05` | VARCHAR(200) |  |  |  |  |
| 135 | `FINTABLENBRACCOUNTGROUP` | CHAR(5) |  |  |  |  |
| 136 | `GLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 137 | `FINANCEACCOUNTGROUPCODE` | CHAR(10) |  |  |  |  |
| 138 | `VARFORACCSTATEMENTSTDTABLECOD` | CHAR(5) |  |  |  |  |
| 139 | `VARIANTFORACCOUNTSTATEMENTCODE` | CHAR(10) |  |  |  |  |
| 140 | `VARFORBLNCNFSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 141 | `VARFORBALANCECONFIRMATIONCODE` | CHAR(10) |  |  |  |  |
| 142 | `VATTAXCODE` | CHAR(5) |  |  |  |  |
| 143 | `FININITIALDATE` | DATE |  |  |  |  |
| 144 | `FINFINALDATE` | DATE |  |  |  |  |
| 145 | `FININACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 146 | `NOTEFORBOOKING` | VARCHAR(100) |  |  |  |  |
| 147 | `REMINDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 148 | `REMINDERDELIVERY` | CHAR(1) |  |  |  |  |
| 149 | `REMBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 150 | `REMBLOCKCODE` | CHAR(2) |  |  |  |  |
| 151 | `REMINDERBLOCKDATE` | DATE |  |  |  |  |
| 152 | `BUSINESSPRNFORREMINDERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 153 | `COLLECTIONDIFFERENT` | SMALLINT | NOT NULL |  |  |  |
| 154 | `COLLECTIONADDRESSNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 155 | `BADDEBTSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 156 | `BADDEBTSCODE` | CHAR(10) |  |  |  |  |
| 157 | `VALUEADJUSTMENTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 158 | `VALUEADJUSTMENTCODE` | CHAR(10) |  |  |  |  |
| 159 | `VALUEADJUSTMENTRATE` | DECIMAL(5,2) |  |  |  |  |
| 160 | `CSMSUPSTATUSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 161 | `CUSTOMERSUPPLIERSTATUSCODE` | CHAR(10) |  |  |  |  |
| 162 | `NOTEFORREMINDER` | VARCHAR(100) |  |  |  |  |
| 163 | `PAYMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 164 | `PAYMENTBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 165 | `PAYMENTBLOCKCODE` | CHAR(2) |  |  |  |  |
| 166 | `PAYMENTHOLDDATE` | DATE |  |  |  |  |
| 167 | `VARFORPAYMENTADVICESTDTABLECOD` | CHAR(5) |  |  |  |  |
| 168 | `VARIANTFORPAYMENTADVICECODE` | CHAR(10) |  |  |  |  |
| 169 | `BUSINESSPRNFORPAYMENTNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 170 | `NOTEFORPAYMENT` | VARCHAR(100) |  |  |  |  |
| 171 | `CREATIONDATETIME2` | TIMESTAMP |  |  |  |  |
| 172 | `CREATIONUSER2` | CHAR(50) |  |  |  |  |
| 173 | `LASTUPDATEDATETIME2` | TIMESTAMP |  |  |  |  |
| 174 | `LASTUPDATEUSER2` | CHAR(50) |  |  |  |  |
| 175 | `USECREATIONUSER2` | SMALLINT | NOT NULL |  |  |  |
| 176 | `CREATIONDATETIMEUTC2` | TIMESTAMP |  |  |  |  |
| 177 | `CREATIONDATETIMECMPDIV2` | TIMESTAMP |  |  |  |  |
| 178 | `CREATIONDATETIMEUSER2` | TIMESTAMP |  |  |  |  |
| 179 | `LASTUPDATEDATETIMEUTC2` | TIMESTAMP |  |  |  |  |
| 180 | `LASTUPDATEDATETIMECMPDIV2` | TIMESTAMP |  |  |  |  |
| 181 | `LASTUPDATEDATETIMEUSER2` | TIMESTAMP |  |  |  |  |
| 182 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 183 | `RANGECODE` | CHAR(15) |  |  |  |  |
| 184 | `RANGEDESCRIPTION` | CHAR(100) |  |  |  |  |
| 185 | `RANGEDIVISIONCODE` | CHAR(15) |  |  |  |  |
| 186 | `RANGEDIVISIONDESCRIPTION` | CHAR(100) |  |  |  |  |
| 187 | `COMMISSIONERATE` | CHAR(30) |  |  |  |  |
| 188 | `CEREGISTRATIONNO` | CHAR(30) |  |  |  |  |
| 189 | `CEREGISTRATIONDATE` | DATE |  |  |  |  |
| 190 | `ECCTYPECODE` | CHAR(3) |  |  |  |  |
| 191 | `ECCNO` | CHAR(30) |  |  |  |  |
| 192 | `ECCDATE` | DATE |  |  |  |  |
| 193 | `CSTNO` | CHAR(30) |  |  |  |  |
| 194 | `CSTDATE` | DATE |  |  |  |  |
| 195 | `SSTNO` | CHAR(30) |  |  |  |  |
| 196 | `SSTDATE` | DATE |  |  |  |  |
| 197 | `SALESTAXCODE` | CHAR(30) |  |  |  |  |
| 198 | `SSINUMBER` | CHAR(30) |  |  |  |  |
| 199 | `SSIDATE` | DATE |  |  |  |  |
| 200 | `TAXTEMPLATEHEADERTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 201 | `TAXTEMPLATEHEADERCODE` | CHAR(3) |  |  |  |  |
| 202 | `TAXTEMPLATEDETAILTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 203 | `TAXTEMPLATEDETAILCODE` | CHAR(3) |  |  |  |  |
| 204 | `PORTOFDISCHARGECODE` | CHAR(10) |  |  |  |  |
| 205 | `PORTOFLOADINGCODE` | CHAR(10) |  |  |  |  |
| 206 | `FINALDESTINATIONCODE` | CHAR(3) |  |  |  |  |
| 207 | `COUNTRYOFDESTINATIONCODE` | CHAR(3) |  |  |  |  |
| 208 | `GLCODE` | CHAR(20) |  |  |  |  |
| 209 | `STATECODE` | CHAR(3) |  |  |  |  |
| 210 | `INSURANCECHARGES` | DECIMAL(18,5) |  |  |  |  |
| 211 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 212 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 213 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 214 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 215 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 216 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 217 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 218 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 219 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 220 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 221 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 222 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 223 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 224 | `ASSOCIATIONMARK` | SMALLINT | NOT NULL |  |  |  |
| 225 | `ASSOCIATIONPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 226 | `ASSOCIATIONMEMBER` | CHAR(20) |  |  |  |  |
| 227 | `FISCALREPRESENTATIVENUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 228 | `PERMESTABLISHMENTCODE` | CHAR(8) |  |  |  |  |
| 229 | `FISCALREPRESENTATIVEUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 230 | `GENDER` | CHAR(1) |  |  |  |  |
| 231 | `DATEOFBIRTH` | DATE |  |  |  |  |
| 232 | `COUNTRYOFBIRTHCODE` | CHAR(3) |  |  |  |  |
| 233 | `DISTRICTOFBIRTH` | VARCHAR(200) |  |  |  |  |
| 234 | `PLACEOFBIRTH` | VARCHAR(200) |  |  |  |  |
| 235 | `EDATATRANSFERTYPE` | CHAR(1) |  |  |  |  |
| 236 | `EDATATRANSFERUNIQUEID` | CHAR(50) |  |  |  |  |
| 237 | `EDATATRANSFEREMAIL` | CHAR(150) |  |  |  |  |
| 238 | `INTERDIVISIONLINKCODE` | CHAR(10) |  |  |  |  |
| 239 | `RFPARTNERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 240 | `INSURANCESELFRETENTION` | DECIMAL(5,2) |  |  |  |  |
| 241 | `ACTIONBUTTON` | CHAR(20) |  |  |  |  |
| 242 | `NATIONALITY` | CHAR(20) |  |  |  |  |
| 243 | `DUEDATEEXCEPTIONCODE` | CHAR(6) |  |  |  |  |
| 244 | `TYPEOFORDERPARTNER` | CHAR(2) |  |  |  |  |
| 245 | `PANNO` | CHAR(10) |  |  |  |  |
| 246 | `TCSAPPLICABILITY` | SMALLINT | NOT NULL |  |  |  |
| 247 | `TDSAPPLICABILITY` | SMALLINT | NOT NULL |  |  |  |
| 248 | `TCSEXEMPTION` | SMALLINT | NOT NULL |  |  |  |
| 249 | `MSMENUMBER` | CHAR(30) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FULLORDERPARTNERIBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.ABSUNIQUEID,
       t.CUSTOMERSUPPLIERCOMPANYCODE,
       t.CUSTOMERSUPPLIERTYPE,
       t.CUSTOMERSUPPLIERCODE,
       t.WAREHOUSECODE,
       t.ORDERBUSINESSPARTNERNUMBERID,
       t.ORDERLOGICALWAREHOUSECODE,
       t.ORIGININFORMATIONTYPECODE,
       t.ENDDATE,
       t.SUBSTITUTEBPNUMBERID,
       t.LEGALNAME1
FROM   DB2ADMIN.FULLORDERPARTNERIBEAN t
FETCH FIRST 100 ROWS ONLY;
```
