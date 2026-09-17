# DB2ADMIN.SALESDOCUMENTLINEDISCOUNTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 55
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 96467

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
| 11 | `EXCLUDEDINCMSCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 12 | `EXCLUDEDINCOMMISSIONRETRIEVING` | SMALLINT | NOT NULL |  |  |  |
| 13 | `DISCOUNTGROUPCODE` | CHAR(3) |  |  |  |  |
| 14 | `PAYMENTDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 15 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 16 | `FREEGIFTDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 17 | `FREEGIFTDISCOUNTEQUALITEMSOLD` | SMALLINT | NOT NULL |  |  |  |
| 18 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 19 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 20 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 30 | `DOCUMENTLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 31 | `DOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 32 | `DOCUMENTLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 33 | `DEFSALDSCDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 34 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 35 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 36 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 37 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 38 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 39 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 40 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 41 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 42 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 43 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 44 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 45 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 46 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 47 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 48 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 49 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 50 | `ADVANCEINVOICEDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 51 | `PREVIOUSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 52 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 53 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 54 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESDOCUMENTLINE**.`ABSUNIQUEID` (high confidence — name = 'SALESDOCUMENTLINE' + known child suffix 'DISCOUNT')
  - JOIN predicate: `SALESDOCUMENTLINEDISCOUNTBEAN.FATHERID = SALESDOCUMENTLINE.ABSUNIQUEID`

## Indexes

- `SALDOCLINEDISCOUNTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
       t.EXCLUDEDINCMSCALCULATION
FROM   DB2ADMIN.SALESDOCUMENTLINEDISCOUNTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
