# DB2ADMIN.FINBUDGETBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`
- **Columns**: 32
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 225087

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 4 | `FINANCEMONTHCODE` | INTEGER | NOT NULL |  |  |  |
| 5 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 6 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 7 | `COSTCENTERDESC` | CHAR(100) |  |  |  |  |
| 8 | `GLCODE` | CHAR(20) |  |  |  |  |
| 9 | `GLCODEDESC` | CHAR(100) |  |  |  |  |
| 10 | `COSTBUDGETCODE` | CHAR(4) |  |  |  |  |
| 11 | `AMOUNTBC` | DECIMAL(18,5) |  |  |  |  |
| 12 | `AMOUNTEC` | DECIMAL(28,15) |  |  |  |  |
| 13 | `AMOUNTCC` | DECIMAL(18,5) |  |  |  |  |
| 14 | `REMARKS` | CHAR(100) |  |  |  |  |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 17 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 20 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 21 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 22 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 23 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 24 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 26 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 28 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 29 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 30 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 31 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINBUDGETBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FINANCIALYEARCODE,
       t.FINANCEMONTHCODE,
       t.PROFITCENTERPROFITCENTERCODE,
       t.COSTCENTERCOSTCENTERCODE,
       t.COSTCENTERDESC,
       t.GLCODE,
       t.GLCODEDESC,
       t.COSTBUDGETCODE,
       t.AMOUNTBC
FROM   DB2ADMIN.FINBUDGETBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
