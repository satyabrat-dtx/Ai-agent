# DB2ADMIN.SALESDOCUMENTDISCOUNTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 34
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 95878

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
| 16 | `DEFSALDSCDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 17 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 18 | `SALESORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 19 | `SALESORDERCODE` | CHAR(15) |  |  |  |  |
| 20 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 21 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 22 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 23 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 24 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 25 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 27 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 29 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 31 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 32 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 33 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'SALESDOCUMENT' + known child suffix 'DISCOUNT')
  - JOIN predicate: `SALESDOCUMENTDISCOUNTBEAN.FATHERID = SALESDOCUMENT.ABSUNIQUEID`

## Indexes

- `SALESDOCUMENTDISCOUNTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.SALESDOCUMENTDISCOUNTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
