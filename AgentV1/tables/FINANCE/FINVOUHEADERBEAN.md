# DB2ADMIN.FINVOUHEADERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`
- **Columns**: 69
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 99124

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `INTERNALVOUCHERCODE` | DECIMAL(15,0) |  |  |  |  |
| 4 | `VOUCHERTEMPLATECODE` | CHAR(5) |  |  |  |  |
| 5 | `VOUCHERENTRYTYPE` | CHAR(2) |  |  |  |  |
| 6 | `POSTINGDATE` | DATE |  |  |  |  |
| 7 | `VOUCHERDATE` | DATE |  |  |  |  |
| 8 | `VOUCHERNUMBER` | CHAR(20) |  |  |  |  |
| 9 | `EXTERNALVOUCHERDATE` | DATE |  |  |  |  |
| 10 | `EXTERNALVOUCHERNUMBER` | CHAR(20) |  |  |  |  |
| 11 | `AMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 12 | `DEBITCREDITINDICATOR` | CHAR(1) |  |  |  |  |
| 13 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 14 | `EXCHANGERATE` | DECIMAL(15,7) |  |  |  |  |
| 15 | `AMOUNTCURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 16 | `NETGROSS` | CHAR(1) |  |  |  |  |
| 17 | `JOURNALNOTEKEYSTDTABLECODE` | CHAR(5) |  |  |  |  |
| 18 | `JOURNALNOTEKEYCODE` | CHAR(10) |  |  |  |  |
| 19 | `JOURNALNOTE` | CHAR(50) |  |  |  |  |
| 20 | `JOURNALNOTELONG` | VARCHAR(140) |  |  |  |  |
| 21 | `POSTIMMEDIATE` | SMALLINT | NOT NULL |  |  |  |
| 22 | `VOUCHERSTATUS` | CHAR(2) |  |  |  |  |
| 23 | `NOWTRNNUMBERTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 24 | `TAXPOINTDATE` | DATE |  |  |  |  |
| 25 | `SALESTAXIDENTIFICATION` | CHAR(20) |  |  |  |  |
| 26 | `TAXNUMBER` | CHAR(20) |  |  |  |  |
| 27 | `NOTAXRELEVANCE` | SMALLINT | NOT NULL |  |  |  |
| 28 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 29 | `VALUEDATE` | DATE |  |  |  |  |
| 30 | `DISCOUNTABLEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 31 | `PAYMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 32 | `OPENITEMTEXTKEYSTDTABLECODE` | CHAR(5) |  |  |  |  |
| 33 | `OPENITEMTEXTKEYCODE` | CHAR(10) |  |  |  |  |
| 34 | `OPENITEMTEXT` | CHAR(50) |  |  |  |  |
| 35 | `OPENITEMTEXTLONG` | VARCHAR(140) |  |  |  |  |
| 36 | `POSTINGPERIOD` | INTEGER | NOT NULL |  |  |  |
| 37 | `POSTINGYEAR` | DECIMAL(4,0) |  |  |  |  |
| 38 | `MARKSHORTFISCALYEAR` | CHAR(1) |  |  |  |  |
| 39 | `GLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 40 | `VALUATIONBASE` | DATE |  |  |  |  |
| 41 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 42 | `REFERENCEDATE` | DATE |  |  |  |  |
| 43 | `REFERENCENUMBER` | CHAR(20) |  |  |  |  |
| 44 | `ADVANCEPAYMENTREFERENCENUMBER` | CHAR(20) |  |  |  |  |
| 45 | `ADVICENOTE` | CHAR(20) |  |  |  |  |
| 46 | `CLOSINGINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 47 | `BARCODE` | CHAR(30) |  |  |  |  |
| 48 | `ACCOUNTSTATEMENTNUMBER` | CHAR(10) |  |  |  |  |
| 49 | `JOURNALCODE` | CHAR(10) |  |  |  |  |
| 50 | `INFOTYPECODE` | CHAR(2) |  |  |  |  |
| 51 | `ORDERPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 52 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 53 | `CLEARINGNUMBER` | DECIMAL(15,0) |  |  |  |  |
| 54 | `VOUCHERSOURCE` | CHAR(10) |  |  |  |  |
| 55 | `BALANCEVOUCHER` | DECIMAL(17,2) |  |  |  |  |
| 56 | `MARKCHECKOUTSIDEIMPORT` | SMALLINT | NOT NULL |  |  |  |
| 57 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 58 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 59 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 60 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 61 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 62 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 63 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 64 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 65 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 66 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 67 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 68 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.INTERNALVOUCHERCODE,
       t.VOUCHERTEMPLATECODE,
       t.VOUCHERENTRYTYPE,
       t.POSTINGDATE,
       t.VOUCHERDATE,
       t.VOUCHERNUMBER,
       t.EXTERNALVOUCHERDATE,
       t.EXTERNALVOUCHERNUMBER,
       t.AMOUNT
FROM   DB2ADMIN.FINVOUHEADERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
