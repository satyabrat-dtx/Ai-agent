# DB2ADMIN.APPSALESORDERLINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 30
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 114696

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT |  |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINEID` | CHAR(50) |  |  |  |  |
| 3 | `IDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `PRICE` | DECIMAL(4,1) |  |  |  |  |
| 6 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 7 | `UNITOFQTY` | CHAR(10) |  |  |  |  |
| 8 | `COMMENTS` | CLOB(1000000) |  |  |  |  |
| 9 | `DISCOUNT` | DECIMAL(2,0) |  |  |  |  |
| 10 | `COMMENTS1` | CHAR(1) |  |  |  |  |
| 11 | `COMMENTS2` | CHAR(1) |  |  |  |  |
| 12 | `COMMENTSIMAGE1` | BLOB(1000000) |  |  |  |  |
| 13 | `COMMENTSIMAGE2` | BLOB(1000000) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 18 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 19 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 20 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |
| 21 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 22 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 24 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 26 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 28 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 29 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **APPSALESORDER**.`ABSUNIQUEID` (high confidence — name = 'APPSALESORDER' + known child suffix 'LINE')
  - JOIN predicate: `APPSALESORDERLINEBEAN.FATHERID = APPSALESORDER.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINEID,
       t.IDENTIFIER,
       t.ITEMTYPECODE,
       t.PRICE,
       t.QUANTITY,
       t.UNITOFQTY,
       t.COMMENTS,
       t.DISCOUNT,
       t.COMMENTS1,
       t.COMMENTS2
FROM   DB2ADMIN.APPSALESORDERLINEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
