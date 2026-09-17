# DB2ADMIN.DIRECTINVOICEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 79
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 218806

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `BOOKINGFOR` | CHAR(1) |  |  |  |  |
| 4 | `DOCUMENT` | CHAR(1) |  |  |  |  |
| 5 | `TEMPLATECODE` | CHAR(8) |  |  |  |  |
| 6 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 9 | `DOTPARKINGDATE` | DATE |  |  |  |  |
| 10 | `OPTDSTDSTEUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `OPTDSTDSTYPECODE` | CHAR(10) |  |  |  |  |
| 12 | `OPTDSTDSCODE` | CHAR(6) |  |  |  |  |
| 13 | `OPTDSTDSITAXCODE` | CHAR(3) |  |  |  |  |
| 14 | `OPTDSEXEMPTIONFROMDATE` | DATE |  |  |  |  |
| 15 | `TDSPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 16 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 17 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `TDSEXEMPTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 19 | `TDSGLCODE` | CHAR(20) |  |  |  |  |
| 20 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 21 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 22 | `INVOICEDATE` | DATE |  |  |  |  |
| 23 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 24 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 25 | `PAYMENTTERMCODE` | CHAR(3) |  |  |  |  |
| 26 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 27 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 28 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 29 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 30 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 31 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 32 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 33 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 34 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 35 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 36 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 37 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 38 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 39 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 40 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 41 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 42 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 43 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |
| 44 | `REFERENCETEXT2` | CHAR(20) |  |  |  |  |
| 45 | `REFERENCETEXT3` | CHAR(20) |  |  |  |  |
| 46 | `REFERENCETEXT4` | CHAR(20) |  |  |  |  |
| 47 | `REFERENCETEXT5` | CHAR(20) |  |  |  |  |
| 48 | `FIRSTUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 49 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 50 | `SNDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 51 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 52 | `THIRDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 53 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 54 | `FRUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 55 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 56 | `FIFTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 57 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 58 | `SIXTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 59 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 60 | `SEUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 61 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 62 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 63 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 64 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 65 | `TYPEFOREINVOICE` | CHAR(1) |  |  |  |  |
| 66 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 67 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 68 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 69 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 70 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 71 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 72 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 73 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 74 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 75 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 76 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 77 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 78 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DIRECTINVOICEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.BOOKINGFOR,
       t.DOCUMENT,
       t.TEMPLATECODE,
       t.COUNTERCODE,
       t.CODE,
       t.DOCUMENTDATE,
       t.DOTPARKINGDATE,
       t.OPTDSTDSTEUSGENGROUPTYPECODE,
       t.OPTDSTDSTYPECODE
FROM   DB2ADMIN.DIRECTINVOICEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
