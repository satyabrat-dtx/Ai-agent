# DB2ADMIN.FINVOULINESBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 37
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 99212

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT |  |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `VOUCHERLINE` | DECIMAL(5,0) |  |  |  |  |
| 3 | `GLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 4 | `SUBACCOUNTTYPE` | CHAR(1) |  |  |  |  |
| 5 | `SUBACCOUNTCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 6 | `AMOUNT1` | DECIMAL(17,2) |  |  |  |  |
| 7 | `DEBITCREDITINDICATOR` | CHAR(1) |  |  |  |  |
| 8 | `AMOUNT1CURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 9 | `TAXCODECODE` | CHAR(5) |  |  |  |  |
| 10 | `AMOUNT2` | DECIMAL(17,2) |  |  |  |  |
| 11 | `TEXTKEYSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 12 | `TEXTKEYCODE` | CHAR(10) |  |  |  |  |
| 13 | `TEXT` | CHAR(50) |  |  |  |  |
| 14 | `TEXTLONG` | VARCHAR(140) |  |  |  |  |
| 15 | `NOWTRNLINETRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 16 | `NOWTRNLINETRNLINENUMBER` | INTEGER |  |  |  |  |
| 17 | `AMOUNT2CURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 18 | `INFORMATIONDATE` | DATE |  |  |  |  |
| 19 | `ACCOUNTASSOCIATE` | CHAR(10) |  |  |  |  |
| 20 | `QUANTITY` | DECIMAL(15,3) |  |  |  |  |
| 21 | `QUANTITYUNITCODE` | CHAR(5) |  |  |  |  |
| 22 | `MARKSPECIALGLCODE` | CHAR(2) |  |  |  |  |
| 23 | `GLACCOUNTDESCRIPTION` | VARCHAR(40) |  |  |  |  |
| 24 | `BALANCEVOUCHER` | DECIMAL(17,2) |  |  |  |  |
| 25 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 26 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 27 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 29 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 31 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 33 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 34 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 35 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 36 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `FINVOULINESBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.VOUCHERLINE,
       t.GLACCOUNTCODE,
       t.SUBACCOUNTTYPE,
       t.SUBACCOUNTCUSTOMERSUPPLIERCODE,
       t.AMOUNT1,
       t.DEBITCREDITINDICATOR,
       t.AMOUNT1CURRENCY1,
       t.TAXCODECODE,
       t.AMOUNT2,
       t.TEXTKEYSTANDARDTABLECODE
FROM   DB2ADMIN.FINVOULINESBEAN t
FETCH FIRST 100 ROWS ONLY;
```
