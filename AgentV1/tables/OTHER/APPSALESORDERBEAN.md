# DB2ADMIN.APPSALESORDERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 33
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 114644

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ORDERID` | CHAR(50) |  |  |  |  |
| 3 | `CREATEDBY` | CHAR(5) |  |  |  |  |
| 4 | `CURRENCY` | CHAR(10) |  |  |  |  |
| 5 | `ORDERTERMS` | CHAR(100) |  |  |  |  |
| 6 | `EXPDELIVERYDATE` | DATE |  |  |  |  |
| 7 | `ORDERDATE` | DATE |  |  |  |  |
| 8 | `TEMPLATESALESORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 9 | `COMMENTS` | CLOB(1000000) |  |  |  |  |
| 10 | `CUSTOMERID` | CHAR(10) |  |  |  |  |
| 11 | `COMMENTS1` | CHAR(1) |  |  |  |  |
| 12 | `COMMENTS2` | CHAR(1) |  |  |  |  |
| 13 | `COMMENTSIMAGE1` | BLOB(1000000) |  |  |  |  |
| 14 | `COMMENTSIMAGE2` | BLOB(1000000) |  |  |  |  |
| 15 | `DIRTYFLAG` | SMALLINT | NOT NULL |  |  |  |
| 16 | `SALESORDERUPDATED` | SMALLINT | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 21 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 22 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 23 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |
| 24 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 25 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 27 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 29 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 31 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 32 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.ORDERID,
       t.CREATEDBY,
       t.CURRENCY,
       t.ORDERTERMS,
       t.EXPDELIVERYDATE,
       t.ORDERDATE,
       t.TEMPLATESALESORDERTEMPLATECODE,
       t.COMMENTS,
       t.CUSTOMERID,
       t.COMMENTS1
FROM   DB2ADMIN.APPSALESORDERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
