# DB2ADMIN.EXTOPPRICEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 61
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 98719

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINEID` | DECIMAL(5,0) |  |  |  |  |
| 3 | `PRICELISTTYPE` | CHAR(2) |  |  |  |  |
| 4 | `TEMPLATEDEFINITIONTYPE` | CHAR(1) |  |  |  |  |
| 5 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `ENTRYITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 18 | `ENTRYSUBCODE01` | CHAR(20) |  |  |  |  |
| 19 | `ENTRYSUBCODE02` | CHAR(10) |  |  |  |  |
| 20 | `ENTRYSUBCODE03` | CHAR(10) |  |  |  |  |
| 21 | `ENTRYSUBCODE04` | CHAR(10) |  |  |  |  |
| 22 | `ENTRYSUBCODE05` | CHAR(10) |  |  |  |  |
| 23 | `ENTRYSUBCODE06` | CHAR(10) |  |  |  |  |
| 24 | `ENTRYSUBCODE07` | CHAR(10) |  |  |  |  |
| 25 | `ENTRYSUBCODE08` | CHAR(10) |  |  |  |  |
| 26 | `ENTRYSUBCODE09` | CHAR(10) |  |  |  |  |
| 27 | `ENTRYSUBCODE10` | CHAR(10) |  |  |  |  |
| 28 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 29 | `COMPOUNDPRICEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 30 | `BREAKDOWNTYPE` | CHAR(2) |  |  |  |  |
| 31 | `DISCOUNTBREAKDOWNTYPE` | CHAR(2) |  |  |  |  |
| 32 | `CHARGEBREAKDOWNTYPE` | CHAR(2) |  |  |  |  |
| 33 | `DISCOUNTLIMITCALCULATIONMODE` | CHAR(2) |  |  |  |  |
| 34 | `CHARGELIMITCALCULATIONMODE` | CHAR(2) |  |  |  |  |
| 35 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 36 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 37 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 38 | `PRICEBYQUALITYREQUIRED` | CHAR(2) |  |  |  |  |
| 39 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 40 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 41 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 42 | `MINIMUMBATCHQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `MINIMUMBATCHUOMCODE` | CHAR(3) |  |  |  |  |
| 44 | `INITIALDATE` | DATE |  |  |  |  |
| 45 | `FINALDATE` | DATE |  |  |  |  |
| 46 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 47 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 48 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 49 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 50 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 51 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 52 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 53 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 54 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 55 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 56 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 57 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 58 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 59 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 60 | `PROTOTYPEMANAGED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `EXTOPPRICEBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `EXTOPPRICEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINEID,
       t.PRICELISTTYPE,
       t.TEMPLATEDEFINITIONTYPE,
       t.TEMPLATECODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.EXTOPPRICEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
