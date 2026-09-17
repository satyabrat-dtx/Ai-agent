# DB2ADMIN.ORDPRNSPECIALIZEDDATABEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 170
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 49040

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `INITIALDATE` | DATE |  |  |  |  |
| 3 | `FINALDATE` | DATE |  |  |  |  |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `BRANDCODE` | CHAR(8) |  |  |  |  |
| 6 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 7 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 8 | `AREACODE` | CHAR(3) |  |  |  |  |
| 9 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 10 | `ORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `COMPANYLIABLEINITIALSCODE` | CHAR(50) |  |  |  |  |
| 12 | `ORDERALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `BLOCKCONTROLREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 15 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 16 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 17 | `WORKINGCALENDARCODE` | CHAR(3) |  |  |  |  |
| 18 | `DATECALCULATIONCODE` | CHAR(3) |  |  |  |  |
| 19 | `MINIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 20 | `MAXIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `MINIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 22 | `MAXIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `MINIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 24 | `MAXIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 25 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 26 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 27 | `GROUPORDERSONSHIPPING` | INTEGER | NOT NULL |  |  |  |
| 28 | `GROUPSHIPPINGSONINVOICE` | INTEGER | NOT NULL |  |  |  |
| 29 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 30 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 31 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 32 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 33 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 34 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 35 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 36 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 37 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 38 | `CREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 39 | `ENDDATECREDITLIMIT` | DATE |  |  |  |  |
| 40 | `INSURANCECREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 41 | `INSURANCECMYCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 42 | `INSURANCECMYCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 43 | `ENDDATEINSURANCECREDITLIMIT` | DATE |  |  |  |  |
| 44 | `FINANCIALPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 45 | `FINANCIALPARTNERCODE` | CHAR(8) |  |  |  |  |
| 46 | `TAXSTAMPREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 47 | `TAXSTAMPREQUIREDFORCREDIT` | SMALLINT | NOT NULL |  |  |  |
| 48 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 49 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 50 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 51 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 52 | `AGTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 53 | `AGENTGRPCODE` | CHAR(3) |  |  |  |  |
| 54 | `ASSORTGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 55 | `ASSORTGRPCODE` | CHAR(3) |  |  |  |  |
| 56 | `EXSGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 57 | `EXCLUSIVEGRPCODE` | CHAR(3) |  |  |  |  |
| 58 | `BLOCKGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 59 | `BLOCKGRPCODE` | CHAR(3) |  |  |  |  |
| 60 | `PRCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 61 | `PRICEGRPCODE` | CHAR(3) |  |  |  |  |
| 62 | `DSCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 63 | `DISCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 64 | `CHARGEGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 65 | `CHARGEGRPCODE` | CHAR(3) |  |  |  |  |
| 66 | `RESTRICGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 67 | `RESTRICGRPCODE` | CHAR(3) |  |  |  |  |
| 68 | `CMTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 69 | `COMMENTGRPCODE` | CHAR(3) |  |  |  |  |
| 70 | `TAXGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 71 | `TAXGRPCODE` | CHAR(3) |  |  |  |  |
| 72 | `MNGACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 73 | `MANAGEMENTACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 74 | `FNCACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 75 | `FINANCIALACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 76 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 77 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 78 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 79 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 80 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 81 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 82 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 83 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 84 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 85 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 86 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 87 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 88 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 89 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 90 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 91 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 92 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 93 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 94 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 95 | `COMPANYBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 96 | `RISKNUMBER` | CHAR(30) |  |  |  |  |
| 97 | `TYPEOFINSURANCESYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 98 | `TYPEOFINSURANCECODE` | CHAR(10) |  |  |  |  |
| 99 | `RISKCATEGORYSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 100 | `RISKCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 101 | `CREDITREPORTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 102 | `CREDITREPORTCODE` | CHAR(10) |  |  |  |  |
| 103 | `CREDITREQUEST` | SMALLINT | NOT NULL |  |  |  |
| 104 | `CREDITREQUESTDATE` | DATE |  |  |  |  |
| 105 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 106 | `FINTABLENBRACCOUNTGROUP` | CHAR(5) |  |  |  |  |
| 107 | `GLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 108 | `FINANCEACCOUNTGROUPCODE` | CHAR(10) |  |  |  |  |
| 109 | `VARFORACCSTATEMENTSTDTABLECOD` | CHAR(5) |  |  |  |  |
| 110 | `VARIANTFORACCOUNTSTATEMENTCODE` | CHAR(10) |  |  |  |  |
| 111 | `VARFORBLNCNFSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 112 | `VARFORBALANCECONFIRMATIONCODE` | CHAR(10) |  |  |  |  |
| 113 | `FININITIALDATE` | DATE |  |  |  |  |
| 114 | `FINFINALDATE` | DATE |  |  |  |  |
| 115 | `FININACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 116 | `NOTEFORBOOKING` | VARCHAR(100) |  |  |  |  |
| 117 | `REMINDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 118 | `REMINDERDELIVERY` | CHAR(1) |  |  |  |  |
| 119 | `REMBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 120 | `REMBLOCKCODE` | CHAR(2) |  |  |  |  |
| 121 | `REMINDERBLOCKDATE` | DATE |  |  |  |  |
| 122 | `BUSINESSPRNFORREMINDERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 123 | `COLLECTIONDIFFERENT` | SMALLINT | NOT NULL |  |  |  |
| 124 | `COLLECTIONADDRESSNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 125 | `BADDEBTSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 126 | `BADDEBTSCODE` | CHAR(10) |  |  |  |  |
| 127 | `VALUEADJUSTMENTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 128 | `VALUEADJUSTMENTCODE` | CHAR(10) |  |  |  |  |
| 129 | `VALUEADJUSTMENTRATE` | DECIMAL(5,2) |  |  |  |  |
| 130 | `CSMSUPSTATUSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 131 | `CUSTOMERSUPPLIERSTATUSCODE` | CHAR(10) |  |  |  |  |
| 132 | `NOTEFORREMINDER` | VARCHAR(100) |  |  |  |  |
| 133 | `PAYMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 134 | `PAYMENTBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 135 | `PAYMENTBLOCKCODE` | CHAR(2) |  |  |  |  |
| 136 | `PAYMENTHOLDDATE` | DATE |  |  |  |  |
| 137 | `VARFORPAYMENTADVICESTDTABLECOD` | CHAR(5) |  |  |  |  |
| 138 | `VARIANTFORPAYMENTADVICECODE` | CHAR(10) |  |  |  |  |
| 139 | `BUSINESSPRNFORPAYMENTNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 140 | `NOTEFORPAYMENT` | VARCHAR(100) |  |  |  |  |
| 141 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 142 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 143 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 144 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 145 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 146 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 147 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 148 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 149 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 150 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 151 | `VATTAXCODE` | CHAR(5) |  |  |  |  |
| 152 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 153 | `TAXSTAMPCHARGEDONCREDITNOTE` | SMALLINT | NOT NULL |  |  |  |
| 154 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 155 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 156 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 157 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 158 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 159 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 160 | `ASSOCIATIONMARK` | SMALLINT | NOT NULL |  |  |  |
| 161 | `ASSOCIATIONPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 162 | `ASSOCIATIONMEMBER` | CHAR(20) |  |  |  |  |
| 163 | `INSURANCESELFRETENTION` | DECIMAL(5,2) |  |  |  |  |
| 164 | `RFPARTNERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 165 | `DUEDATEEXCEPTIONCODE` | CHAR(6) |  |  |  |  |
| 166 | `WFMSTATUS` | INTEGER | NOT NULL |  |  |  |
| 167 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 168 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 169 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ORDPRNSPECIALIZEDDATABEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ORDPRNSPECIALIZEDDATABEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.INITIALDATE,
       t.FINALDATE,
       t.DIVISIONCODE,
       t.BRANDCODE,
       t.STATISTICALGROUPCODE,
       t.MARKETCODE,
       t.AREACODE,
       t.ORDERCATEGORYCODE,
       t.ORDERTEMPLATECODE,
       t.COMPANYLIABLEINITIALSCODE
FROM   DB2ADMIN.ORDPRNSPECIALIZEDDATABEAN t
FETCH FIRST 100 ROWS ONLY;
```
