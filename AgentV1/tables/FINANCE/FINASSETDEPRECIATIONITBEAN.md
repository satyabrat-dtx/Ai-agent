# DB2ADMIN.FINASSETDEPRECIATIONITBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`
- **Columns**: 23
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239397

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `FINBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `FINASSETCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `FINASSETCODE` | CHAR(15) |  |  |  |  |
| 5 | `FINYEARTODATE` | DATE |  |  |  |  |
| 6 | `ADDITIONALFLAG` | CHAR(1) |  |  |  |  |
| 7 | `FINMAINASSETBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 8 | `FINMAINASSETASSETUGENGRPTECOD` | CHAR(3) |  |  |  |  |
| 9 | `FINMAINASSETASSETCODE` | CHAR(10) |  |  |  |  |
| 10 | `FINMAINASSETCODE` | CHAR(15) |  |  |  |  |
| 11 | `DEPRECIATIONAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 13 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 14 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 15 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 17 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 18 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 19 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 21 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 22 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINASSETDEPRECIATIONITBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.FINBUSINESSUNITCODE,
       t.FINASSETCOUNTERCODE,
       t.FINASSETCODE,
       t.FINYEARTODATE,
       t.ADDITIONALFLAG,
       t.FINMAINASSETBUSINESSUNITCODE,
       t.FINMAINASSETASSETUGENGRPTECOD,
       t.FINMAINASSETASSETCODE,
       t.FINMAINASSETCODE,
       t.DEPRECIATIONAMOUNT
FROM   DB2ADMIN.FINASSETDEPRECIATIONITBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
