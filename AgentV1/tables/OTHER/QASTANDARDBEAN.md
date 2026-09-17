# DB2ADMIN.QASTANDARDBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 36
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 85905

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `DFTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `GCDGRPUSERGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 15 | `GCDGROUPCODE` | CHAR(10) |  |  |  |  |
| 16 | `GCDCSMCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 17 | `GCDCSMCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 22 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 23 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 24 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 25 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 26 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 27 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 29 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 31 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 33 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 34 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 35 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.DFTITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.QASTANDARDBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
