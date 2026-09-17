# DB2ADMIN.PURCHASEPRICEDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 21
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93398

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `NUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 3 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 4 | `BREAKDOWNINITIALLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 5 | `BREAKDOWNLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 7 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 9 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 10 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 11 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 12 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 13 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 14 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 15 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 17 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 18 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 19 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 20 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PURCHASEPRICEDETAILBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PURCHASEPRICEDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.NUMBERLINEID,
       t.UNITOFMEASURECODE,
       t.BREAKDOWNINITIALLIMIT,
       t.BREAKDOWNLIMIT,
       t.PRICETYPE,
       t.PRICE,
       t.PRICEINCLUDINGTAX,
       t.WSOPERATION,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME
FROM   DB2ADMIN.PURCHASEPRICEDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
