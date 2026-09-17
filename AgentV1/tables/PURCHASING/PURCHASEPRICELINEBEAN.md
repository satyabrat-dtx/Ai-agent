# DB2ADMIN.PURCHASEPRICELINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 52
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93451

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINEID` | DECIMAL(7,0) |  |  |  |  |
| 3 | `TEMPLATEDEFINITIONTYPE` | CHAR(1) |  |  |  |  |
| 4 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 6 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 17 | `COMPOUNDPRICEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `BREAKDOWNTYPE` | CHAR(2) |  |  |  |  |
| 19 | `DISCOUNTBREAKDOWNTYPE` | CHAR(2) |  |  |  |  |
| 20 | `CHARGEBREAKDOWNTYPE` | CHAR(2) |  |  |  |  |
| 21 | `DISCOUNTLIMITCALCULATIONMODE` | CHAR(2) |  |  |  |  |
| 22 | `CHARGELIMITCALCULATIONMODE` | CHAR(2) |  |  |  |  |
| 23 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 24 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 25 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 26 | `PRICEBYQUALITYREQUIRED` | CHAR(2) |  |  |  |  |
| 27 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 28 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 29 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 30 | `MINIMUMBATCHQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `MINIMUMBATCHUOMCODE` | CHAR(3) |  |  |  |  |
| 32 | `PRIORITY` | INTEGER | NOT NULL |  |  |  |
| 33 | `INITIALDATE` | DATE |  |  |  |  |
| 34 | `FINALDATE` | DATE |  |  |  |  |
| 35 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 36 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 37 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 38 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 39 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 40 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 41 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 42 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 43 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 44 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 45 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 46 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 47 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 48 | `PROTOTYPEMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 49 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 50 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 51 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PURCHASEPRICELINEBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PURCHASEPRICELINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINEID,
       t.TEMPLATEDEFINITIONTYPE,
       t.TEMPLATECODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.PURCHASEPRICELINEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
