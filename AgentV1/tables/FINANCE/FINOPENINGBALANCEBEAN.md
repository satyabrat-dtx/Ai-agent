# DB2ADMIN.FINOPENINGBALANCEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`
- **Columns**: 147
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181591

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 4 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `FINANCEMONTHCODE` | INTEGER | NOT NULL |  |  |  |
| 6 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 7 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 8 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 9 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `GLCODE` | CHAR(20) |  |  |  |  |
| 12 | `FINANCEDOCUMENTDATE` | DATE |  |  |  |  |
| 13 | `POSTINGDATE` | DATE |  |  |  |  |
| 14 | `DUEDATE` | DATE |  |  |  |  |
| 15 | `FLAGDRCR` | INTEGER | NOT NULL |  |  |  |
| 16 | `DOCUMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 17 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 18 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 19 | `ASSETCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 20 | `ASSETCODE` | CHAR(15) |  |  |  |  |
| 21 | `REFERENCETEXT1` | CHAR(100) |  |  |  |  |
| 22 | `FIRSTUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 24 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 25 | `THIRDUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 26 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 27 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 28 | `FIFTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 29 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 30 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 31 | `PROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 32 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 33 | `MRNINVOICENO` | CHAR(25) |  |  |  |  |
| 34 | `MRNINVOICEDATE` | DATE |  |  |  |  |
| 35 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 36 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 37 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 38 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 39 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 40 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 41 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 42 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 43 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 44 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 45 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 46 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 47 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 48 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 49 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 50 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 51 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 52 | `DIRECTENTRY` | SMALLINT | NOT NULL |  |  |  |
| 53 | `SNDUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 54 | `FRUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 55 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 56 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 57 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 58 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 59 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 60 | `PROPOSALREFNO` | CHAR(20) |  |  |  |  |
| 61 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 62 | `INVOICEDATE` | DATE |  |  |  |  |
| 63 | `FINDOCUMENTTEMPDESC` | VARCHAR(200) |  |  |  |  |
| 64 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 65 | `TDSEXEMPTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 66 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 67 | `CREDITAMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 68 | `DIFFERECEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 69 | `DEBITAMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 70 | `DIFFERENCEAMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 71 | `SIXTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 72 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 73 | `SEUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 74 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 75 | `TRANSACTIONREFNO` | CHAR(20) |  |  |  |  |
| 76 | `POPAYMENTREFNO` | CHAR(20) |  |  |  |  |
| 77 | `BUTRANSACTIONNO` | CHAR(20) |  |  |  |  |
| 78 | `EOAEXTERNALOPERATIONCNTCODE` | CHAR(8) |  |  |  |  |
| 79 | `EOAEXTERNALOPERATIONCODE` | CHAR(15) |  |  |  |  |
| 80 | `EOALINENO` | INTEGER | NOT NULL |  |  |  |
| 81 | `PERIODCOSTEVENTCODE` | CHAR(15) |  |  |  |  |
| 82 | `PERIODCOSTWHSACCGROUPCODE` | CHAR(3) |  |  |  |  |
| 83 | `PERCOSTPERPERCALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 84 | `PERCOSTPERPERCALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 85 | `PERIODCOSTPERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 86 | `PERIODCOSTBUSINESSAREACODE` | CHAR(50) |  |  |  |  |
| 87 | `LCDETAILPURDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 88 | `LCDETAILPURLCNO` | CHAR(35) |  |  |  |  |
| 89 | `LCDETAILPURLCDATE` | DATE |  |  |  |  |
| 90 | `LCAMDPURREGLCDLTPURDIVISIONCOD` | CHAR(3) |  |  |  |  |
| 91 | `LCAMDPURREGLCDETAILPURLCNO` | CHAR(35) |  |  |  |  |
| 92 | `LCAMDPURREGLCDETAILPURLCDATE` | DATE |  |  |  |  |
| 93 | `LCAMDPURREGLCAMENDMENTNO` | DECIMAL(2,0) |  |  |  |  |
| 94 | `LCCANCELPURLCDLTPURCMYCODE` | CHAR(3) |  |  |  |  |
| 95 | `LCCANCELPURLCDLTPURDIVISIONCOD` | CHAR(3) |  |  |  |  |
| 96 | `LCCANCELPURLCDETAILPURLCNO` | CHAR(35) |  |  |  |  |
| 97 | `LCCANCELPURLCDETAILPURLCDATE` | DATE |  |  |  |  |
| 98 | `LCCANCELPURLINENUMBER` | DECIMAL(18,5) |  |  |  |  |
| 99 | `IMPFCPAYMENTCODE` | CHAR(5) |  |  |  |  |
| 100 | `PCLETTERNO` | CHAR(5) |  |  |  |  |
| 101 | `FCFCNO` | CHAR(10) |  |  |  |  |
| 102 | `FCCFCNO` | CHAR(10) |  |  |  |  |
| 103 | `IFCCODE` | CHAR(5) |  |  |  |  |
| 104 | `NESFINEXPNEXTFINEXPNCODE` | CHAR(10) |  |  |  |  |
| 105 | `NESFINEXPNEXTEBANKREFNO` | CHAR(15) |  |  |  |  |
| 106 | `NESFINEXPNEXTEBANKDATE` | DATE |  |  |  |  |
| 107 | `NESFINEXPNEGOTIATIONEXTLINENO` | INTEGER | NOT NULL |  |  |  |
| 108 | `NESINTERESTGLCODE` | CHAR(20) |  |  |  |  |
| 109 | `NEFINEXPNEGOTIATIONCODE` | CHAR(10) |  |  |  |  |
| 110 | `NEEXTENSIONBANKREFNO` | CHAR(15) |  |  |  |  |
| 111 | `NEEXTENSIONBANKDATE` | DATE |  |  |  |  |
| 112 | `NELINENO` | INTEGER | NOT NULL |  |  |  |
| 113 | `NSFINEXPNEGOTIATIONCODE` | CHAR(10) |  |  |  |  |
| 114 | `NSINTERESTGLCODE` | CHAR(20) |  |  |  |  |
| 115 | `NGNCODE` | CHAR(10) |  |  |  |  |
| 116 | `RNCODE` | CHAR(15) |  |  |  |  |
| 117 | `BAACODE` | CHAR(5) |  |  |  |  |
| 118 | `BACODE` | CHAR(10) |  |  |  |  |
| 119 | `EACODE` | CHAR(5) |  |  |  |  |
| 120 | `LDISBURSEMENTSLTEUGENGRPTECOD` | CHAR(3) |  |  |  |  |
| 121 | `LOANDISBURSEMENTSLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 122 | `LOANDISBURSEMENTSCODELOANNO` | CHAR(10) |  |  |  |  |
| 123 | `LOANDISBURSEMENTSSLNO` | INTEGER | NOT NULL |  |  |  |
| 124 | `LOANREPAYMENTBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 125 | `LOANREPAYMENTFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 126 | `LRLTEUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 127 | `LOANREPAYMENTLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 128 | `LOANREPAYMENTCODELOANNO` | CHAR(10) |  |  |  |  |
| 129 | `LOANREPAYMENTREPAYMENTDATE` | DATE |  |  |  |  |
| 130 | `LOANREPAYMENTSLNO` | INTEGER | NOT NULL |  |  |  |
| 131 | `LCAPSUBSIDYLTEUGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 132 | `LOANCAPITALSUBSIDYLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 133 | `LOANCAPITALSUBSIDYCODELOANNO` | CHAR(10) |  |  |  |  |
| 134 | `LOANCAPITALSUBSIDYSLNO` | INTEGER | NOT NULL |  |  |  |
| 135 | `LNINTSUBSIDYLTEUGENGRPTECODE` | CHAR(3) |  |  |  |  |
| 136 | `LNINTSUBSIDYLOANTYPECODE` | CHAR(10) |  |  |  |  |
| 137 | `LNINTSUBSIDYCODELOANNO` | CHAR(10) |  |  |  |  |
| 138 | `LNINTSUBSIDYSLNO` | INTEGER | NOT NULL |  |  |  |
| 139 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 140 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 141 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 142 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 143 | `EXPORTSHIPPINGEDIDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 144 | `EXPORTSHIPPINGEDICODE` | CHAR(12) |  |  |  |  |
| 145 | `EXPORTSHPFOCUSDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 146 | `EXPORTSHIPPINGFOCUSCODE` | CHAR(12) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINOPENINGBALANCEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FINANCIALYEARCODE,
       t.DOCUMENTTEMPLATECODE,
       t.FINANCEMONTHCODE,
       t.CURRENTSTATUS,
       t.CUSTOMERTYPE,
       t.CUSTOMERCODE,
       t.SUPPLIERTYPE,
       t.SUPPLIERCODE,
       t.GLCODE
FROM   DB2ADMIN.FINOPENINGBALANCEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
