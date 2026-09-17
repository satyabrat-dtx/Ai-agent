# DB2ADMIN.FINDOCUMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`
- **Columns**: 245
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203967

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `DIRECTENTRY` | SMALLINT | NOT NULL |  |  |  |
| 4 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 5 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `FINANCEMONTHCODE` | INTEGER | NOT NULL |  |  |  |
| 7 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `DOCUMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `REVALUATIONBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 10 | `REVALUATIONFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 11 | `REVALUATIONREVALUATIONDATE` | DATE |  |  |  |  |
| 12 | `REVALUATIONPROCESSTYPE` | CHAR(1) |  |  |  |  |
| 13 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 14 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 15 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 16 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 17 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 18 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 19 | `EMPLOYEECODE` | CHAR(9) |  |  |  |  |
| 20 | `OTHERCUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 21 | `OTHERCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 22 | `OTHERVENDORTYPE` | CHAR(1) |  |  |  |  |
| 23 | `OTHERVENDORCODE` | CHAR(8) |  |  |  |  |
| 24 | `GLCODE` | CHAR(20) |  |  |  |  |
| 25 | `NOTDSAPPLICABLE` | SMALLINT | NOT NULL |  |  |  |
| 26 | `OPTDSTDSTEUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 27 | `OPTDSTDSTYPECODE` | CHAR(10) |  |  |  |  |
| 28 | `OPTDSTDSCODE` | CHAR(6) |  |  |  |  |
| 29 | `OPTDSTDSITAXCODE` | CHAR(3) |  |  |  |  |
| 30 | `TDSPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 31 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 32 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 33 | `TDSGLCODE` | CHAR(20) |  |  |  |  |
| 34 | `FINANCEDOCUMENTDATE` | DATE |  |  |  |  |
| 35 | `POSTINGDATE` | DATE |  |  |  |  |
| 36 | `DUEDATE` | DATE |  |  |  |  |
| 37 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 38 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 39 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 40 | `CREDITAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 41 | `DEBITAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 42 | `DOCUMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 43 | `DYNAMICCLEARING` | SMALLINT | NOT NULL |  |  |  |
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
| 64 | `FIRSTUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 65 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 66 | `SNDUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 67 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 68 | `THIRDUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 69 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 70 | `FRUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 71 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 72 | `FIFTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 73 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 74 | `REFERENCEAMT1` | DECIMAL(18,5) |  |  |  |  |
| 75 | `REFERENCEAMT2` | DECIMAL(18,5) |  |  |  |  |
| 76 | `REFERENCEAMT3` | DECIMAL(18,5) |  |  |  |  |
| 77 | `REFERENCEAMT4` | DECIMAL(18,5) |  |  |  |  |
| 78 | `REFERENCEAMT5` | DECIMAL(18,5) |  |  |  |  |
| 79 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 80 | `PROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 81 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 82 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 83 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 84 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 85 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 86 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 87 | `PURCHASEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 88 | `PURINVOICEORDPRNCSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 89 | `PURINVOICEORDPRNCSMSUPCODE` | CHAR(8) |  |  |  |  |
| 90 | `PURCHASEINVOICECODE` | CHAR(25) |  |  |  |  |
| 91 | `PURCHASEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 92 | `EXPENSEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 93 | `EXPENSEINVOICEORDPRNCSMSUPTE` | CHAR(1) |  |  |  |  |
| 94 | `EXPENSEINVOICEORDPRNCSMSUPCOD` | CHAR(8) |  |  |  |  |
| 95 | `EXPENSEINVOICECODE` | CHAR(25) |  |  |  |  |
| 96 | `EXPENSEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 97 | `MRNREJMDMRNHEADERDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 98 | `MRNREJMDMRNHEADERMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 99 | `MRNREJMDMRNHEADERCODE` | DECIMAL(11,0) |  |  |  |  |
| 100 | `MRNREJMDLINEID` | INTEGER | NOT NULL |  |  |  |
| 101 | `MRNREJREJECTIONLINEID` | INTEGER | NOT NULL |  |  |  |
| 102 | `POADVANCEPURORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 103 | `POADVANCEPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 104 | `POADVANCELINENO` | INTEGER | NOT NULL |  |  |  |
| 105 | `EMPLADVANCELRDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 106 | `EMPLADVANCELREMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 107 | `EMPLADVANCELREQUESTLOANTYPE` | INTEGER | NOT NULL |  |  |  |
| 108 | `EMPLADVANCELREQUESTLOANCODE` | CHAR(4) |  |  |  |  |
| 109 | `EMPLADVANCELRLOANVOUCHERNO` | DECIMAL(15,0) |  |  |  |  |
| 110 | `EMPLOANADVANCECODE` | BIGINT | NOT NULL |  |  |  |
| 111 | `PROPOSALREFNO` | CHAR(20) |  |  |  |  |
| 112 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 113 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 114 | `COMMERCIALINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 115 | `COMMERCIALINVOICECODE` | CHAR(20) |  |  |  |  |
| 116 | `SDCREDITPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 117 | `SDCREDITPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 118 | `DIRECTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 119 | `DIRECTINVOICECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 120 | `DIRECTINVOICECODE` | CHAR(15) |  |  |  |  |
| 121 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 122 | `INVOICEDATE` | DATE |  |  |  |  |
| 123 | `MRNDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 124 | `MRNMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 125 | `MRNCODE` | DECIMAL(11,0) |  |  |  |  |
| 126 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 127 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 128 | `CONSUMPTIONDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 129 | `CONSUMPTIONITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 130 | `CONSUMPTIONBUSINESSAREACODE` | CHAR(50) |  |  |  |  |
| 131 | `CONSUMPTIONSTARTDATE` | DATE |  |  |  |  |
| 132 | `CONSUMPTIONENDDATE` | DATE |  |  |  |  |
| 133 | `CONSUMPTIONLGLWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 134 | `PAYROLLPOSTINGSNO` | BIGINT | NOT NULL |  |  |  |
| 135 | `PAYROLLPOSTINGPAYROLLCODE` | CHAR(3) |  |  |  |  |
| 136 | `PAYROLLPOSTINGPROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 137 | `INTERNALORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 138 | `INTERNALORDERCODE` | CHAR(15) |  |  |  |  |
| 139 | `RG23IIAEXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 140 | `RG23IIAEXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 141 | `RG23IIACODE` | CHAR(15) |  |  |  |  |
| 142 | `RG23IICEXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 143 | `RG23IICEXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 144 | `RG23IICCODE` | CHAR(15) |  |  |  |  |
| 145 | `EXPORTSHIPPINGBILLDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 146 | `EXPORTSHIPPINGBILLCODE` | CHAR(12) |  |  |  |  |
| 147 | `MRNINVOICENO` | CHAR(25) |  |  |  |  |
| 148 | `MRNINVOICEDATE` | DATE |  |  |  |  |
| 149 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 150 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 151 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 152 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 153 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 154 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 155 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 156 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 157 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 158 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 159 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 160 | `FINDOCUMENTTEMPDESC` | VARCHAR(200) |  |  |  |  |
| 161 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 162 | `OPTDSEXEMPTIONFROMDATE` | DATE |  |  |  |  |
| 163 | `TDSEXEMPTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 164 | `CREDITAMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 165 | `DIFFERECEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 166 | `DEBITAMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 167 | `DIFFERENCEAMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 168 | `SIXTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 169 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 170 | `SEUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 171 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 172 | `TRANSACTIONREFNO` | CHAR(20) |  |  |  |  |
| 173 | `POPAYMENTREFNO` | CHAR(20) |  |  |  |  |
| 174 | `BUTRANSACTIONNO` | CHAR(20) |  |  |  |  |
| 175 | `EOAEXTERNALOPERATIONCNTCODE` | CHAR(8) |  |  |  |  |
| 176 | `EOAEXTERNALOPERATIONCODE` | CHAR(15) |  |  |  |  |
| 177 | `EOALINENO` | INTEGER | NOT NULL |  |  |  |
| 178 | `PERIODCOSTEVENTCODE` | CHAR(15) |  |  |  |  |
| 179 | `PERIODCOSTWHSACCGROUPCODE` | CHAR(3) |  |  |  |  |
| 180 | `PERCOSTPERPERCALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 181 | `PERCOSTPERPERCALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 182 | `PERIODCOSTPERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 183 | `PERIODCOSTBUSINESSAREACODE` | CHAR(50) |  |  |  |  |
| 184 | `LCDETAILPURDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 185 | `LCDETAILPURLCNO` | CHAR(35) |  |  |  |  |
| 186 | `LCDETAILPURLCDATE` | DATE |  |  |  |  |
| 187 | `LCAMDPURREGLCDLTPURDIVISIONCOD` | CHAR(3) |  |  |  |  |
| 188 | `LCAMDPURREGLCDETAILPURLCNO` | CHAR(35) |  |  |  |  |
| 189 | `LCAMDPURREGLCDETAILPURLCDATE` | DATE |  |  |  |  |
| 190 | `LCAMDPURREGLCAMENDMENTNO` | DECIMAL(2,0) |  |  |  |  |
| 191 | `LCCANCELPURLCDLTPURCMYCODE` | CHAR(3) |  |  |  |  |
| 192 | `LCCANCELPURLCDLTPURDIVISIONCOD` | CHAR(3) |  |  |  |  |
| 193 | `LCCANCELPURLCDETAILPURLCNO` | CHAR(35) |  |  |  |  |
| 194 | `LCCANCELPURLCDETAILPURLCDATE` | DATE |  |  |  |  |
| 195 | `LCCANCELPURLINENUMBER` | DECIMAL(18,5) |  |  |  |  |
| 196 | `IMPFCPAYMENTCODE` | CHAR(5) |  |  |  |  |
| 197 | `PCLETTERNO` | CHAR(5) |  |  |  |  |
| 198 | `FCFCNO` | CHAR(10) |  |  |  |  |
| 199 | `FCCFCNO` | CHAR(10) |  |  |  |  |
| 200 | `IFCCODE` | CHAR(5) |  |  |  |  |
| 201 | `NESFINEXPNEXTFINEXPNCODE` | CHAR(10) |  |  |  |  |
| 202 | `NESFINEXPNEXTEBANKREFNO` | CHAR(15) |  |  |  |  |
| 203 | `NESFINEXPNEXTEBANKDATE` | DATE |  |  |  |  |
| 204 | `NESFINEXPNEGOTIATIONEXTLINENO` | INTEGER | NOT NULL |  |  |  |
| 205 | `NESINTERESTGLCODE` | CHAR(20) |  |  |  |  |
| 206 | `NEFINEXPNEGOTIATIONCODE` | CHAR(10) |  |  |  |  |
| 207 | `NEEXTENSIONBANKREFNO` | CHAR(15) |  |  |  |  |
| 208 | `NEEXTENSIONBANKDATE` | DATE |  |  |  |  |
| 209 | `NELINENO` | INTEGER | NOT NULL |  |  |  |
| 210 | `NSFINEXPNEGOTIATIONCODE` | CHAR(10) |  |  |  |  |
| 211 | `NSINTERESTGLCODE` | CHAR(20) |  |  |  |  |
| 212 | `NGNCODE` | CHAR(10) |  |  |  |  |
| 213 | `RNCODE` | CHAR(15) |  |  |  |  |
| 214 | `BAACODE` | CHAR(5) |  |  |  |  |
| 215 | `BACODE` | CHAR(10) |  |  |  |  |
| 216 | `EACODE` | CHAR(5) |  |  |  |  |
| 217 | `LDISBURSEMENTSLTEUGENGRPTECOD` | CHAR(3) |  |  |  |  |
| 218 | `LOANDISBURSEMENTSLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 219 | `LOANDISBURSEMENTSCODELOANNO` | CHAR(10) |  |  |  |  |
| 220 | `LOANDISBURSEMENTSSLNO` | INTEGER | NOT NULL |  |  |  |
| 221 | `LOANREPAYMENTBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 222 | `LOANREPAYMENTFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 223 | `LRLTEUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 224 | `LOANREPAYMENTLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 225 | `LOANREPAYMENTCODELOANNO` | CHAR(10) |  |  |  |  |
| 226 | `LOANREPAYMENTREPAYMENTDATE` | DATE |  |  |  |  |
| 227 | `LOANREPAYMENTSLNO` | INTEGER | NOT NULL |  |  |  |
| 228 | `LCAPSUBSIDYLTEUGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 229 | `LOANCAPITALSUBSIDYLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 230 | `LOANCAPITALSUBSIDYCODELOANNO` | CHAR(10) |  |  |  |  |
| 231 | `LOANCAPITALSUBSIDYSLNO` | INTEGER | NOT NULL |  |  |  |
| 232 | `LNINTSUBSIDYLTEUGENGRPTECODE` | CHAR(3) |  |  |  |  |
| 233 | `LNINTSUBSIDYLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 234 | `LNINTSUBSIDYCODELOANNO` | CHAR(10) |  |  |  |  |
| 235 | `LNINTSUBSIDYSLNO` | INTEGER | NOT NULL |  |  |  |
| 236 | `DIGITALSIGNATURE` | CLOB(1000000) |  |  |  |  |
| 237 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 238 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 239 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 240 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 241 | `EXPORTSHIPPINGEDIDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 242 | `EXPORTSHIPPINGEDICODE` | CHAR(12) |  |  |  |  |
| 243 | `EXPORTSHPFOCUSDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 244 | `EXPORTSHIPPINGFOCUSCODE` | CHAR(12) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINDOCUMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.DIRECTENTRY,
       t.FINANCIALYEARCODE,
       t.DOCUMENTTEMPLATECODE,
       t.FINANCEMONTHCODE,
       t.CODE,
       t.DOCUMENTTYPECODE,
       t.REVALUATIONBUSINESSUNITCODE,
       t.REVALUATIONFINANCIALYEARCODE,
       t.REVALUATIONREVALUATIONDATE
FROM   DB2ADMIN.FINDOCUMENTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
