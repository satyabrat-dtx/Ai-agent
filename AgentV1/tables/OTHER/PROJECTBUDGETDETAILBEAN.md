# DB2ADMIN.PROJECTBUDGETDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 31
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 211984

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 4 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 5 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `BUDGETUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 14 | `BUDGETUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 15 | `BUDGETAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 16 | `BUDGETBEFOREPLANNINGRUN` | DECIMAL(18,5) |  |  |  |  |
| 17 | `ADDBUDGETAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 19 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 20 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 21 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 23 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 25 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 27 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 29 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 30 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **PROJECT**.`ABSUNIQUEID` (medium confidence — name = 'PROJECT' + recurring fragment 'BUDGETDETAIL' (seen in 3 tables))
  - JOIN predicate: `PROJECTBUDGETDETAILBEAN.FATHERID = PROJECT.ABSUNIQUEID`

## Indexes

- `PROJECTBUDGETDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09
FROM   DB2ADMIN.PROJECTBUDGETDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
