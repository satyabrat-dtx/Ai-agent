# DB2ADMIN.RFQDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 54
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 110426

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 13 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `UOMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 15 | `PAYMENTMETHODDESC` | CHAR(100) |  |  |  |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `DELIVERYTERMDESC` | CHAR(100) |  |  |  |  |
| 18 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `SHIPMENTTERMDESC` | CHAR(100) |  |  |  |  |
| 20 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 21 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 22 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 23 | `DELIVERYDATE` | DATE |  |  |  |  |
| 24 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 25 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 26 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 27 | `STATUS` | CHAR(1) |  |  |  |  |
| 28 | `MANUALCLOSURE` | SMALLINT | NOT NULL |  |  |  |
| 29 | `REMARK` | VARCHAR(1000) |  |  |  |  |
| 30 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 31 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 32 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 33 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 34 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 35 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 36 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 37 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 38 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 39 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 40 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 41 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 42 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 43 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 44 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 45 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 46 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 47 | `ADDITIONALDATA` | BLOB(1000000) |  |  |  |  |
| 48 | `SECONDARYUOMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 49 | `PACKAGINGUOMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 50 | `SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `SECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 53 | `PACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `RFQDETAILBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `RFQDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.LINENO,
       t.DIVISIONCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.RFQDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
