# DB2ADMIN.INVESTMENTDECENTRYBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 40
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 173235

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `FINANCIALYEARCODE` | CHAR(6) |  |  |  |  |
| 3 | `EMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 4 | `GROUPCODE` | CHAR(10) |  |  |  |  |
| 5 | `GROUPITEMCODE` | CHAR(10) |  |  |  |  |
| 6 | `ITEMPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 7 | `ITEMMAXAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 8 | `DECLAREDAMT` | DECIMAL(17,2) |  |  |  |  |
| 9 | `DECLAREDDATE` | DATE |  |  |  |  |
| 10 | `ACTUALAMT` | DECIMAL(17,2) |  |  |  |  |
| 11 | `AUTHORIZEDFLAG` | INTEGER | NOT NULL |  |  |  |
| 12 | `REQUESTDATE` | DATE |  |  |  |  |
| 13 | `APPROVEDBYCODE` | CHAR(9) |  |  |  |  |
| 14 | `APPROVEDDATE` | DATE |  |  |  |  |
| 15 | `REQPENDINGWITH` | CHAR(10) |  |  |  |  |
| 16 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 24 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 26 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 27 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 28 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 29 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 30 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 31 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 33 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 34 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 35 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 36 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 37 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 38 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 39 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INVESTMENTDECENTRYBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.FINANCIALYEARCODE,
       t.EMPLOYEEIDCODE,
       t.GROUPCODE,
       t.GROUPITEMCODE,
       t.ITEMPERCENTAGE,
       t.ITEMMAXAMOUNT,
       t.DECLAREDAMT,
       t.DECLAREDDATE,
       t.ACTUALAMT,
       t.AUTHORIZEDFLAG
FROM   DB2ADMIN.INVESTMENTDECENTRYBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
