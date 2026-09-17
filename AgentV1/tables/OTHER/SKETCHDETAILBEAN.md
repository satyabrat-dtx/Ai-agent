# DB2ADMIN.SKETCHDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 15
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235473

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `SKETCHTYPEDETAILCODE` | CHAR(10) |  |  |  |  |
| 3 | `BASEUOMCODE` | CHAR(3) |  |  |  |  |
| 4 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 5 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 6 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 7 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 8 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 9 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 10 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 11 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 12 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 13 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 14 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SKETCH**.`ABSUNIQUEID` (high confidence — name = 'SKETCH' + known child suffix 'DETAIL')
  - JOIN predicate: `SKETCHDETAILBEAN.FATHERID = SKETCH.ABSUNIQUEID`

## Indexes

- `SKETCHDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.SKETCHTYPEDETAILCODE,
       t.BASEUOMCODE,
       t.WSOPERATION,
       t.IMPOPERATIONUSER,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER,
       t.IMPLASTUPDATEDATETIME,
       t.IMPLASTUPDATEUSER,
       t.IMPORTDATETIME
FROM   DB2ADMIN.SKETCHDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
