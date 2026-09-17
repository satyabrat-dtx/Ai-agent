# DB2ADMIN.QUALITYLINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 31
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121003

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINE` | INTEGER | NOT NULL |  |  |  |
| 3 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 4 | `CHARACTERISTICCODE` | CHAR(10) |  |  |  |  |
| 5 | `MANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SUBCODEMIN` | CHAR(50) |  |  |  |  |
| 7 | `SUBCODEMAX` | CHAR(50) |  |  |  |  |
| 8 | `SUBCODEMEDIOMIN` | CHAR(50) |  |  |  |  |
| 9 | `SUBCODEMEDIOMAX` | CHAR(50) |  |  |  |  |
| 10 | `SUBCODESTANDARD` | CHAR(50) |  |  |  |  |
| 11 | `REPETITIONNUMBER` | INTEGER | NOT NULL |  |  |  |
| 12 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 13 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 14 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 15 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 17 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 18 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 19 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 21 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 22 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 23 | `GROUPCODE` | CHAR(3) |  |  |  |  |
| 24 | `STATUSINACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 25 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 26 | `INTERNALSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 27 | `ISOSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 28 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 29 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 30 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `QUALITYLINEBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `QUALITYLINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINE,
       t.SEQUENCE,
       t.CHARACTERISTICCODE,
       t.MANDATORY,
       t.SUBCODEMIN,
       t.SUBCODEMAX,
       t.SUBCODEMEDIOMIN,
       t.SUBCODEMEDIOMAX,
       t.SUBCODESTANDARD,
       t.REPETITIONNUMBER
FROM   DB2ADMIN.QUALITYLINEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
