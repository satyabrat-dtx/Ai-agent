# DB2ADMIN.NETFINTRANSACTIONHEADERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `staging_mirror`
- **Columns**: 124
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 218424

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `BUSINESSAREACODE` | CHAR(50) |  |  |  |  |
| 3 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 4 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `EVENTCODE` | CHAR(15) |  |  |  |  |
| 6 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 8 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 10 | `OTHERCUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 11 | `OTHERCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 12 | `OTHERVENDORTYPE` | CHAR(1) |  |  |  |  |
| 13 | `OTHERVENDORCODE` | CHAR(8) |  |  |  |  |
| 14 | `GLCODE` | CHAR(20) |  |  |  |  |
| 15 | `NOTDSAPPLICABLE` | SMALLINT | NOT NULL |  |  |  |
| 16 | `OPTDSTDSTEUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `OPTDSTDSTYPECODE` | CHAR(10) |  |  |  |  |
| 18 | `OPTDSTDSCODE` | CHAR(6) |  |  |  |  |
| 19 | `OPTDSTDSITAXCODE` | CHAR(3) |  |  |  |  |
| 20 | `OPTDSEXEMPTIONFROMDATE` | DATE |  |  |  |  |
| 21 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 22 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 23 | `TDSGLCODE` | CHAR(20) |  |  |  |  |
| 24 | `TDSPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 25 | `FINANCEDOCUMENTDATE` | DATE |  |  |  |  |
| 26 | `POSTINGDATE` | DATE |  |  |  |  |
| 27 | `DUEDATE` | DATE |  |  |  |  |
| 28 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 29 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 30 | `DOCUMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 31 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 32 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 33 | `DOCCOMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 34 | `CUSTOMERREFERENCE` | CHAR(20) |  |  |  |  |
| 35 | `CUSTOMERREFERENCEDATE` | DATE |  |  |  |  |
| 36 | `VENDORREFERENCE` | CHAR(20) |  |  |  |  |
| 37 | `VENDORREFERENCEDATE` | DATE |  |  |  |  |
| 38 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |
| 39 | `REFERENCETEXT2` | CHAR(20) |  |  |  |  |
| 40 | `REFERENCETEXT3` | CHAR(20) |  |  |  |  |
| 41 | `REFERENCETEXT4` | CHAR(20) |  |  |  |  |
| 42 | `REFERENCETEXT5` | CHAR(20) |  |  |  |  |
| 43 | `FIRSTUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 44 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 45 | `SNDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 46 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 47 | `THIRDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 48 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 49 | `FRUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 50 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 51 | `FIFTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 52 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 53 | `REFERENCEAMT1` | DECIMAL(18,5) |  |  |  |  |
| 54 | `REFERENCEAMT2` | DECIMAL(18,5) |  |  |  |  |
| 55 | `REFERENCEAMT3` | DECIMAL(18,5) |  |  |  |  |
| 56 | `REFERENCEAMT4` | DECIMAL(18,5) |  |  |  |  |
| 57 | `REFERENCEAMT5` | DECIMAL(18,5) |  |  |  |  |
| 58 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 59 | `PURCHASEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 60 | `PURINVORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 61 | `PURINVORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 62 | `PURCHASEINVOICECODE` | CHAR(25) |  |  |  |  |
| 63 | `PURCHASEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 64 | `EXPENSEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 65 | `EXPENSEINVORDPRNCSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 66 | `EXPENSEINVORDPRNCSMSUPCODE` | CHAR(8) |  |  |  |  |
| 67 | `EXPENSEINVOICECODE` | CHAR(25) |  |  |  |  |
| 68 | `EXPENSEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 69 | `MRNREJMDMRNHEADERDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 70 | `MRNREJMDMRNHEADERMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 71 | `MRNREJMDMRNHEADERCODE` | DECIMAL(11,0) |  |  |  |  |
| 72 | `MRNREJMDLINEID` | INTEGER | NOT NULL |  |  |  |
| 73 | `MRNREJREJECTIONLINEID` | INTEGER | NOT NULL |  |  |  |
| 74 | `POADVANCEPURORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 75 | `POADVANCEPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 76 | `POADVANCELINENO` | INTEGER | NOT NULL |  |  |  |
| 77 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 78 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 79 | `COMMERCIALINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 80 | `COMMERCIALINVOICECODE` | CHAR(20) |  |  |  |  |
| 81 | `SDCREDITPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 82 | `SDCREDITPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 83 | `DIRECTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 84 | `DIRECTINVOICECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 85 | `DIRECTINVOICECODE` | CHAR(15) |  |  |  |  |
| 86 | `MRNDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 87 | `MRNMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 88 | `MRNCODE` | DECIMAL(11,0) |  |  |  |  |
| 89 | `QADOCCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 90 | `QADOCCODE` | CHAR(15) |  |  |  |  |
| 91 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 92 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 93 | `CONSUMPTIONDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 94 | `CONSUMPTIONITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 95 | `CONSUMPTIONBUSINESSAREACODE` | CHAR(50) |  |  |  |  |
| 96 | `CONSUMPTIONSTARTDATE` | DATE |  |  |  |  |
| 97 | `CONSUMPTIONENDDATE` | DATE |  |  |  |  |
| 98 | `CONSUMPTIONLGLWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 99 | `INTERNALORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 100 | `INTERNALORDERCODE` | CHAR(15) |  |  |  |  |
| 101 | `EXPORTSHIPPINGBILLDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 102 | `EXPORTSHIPPINGBILLCODE` | CHAR(12) |  |  |  |  |
| 103 | `MRNINVOICENO` | CHAR(25) |  |  |  |  |
| 104 | `MRNINVOICEDATE` | DATE |  |  |  |  |
| 105 | `READFLAG` | SMALLINT | NOT NULL |  |  |  |
| 106 | `POSTINGFLAG` | CHAR(15) |  |  |  |  |
| 107 | `POSTINGMESSAGE` | VARCHAR(1000) |  |  |  |  |
| 108 | `SNO` | BIGINT | NOT NULL |  |  |  |
| 109 | `PAYROLLCODE` | CHAR(3) |  |  |  |  |
| 110 | `PROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 111 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 112 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 113 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 114 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 115 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 116 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 117 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 118 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 119 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 120 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 121 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 122 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 123 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETFINTRNHEADERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.BUSINESSAREACODE,
       t.ENTITYNAME,
       t.CODE,
       t.EVENTCODE,
       t.CUSTOMERTYPE,
       t.CUSTOMERCODE,
       t.SUPPLIERTYPE,
       t.SUPPLIERCODE,
       t.OTHERCUSTOMERTYPE,
       t.OTHERCUSTOMERCODE
FROM   DB2ADMIN.NETFINTRANSACTIONHEADERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
