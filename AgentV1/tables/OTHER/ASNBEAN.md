# DB2ADMIN.ASNBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 39
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 110986

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `PURORDPURORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `PURCHASEORDERPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `PURCHASEORDERORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 6 | `PURCHASEORDERORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 7 | `LINENO` | DECIMAL(3,0) |  |  |  |  |
| 8 | `PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 10 | `LOT` | CHAR(35) |  |  |  |  |
| 11 | `QUALITY` | DECIMAL(5,0) |  |  |  |  |
| 12 | `SUPPLIERLOTCODE` | CHAR(35) |  |  |  |  |
| 13 | `ZONE` | CHAR(3) |  |  |  |  |
| 14 | `LOCATION` | CHAR(10) |  |  |  |  |
| 15 | `CNRITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `CNRSUBCODE01` | CHAR(20) |  |  |  |  |
| 17 | `CNRELEMENT` | CHAR(15) |  |  |  |  |
| 18 | `WEIGHTUOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `GROSS` | DECIMAL(18,5) |  |  |  |  |
| 20 | `NET` | DECIMAL(18,5) |  |  |  |  |
| 21 | `REALNET` | DECIMAL(18,5) |  |  |  |  |
| 22 | `RECEIVINGDOCUMENTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 23 | `RECEIVINGDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 24 | `ASNCODE` | CHAR(15) |  |  |  |  |
| 25 | `ASNDATE` | DATE |  |  |  |  |
| 26 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 27 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 28 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 29 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 30 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 31 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 32 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 33 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 34 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 35 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 36 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 37 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 38 | `ADDITIONALDATA` | BLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ASNBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.PURORDPURORDERCOUNTERCODE,
       t.PURCHASEORDERPURCHASEORDERCODE,
       t.PURCHASEORDERORDERLINE,
       t.PURCHASEORDERORDERSUBLINE,
       t.LINENO,
       t.PRIMARYQUANTITY,
       t.UOMCODE,
       t.LOT,
       t.QUALITY
FROM   DB2ADMIN.ASNBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
