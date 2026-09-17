# DB2ADMIN.ABSMULTIMEDIADEPENDENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 20
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 43700

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `ID` | CHAR(20) |  |  |  |  |
| 3 | `DESCRIPTION` | VARCHAR(250) |  |  | description |  |
| 4 | `LINK` | VARCHAR(250) |  |  |  |  |
| 5 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 6 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 7 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 8 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 9 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 10 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 11 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 12 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 13 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 14 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 15 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 16 | `CLASSTAGS` | VARCHAR(1000) |  |  |  |  |
| 17 | `MULTIMEDIADATA` | BLOB(1000000000) |  |  |  |  |
| 18 | `CHECKSUMCRC32` | CHAR(8) |  |  |  |  |
| 19 | `APPLICATIONTAGS` | VARCHAR(1000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ABSMULTIMEDIADEPENDENTBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ABSMULTIMEDIADEPENDENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.ID,
       t.DESCRIPTION,
       t.LINK,
       t.WSOPERATION,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER,
       t.IMPLASTUPDATEDATETIME,
       t.IMPLASTUPDATEUSER,
       t.IMPORTDATETIME
FROM   DB2ADMIN.ABSMULTIMEDIADEPENDENTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
