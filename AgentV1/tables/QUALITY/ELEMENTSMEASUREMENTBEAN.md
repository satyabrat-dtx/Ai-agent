# DB2ADMIN.ELEMENTSMEASUREMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `QUALITY` (low confidence — table name starts with 'ELEMENT')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 22
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 82785

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `ELEMENTSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `ELEMENTSITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `ELEMENTSSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 4 | `ELEMENTSCODE` | CHAR(15) |  |  |  |  |
| 5 | `MEASUREMENTTYPE` | CHAR(2) |  |  |  |  |
| 6 | `QUANTITYTYPE` | CHAR(2) |  |  |  |  |
| 7 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 8 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 11 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 12 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 13 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 14 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 15 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 16 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 18 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 19 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 20 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 21 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **ELEMENTS**.`ABSUNIQUEID` (medium confidence — name = 'ELEMENTS' + recurring fragment 'MEASUREMENT' (seen in 8 tables))
  - JOIN predicate: `ELEMENTSMEASUREMENTBEAN.FATHERID = ELEMENTS.ABSUNIQUEID`

## Indexes

- `ELEMENTSMEASUREMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.ELEMENTSCOMPANYCODE,
       t.ELEMENTSITEMTYPECODE,
       t.ELEMENTSSUBCODEKEY,
       t.ELEMENTSCODE,
       t.MEASUREMENTTYPE,
       t.QUANTITYTYPE,
       t.UNITOFMEASURECODE,
       t.QUANTITY,
       t.OWNINGCOMPANYCODE,
       t.WSOPERATION,
       t.IMPORTSTATUS
FROM   DB2ADMIN.ELEMENTSMEASUREMENTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
