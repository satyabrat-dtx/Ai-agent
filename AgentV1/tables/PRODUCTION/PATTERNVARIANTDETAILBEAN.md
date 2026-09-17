# DB2ADMIN.PATTERNVARIANTDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (low confidence — table name starts with 'PATTERN')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 36
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 91461

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `WARPWEFTLEVEL` | DECIMAL(2,0) |  |  |  |  |
| 3 | `YARNLEVEL` | CHAR(2) |  |  |  |  |
| 4 | `YARNREFERENCE` | CHAR(3) |  |  |  |  |
| 5 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 6 | `YARNITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `YARNCODE` | CHAR(100) |  |  |  |  |
| 8 | `YARNSUBCODE01` | CHAR(20) |  |  |  |  |
| 9 | `YARNSUBCODE02` | CHAR(10) |  |  |  |  |
| 10 | `YARNSUBCODE03` | CHAR(10) |  |  |  |  |
| 11 | `YARNSUBCODE04` | CHAR(10) |  |  |  |  |
| 12 | `YARNSUBCODE05` | CHAR(10) |  |  |  |  |
| 13 | `YARNSUBCODE06` | CHAR(10) |  |  |  |  |
| 14 | `YARNSUBCODE07` | CHAR(10) |  |  |  |  |
| 15 | `YARNSUBCODE08` | CHAR(10) |  |  |  |  |
| 16 | `YARNSUBCODE09` | CHAR(10) |  |  |  |  |
| 17 | `YARNSUBCODE10` | CHAR(10) |  |  |  |  |
| 18 | `PRODUCED` | SMALLINT | NOT NULL |  |  |  |
| 19 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 20 | `COSTINGPLANTCODE` | CHAR(8) |  |  |  |  |
| 21 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 22 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 23 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 25 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 27 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 29 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 30 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 31 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 32 | `MANAGEYARNWASTEPERCENT` | SMALLINT | NOT NULL |  |  |  |
| 33 | `YARNWASTEPERCENT` | DECIMAL(5,2) |  |  |  |  |
| 34 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 35 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PATTERNVARIANTDETAILBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PATTERNVARIANTDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.WARPWEFTLEVEL,
       t.YARNLEVEL,
       t.YARNREFERENCE,
       t.ORDERTYPE,
       t.YARNITEMTYPECODE,
       t.YARNCODE,
       t.YARNSUBCODE01,
       t.YARNSUBCODE02,
       t.YARNSUBCODE03,
       t.YARNSUBCODE04
FROM   DB2ADMIN.PATTERNVARIANTDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
