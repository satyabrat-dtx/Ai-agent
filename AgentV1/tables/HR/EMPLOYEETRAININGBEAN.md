# DB2ADMIN.EMPLOYEETRAININGBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `HR` (high confidence — table name starts with 'EMPLOYEE')
- **Roles**: `staging_mirror`
- **Columns**: 30
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 172831

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) |  |  |  |  |
| 3 | `SRNO` | DECIMAL(5,0) |  |  |  |  |
| 4 | `TRAININGTYPE` | INTEGER | NOT NULL |  |  |  |
| 5 | `INSTITUTECODEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 6 | `INSTITUTECODECODE` | CHAR(6) |  |  |  |  |
| 7 | `INSTITUTECOUNTRYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 8 | `INSTITUTECOUNTRYCODE` | CHAR(6) |  |  |  |  |
| 9 | `INSTITUTESTATECODE` | CHAR(3) |  |  |  |  |
| 10 | `INSTITUTEDISTRICTDISTRICTCODE` | CHAR(3) |  |  |  |  |
| 11 | `INSTITUTELOCATIONCODE` | CHAR(3) |  |  |  |  |
| 12 | `TRAININGFROM` | DATE |  |  |  |  |
| 13 | `TRAININGTO` | DATE |  |  |  |  |
| 14 | `CONDUCTEDBYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 15 | `CONDUCTEDBYCODE` | CHAR(6) |  |  |  |  |
| 16 | `MAINSUBJECTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 17 | `MAINSUBJECTCODE` | CHAR(6) |  |  |  |  |
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

- `EMPLOYEETRAININGBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.SRNO,
       t.TRAININGTYPE,
       t.INSTITUTECODEICSTABLECODE,
       t.INSTITUTECODECODE,
       t.INSTITUTECOUNTRYICSTABLECODE,
       t.INSTITUTECOUNTRYCODE,
       t.INSTITUTESTATECODE,
       t.INSTITUTEDISTRICTDISTRICTCODE,
       t.INSTITUTELOCATIONCODE
FROM   DB2ADMIN.EMPLOYEETRAININGBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
