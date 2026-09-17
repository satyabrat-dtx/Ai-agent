# DB2ADMIN.SALESDOCUMENTBLOCKSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 27
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 95629

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `BLOCKSORDERTYPE` | CHAR(1) |  |  |  |  |
| 3 | `BLOCKSCODE` | CHAR(3) |  |  |  |  |
| 4 | `BLOCKDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 5 | `APPLICATIONDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 6 | `APPLICATIONDOCUMENTACTIONCODE` | CHAR(3) |  |  |  |  |
| 7 | `APPLYONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 8 | `APPLYONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `APPLYONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `UNBLOCKINGSEQUENCE` | DECIMAL(2,0) |  |  |  |  |
| 11 | `UNBLOCKINGTYPE` | CHAR(2) |  |  |  |  |
| 12 | `UNBLOCKINGUSER` | CHAR(50) |  |  |  |  |
| 13 | `UNBLOCKINGDATE` | DATE |  |  |  |  |
| 14 | `UNBLOCKINGTIME` | TIME |  |  |  |  |
| 15 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 16 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 17 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 18 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 24 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 25 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 26 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'SALESDOCUMENT' + known child suffix 'BLOCKS')
  - JOIN predicate: `SALESDOCUMENTBLOCKSBEAN.FATHERID = SALESDOCUMENT.ABSUNIQUEID`

## Indexes

- `SALESDOCUMENTBLOCKSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.BLOCKSORDERTYPE,
       t.BLOCKSCODE,
       t.BLOCKDESCRIPTION,
       t.APPLICATIONDOCUMENTTYPE,
       t.APPLICATIONDOCUMENTACTIONCODE,
       t.APPLYONCREATE,
       t.APPLYONUPDATE,
       t.APPLYONDELETE,
       t.UNBLOCKINGSEQUENCE,
       t.UNBLOCKINGTYPE
FROM   DB2ADMIN.SALESDOCUMENTBLOCKSBEAN t
FETCH FIRST 100 ROWS ONLY;
```
