# DB2ADMIN.PRODUCTALLOWEDVALUESBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'PRODUCT')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 19
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 46880

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `HORIZONTALVALUE` | CHAR(10) |  |  |  |  |
| 3 | `VERTICALVALUE` | CHAR(10) |  |  |  |  |
| 4 | `ALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `DELETEDSIZE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `DELETEDCOLOR` | SMALLINT | NOT NULL |  |  |  |
| 7 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 9 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 10 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 11 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 12 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 13 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 14 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 15 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 16 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 17 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 18 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **PRODUCT**.`ABSUNIQUEID` (medium confidence — name = 'PRODUCT' + recurring fragment 'ALLOWEDVALUES' (seen in 4 tables))
  - JOIN predicate: `PRODUCTALLOWEDVALUESBEAN.FATHERID = PRODUCT.ABSUNIQUEID`

## Indexes

- `PRODUCTALLOWEDVALUESBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.HORIZONTALVALUE,
       t.VERTICALVALUE,
       t.ALLOWED,
       t.DELETEDSIZE,
       t.DELETEDCOLOR,
       t.OWNINGCOMPANYCODE,
       t.WSOPERATION,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER
FROM   DB2ADMIN.PRODUCTALLOWEDVALUESBEAN t
FETCH FIRST 100 ROWS ONLY;
```
