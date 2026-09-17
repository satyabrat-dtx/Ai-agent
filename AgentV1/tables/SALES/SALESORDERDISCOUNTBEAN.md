# DB2ADMIN.SALESORDERDISCOUNTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 33
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 60392

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
| 18 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 19 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 20 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 21 | `PRECEDINGAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 22 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 23 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 24 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 26 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 28 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 29 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 30 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 31 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 32 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESORDER**.`ABSUNIQUEID` (high confidence — name = 'SALESORDER' + known child suffix 'DISCOUNT')
  - JOIN predicate: `SALESORDERDISCOUNTBEAN.FATHERID = SALESORDER.ABSUNIQUEID`

## Indexes

- `SALESORDERDISCOUNTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.SALESORDERDISCOUNTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
