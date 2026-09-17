# DB2ADMIN.PURORDERDELIVERYBLOCKSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (medium confidence — table name starts with 'PUR')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 28
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 59456

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `BLOCKSORDERTYPE` | CHAR(1) |  |  |  |  |
| 3 | `BLOCKSCODE` | CHAR(3) |  |  |  |  |
| 4 | `BLOCKDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 5 | `APPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 6 | `APPLYONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 7 | `APPLYONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 8 | `APPLYONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `UNBLOCKINGSEQUENCE` | DECIMAL(2,0) |  |  |  |  |
| 10 | `UNBLOCKINGTYPE` | CHAR(2) |  |  |  |  |
| 11 | `UNBLOCKINGUSER` | CHAR(50) |  |  |  |  |
| 12 | `UNBLOCKINGDATE` | DATE |  |  |  |  |
| 13 | `UNBLOCKINGTIME` | TIME |  |  |  |  |
| 14 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 15 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 16 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 17 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 18 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 19 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 21 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 23 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 25 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 26 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 27 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PURORDERDELIVERYBLOCKSBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PURORDDELIVERYBLOCKSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.BLOCKSORDERTYPE,
       t.BLOCKSCODE,
       t.BLOCKDESCRIPTION,
       t.APPLICATIONTYPE,
       t.APPLYONCREATE,
       t.APPLYONUPDATE,
       t.APPLYONDELETE,
       t.UNBLOCKINGSEQUENCE,
       t.UNBLOCKINGTYPE,
       t.UNBLOCKINGUSER
FROM   DB2ADMIN.PURORDERDELIVERYBLOCKSBEAN t
FETCH FIRST 100 ROWS ONLY;
```
