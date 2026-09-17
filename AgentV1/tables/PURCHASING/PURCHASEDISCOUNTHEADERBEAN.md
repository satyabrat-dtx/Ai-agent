# DB2ADMIN.PURCHASEDISCOUNTHEADERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 24
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93342

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINEID` | DECIMAL(3,0) |  |  |  |  |
| 3 | `INITIALDATE` | DATE |  |  |  |  |
| 4 | `FINALDATE` | DATE |  |  |  |  |
| 5 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 6 | `DISCOUNTTYPE` | CHAR(2) |  |  |  |  |
| 7 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 9 | `SIGN` | CHAR(2) |  |  |  |  |
| 10 | `TAXAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 11 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 12 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 13 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 14 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 15 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 17 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 18 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 19 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 21 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 22 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 23 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PURCHASEDISCOUNTHEADERBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PURCHASEDISCOUNTHEADERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINEID,
       t.INITIALDATE,
       t.FINALDATE,
       t.PAYMENTMETHODCODE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN,
       t.TAXAPPLICATIONTYPE,
       t.CALCULATIONTYPE
FROM   DB2ADMIN.PURCHASEDISCOUNTHEADERBEAN t
FETCH FIRST 100 ROWS ONLY;
```
