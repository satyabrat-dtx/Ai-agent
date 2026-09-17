# DB2ADMIN.PURCHASEORDERLINEDISCOUNTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 26
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 59883

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 3 | `SEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 4 | `DISCOUNTTYPE` | CHAR(2) |  |  |  |  |
| 5 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 6 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 7 | `SIGN` | CHAR(2) |  |  |  |  |
| 8 | `TAXAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 9 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 10 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 11 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 12 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 13 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 14 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 15 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 16 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 17 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 18 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 19 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 21 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 23 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 24 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 25 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **PURCHASEORDERLINE**.`ABSUNIQUEID` (high confidence — name = 'PURCHASEORDERLINE' + known child suffix 'DISCOUNT')
  - JOIN predicate: `PURCHASEORDERLINEDISCOUNTBEAN.FATHERID = PURCHASEORDERLINE.ABSUNIQUEID`

## Indexes

- `PURORDERLINEDISCOUNTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.NUMBERID,
       t.SEQUENCE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN,
       t.TAXAPPLICATIONTYPE,
       t.CALCULATIONTYPE,
       t.AMOUNTCALCULATIONTYPE,
       t.CREATIONTYPE
FROM   DB2ADMIN.PURCHASEORDERLINEDISCOUNTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
