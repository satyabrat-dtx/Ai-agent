# DB2ADMIN.FINVOULINESCRITBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 27
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 99268

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT |  |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `SUBLINE` | DECIMAL(5,0) |  |  |  |  |
| 3 | `AMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 4 | `DEBITCREDITINDICATOR` | CHAR(1) |  |  |  |  |
| 5 | `AMOUNTCURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 6 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 7 | `COSTUNITCODE` | CHAR(20) |  |  |  |  |
| 8 | `ASSETCODE` | CHAR(20) |  |  |  |  |
| 9 | `PROFITCENTERCODE` | CHAR(3) |  |  |  |  |
| 10 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 11 | `TEXTKEYSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 12 | `TEXTKEYCODE` | CHAR(10) |  |  |  |  |
| 13 | `TEXT` | CHAR(50) |  |  |  |  |
| 14 | `QUANTITY` | DECIMAL(15,3) |  |  |  |  |
| 15 | `QUANTITYUNITCODE` | CHAR(5) |  |  |  |  |
| 16 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 17 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 18 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 20 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 22 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 24 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 25 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 26 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `FINVOULINESCRITBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.SUBLINE,
       t.AMOUNT,
       t.DEBITCREDITINDICATOR,
       t.AMOUNTCURRENCY1,
       t.COSTCENTERCODE,
       t.COSTUNITCODE,
       t.ASSETCODE,
       t.PROFITCENTERCODE,
       t.WAREHOUSECODE,
       t.TEXTKEYSTANDARDTABLECODE
FROM   DB2ADMIN.FINVOULINESCRITBEAN t
FETCH FIRST 100 ROWS ONLY;
```
