# DB2ADMIN.EMPLOYEENOMINATIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `HR` (high confidence — table name starts with 'EMPLOYEE')
- **Roles**: `staging_mirror`
- **Columns**: 24
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 172663

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 3 | `RELATIONSHIPRLTEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 4 | `RELATIONSHIPRELATIONTYPECODE` | CHAR(6) |  |  |  |  |
| 5 | `NOMINATIONTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 6 | `NOMINATIONTYPECODE` | CHAR(6) |  |  |  |  |
| 7 | `RELATIONNAME` | VARCHAR(200) |  |  |  |  |
| 8 | `AGE` | DECIMAL(2,0) |  |  |  |  |
| 9 | `DATEOFBIRTH` | DATE |  |  |  |  |
| 10 | `NOMINATION` | DECIMAL(5,2) |  |  |  |  |
| 11 | `REMARKS` | CHAR(100) |  |  |  |  |
| 12 | `REQUESTFLAG` | INTEGER | NOT NULL |  |  |  |
| 13 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 14 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 15 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 16 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 18 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 22 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 23 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPLOYEENOMINATIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.RELATIONSHIPRLTEICSTABLECODE,
       t.RELATIONSHIPRELATIONTYPECODE,
       t.NOMINATIONTYPEICSTABLECODE,
       t.NOMINATIONTYPECODE,
       t.RELATIONNAME,
       t.AGE,
       t.DATEOFBIRTH,
       t.NOMINATION,
       t.REMARKS
FROM   DB2ADMIN.EMPLOYEENOMINATIONBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
