# DB2ADMIN.INTERNALPRICELISTDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 19
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 120607

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 5 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 6 | `NUMBEROFKEYSTOINPUT` | INTEGER | NOT NULL |  |  |  |
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
| 18 | `AUTOLINECREATION` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **INTERNALPRICELIST**.`ABSUNIQUEID` (high confidence — name = 'INTERNALPRICELIST' + known child suffix 'DETAIL')
  - JOIN predicate: `INTERNALPRICELISTDETAILBEAN.FATHERID = INTERNALPRICELIST.ABSUNIQUEID`

## Indexes

- `INTPRICELISTDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.COSTGROUPCODE,
       t.ITEMTYPECODE,
       t.PLANTCODE,
       t.CURRENCYCODE,
       t.NUMBEROFKEYSTOINPUT,
       t.WSOPERATION,
       t.IMPOPERATIONUSER,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER
FROM   DB2ADMIN.INTERNALPRICELISTDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
