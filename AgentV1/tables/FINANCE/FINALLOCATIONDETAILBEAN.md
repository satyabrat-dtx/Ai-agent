# DB2ADMIN.FINALLOCATIONDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 35
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 223666

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LINESEQUENCE` | DECIMAL(8,0) |  |  |  |  |
| 3 | `UGGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `UGGCODE` | CHAR(10) |  |  |  |  |
| 5 | `FACTOR` | DECIMAL(5,2) |  |  |  |  |
| 6 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 7 | `PROFITCENTREPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 8 | `COSTCENTRECOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 9 | `GLCODE` | CHAR(20) |  |  |  |  |
| 10 | `FIRSTSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `FIRSTSEGCODE` | CHAR(10) |  |  |  |  |
| 12 | `SNDSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 13 | `SECONDSEGCODE` | CHAR(10) |  |  |  |  |
| 14 | `THIRDSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 15 | `THIRDSEGCODE` | CHAR(10) |  |  |  |  |
| 16 | `FRSEGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `FOURTHSEGCODE` | CHAR(10) |  |  |  |  |
| 18 | `FIFTHSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 19 | `FIFTHSEGCODE` | CHAR(10) |  |  |  |  |
| 20 | `SIXTHSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 21 | `SIXTHSEGCODE` | CHAR(10) |  |  |  |  |
| 22 | `SESEGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `SEVENTHSEGCODE` | CHAR(10) |  |  |  |  |
| 24 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 25 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 26 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 27 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 29 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 31 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 33 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 34 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **FINALLOCATION**.`ABSUNIQUEID` (high confidence — name = 'FINALLOCATION' + known child suffix 'DETAIL')
  - JOIN predicate: `FINALLOCATIONDETAILBEAN.FATHERID = FINALLOCATION.ABSUNIQUEID`

## Indexes

- `FINALLOCATIONDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LINESEQUENCE,
       t.UGGUSERGENERICGROUPTYPECODE,
       t.UGGCODE,
       t.FACTOR,
       t.BUSINESSUNITCODE,
       t.PROFITCENTREPROFITCENTERCODE,
       t.COSTCENTRECOSTCENTERCODE,
       t.GLCODE,
       t.FIRSTSEGUGENERICGROUPTYPECODE,
       t.FIRSTSEGCODE
FROM   DB2ADMIN.FINALLOCATIONDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
