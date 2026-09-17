# DB2ADMIN.SALESORDERDELIVERYBLOCKSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 29
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 60268

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
| 16 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 17 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 18 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 19 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 20 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 26 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 27 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 28 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESORDERDELIVERY**.`ABSUNIQUEID` (high confidence — name = 'SALESORDERDELIVERY' + known child suffix 'BLOCKS')
  - JOIN predicate: `SALESORDERDELIVERYBLOCKSBEAN.FATHERID = SALESORDERDELIVERY.ABSUNIQUEID`

## Indexes

- `SALORDDELIVERYBLOCKSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.SALESORDERDELIVERYBLOCKSBEAN t
FETCH FIRST 100 ROWS ONLY;
```
