# DB2ADMIN.USAACCOUNTINGJOURNALBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `staging_mirror`
- **Columns**: 43
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108191

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `TRANSACTIONNUMBER` | CHAR(16) |  |  |  |  |
| 3 | `DOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 4 | `JOURNALNUM` | CHAR(10) |  |  |  |  |
| 5 | `ACCOUNTTYPE` | CHAR(1) |  |  |  |  |
| 6 | `ACCOUNTNUM` | CHAR(15) |  |  |  |  |
| 7 | `TXD` | CHAR(30) |  |  |  |  |
| 8 | `AMOUNTCURDEBIT` | DECIMAL(17,2) |  |  |  |  |
| 9 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 10 | `EXCHRATE` | DECIMAL(5,0) |  |  |  |  |
| 11 | `COSTCENTER` | CHAR(20) |  |  |  |  |
| 12 | `FINANCIALPARCODE` | CHAR(15) |  |  |  |  |
| 13 | `VOUCHER` | CHAR(12) |  |  |  |  |
| 14 | `AMOUNTCURCREDIT` | DECIMAL(17,2) |  |  |  |  |
| 15 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 16 | `INVOICE` | CHAR(15) |  |  |  |  |
| 17 | `DOCUMENTNUMBER` | CHAR(15) |  |  |  |  |
| 18 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 19 | `PAYMODE` | CHAR(5) |  |  |  |  |
| 20 | `DUEDATE` | DATE |  |  |  |  |
| 21 | `TAXGROUP` | CHAR(50) |  |  |  |  |
| 22 | `TAXITEMGROUP` | CHAR(10) |  |  |  |  |
| 23 | `POSTINGPROFILE` | CHAR(10) |  |  |  |  |
| 24 | `ACCOUNTTYPEOFFSET` | CHAR(1) |  |  |  |  |
| 25 | `ACCOUNTNUMOFFSET` | CHAR(15) |  |  |  |  |
| 26 | `DOCUMENTCLASS` | CHAR(2) |  |  |  |  |
| 27 | `ACCOUNTINGTYPE` | CHAR(2) |  |  |  |  |
| 28 | `PERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 29 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 30 | `ACKDATETIME` | TIMESTAMP |  |  |  |  |
| 31 | `ACKUSER` | CHAR(25) |  |  |  |  |
| 32 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 33 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 34 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 35 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 36 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 37 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 38 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 39 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 40 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 41 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 42 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.TRANSACTIONNUMBER,
       t.DOCUMENTTYPE,
       t.JOURNALNUM,
       t.ACCOUNTTYPE,
       t.ACCOUNTNUM,
       t.TXD,
       t.AMOUNTCURDEBIT,
       t.CURRENCYCODE,
       t.EXCHRATE,
       t.COSTCENTER
FROM   DB2ADMIN.USAACCOUNTINGJOURNALBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
