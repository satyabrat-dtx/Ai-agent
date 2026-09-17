# DB2ADMIN.PURCHASECHARGEDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 29
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93163

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINEID` | DECIMAL(3,0) |  |  |  |  |
| 3 | `BREAKDOWNUOMCODE` | CHAR(3) |  |  |  |  |
| 4 | `BREAKDOWNCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 5 | `BREAKDOWNLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `INITIALDATE` | DATE |  |  |  |  |
| 7 | `FINALDATE` | DATE |  |  |  |  |
| 8 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 9 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `CALCULATEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 12 | `CHARGETYPE` | CHAR(2) |  |  |  |  |
| 13 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 14 | `CHARGECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 15 | `SIGN` | CHAR(2) |  |  |  |  |
| 16 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 17 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 18 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 19 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 20 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 26 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 27 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 28 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PURCHASECHARGEDETAILBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PURCHASECHARGEDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINEID,
       t.BREAKDOWNUOMCODE,
       t.BREAKDOWNCURRENCYCODE,
       t.BREAKDOWNLIMIT,
       t.INITIALDATE,
       t.FINALDATE,
       t.PAYMENTMETHODCODE,
       t.ITEMTYPECODE,
       t.CALCULATEDVALUE,
       t.CHARGESSUBCODE01
FROM   DB2ADMIN.PURCHASECHARGEDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
