# DB2ADMIN.PRODUCTMEASUREMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'PRODUCT')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 18
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 82839

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `MEASUREMENTTYPE` | CHAR(2) |  |  |  |  |
| 3 | `QUANTITYTYPE` | CHAR(2) |  |  |  |  |
| 4 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 5 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 6 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 8 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 9 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 10 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 11 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 12 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 13 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 14 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 15 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 16 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 17 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **PRODUCT**.`ABSUNIQUEID` (medium confidence — name = 'PRODUCT' + recurring fragment 'MEASUREMENT' (seen in 8 tables))
  - JOIN predicate: `PRODUCTMEASUREMENTBEAN.FATHERID = PRODUCT.ABSUNIQUEID`

## Indexes

- `PRODUCTMEASUREMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.MEASUREMENTTYPE,
       t.QUANTITYTYPE,
       t.UNITOFMEASURECODE,
       t.QUANTITY,
       t.OWNINGCOMPANYCODE,
       t.WSOPERATION,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER,
       t.IMPLASTUPDATEDATETIME
FROM   DB2ADMIN.PRODUCTMEASUREMENTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
