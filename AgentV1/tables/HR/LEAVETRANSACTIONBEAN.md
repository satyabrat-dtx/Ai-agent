# DB2ADMIN.LEAVETRANSACTIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `HR` (high confidence — table name starts with 'LEAVE')
- **Roles**: `staging_mirror`
- **Columns**: 37
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 173429

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LEAVECALENDARCALENDARCODE` | CHAR(3) |  |  |  |  |
| 3 | `EMPLOYEECODE` | CHAR(9) |  |  |  |  |
| 4 | `LEAVECODE` | CHAR(3) |  |  |  |  |
| 5 | `SERIALNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 6 | `DATELEAVEFROM` | DATE |  |  |  |  |
| 7 | `DATELEAVETO` | DATE |  |  |  |  |
| 8 | `NOOFLEAVEDAYS` | DECIMAL(5,2) |  |  |  |  |
| 9 | `NOOFHOURS` | DECIMAL(7,3) |  |  |  |  |
| 10 | `SESSIONLEAVEFROM` | INTEGER | NOT NULL |  |  |  |
| 11 | `SESSIONLEAVETO` | INTEGER | NOT NULL |  |  |  |
| 12 | `LEAVEDONATEDTOCODE` | CHAR(9) |  |  |  |  |
| 13 | `NOOFLEAVEDAYSDONATED` | DECIMAL(5,2) |  |  |  |  |
| 14 | `ADJUSTMENTFLAG` | INTEGER | NOT NULL |  |  |  |
| 15 | `NOOFADJUSTMENTLEAVEDAYS` | DECIMAL(5,2) |  |  |  |  |
| 16 | `TRANSACTIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 17 | `LEAVEREASON` | CHAR(100) |  |  |  |  |
| 18 | `FLAGAUTHORIZED` | INTEGER | NOT NULL |  |  |  |
| 19 | `APPROVEDBYCODE` | CHAR(9) |  |  |  |  |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 22 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 25 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 26 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 27 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 28 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 29 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 31 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 33 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 34 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 35 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 36 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LEAVETRANSACTIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.LEAVECALENDARCALENDARCODE,
       t.EMPLOYEECODE,
       t.LEAVECODE,
       t.SERIALNUMBER,
       t.DATELEAVEFROM,
       t.DATELEAVETO,
       t.NOOFLEAVEDAYS,
       t.NOOFHOURS,
       t.SESSIONLEAVEFROM,
       t.SESSIONLEAVETO
FROM   DB2ADMIN.LEAVETRANSACTIONBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
