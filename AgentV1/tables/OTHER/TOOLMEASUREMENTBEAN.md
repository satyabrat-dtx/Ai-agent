# DB2ADMIN.TOOLMEASUREMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 21
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 91067

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 3 | `BASEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 4 | `MEASUREMENTTYPE` | CHAR(2) |  |  |  |  |
| 5 | `QUANTITYTYPE` | CHAR(2) |  |  |  |  |
| 6 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 7 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 8 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
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
| 20 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **TOOL**.`ABSUNIQUEID` (medium confidence — name = 'TOOL' + recurring fragment 'MEASUREMENT' (seen in 8 tables))
  - JOIN predicate: `TOOLMEASUREMENTBEAN.FATHERID = TOOL.ABSUNIQUEID`

## Indexes

- `TOOLMEASUREMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.FORCEDWARNING,
       t.BASEUNITOFMEASURECODE,
       t.MEASUREMENTTYPE,
       t.QUANTITYTYPE,
       t.UNITOFMEASURECODE,
       t.QUANTITY,
       t.DIRTYFIELD,
       t.OWNINGCOMPANYCODE,
       t.WSOPERATION,
       t.IMPORTSTATUS
FROM   DB2ADMIN.TOOLMEASUREMENTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
