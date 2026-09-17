# DB2ADMIN.PDMAR4BEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `staging_mirror`
- **Columns**: 50
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 58954

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `AZRECTYCODE` | CHAR(3) |  |  |  |  |
| 3 | `AZTPREC` | DECIMAL(1,0) |  |  |  |  |
| 4 | `AZCITEM` | CHAR(15) |  |  |  |  |
| 5 | `AZVERNR` | CHAR(3) |  |  |  |  |
| 6 | `AZVERST` | DECIMAL(3,0) |  |  |  |  |
| 7 | `AZCDSIZ` | CHAR(10) |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 10 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `AZMOLTI` | DECIMAL(7,2) |  |  |  |  |
| 20 | `AZFLUSE` | CHAR(1) |  |  |  |  |
| 21 | `AZPAKTY` | CHAR(10) |  |  |  |  |
| 22 | `AZ_PAKQY` | DECIMAL(9,0) |  |  |  |  |
| 23 | `AZDSC` | CHAR(50) |  |  |  |  |
| 24 | `AZANNUL` | CHAR(1) |  |  |  |  |
| 25 | `AZ_SIZID` | DECIMAL(5,0) |  |  |  |  |
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
| 36 | `AZ_ALFA1` | CHAR(20) |  |  |  |  |
| 37 | `AZ_ALFA2` | CHAR(20) |  |  |  |  |
| 38 | `AZ_ALFA3` | CHAR(20) |  |  |  |  |
| 39 | `AZ_ALFA4` | CHAR(20) |  |  |  |  |
| 40 | `AZ_ALFA5` | CHAR(20) |  |  |  |  |
| 41 | `AZ_NUME1` | DECIMAL(29,9) |  |  |  |  |
| 42 | `AZ_NUME2` | DECIMAL(29,9) |  |  |  |  |
| 43 | `AZ_NUME3` | DECIMAL(29,9) |  |  |  |  |
| 44 | `AZ_NUME4` | DECIMAL(29,9) |  |  |  |  |
| 45 | `AZ_NUME5` | DECIMAL(29,9) |  |  |  |  |
| 46 | `AZ_FLSAM` | CHAR(1) |  |  |  |  |
| 47 | `AZ_PROPO` | DECIMAL(11,2) |  |  |  |  |
| 48 | `AZ_PERCE` | DECIMAL(11,2) |  |  |  |  |
| 49 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PDMAR4BEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.AZRECTYCODE,
       t.AZTPREC,
       t.AZCITEM,
       t.AZVERNR,
       t.AZVERST,
       t.AZCDSIZ,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03
FROM   DB2ADMIN.PDMAR4BEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
