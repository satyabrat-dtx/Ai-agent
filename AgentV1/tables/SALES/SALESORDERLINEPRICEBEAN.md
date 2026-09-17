# DB2ADMIN.SALESORDERLINEPRICEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 25
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 60848

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `QUALITYLEVELITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 4 | `SOURCEPRICETYPE` | CHAR(2) |  |  |  |  |
| 5 | `NUMBERLINEID` | DECIMAL(2,0) |  |  |  |  |
| 6 | `COMPOUNDPRICETYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 8 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `PRICEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 10 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 11 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 12 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 13 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 14 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 15 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 16 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 18 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 22 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 23 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 24 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESORDERLINE**.`ABSUNIQUEID` (high confidence — name = 'SALESORDERLINE' + known child suffix 'PRICE')
  - JOIN predicate: `SALESORDERLINEPRICEBEAN.FATHERID = SALESORDERLINE.ABSUNIQUEID`

## Indexes

- `SALESORDERLINEPRICEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.QUALITYLEVELITEMTYPECODE,
       t.QUALITYLEVELCODE,
       t.SOURCEPRICETYPE,
       t.NUMBERLINEID,
       t.COMPOUNDPRICETYPECODE,
       t.PRICETYPE,
       t.PRICE,
       t.PRICEPERCENTAGE,
       t.PRICESIGN,
       t.PRICEINCLUDINGTAX
FROM   DB2ADMIN.SALESORDERLINEPRICEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
