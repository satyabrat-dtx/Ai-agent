# DB2ADMIN.LOANREQUESTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 37
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 173498

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `LOANFOR` | INTEGER | NOT NULL |  |  |  |
| 4 | `EMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 5 | `LOANTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `LOANCODE` | CHAR(4) |  |  |  |  |
| 7 | `LOANVOUCHERNO` | DECIMAL(15,0) |  |  |  |  |
| 8 | `OLDLOANVOUCHERNO` | DECIMAL(15,0) |  |  |  |  |
| 9 | `GAURENTEERIDCODE` | CHAR(9) |  |  |  |  |
| 10 | `GAURENTEERID2CODE` | CHAR(9) |  |  |  |  |
| 11 | `REQUESTEDAMOUNT` | DECIMAL(11,2) |  |  |  |  |
| 12 | `REQUESTEDDATE` | DATE |  |  |  |  |
| 13 | `SANCTIONEDAMOUNT` | DECIMAL(11,2) |  |  |  |  |
| 14 | `SANCTIONEDDATE` | DATE |  |  |  |  |
| 15 | `APPROVEDBYCODE` | CHAR(9) |  |  |  |  |
| 16 | `APPROVEDESC` | CHAR(100) |  |  |  |  |
| 17 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 18 | `SERVICESTATUS` | VARCHAR(100) |  |  |  |  |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 21 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 24 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 25 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 26 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 27 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 28 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 29 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 30 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 31 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 32 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 33 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 34 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 35 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 36 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOANREQUESTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.LOANFOR,
       t.EMPLOYEEIDCODE,
       t.LOANTYPE,
       t.LOANCODE,
       t.LOANVOUCHERNO,
       t.OLDLOANVOUCHERNO,
       t.GAURENTEERIDCODE,
       t.GAURENTEERID2CODE,
       t.REQUESTEDAMOUNT
FROM   DB2ADMIN.LOANREQUESTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
