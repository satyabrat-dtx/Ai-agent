# DB2ADMIN.FULLORDERPARTNERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 217
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 73296

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
| 23 | `COMPANYSUPPLIERCODE` | CHAR(10) |  |  |  |  |
| 24 | `TAXSTAMPREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 25 | `TAXSTAMPREQUIREDFORCREDIT` | SMALLINT | NOT NULL |  |  |  |
| 26 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 27 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 28 | `FINANCIALPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 29 | `FINANCIALPARTNERCODE` | CHAR(8) |  |  |  |  |
| 30 | `COMPANYBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 31 | `ACKNOWLEDGEMENTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 32 | `ACKNOWLEDGEMENTTYPE` | CHAR(2) |  |  |  |  |
| 33 | `CREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 34 | `ENDDATECREDITLIMIT` | DATE |  |  |  |  |
| 35 | `INSURANCECREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 36 | `INSURANCECMYCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 37 | `INSURANCECMYCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 38 | `ENDDATEINSURANCECREDITLIMIT` | DATE |  |  |  |  |
| 39 | `AREACODE` | CHAR(3) |  |  |  |  |
| 40 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 41 | `ORDERALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 42 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 43 | `BLOCKCONTROLREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 44 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 45 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 46 | `WORKINGCALENDARCODE` | CHAR(3) |  |  |  |  |
| 47 | `DATECALCULATIONCODE` | CHAR(3) |  |  |  |  |
| 48 | `COMPANYLIABLEINITIALSCODE` | CHAR(50) |  |  |  |  |
| 49 | `MINIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 50 | `MAXIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 51 | `MINIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 52 | `MAXIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 53 | `MINIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 54 | `MAXIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 55 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 56 | `GROUPORDERSONSHIPPING` | INTEGER | NOT NULL |  |  |  |
| 57 | `GROUPSHIPPINGSONINVOICE` | INTEGER | NOT NULL |  |  |  |
| 58 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 59 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 60 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 61 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 62 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 63 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 64 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 65 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 66 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 67 | `AGTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 68 | `AGENTGRPCODE` | CHAR(3) |  |  |  |  |
| 69 | `ASSORTGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 70 | `ASSORTGRPCODE` | CHAR(3) |  |  |  |  |
| 71 | `EXSGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 72 | `EXCLUSIVEGRPCODE` | CHAR(3) |  |  |  |  |
| 73 | `BLOCKGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 74 | `BLOCKGRPCODE` | CHAR(3) |  |  |  |  |
| 75 | `PRCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 76 | `PRICEGRPCODE` | CHAR(3) |  |  |  |  |
| 77 | `DSCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 78 | `DISCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 79 | `CHARGEGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 80 | `CHARGEGRPCODE` | CHAR(3) |  |  |  |  |
| 81 | `RESTRICGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 82 | `RESTRICGRPCODE` | CHAR(3) |  |  |  |  |
| 83 | `CMTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 84 | `COMMENTGRPCODE` | CHAR(3) |  |  |  |  |
| 85 | `TAXGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 86 | `TAXGRPCODE` | CHAR(3) |  |  |  |  |
| 87 | `MNGACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 88 | `MANAGEMENTACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 89 | `FNCACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 90 | `FINANCIALACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 91 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 92 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 93 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 94 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 95 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 96 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 97 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 98 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 99 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 100 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 101 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 102 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 103 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 104 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 105 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 106 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 107 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 108 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 109 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 110 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 111 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 112 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 113 | `PERSON` | VARCHAR(200) |  |  |  |  |
| 114 | `ROLEINTHECOMPANY` | VARCHAR(200) |  |  |  |  |
| 115 | `PHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 116 | `FAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 117 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 118 | `BOOKLINE01` | VARCHAR(200) |  |  |  |  |
| 119 | `BOOKLINE02` | VARCHAR(200) |  |  |  |  |
| 120 | `BOOKLINE03` | VARCHAR(200) |  |  |  |  |
| 121 | `BOOKLINE04` | VARCHAR(200) |  |  |  |  |
| 122 | `BOOKLINE05` | VARCHAR(200) |  |  |  |  |
| 123 | `CREATIONDATETIME2` | TIMESTAMP |  |  |  |  |
| 124 | `CREATIONUSER2` | CHAR(50) |  |  |  |  |
| 125 | `LASTUPDATEDATETIME2` | TIMESTAMP |  |  |  |  |
| 126 | `LASTUPDATEUSER2` | CHAR(50) |  |  |  |  |
| 127 | `USECREATIONUSER2` | SMALLINT | NOT NULL |  |  |  |
| 128 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 129 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 130 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 131 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 132 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 133 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 134 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 135 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 136 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 137 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 138 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 139 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 140 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 141 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 142 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 143 | `RISKCATEGORYSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 144 | `RISKCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 145 | `RISKNUMBER` | CHAR(30) |  |  |  |  |
| 146 | `TYPEOFINSURANCESYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 147 | `TYPEOFINSURANCECODE` | CHAR(10) |  |  |  |  |
| 148 | `CREDITREPORTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 149 | `CREDITREPORTCODE` | CHAR(10) |  |  |  |  |
| 150 | `CREDITREQUEST` | SMALLINT | NOT NULL |  |  |  |
| 151 | `CREDITREQUESTDATE` | DATE |  |  |  |  |
| 152 | `FINTABLENBRACCOUNTGROUP` | CHAR(5) |  |  |  |  |
| 153 | `GLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 154 | `FINANCEACCOUNTGROUPCODE` | CHAR(10) |  |  |  |  |
| 155 | `VARFORACCSTATEMENTSTDTABLECOD` | CHAR(5) |  |  |  |  |
| 156 | `VARIANTFORACCOUNTSTATEMENTCODE` | CHAR(10) |  |  |  |  |
| 157 | `VARFORBLNCNFSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 158 | `VARFORBALANCECONFIRMATIONCODE` | CHAR(10) |  |  |  |  |
| 159 | `FININITIALDATE` | DATE |  |  |  |  |
| 160 | `FINFINALDATE` | DATE |  |  |  |  |
| 161 | `FININACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 162 | `NOTEFORBOOKING` | VARCHAR(100) |  |  |  |  |
| 163 | `REMINDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 164 | `REMINDERDELIVERY` | CHAR(1) |  |  |  |  |
| 165 | `REMBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 166 | `REMBLOCKCODE` | CHAR(2) |  |  |  |  |
| 167 | `REMINDERBLOCKDATE` | DATE |  |  |  |  |
| 168 | `BUSINESSPRNFORREMINDERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 169 | `COLLECTIONDIFFERENT` | SMALLINT | NOT NULL |  |  |  |
| 170 | `COLLECTIONADDRESSNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 171 | `BADDEBTSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 172 | `BADDEBTSCODE` | CHAR(10) |  |  |  |  |
| 173 | `VALUEADJUSTMENTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 174 | `VALUEADJUSTMENTCODE` | CHAR(10) |  |  |  |  |
| 175 | `VALUEADJUSTMENTRATE` | DECIMAL(5,2) |  |  |  |  |
| 176 | `CSMSUPSTATUSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 177 | `CUSTOMERSUPPLIERSTATUSCODE` | CHAR(10) |  |  |  |  |
| 178 | `NOTEFORREMINDER` | VARCHAR(100) |  |  |  |  |
| 179 | `PAYMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 180 | `PAYMENTBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 181 | `PAYMENTBLOCKCODE` | CHAR(2) |  |  |  |  |
| 182 | `PAYMENTHOLDDATE` | DATE |  |  |  |  |
| 183 | `VARFORPAYMENTADVICESTDTABLECOD` | CHAR(5) |  |  |  |  |
| 184 | `VARIANTFORPAYMENTADVICECODE` | CHAR(10) |  |  |  |  |
| 185 | `BUSINESSPRNFORPAYMENTNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 186 | `NOTEFORPAYMENT` | VARCHAR(100) |  |  |  |  |
| 187 | `NUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 188 | `INTERCOMPANYDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 189 | `VATTAXCODE` | CHAR(5) |  |  |  |  |
| 190 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 191 | `CREATIONDATETIMEUTC2` | TIMESTAMP |  |  |  |  |
| 192 | `CREATIONDATETIMECMPDIV2` | TIMESTAMP |  |  |  |  |
| 193 | `CREATIONDATETIMEUSER2` | TIMESTAMP |  |  |  |  |
| 194 | `LASTUPDATEDATETIMEUTC2` | TIMESTAMP |  |  |  |  |
| 195 | `LASTUPDATEDATETIMECMPDIV2` | TIMESTAMP |  |  |  |  |
| 196 | `LASTUPDATEDATETIMEUSER2` | TIMESTAMP |  |  |  |  |
| 197 | `ASSOCIATIONMARK` | SMALLINT | NOT NULL |  |  |  |
| 198 | `ASSOCIATIONPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 199 | `ASSOCIATIONMEMBER` | CHAR(20) |  |  |  |  |
| 200 | `FISCALREPRESENTATIVENUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 201 | `PERMESTABLISHMENTCODE` | CHAR(8) |  |  |  |  |
| 202 | `FISCALREPRESENTATIVEUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 203 | `GENDER` | CHAR(1) |  |  |  |  |
| 204 | `DATEOFBIRTH` | DATE |  |  |  |  |
| 205 | `COUNTRYOFBIRTHCODE` | CHAR(3) |  |  |  |  |
| 206 | `DISTRICTOFBIRTH` | VARCHAR(200) |  |  |  |  |
| 207 | `PLACEOFBIRTH` | VARCHAR(200) |  |  |  |  |
| 208 | `EDATATRANSFERTYPE` | CHAR(1) |  |  |  |  |
| 209 | `EDATATRANSFERUNIQUEID` | CHAR(50) |  |  |  |  |
| 210 | `EDATATRANSFEREMAIL` | CHAR(150) |  |  |  |  |
| 211 | `INTERDIVISIONLINKCODE` | CHAR(10) |  |  |  |  |
| 212 | `RFPARTNERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 213 | `INSURANCESELFRETENTION` | DECIMAL(5,2) |  |  |  |  |
| 214 | `ACTIONBUTTON` | CHAR(20) |  |  |  |  |
| 215 | `NATIONALITY` | CHAR(20) |  |  |  |  |
| 216 | `DUEDATEEXCEPTIONCODE` | CHAR(6) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FULLORDERPARTNERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.FULLORDERPARTNERBEAN t
FETCH FIRST 100 ROWS ONLY;
```
