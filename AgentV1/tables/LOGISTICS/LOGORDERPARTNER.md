# DB2ADMIN.LOGORDERPARTNER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 171
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 58034

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CUSTOMERSUPPLIERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 2 | `CUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 3 | `ORDERBUSINESSPARTNERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 4 | `ORDERLOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 5 | `REPRESENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `COMPANYSUPPLIERCODE` | CHAR(10) |  |  |  |  |
| 7 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 8 | `AREACODE` | CHAR(3) |  |  |  |  |
| 9 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 10 | `COMPANYLIABLEINITIALSCODE` | CHAR(50) |  |  |  |  |
| 11 | `ORDERALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `BLOCKCONTROLREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 14 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 15 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 16 | `WORKINGCALENDARCODE` | CHAR(3) |  |  |  |  |
| 17 | `DATECALCULATIONCODE` | CHAR(3) |  |  |  |  |
| 18 | `MINIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 19 | `MAXIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 20 | `MINIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `MAXIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 22 | `MINIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `MAXIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 24 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 25 | `GROUPORDERSONSHIPPING` | INTEGER | NOT NULL |  |  |  |
| 26 | `GROUPSHIPPINGSONINVOICE` | INTEGER | NOT NULL |  |  |  |
| 27 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 28 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 29 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 30 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 31 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 32 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 33 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 34 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 35 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 36 | `CREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 37 | `ENDDATECREDITLIMIT` | DATE |  |  |  |  |
| 38 | `INSURANCECREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 39 | `INSURANCECMYCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 40 | `INSURANCECMYCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 41 | `ENDDATEINSURANCECREDITLIMIT` | DATE |  |  |  |  |
| 42 | `FINANCIALPARTNERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 43 | `FINANCIALPARTNERCODE` | CHAR(8) |  |  |  |  |
| 44 | `TAXSTAMPREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 45 | `TAXSTAMPREQUIREDFORCREDIT` | SMALLINT | NOT NULL |  |  |  |
| 46 | `ACKNOWLEDGEMENTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 47 | `ACKNOWLEDGEMENTTYPE` | CHAR(2) |  |  |  |  |
| 48 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 49 | `AGTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 50 | `AGENTGRPCODE` | CHAR(3) |  |  |  |  |
| 51 | `ASSORTGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 52 | `ASSORTGRPCODE` | CHAR(3) |  |  |  |  |
| 53 | `EXSGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 54 | `EXCLUSIVEGRPCODE` | CHAR(3) |  |  |  |  |
| 55 | `BLOCKGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 56 | `BLOCKGRPCODE` | CHAR(3) |  |  |  |  |
| 57 | `PRCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 58 | `PRICEGRPCODE` | CHAR(3) |  |  |  |  |
| 59 | `DSCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 60 | `DISCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 61 | `CHARGEGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 62 | `CHARGEGRPCODE` | CHAR(3) |  |  |  |  |
| 63 | `RESTRICGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 64 | `RESTRICGRPCODE` | CHAR(3) |  |  |  |  |
| 65 | `CMTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 66 | `COMMENTGRPCODE` | CHAR(3) |  |  |  |  |
| 67 | `TAXGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 68 | `TAXGRPCODE` | CHAR(3) |  |  |  |  |
| 69 | `MNGACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 70 | `MANAGEMENTACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 71 | `FNCACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 72 | `FINANCIALACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 73 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 74 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 75 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 76 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 77 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 78 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 79 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 80 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 81 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 82 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 83 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 84 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 85 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 86 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 87 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 88 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 89 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 90 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 91 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 92 | `ORDLGLWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 93 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 94 | `CMYLIABLEINITIALSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 95 | `DATECALCULATIONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 96 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 97 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 98 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 99 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 100 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 101 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 102 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 103 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 104 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 105 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 106 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 107 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 108 | `RISKNUMBER` | CHAR(30) |  |  |  |  |
| 109 | `TYPEOFINSURANCESYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 110 | `TYPEOFINSURANCECODE` | CHAR(10) |  |  |  |  |
| 111 | `RISKCATEGORYSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 112 | `RISKCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 113 | `CREDITREPORTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 114 | `CREDITREPORTCODE` | CHAR(10) |  |  |  |  |
| 115 | `CREDITREQUEST` | SMALLINT | NOT NULL |  |  |  |
| 116 | `CREDITREQUESTDATE` | DATE |  |  |  |  |
| 117 | `FINTABLENBRACCOUNTGROUP` | CHAR(5) |  |  |  |  |
| 118 | `GLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 119 | `FINANCEACCOUNTGROUPCODE` | CHAR(10) |  |  |  |  |
| 120 | `VARFORACCSTATEMENTSTDTABLECOD` | CHAR(5) |  |  |  |  |
| 121 | `VARIANTFORACCOUNTSTATEMENTCODE` | CHAR(10) |  |  |  |  |
| 122 | `VARFORBLNCNFSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 123 | `VARFORBALANCECONFIRMATIONCODE` | CHAR(10) |  |  |  |  |
| 124 | `FININITIALDATE` | DATE |  |  |  |  |
| 125 | `FINFINALDATE` | DATE |  |  |  |  |
| 126 | `FININACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 127 | `NOTEFORBOOKING` | VARCHAR(100) |  |  |  |  |
| 128 | `REMINDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 129 | `REMINDERDELIVERY` | CHAR(1) |  |  |  |  |
| 130 | `REMBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 131 | `REMBLOCKCODE` | CHAR(2) |  |  |  |  |
| 132 | `REMINDERBLOCKDATE` | DATE |  |  |  |  |
| 133 | `BUSINESSPRNFORREMINDERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 134 | `COLLECTIONDIFFERENT` | SMALLINT | NOT NULL |  |  |  |
| 135 | `COLLECTIONADDRESSNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 136 | `BADDEBTSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 137 | `BADDEBTSCODE` | CHAR(10) |  |  |  |  |
| 138 | `VALUEADJUSTMENTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 139 | `VALUEADJUSTMENTCODE` | CHAR(10) |  |  |  |  |
| 140 | `VALUEADJUSTMENTRATE` | DECIMAL(5,2) |  |  |  |  |
| 141 | `CSMSUPSTATUSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 142 | `CUSTOMERSUPPLIERSTATUSCODE` | CHAR(10) |  |  |  |  |
| 143 | `NOTEFORREMINDER` | VARCHAR(100) |  |  |  |  |
| 144 | `PAYMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 145 | `PAYMENTBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 146 | `PAYMENTBLOCKCODE` | CHAR(2) |  |  |  |  |
| 147 | `PAYMENTHOLDDATE` | DATE |  |  |  |  |
| 148 | `VARFORPAYMENTADVICESTDTABLECOD` | CHAR(5) |  |  |  |  |
| 149 | `VARIANTFORPAYMENTADVICECODE` | CHAR(10) |  |  |  |  |
| 150 | `BUSINESSPRNFORPAYMENTNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 151 | `NOTEFORPAYMENT` | VARCHAR(100) |  |  |  |  |
| 152 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 153 | `INTERCOMPANYDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 154 | `VATTAXCODE` | CHAR(5) |  |  |  |  |
| 155 | `TAXSTAMPCHARGEDONCREDITNOTE` | SMALLINT | NOT NULL |  |  |  |
| 156 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 157 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 158 | `ASSOCIATIONMARK` | SMALLINT | NOT NULL |  |  |  |
| 159 | `ASSOCIATIONPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 160 | `ASSOCIATIONMEMBER` | CHAR(20) |  |  |  |  |
| 161 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 162 | `INTERDIVISIONLINKCODE` | CHAR(10) |  |  |  |  |
| 163 | `EDATATRANSFERTYPE` | CHAR(1) |  |  |  |  |
| 164 | `EDATATRANSFERUNIQUEID` | CHAR(50) |  |  |  |  |
| 165 | `EDATATRANSFEREMAIL` | CHAR(150) |  |  |  |  |
| 166 | `INSURANCESELFRETENTION` | DECIMAL(5,2) |  |  |  |  |
| 167 | `RFPARTNERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 168 | `DUEDATEEXCEPTIONCODE` | CHAR(6) |  |  |  |  |
| 169 | `WFMSTATUS` | INTEGER | NOT NULL |  |  |  |
| 170 | `TAXREGIMECODE` | CHAR(4) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGORDERPARTNER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGORDERPARTNERBANK`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)

## Starter query

```sql
SELECT t.CUSTOMERSUPPLIERCOMPANYCODE,
       t.CUSTOMERSUPPLIERTYPE,
       t.CUSTOMERSUPPLIERCODE,
       t.ORDERBUSINESSPARTNERNUMBERID,
       t.ORDERLOGICALWAREHOUSECODE,
       t.REPRESENTCOMPANYCODE,
       t.COMPANYSUPPLIERCODE,
       t.MARKETCODE,
       t.AREACODE,
       t.ORDERCATEGORYCODE,
       t.COMPANYLIABLEINITIALSCODE,
       t.ORDERALLOWED
FROM   DB2ADMIN.LOGORDERPARTNER t
FETCH FIRST 100 ROWS ONLY;
```
