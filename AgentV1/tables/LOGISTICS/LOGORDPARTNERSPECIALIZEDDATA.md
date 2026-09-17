# DB2ADMIN.LOGORDPARTNERSPECIALIZEDDATA

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 172
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 58442

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ORDPRNCSMSUPPLIERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 2 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 3 | `INITIALDATE` | DATE |  |  |  |  |
| 4 | `FINALDATE` | DATE | NOT NULL |  |  |  |
| 5 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 6 | `BRANDCODE` | CHAR(8) | NOT NULL |  |  |  |
| 7 | `STATISTICALGROUPCODE` | CHAR(6) | NOT NULL |  |  |  |
| 8 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 9 | `AREACODE` | CHAR(3) |  |  |  |  |
| 10 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 11 | `ORDERTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 12 | `COMPANYLIABLEINITIALSCODE` | CHAR(50) |  |  |  |  |
| 13 | `ORDERALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `BLOCKCONTROLREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 16 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 17 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 18 | `WORKINGCALENDARCODE` | CHAR(3) |  |  |  |  |
| 19 | `DATECALCULATIONCODE` | CHAR(3) |  |  |  |  |
| 20 | `MINIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `MAXIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 22 | `MINIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `MAXIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 24 | `MINIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 25 | `MAXIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 26 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 27 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 28 | `GROUPORDERSONSHIPPING` | INTEGER | NOT NULL |  |  |  |
| 29 | `GROUPSHIPPINGSONINVOICE` | INTEGER | NOT NULL |  |  |  |
| 30 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 31 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 32 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 33 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 34 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 35 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 36 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 37 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 38 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 39 | `CREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 40 | `ENDDATECREDITLIMIT` | DATE |  |  |  |  |
| 41 | `INSURANCECREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 42 | `INSURANCECMYCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 43 | `INSURANCECMYCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 44 | `ENDDATEINSURANCECREDITLIMIT` | DATE |  |  |  |  |
| 45 | `FINANCIALPARTNERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 46 | `FINANCIALPARTNERCODE` | CHAR(8) |  |  |  |  |
| 47 | `TAXSTAMPREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 48 | `TAXSTAMPREQUIREDFORCREDIT` | SMALLINT | NOT NULL |  |  |  |
| 49 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 50 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 51 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 52 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 53 | `AGTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 54 | `AGENTGRPCODE` | CHAR(3) |  |  |  |  |
| 55 | `ASSORTGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 56 | `ASSORTGRPCODE` | CHAR(3) |  |  |  |  |
| 57 | `EXSGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 58 | `EXCLUSIVEGRPCODE` | CHAR(3) |  |  |  |  |
| 59 | `BLOCKGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 60 | `BLOCKGRPCODE` | CHAR(3) |  |  |  |  |
| 61 | `PRCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 62 | `PRICEGRPCODE` | CHAR(3) |  |  |  |  |
| 63 | `DSCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 64 | `DISCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 65 | `CHARGEGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 66 | `CHARGEGRPCODE` | CHAR(3) |  |  |  |  |
| 67 | `RESTRICGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 68 | `RESTRICGRPCODE` | CHAR(3) |  |  |  |  |
| 69 | `CMTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 70 | `COMMENTGRPCODE` | CHAR(3) |  |  |  |  |
| 71 | `TAXGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 72 | `TAXGRPCODE` | CHAR(3) |  |  |  |  |
| 73 | `MNGACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 74 | `MANAGEMENTACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 75 | `FNCACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 76 | `FINANCIALACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 77 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 78 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 79 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 80 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 81 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 82 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 83 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 84 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 85 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 86 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 87 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 88 | `CMYLIABLEINITIALSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 89 | `DATECALCULATIONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 90 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 91 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 92 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 93 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 94 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 95 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 96 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 97 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 98 | `COMPANYBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 99 | `RISKNUMBER` | CHAR(30) |  |  |  |  |
| 100 | `TYPEOFINSURANCESYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 101 | `TYPEOFINSURANCECODE` | CHAR(10) |  |  |  |  |
| 102 | `RISKCATEGORYSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 103 | `RISKCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 104 | `CREDITREPORTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 105 | `CREDITREPORTCODE` | CHAR(10) |  |  |  |  |
| 106 | `CREDITREQUEST` | SMALLINT | NOT NULL |  |  |  |
| 107 | `CREDITREQUESTDATE` | DATE |  |  |  |  |
| 108 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 109 | `FINTABLENBRACCOUNTGROUP` | CHAR(5) |  |  |  |  |
| 110 | `GLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 111 | `FINANCEACCOUNTGROUPCODE` | CHAR(10) |  |  |  |  |
| 112 | `VARFORACCSTATEMENTSTDTABLECOD` | CHAR(5) |  |  |  |  |
| 113 | `VARIANTFORACCOUNTSTATEMENTCODE` | CHAR(10) |  |  |  |  |
| 114 | `VARFORBLNCNFSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 115 | `VARFORBALANCECONFIRMATIONCODE` | CHAR(10) |  |  |  |  |
| 116 | `FININITIALDATE` | DATE |  |  |  |  |
| 117 | `FINFINALDATE` | DATE |  |  |  |  |
| 118 | `FININACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 119 | `NOTEFORBOOKING` | VARCHAR(100) |  |  |  |  |
| 120 | `REMINDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 121 | `REMINDERDELIVERY` | CHAR(1) |  |  |  |  |
| 122 | `REMBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 123 | `REMBLOCKCODE` | CHAR(2) |  |  |  |  |
| 124 | `REMINDERBLOCKDATE` | DATE |  |  |  |  |
| 125 | `BUSINESSPRNFORREMINDERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 126 | `COLLECTIONDIFFERENT` | SMALLINT | NOT NULL |  |  |  |
| 127 | `COLLECTIONADDRESSNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 128 | `BADDEBTSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 129 | `BADDEBTSCODE` | CHAR(10) |  |  |  |  |
| 130 | `VALUEADJUSTMENTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 131 | `VALUEADJUSTMENTCODE` | CHAR(10) |  |  |  |  |
| 132 | `VALUEADJUSTMENTRATE` | DECIMAL(5,2) |  |  |  |  |
| 133 | `CSMSUPSTATUSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 134 | `CUSTOMERSUPPLIERSTATUSCODE` | CHAR(10) |  |  |  |  |
| 135 | `NOTEFORREMINDER` | VARCHAR(100) |  |  |  |  |
| 136 | `PAYMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 137 | `PAYMENTBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 138 | `PAYMENTBLOCKCODE` | CHAR(2) |  |  |  |  |
| 139 | `PAYMENTHOLDDATE` | DATE |  |  |  |  |
| 140 | `VARFORPAYMENTADVICESTDTABLECOD` | CHAR(5) |  |  |  |  |
| 141 | `VARIANTFORPAYMENTADVICECODE` | CHAR(10) |  |  |  |  |
| 142 | `BUSINESSPRNFORPAYMENTNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 143 | `NOTEFORPAYMENT` | VARCHAR(100) |  |  |  |  |
| 144 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 145 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 146 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 147 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 148 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 149 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 150 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 151 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 152 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 153 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 154 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 155 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 156 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 157 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 158 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 159 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 160 | `VATTAXCODE` | CHAR(5) |  |  |  |  |
| 161 | `TAXSTAMPCHARGEDONCREDITNOTE` | SMALLINT | NOT NULL |  |  |  |
| 162 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 163 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 164 | `ASSOCIATIONMARK` | SMALLINT | NOT NULL |  |  |  |
| 165 | `ASSOCIATIONPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 166 | `ASSOCIATIONMEMBER` | CHAR(20) |  |  |  |  |
| 167 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 168 | `INSURANCESELFRETENTION` | DECIMAL(5,2) |  |  |  |  |
| 169 | `RFPARTNERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 170 | `DUEDATEEXCEPTIONCODE` | CHAR(6) |  |  |  |  |
| 171 | `WFMSTATUS` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGORDPARTNERSPECIALIZEDDATA.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.ORDPRNCSMSUPPLIERCOMPANYCODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.INITIALDATE,
       t.FINALDATE,
       t.DIVISIONCODE,
       t.BRANDCODE,
       t.STATISTICALGROUPCODE,
       t.MARKETCODE,
       t.AREACODE,
       t.ORDERCATEGORYCODE,
       t.ORDERTEMPLATECODE
FROM   DB2ADMIN.LOGORDPARTNERSPECIALIZEDDATA t
FETCH FIRST 100 ROWS ONLY;
```
