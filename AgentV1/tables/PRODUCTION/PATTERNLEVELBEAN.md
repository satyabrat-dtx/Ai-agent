# DB2ADMIN.PATTERNLEVELBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (low confidence — table name starts with 'PATTERN')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 35
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 91344

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `WARPWEFTLEVEL` | DECIMAL(2,0) |  |  |  |  |
| 3 | `LVLNOOFENDS` | DECIMAL(7,0) |  |  |  |  |
| 4 | `LVLNOOFENDSEXTRA` | DECIMAL(11,4) |  |  |  |  |
| 5 | `LVLREEDWIDTH` | DECIMAL(11,4) |  |  |  |  |
| 6 | `LVLREEDWIDTHEXTRA` | DECIMAL(11,4) |  |  |  |  |
| 7 | `LVLWASTEPERCENT` | DECIMAL(5,2) |  |  |  |  |
| 8 | `LVLNOOFYARNSFORUOM` | DECIMAL(11,4) |  |  |  |  |
| 9 | `LVLMULTIPLIER` | DECIMAL(5,0) |  |  |  |  |
| 10 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 11 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 12 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
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
| 32 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 33 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 34 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **PATTERN**.`ABSUNIQUEID` (medium confidence — name = 'PATTERN' + recurring fragment 'LEVEL' (seen in 6 tables))
  - JOIN predicate: `PATTERNLEVELBEAN.FATHERID = PATTERN.ABSUNIQUEID`

## Indexes

- `PATTERNLEVELBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.WARPWEFTLEVEL,
       t.LVLNOOFENDS,
       t.LVLNOOFENDSEXTRA,
       t.LVLREEDWIDTH,
       t.LVLREEDWIDTHEXTRA,
       t.LVLWASTEPERCENT,
       t.LVLNOOFYARNSFORUOM,
       t.LVLMULTIPLIER,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01
FROM   DB2ADMIN.PATTERNLEVELBEAN t
FETCH FIRST 100 ROWS ONLY;
```
