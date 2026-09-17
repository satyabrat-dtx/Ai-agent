# DB2ADMIN.INTERNALPRICELISTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `staging_mirror`
- **Columns**: 18
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 120557

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `AVOIDAUTOCREATIONOFDETAILS` | SMALLINT | NOT NULL |  |  |  |
| 4 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) |  |  |  |  |
| 5 | `COSTSCOSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 6 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 7 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 8 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 9 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 10 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 11 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 12 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 13 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 14 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 15 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 16 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 17 | `ALLWAREHOUSEACCOUNTINGGROUPS` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INTERNALPRICELISTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.AVOIDAUTOCREATIONOFDETAILS,
       t.WAREHOUSEACCOUNTINGGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.WSOPERATION,
       t.IMPOPERATIONUSER,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER,
       t.IMPLASTUPDATEDATETIME
FROM   DB2ADMIN.INTERNALPRICELISTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
