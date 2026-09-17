# DB2ADMIN.EMPLOYEEEDUCATIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `HR` (high confidence — table name starts with 'EMPLOYEE')
- **Roles**: `staging_mirror`
- **Columns**: 29
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 172133

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 3 | `EDUCATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 4 | `EDUCATIONCODE` | CHAR(6) |  |  |  |  |
| 5 | `EDUCATIONTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 6 | `EDUCATIONTYPECODE` | CHAR(6) |  |  |  |  |
| 7 | `DURATION` | DECIMAL(5,0) |  |  |  |  |
| 8 | `EDUCATIONINSTITUTEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 9 | `EDUCATIONINSTITUTECODE` | CHAR(6) |  |  |  |  |
| 10 | `COUNTRYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 11 | `COUNTRYCODE` | CHAR(6) |  |  |  |  |
| 12 | `STATECODE` | CHAR(3) |  |  |  |  |
| 13 | `DISTRICTDISTRICTCODE` | CHAR(3) |  |  |  |  |
| 14 | `INSTITUTIONLOCATIONCODE` | CHAR(3) |  |  |  |  |
| 15 | `YEAROFPASSING` | DECIMAL(5,0) |  |  |  |  |
| 16 | `MARKSGRADE` | CHAR(50) |  |  |  |  |
| 17 | `REQUESTFLAG` | INTEGER | NOT NULL |  |  |  |
| 18 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 19 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 21 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 23 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 25 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 27 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 28 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPLOYEEEDUCATIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.EDUCATIONICSTABLECODE,
       t.EDUCATIONCODE,
       t.EDUCATIONTYPEICSTABLECODE,
       t.EDUCATIONTYPECODE,
       t.DURATION,
       t.EDUCATIONINSTITUTEICSTABLECODE,
       t.EDUCATIONINSTITUTECODE,
       t.COUNTRYICSTABLECODE,
       t.COUNTRYCODE
FROM   DB2ADMIN.EMPLOYEEEDUCATIONBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
