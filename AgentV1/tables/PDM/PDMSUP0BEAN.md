# DB2ADMIN.PDMSUP0BEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `staging_mirror`
- **Columns**: 35
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 49242

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `AFRECTYCODE` | CHAR(3) |  |  |  |  |
| 3 | `AFTPREC` | DECIMAL(1,0) |  |  |  |  |
| 4 | `AFCITEM` | CHAR(15) |  |  |  |  |
| 5 | `AFVERNR` | CHAR(3) |  |  |  |  |
| 6 | `AFVERST` | DECIMAL(3,0) |  |  |  |  |
| 7 | `CSTSUPPCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 8 | `CSTSUPPCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 9 | `AFARTCD` | CHAR(50) |  |  |  |  |
| 10 | `AFARTDS` | CHAR(50) |  |  |  |  |
| 11 | `AFFLUSE` | CHAR(1) |  |  |  |  |
| 12 | `AFFLFAV` | CHAR(1) |  |  |  |  |
| 13 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 14 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 15 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 25 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 26 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 28 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 29 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 30 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 31 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 32 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 33 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 34 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PDMSUP0BEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.AFRECTYCODE,
       t.AFTPREC,
       t.AFCITEM,
       t.AFVERNR,
       t.AFVERST,
       t.CSTSUPPCUSTOMERSUPPLIERTYPE,
       t.CSTSUPPCUSTOMERSUPPLIERCODE,
       t.AFARTCD,
       t.AFARTDS,
       t.AFFLUSE
FROM   DB2ADMIN.PDMSUP0BEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
