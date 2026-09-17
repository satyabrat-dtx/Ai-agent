# DB2ADMIN.WORKCENTERDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (high confidence — table name starts with 'WORKCENTER')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 24
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 82954

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `MAINRESOURCECODE` | CHAR(8) |  |  |  |  |
| 3 | `NUMBEROFMAINRESOURCES` | DECIMAL(3,0) |  |  |  |  |
| 4 | `VALIDITYBEGINDATE` | DATE |  |  |  |  |
| 5 | `VALIDITYENDDATE` | DATE |  |  |  |  |
| 6 | `EXCEPTIONREASON` | CHAR(30) |  |  |  |  |
| 7 | `EXCEPTIONNROFMAINRESOURCES` | DECIMAL(3,0) |  |  |  |  |
| 8 | `EXCEPTIONCALENDARCODE` | CHAR(3) |  |  |  |  |
| 9 | `THEORETICSPEEDTIMETYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `THEORETICSPEEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `THEORETICSPEEDTIMEUOMCODE` | CHAR(3) |  |  |  |  |
| 12 | `THEORETICSPEEDQTYUOMCODE` | CHAR(3) |  |  |  |  |
| 13 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 14 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 15 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 17 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 18 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 19 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 21 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 22 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 23 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **WORKCENTER**.`ABSUNIQUEID` (high confidence — name = 'WORKCENTER' + known child suffix 'DETAIL')
  - JOIN predicate: `WORKCENTERDETAILBEAN.FATHERID = WORKCENTER.ABSUNIQUEID`

## Indexes

- `WORKCENTERDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.MAINRESOURCECODE,
       t.NUMBEROFMAINRESOURCES,
       t.VALIDITYBEGINDATE,
       t.VALIDITYENDDATE,
       t.EXCEPTIONREASON,
       t.EXCEPTIONNROFMAINRESOURCES,
       t.EXCEPTIONCALENDARCODE,
       t.THEORETICSPEEDTIMETYPECODE,
       t.THEORETICSPEEDVALUE,
       t.THEORETICSPEEDTIMEUOMCODE
FROM   DB2ADMIN.WORKCENTERDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
