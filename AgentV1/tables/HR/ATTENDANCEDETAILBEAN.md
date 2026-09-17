# DB2ADMIN.ATTENDANCEDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `HR` (high confidence — table name starts with 'ATTENDANCE')
- **Roles**: `staging_mirror`
- **Columns**: 49
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 173045

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `EMPLOYEECODE` | CHAR(9) |  |  |  |  |
| 3 | `ATTENDANCEDATE` | DATE |  |  |  |  |
| 4 | `DAYSESSION` | INTEGER | NOT NULL |  |  |  |
| 5 | `ATTENDANCECODE` | CHAR(1) |  |  |  |  |
| 6 | `NUMBEROFHRS` | DECIMAL(7,3) |  |  |  |  |
| 7 | `SHIFTCODE` | CHAR(3) |  |  |  |  |
| 8 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 9 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 10 | `LEAVECODE` | CHAR(3) |  |  |  |  |
| 11 | `PAYROLLCODE` | CHAR(3) |  |  |  |  |
| 12 | `ATTENDANCETYPECODE` | CHAR(3) |  |  |  |  |
| 13 | `RECORDFOR` | INTEGER | NOT NULL |  |  |  |
| 14 | `FLAGPAYABLE` | INTEGER | NOT NULL |  |  |  |
| 15 | `INTIME` | TIME |  |  |  |  |
| 16 | `OUTTIME` | TIME |  |  |  |  |
| 17 | `WORKINGDEPTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 18 | `WORKINGSECTIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 19 | `WORKINGSECTIONCODE` | CHAR(6) |  |  |  |  |
| 20 | `WORKINGMACHINETYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 21 | `WORKINGMACHINETYPECODE` | CHAR(6) |  |  |  |  |
| 22 | `WORKINGMACHINENOICSTABLECODE` | CHAR(4) |  |  |  |  |
| 23 | `WORKINGMACHINENOCODE` | CHAR(6) |  |  |  |  |
| 24 | `WORKINGDESIGNATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 25 | `WORKINGDESIGNATIONCODE` | CHAR(6) |  |  |  |  |
| 26 | `WORKINGMILLNOICSTABLECODE` | CHAR(4) |  |  |  |  |
| 27 | `WORKINGMILLNOCODE` | CHAR(6) |  |  |  |  |
| 28 | `WORKLOADINCENTIVE` | DECIMAL(5,2) |  |  |  |  |
| 29 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 30 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 31 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 32 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 33 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 34 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 35 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 36 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 37 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 38 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 39 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 40 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 41 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 42 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 43 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 44 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 45 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 46 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 47 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 48 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ATTENDANCEDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.EMPLOYEECODE,
       t.ATTENDANCEDATE,
       t.DAYSESSION,
       t.ATTENDANCECODE,
       t.NUMBEROFHRS,
       t.SHIFTCODE,
       t.DIVISIONCODE,
       t.FACTORYCODE,
       t.LEAVECODE,
       t.PAYROLLCODE
FROM   DB2ADMIN.ATTENDANCEDETAILBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
