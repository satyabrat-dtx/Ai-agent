# DB2ADMIN.PDMNOWITEMKEYLINKBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `staging_mirror`
- **Columns**: 29
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 91576

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DBRECTYCODE` | CHAR(3) |  |  |  |  |
| 3 | `DBTPREC` | DECIMAL(1,0) |  |  |  |  |
| 4 | `DBCITEM` | CHAR(15) |  |  |  |  |
| 5 | `DBVERNR` | CHAR(3) |  |  |  |  |
| 6 | `DBVERST` | DECIMAL(3,0) |  |  |  |  |
| 7 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 19 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 20 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 26 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 27 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 28 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PDMNOWITEMKEYLINKBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DBRECTYCODE,
       t.DBTPREC,
       t.DBCITEM,
       t.DBVERNR,
       t.DBVERST,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.PDMNOWITEMKEYLINKBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
