# DB2ADMIN.PDMSUP1BEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 18
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 49309

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `AF_COLORUSERGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `AF_COLORCODE` | CHAR(10) |  |  |  |  |
| 4 | `AF_ATCDKE1` | CHAR(10) |  |  |  |  |
| 5 | `AF_COLCD` | CHAR(50) |  |  |  |  |
| 6 | `AF_COLDS` | VARCHAR(255) |  |  |  |  |
| 7 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 8 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 9 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 10 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 11 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 12 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 13 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 14 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 15 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 16 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 17 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PDMSUP1BEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PDMSUP1BEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.AF_COLORUSERGENGROUPTYPECODE,
       t.AF_COLORCODE,
       t.AF_ATCDKE1,
       t.AF_COLCD,
       t.AF_COLDS,
       t.WSOPERATION,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER,
       t.IMPLASTUPDATEDATETIME
FROM   DB2ADMIN.PDMSUP1BEAN t
FETCH FIRST 100 ROWS ONLY;
```
