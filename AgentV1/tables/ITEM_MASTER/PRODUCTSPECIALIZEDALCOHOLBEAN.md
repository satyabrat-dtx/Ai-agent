# DB2ADMIN.PRODUCTSPECIALIZEDALCOHOLBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'PRODUCT')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 17
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 86517

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `HYDRATEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 3 | `ANHYDRATEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 4 | `DEGREE` | DECIMAL(15,5) |  |  |  |  |
| 5 | `DENSITY` | DECIMAL(15,5) |  |  |  |  |
| 6 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 7 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 8 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 9 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 10 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 11 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 12 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 13 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 14 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 15 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 16 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PRODUCTSPECIALIZEDALCOHOLBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PRDSPECIALIZEDALCOHOLBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.HYDRATEQUANTITY,
       t.ANHYDRATEQUANTITY,
       t.DEGREE,
       t.DENSITY,
       t.WSOPERATION,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER,
       t.IMPLASTUPDATEDATETIME,
       t.IMPLASTUPDATEUSER
FROM   DB2ADMIN.PRODUCTSPECIALIZEDALCOHOLBEAN t
FETCH FIRST 100 ROWS ONLY;
```
