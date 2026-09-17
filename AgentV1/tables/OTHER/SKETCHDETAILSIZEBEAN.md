# DB2ADMIN.SKETCHDETAILSIZEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 18
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235520

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `SKETCHGROUPCODE` | CHAR(10) |  |  |  |  |
| 3 | `SIZESIZESTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `SIZECODE` | CHAR(10) |  |  |  |  |
| 5 | `MEASURE` | DECIMAL(5,2) |  |  |  |  |
| 6 | `TOLERANCEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 7 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 8 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 9 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 10 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 11 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 12 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 13 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 14 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 15 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 16 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 17 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SKETCHDETAIL**.`ABSUNIQUEID` (medium confidence — name = 'SKETCHDETAIL' + recurring fragment 'SIZE' (seen in 5 tables))
  - JOIN predicate: `SKETCHDETAILSIZEBEAN.FATHERID = SKETCHDETAIL.ABSUNIQUEID`

## Indexes

- `SKETCHDETAILSIZEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.SKETCHGROUPCODE,
       t.SIZESIZESTYPECODE,
       t.SIZECODE,
       t.MEASURE,
       t.TOLERANCEPERCENTAGE,
       t.WSOPERATION,
       t.IMPOPERATIONUSER,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER
FROM   DB2ADMIN.SKETCHDETAILSIZEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
