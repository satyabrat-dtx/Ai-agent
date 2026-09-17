# DB2ADMIN.RECIPEENGCHANGELOGBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 32
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 67663

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `ENGINEERINGCHANGENUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 3 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 6 | `RECIPEITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `RECIPESUBCODE01` | CHAR(20) |  |  |  |  |
| 8 | `RECIPESUBCODE02` | CHAR(10) |  |  |  |  |
| 9 | `RECIPESUBCODE03` | CHAR(10) |  |  |  |  |
| 10 | `RECIPESUBCODE04` | CHAR(10) |  |  |  |  |
| 11 | `RECIPESUBCODE05` | CHAR(10) |  |  |  |  |
| 12 | `RECIPESUBCODE06` | CHAR(10) |  |  |  |  |
| 13 | `RECIPESUBCODE07` | CHAR(10) |  |  |  |  |
| 14 | `RECIPESUBCODE08` | CHAR(10) |  |  |  |  |
| 15 | `RECIPESUBCODE09` | CHAR(10) |  |  |  |  |
| 16 | `RECIPESUBCODE10` | CHAR(10) |  |  |  |  |
| 17 | `RECIPESUFFIXCODE` | CHAR(20) |  |  |  |  |
| 18 | `RELEASEDATE` | DATE |  |  |  |  |
| 19 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 20 | `APPLICABLE` | SMALLINT | NOT NULL |  |  |  |
| 21 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 22 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 23 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 25 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 27 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 29 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 30 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 31 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `RECIPEENGCHANGELOGBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `RECIPEENGCHANGELOGBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.ENGINEERINGCHANGENUMBERID,
       t.COUNTERCODE,
       t.CODE,
       t.LOGREASONCODE,
       t.RECIPEITEMTYPECODE,
       t.RECIPESUBCODE01,
       t.RECIPESUBCODE02,
       t.RECIPESUBCODE03,
       t.RECIPESUBCODE04,
       t.RECIPESUBCODE05
FROM   DB2ADMIN.RECIPEENGCHANGELOGBEAN t
FETCH FIRST 100 ROWS ONLY;
```
