# DB2ADMIN.SHIPMENTEXCHANGERATEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 27
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 148234

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 3 | `EFFECTIVEFROMDATE` | DATE |  |  |  |  |
| 4 | `PURCHASERATE` | DECIMAL(28,15) |  |  |  |  |
| 5 | `SALESRATE` | DECIMAL(28,15) |  |  |  |  |
| 6 | `DECIMALPOINT` | INTEGER | NOT NULL |  |  |  |
| 7 | `ROUNDOFF` | INTEGER | NOT NULL |  |  |  |
| 8 | `NUMBEROFDECIMALS` | INTEGER | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 11 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 14 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 15 | `FLAG` | CHAR(12) |  |  |  |  |
| 16 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 17 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |
| 18 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 19 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 21 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 23 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 25 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 26 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SHIPMENTEXCHANGERATEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CURRENCYCODE,
       t.EFFECTIVEFROMDATE,
       t.PURCHASERATE,
       t.SALESRATE,
       t.DECIMALPOINT,
       t.ROUNDOFF,
       t.NUMBEROFDECIMALS,
       t.CREATIONDATETIMEUTC,
       t.CREATIONDATETIMECMPDIV,
       t.CREATIONDATETIMEUSER
FROM   DB2ADMIN.SHIPMENTEXCHANGERATEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
