# DB2ADMIN.ADVANCEIBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 69
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 219801

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 3 | `PURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 4 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 5 | `ADUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `ADCODE` | CHAR(10) |  |  |  |  |
| 7 | `SUPPLIERNAME` | VARCHAR(200) |  |  |  |  |
| 8 | `DUEDATE` | DATE |  |  |  |  |
| 9 | `POADVANCEDATE` | DATE |  |  |  |  |
| 10 | `INVOICEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `PAYMENTADVPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 12 | `PAYMENTADVAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 13 | `CASHDISCOUNTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 14 | `NETAMTAFTERDEDUCTION` | DECIMAL(18,5) |  |  |  |  |
| 15 | `UPDATEAMTFLAG` | INTEGER | NOT NULL |  |  |  |
| 16 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 17 | `PAYMENTBY` | INTEGER | NOT NULL |  |  |  |
| 18 | `OLDPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 19 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 20 | `OLDDOCUMENTCURR` | DECIMAL(18,5) |  |  |  |  |
| 21 | `PERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 22 | `CALCULATEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `CALCULATEDVALUER` | DECIMAL(18,5) |  |  |  |  |
| 24 | `DOCCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 25 | `PAYEMENTMADE` | INTEGER | NOT NULL |  |  |  |
| 26 | `POLINE` | CHAR(15) |  |  |  |  |
| 27 | `LCPURDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 28 | `LCPURLCNO` | CHAR(35) |  |  |  |  |
| 29 | `LCPURLCDATE` | DATE |  |  |  |  |
| 30 | `REMARKS` | CHAR(140) |  |  |  |  |
| 31 | `REMARK1` | VARCHAR(200) |  |  |  |  |
| 32 | `REMARK2` | DECIMAL(10,0) |  |  |  |  |
| 33 | `STATUS` | CHAR(1) |  |  |  |  |
| 34 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 35 | `UNDERPROPOSAL` | SMALLINT | NOT NULL |  |  |  |
| 36 | `FLAG` | CHAR(15) |  |  |  |  |
| 37 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 38 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 39 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 40 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 41 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 42 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 43 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 44 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 45 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 46 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 47 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 48 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 49 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 50 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 51 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 52 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 53 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 54 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |
| 55 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 56 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 57 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 58 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 59 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 60 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 61 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 62 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 63 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 64 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 65 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 66 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 67 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 68 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADVANCEIBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.PAYMENTMETHODCODE,
       t.ADUSERGENERICGROUPTYPECODE,
       t.ADCODE,
       t.SUPPLIERNAME,
       t.DUEDATE,
       t.POADVANCEDATE,
       t.INVOICEAMOUNT,
       t.PAYMENTADVPERCENTAGE
FROM   DB2ADMIN.ADVANCEIBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
