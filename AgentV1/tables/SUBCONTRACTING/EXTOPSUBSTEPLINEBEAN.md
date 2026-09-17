# DB2ADMIN.EXTOPSUBSTEPLINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 28
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235963

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `EXTOPLINECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `EXTOPLINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 3 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 4 | `EXTOPLINECODE` | CHAR(15) |  |  |  |  |
| 5 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 6 | `SUBSTEPLINE` | DECIMAL(5,0) |  |  |  |  |
| 7 | `PROGRESSDATE` | DATE |  |  |  |  |
| 8 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 9 | `PROGRESSQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 11 | `STOPGRPUSERGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 12 | `STOPPAGEGRPCODE` | CHAR(10) |  |  |  |  |
| 13 | `STOPPAGETIME` | TIME |  |  |  |  |
| 14 | `DECISIONSTATUSREMARKS` | VARCHAR(1000) |  |  |  |  |
| 15 | `MACHINETESTREMARKS` | VARCHAR(1000) |  |  |  |  |
| 16 | `PREVENTIONGRPCODES` | CHAR(90) |  |  |  |  |
| 17 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 18 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 19 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 20 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 26 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 27 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `EXTOPSUBSTEPLINEBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `EXTOPSUBSTEPLINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.EXTOPLINECOMPANYCODE,
       t.EXTOPLINECOUNTERCODE,
       t.IMPORTAUTOCOUNTER,
       t.EXTOPLINECODE,
       t.EXTOPLINEORDERLINE,
       t.SUBSTEPLINE,
       t.PROGRESSDATE,
       t.OPERATIONCODE,
       t.PROGRESSQUANTITY,
       t.UNITOFMEASURECODE,
       t.STOPGRPUSERGENGROUPTYPECODE
FROM   DB2ADMIN.EXTOPSUBSTEPLINEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
