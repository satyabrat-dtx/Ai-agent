# DB2ADMIN.PRDSPECIALIZEDCHEMICALBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 34
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 86566

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `USEDFORBINDERCONSUMPTION` | SMALLINT | NOT NULL |  |  |  |
| 3 | `STANDARDTITER` | DECIMAL(5,2) |  |  |  |  |
| 4 | `RESINCONCENTRATIONPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 5 | `DILUTIONPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 6 | `DILUTIONORCONCENTRATION` | CHAR(1) |  |  |  |  |
| 7 | `SPECIFICGRAVITY` | DECIMAL(5,2) |  |  |  |  |
| 8 | `SPECIFICGRAVITYUOMCODE` | CHAR(3) |  |  |  |  |
| 9 | `ACTIVATIONPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 10 | `COLORANTTYPE` | CHAR(1) |  |  |  |  |
| 11 | `WATERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 12 | `WATERSUBCODE01` | CHAR(20) |  |  |  |  |
| 13 | `WATERSUBCODE02` | CHAR(10) |  |  |  |  |
| 14 | `WATERSUBCODE03` | CHAR(10) |  |  |  |  |
| 15 | `WATERSUBCODE04` | CHAR(10) |  |  |  |  |
| 16 | `WATERSUBCODE05` | CHAR(10) |  |  |  |  |
| 17 | `WATERSUBCODE06` | CHAR(10) |  |  |  |  |
| 18 | `WATERSUBCODE07` | CHAR(10) |  |  |  |  |
| 19 | `WATERSUBCODE08` | CHAR(10) |  |  |  |  |
| 20 | `WATERSUBCODE09` | CHAR(10) |  |  |  |  |
| 21 | `WATERSUBCODE10` | CHAR(10) |  |  |  |  |
| 22 | `USEDFORWATERCONSUMPTION` | SMALLINT | NOT NULL |  |  |  |
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

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PRDSPECIALIZEDCHEMICALBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PRDSPCCHEMICALBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.USEDFORBINDERCONSUMPTION,
       t.STANDARDTITER,
       t.RESINCONCENTRATIONPERCENTAGE,
       t.DILUTIONPERCENTAGE,
       t.DILUTIONORCONCENTRATION,
       t.SPECIFICGRAVITY,
       t.SPECIFICGRAVITYUOMCODE,
       t.ACTIVATIONPERCENTAGE,
       t.COLORANTTYPE,
       t.WATERITEMTYPECODE
FROM   DB2ADMIN.PRDSPECIALIZEDCHEMICALBEAN t
FETCH FIRST 100 ROWS ONLY;
```
