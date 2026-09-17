# DB2ADMIN.EMPLOYEEADDRESSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `HR` (high confidence — table name starts with 'EMPLOYEE')
- **Roles**: `staging_mirror`
- **Columns**: 30
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 171787

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 3 | `ADDRESSTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 4 | `ADDRESSTYPECODE` | CHAR(6) |  |  |  |  |
| 5 | `ADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 6 | `ADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 7 | `ADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 8 | `ADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 9 | `COUNTRYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 10 | `COUNTRYCODE` | CHAR(6) |  |  |  |  |
| 11 | `STATECODE` | CHAR(3) |  |  |  |  |
| 12 | `DISTRICTDISTRICTCODE` | CHAR(3) |  |  |  |  |
| 13 | `CITYCODE` | CHAR(3) |  |  |  |  |
| 14 | `PINCODE` | CHAR(10) |  |  |  |  |
| 15 | `EMAILID` | CHAR(25) |  |  |  |  |
| 16 | `TELEPHONELANDLINE` | CHAR(12) |  |  |  |  |
| 17 | `TELEPHONEMOBILE` | CHAR(12) |  |  |  |  |
| 18 | `REQUESTFLAG` | INTEGER | NOT NULL |  |  |  |
| 19 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 20 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 21 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 22 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 26 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 28 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 29 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPLOYEEADDRESSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.ADDRESSTYPEICSTABLECODE,
       t.ADDRESSTYPECODE,
       t.ADDRESSLINE1,
       t.ADDRESSLINE2,
       t.ADDRESSLINE3,
       t.ADDRESSLINE4,
       t.COUNTRYICSTABLECODE,
       t.COUNTRYCODE,
       t.STATECODE
FROM   DB2ADMIN.EMPLOYEEADDRESSBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
