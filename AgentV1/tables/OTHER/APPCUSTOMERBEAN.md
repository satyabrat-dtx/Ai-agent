# DB2ADMIN.APPCUSTOMERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 41
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 114584

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `CUSTOMERID` | CHAR(5) |  |  |  |  |
| 4 | `CUSTOMERNAME` | VARCHAR(100) |  |  |  |  |
| 5 | `CURRENCYCODE` | CHAR(10) |  |  |  |  |
| 6 | `CREATEDBYCODE` | CHAR(3) |  |  |  |  |
| 7 | `CUSTOMERCARDIMAGE` | BLOB(1000000) |  |  |  |  |
| 8 | `CUSTOMERCARDMIMETYPE` | CHAR(10) |  |  |  |  |
| 9 | `ADDRESSEE` | VARCHAR(100) |  |  |  |  |
| 10 | `ADDRESSLINE1` | VARCHAR(100) |  |  |  |  |
| 11 | `ADDRESSLINE2` | VARCHAR(100) |  |  |  |  |
| 12 | `ADDRESSLINE3` | VARCHAR(100) |  |  |  |  |
| 13 | `ADDRESSLINE4` | VARCHAR(100) |  |  |  |  |
| 14 | `ADDRESSLINE5` | VARCHAR(100) |  |  |  |  |
| 15 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 16 | `TOWN` | VARCHAR(100) |  |  |  |  |
| 17 | `COUNTRYNAME` | VARCHAR(100) |  |  |  |  |
| 18 | `DISTRICT` | VARCHAR(100) |  |  |  |  |
| 19 | `ADDRESSPHONENUMBER` | VARCHAR(40) |  |  |  |  |
| 20 | `ADDRESSFAXNUMBER` | VARCHAR(40) |  |  |  |  |
| 21 | `EMAILADDRESS` | VARCHAR(100) |  |  |  |  |
| 22 | `BUSINESSCARD` | CHAR(1) |  |  |  |  |
| 23 | `DIRTYFLAG` | SMALLINT | NOT NULL |  |  |  |
| 24 | `ORDERPARTNERUPDATED` | SMALLINT | NOT NULL |  |  |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 29 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 30 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 31 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |
| 32 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 33 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 34 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 35 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 36 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 37 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 38 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 39 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 40 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.OPERATIONTYPE,
       t.COMPANYCODE,
       t.CUSTOMERID,
       t.CUSTOMERNAME,
       t.CURRENCYCODE,
       t.CREATEDBYCODE,
       t.CUSTOMERCARDIMAGE,
       t.CUSTOMERCARDMIMETYPE,
       t.ADDRESSEE,
       t.ADDRESSLINE1,
       t.ADDRESSLINE2
FROM   DB2ADMIN.APPCUSTOMERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
