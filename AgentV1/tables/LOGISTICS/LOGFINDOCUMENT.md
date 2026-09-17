# DB2ADMIN.LOGFINDOCUMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 243
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 179452

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `FINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 5 | `DOCUMENTTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `DOCUMENTTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `FINANCEMONTHCODE` | INTEGER | NOT NULL |  |  |  |
| 8 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `DOCUMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `REVALUATIONBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 11 | `REVALUATIONFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 12 | `REVALUATIONREVALUATIONDATE` | DATE |  |  |  |  |
| 13 | `REVALUATIONPROCESSTYPE` | CHAR(1) |  |  |  |  |
| 14 | `CURRENTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 15 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 16 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 17 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 18 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 19 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 20 | `EMPLOYEECODE` | CHAR(9) |  |  |  |  |
| 21 | `OTHERCUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `OTHERCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 23 | `OTHERVENDORTYPE` | CHAR(1) |  |  |  |  |
| 24 | `OTHERVENDORCODE` | CHAR(8) |  |  |  |  |
| 25 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `GLCODE` | CHAR(20) |  |  |  |  |
| 27 | `OPTDSTDSTEUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 28 | `OPTDSTDSTYPECODE` | CHAR(10) |  |  |  |  |
| 29 | `OPTDSTDSCODE` | CHAR(6) |  |  |  |  |
| 30 | `OPTDSTDSITAXCODE` | CHAR(3) |  |  |  |  |
| 31 | `TDSPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 32 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 33 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 34 | `TDSGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `TDSGLCODE` | CHAR(20) |  |  |  |  |
| 36 | `FINANCEDOCUMENTDATE` | DATE | NOT NULL |  |  |  |
| 37 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 38 | `DUEDATE` | DATE |  |  |  |  |
| 39 | `TERMSOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 40 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 41 | `STATISTICALGROUPCODE` | CHAR(6) | NOT NULL |  |  |  |
| 42 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 43 | `DOCUMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 44 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 45 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 46 | `DOCCOMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 47 | `CHEQUELOTCODE` | CHAR(10) |  |  |  |  |
| 48 | `CHEQUENUMBER` | CHAR(20) |  |  |  |  |
| 49 | `CHEQUEDATE` | DATE |  |  |  |  |
| 50 | `CUSTOMERREFERENCE` | CHAR(20) |  |  |  |  |
| 51 | `CUSTOMERREFERENCEDATE` | DATE |  |  |  |  |
| 52 | `VENDORREFERENCE` | CHAR(20) |  |  |  |  |
| 53 | `VENDORREFERENCEDATE` | DATE |  |  |  |  |
| 54 | `REFFINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 55 | `REFFINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 56 | `REFFINDOCDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 57 | `REFFINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 58 | `REFFINDOCCODE` | CHAR(15) |  |  |  |  |
| 59 | `REFERENCETEXT1` | CHAR(100) |  |  |  |  |
| 60 | `REFERENCETEXT2` | CHAR(50) |  |  |  |  |
| 61 | `REFERENCETEXT3` | CHAR(50) |  |  |  |  |
| 62 | `REFERENCETEXT4` | CHAR(50) |  |  |  |  |
| 63 | `REFERENCETEXT5` | CHAR(50) |  |  |  |  |
| 64 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 65 | `FIRSTUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 66 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 67 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 68 | `SNDUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 69 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 70 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 71 | `THIRDUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 72 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 73 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 74 | `FRUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 75 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 76 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 77 | `FIFTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 78 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 79 | `REFERENCEAMT1` | DECIMAL(18,5) |  |  |  |  |
| 80 | `REFERENCEAMT2` | DECIMAL(18,5) |  |  |  |  |
| 81 | `REFERENCEAMT3` | DECIMAL(18,5) |  |  |  |  |
| 82 | `REFERENCEAMT4` | DECIMAL(18,5) |  |  |  |  |
| 83 | `REFERENCEAMT5` | DECIMAL(18,5) |  |  |  |  |
| 84 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 85 | `PURCHASEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 86 | `PURINVOICEORDPRNCSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 87 | `PURINVOICEORDPRNCSMSUPCODE` | CHAR(8) |  |  |  |  |
| 88 | `PURCHASEINVOICECODE` | CHAR(25) |  |  |  |  |
| 89 | `PURCHASEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 90 | `EXPENSEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 91 | `EXPENSEINVOICEORDPRNCSMSUPTE` | CHAR(1) |  |  |  |  |
| 92 | `EXPENSEINVOICEORDPRNCSMSUPCOD` | CHAR(8) |  |  |  |  |
| 93 | `EXPENSEINVOICECODE` | CHAR(25) |  |  |  |  |
| 94 | `EXPENSEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 95 | `MRNREJMDMRNHEADERDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 96 | `MRNREJMDMRNHEADERMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 97 | `MRNREJMDMRNHEADERCODE` | DECIMAL(11,0) |  |  |  |  |
| 98 | `MRNREJMDLINEID` | INTEGER | NOT NULL |  |  |  |
| 99 | `MRNREJREJECTIONLINEID` | INTEGER | NOT NULL |  |  |  |
| 100 | `POADVANCEPURORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 101 | `POADVANCEPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 102 | `POADVANCELINENO` | INTEGER | NOT NULL |  |  |  |
| 103 | `EMPLADVANCELRDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 104 | `EMPLADVANCELREMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 105 | `EMPLADVANCELREQUESTLOANTYPE` | INTEGER | NOT NULL |  |  |  |
| 106 | `EMPLADVANCELREQUESTLOANCODE` | CHAR(4) |  |  |  |  |
| 107 | `EMPLADVANCELRLOANVOUCHERNO` | DECIMAL(15,0) |  |  |  |  |
| 108 | `EMPLOANADVANCECODE` | BIGINT | NOT NULL |  |  |  |
| 109 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 110 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 111 | `COMMERCIALINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 112 | `COMMERCIALINVOICECODE` | CHAR(20) |  |  |  |  |
| 113 | `SDCREDITPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 114 | `SDCREDITPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 115 | `DIRECTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 116 | `DIRECTINVOICECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 117 | `DIRECTINVOICECODE` | CHAR(15) |  |  |  |  |
| 118 | `MRNDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 119 | `MRNMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 120 | `MRNCODE` | DECIMAL(11,0) |  |  |  |  |
| 121 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 122 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 123 | `CONSUMPTIONDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 124 | `CONSUMPTIONITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 125 | `CONSUMPTIONBUSINESSAREACODE` | CHAR(50) |  |  |  |  |
| 126 | `CONSUMPTIONSTARTDATE` | DATE |  |  |  |  |
| 127 | `CONSUMPTIONENDDATE` | DATE |  |  |  |  |
| 128 | `PAYROLLPOSTINGSNO` | BIGINT | NOT NULL |  |  |  |
| 129 | `PAYROLLPOSTINGPAYROLLCODE` | CHAR(3) |  |  |  |  |
| 130 | `PAYROLLPOSTINGPROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 131 | `INTERNALORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 132 | `INTERNALORDERCODE` | CHAR(15) |  |  |  |  |
| 133 | `RG23IIAEXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 134 | `RG23IIAEXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 135 | `RG23IIACODE` | CHAR(15) |  |  |  |  |
| 136 | `RG23IICEXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 137 | `RG23IICEXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 138 | `RG23IICCODE` | CHAR(15) |  |  |  |  |
| 139 | `EXPORTSHIPPINGBILLDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 140 | `EXPORTSHIPPINGBILLCODE` | CHAR(12) |  |  |  |  |
| 141 | `MRNINVOICENO` | CHAR(25) |  |  |  |  |
| 142 | `MRNINVOICEDATE` | DATE |  |  |  |  |
| 143 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 144 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 145 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 146 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 147 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 148 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 149 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 150 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 151 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 152 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 153 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 154 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 155 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 156 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 157 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 158 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 159 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 160 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 161 | `PROPOSALREFNO` | CHAR(20) |  |  |  |  |
| 162 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 163 | `INVOICEDATE` | DATE |  |  |  |  |
| 164 | `CONSUMPTIONLGLWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 165 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 166 | `OPTDSEXEMPTIONFROMDATE` | DATE |  |  |  |  |
| 167 | `TDSEXEMPTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 168 | `SIXTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 169 | `SIXTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 170 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 171 | `SEVENTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 172 | `SEUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 173 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 174 | `TRANSACTIONREFNO` | CHAR(20) |  |  |  |  |
| 175 | `POPAYMENTREFNO` | CHAR(20) |  |  |  |  |
| 176 | `BUTRANSACTIONNO` | CHAR(20) |  |  |  |  |
| 177 | `EOAEXTERNALOPERATIONCNTCODE` | CHAR(8) |  |  |  |  |
| 178 | `EOAEXTERNALOPERATIONCODE` | CHAR(15) |  |  |  |  |
| 179 | `EOALINENO` | INTEGER | NOT NULL |  |  |  |
| 180 | `PERIODCOSTEVENTCODE` | CHAR(15) |  |  |  |  |
| 181 | `PERIODCOSTWHSACCGROUPCODE` | CHAR(3) |  |  |  |  |
| 182 | `PERCOSTPERPERCALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 183 | `PERCOSTPERPERCALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 184 | `PERIODCOSTPERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 185 | `PERIODCOSTBUSINESSAREACODE` | CHAR(50) |  |  |  |  |
| 186 | `LCDETAILPURDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 187 | `LCDETAILPURLCNO` | CHAR(35) |  |  |  |  |
| 188 | `LCDETAILPURLCDATE` | DATE |  |  |  |  |
| 189 | `LCAMDPURREGLCDLTPURDIVISIONCOD` | CHAR(3) |  |  |  |  |
| 190 | `LCAMDPURREGLCDETAILPURLCNO` | CHAR(35) |  |  |  |  |
| 191 | `LCAMDPURREGLCDETAILPURLCDATE` | DATE |  |  |  |  |
| 192 | `LCAMDPURREGLCAMENDMENTNO` | DECIMAL(2,0) |  |  |  |  |
| 193 | `LCCANCELPURLCDLTPURCMYCODE` | CHAR(3) |  |  |  |  |
| 194 | `LCCANCELPURLCDLTPURDIVISIONCOD` | CHAR(3) |  |  |  |  |
| 195 | `LCCANCELPURLCDETAILPURLCNO` | CHAR(35) |  |  |  |  |
| 196 | `LCCANCELPURLCDETAILPURLCDATE` | DATE |  |  |  |  |
| 197 | `LCCANCELPURLINENUMBER` | DECIMAL(18,5) |  |  |  |  |
| 198 | `IMPFCPAYMENTCODE` | CHAR(5) |  |  |  |  |
| 199 | `PCLETTERNO` | CHAR(5) |  |  |  |  |
| 200 | `FCFCNO` | CHAR(10) |  |  |  |  |
| 201 | `FCCFCNO` | CHAR(10) |  |  |  |  |
| 202 | `IFCCODE` | CHAR(5) |  |  |  |  |
| 203 | `NESFINEXPNEXTFINEXPNCODE` | CHAR(10) |  |  |  |  |
| 204 | `NESFINEXPNEXTEBANKREFNO` | CHAR(15) |  |  |  |  |
| 205 | `NESFINEXPNEXTEBANKDATE` | DATE |  |  |  |  |
| 206 | `NESFINEXPNEGOTIATIONEXTLINENO` | INTEGER | NOT NULL |  |  |  |
| 207 | `NESINTERESTGLCODE` | CHAR(20) |  |  |  |  |
| 208 | `NEFINEXPNEGOTIATIONCODE` | CHAR(10) |  |  |  |  |
| 209 | `NEEXTENSIONBANKREFNO` | CHAR(15) |  |  |  |  |
| 210 | `NEEXTENSIONBANKDATE` | DATE |  |  |  |  |
| 211 | `NELINENO` | INTEGER | NOT NULL |  |  |  |
| 212 | `NSFINEXPNEGOTIATIONCODE` | CHAR(10) |  |  |  |  |
| 213 | `NSINTERESTGLCODE` | CHAR(20) |  |  |  |  |
| 214 | `NGNCODE` | CHAR(10) |  |  |  |  |
| 215 | `RNCODE` | CHAR(15) |  |  |  |  |
| 216 | `BAACODE` | CHAR(5) |  |  |  |  |
| 217 | `BACODE` | CHAR(10) |  |  |  |  |
| 218 | `EACODE` | CHAR(5) |  |  |  |  |
| 219 | `LDISBURSEMENTSLTEUGENGRPTECOD` | CHAR(3) |  |  |  |  |
| 220 | `LOANDISBURSEMENTSLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 221 | `LOANDISBURSEMENTSCODELOANNO` | CHAR(10) |  |  |  |  |
| 222 | `LOANDISBURSEMENTSSLNO` | INTEGER | NOT NULL |  |  |  |
| 223 | `LOANREPAYMENTBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 224 | `LOANREPAYMENTFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 225 | `LRLTEUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 226 | `LOANREPAYMENTLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 227 | `LOANREPAYMENTCODELOANNO` | CHAR(10) |  |  |  |  |
| 228 | `LOANREPAYMENTREPAYMENTDATE` | DATE |  |  |  |  |
| 229 | `LOANREPAYMENTSLNO` | INTEGER | NOT NULL |  |  |  |
| 230 | `LCAPSUBSIDYLTEUGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 231 | `LOANCAPITALSUBSIDYLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 232 | `LOANCAPITALSUBSIDYCODELOANNO` | CHAR(10) |  |  |  |  |
| 233 | `LOANCAPITALSUBSIDYSLNO` | INTEGER | NOT NULL |  |  |  |
| 234 | `LNINTSUBSIDYLTEUGENGRPTECODE` | CHAR(3) |  |  |  |  |
| 235 | `LNINTSUBSIDYLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 236 | `LNINTSUBSIDYCODELOANNO` | CHAR(10) |  |  |  |  |
| 237 | `LNINTSUBSIDYSLNO` | INTEGER | NOT NULL |  |  |  |
| 238 | `DIGITALSIGNATURE` | CLOB(1000000) |  |  |  |  |
| 239 | `EXPORTSHIPPINGEDIDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 240 | `EXPORTSHIPPINGEDICODE` | CHAR(12) |  |  |  |  |
| 241 | `EXPORTSHPFOCUSDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 242 | `EXPORTSHIPPINGFOCUSCODE` | CHAR(12) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINDOCUMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGFINDOCUMENTTEMPLATE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGFINDOCUMENTLINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.ABSVERSIONNUMBER,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.DOCUMENTTEMPLATECOMPANYCODE,
       t.DOCUMENTTEMPLATECODE,
       t.FINANCEMONTHCODE,
       t.CODE,
       t.DOCUMENTTYPECODE,
       t.REVALUATIONBUSINESSUNITCODE,
       t.REVALUATIONFINANCIALYEARCODE
FROM   DB2ADMIN.LOGFINDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
