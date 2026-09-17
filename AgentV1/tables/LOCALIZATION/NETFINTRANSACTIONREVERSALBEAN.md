# DB2ADMIN.NETFINTRANSACTIONREVERSALBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `staging_mirror`
- **Columns**: 15
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 201284

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `REFFINDOCCODE` | CHAR(15) |  |  |  |  |
| 3 | `READFLAG` | SMALLINT | NOT NULL |  |  |  |
| 4 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 5 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 6 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 7 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 8 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 9 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 10 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 11 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 12 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 13 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 14 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETFINTRNREVERSALBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.REFFINDOCCODE,
       t.READFLAG,
       t.WSOPERATION,
       t.IMPOPERATIONUSER,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER,
       t.IMPLASTUPDATEDATETIME,
       t.IMPLASTUPDATEUSER,
       t.IMPORTDATETIME
FROM   DB2ADMIN.NETFINTRANSACTIONREVERSALBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
