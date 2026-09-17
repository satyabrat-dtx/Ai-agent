# DB2ADMIN.LOGPURCHASEORDERBLOCKS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 31
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 53052

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURCHASEORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `PURCHASEORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `BLOCKSORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 4 | `BLOCKSCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `BLOCKDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 6 | `APPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `APPLYONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 8 | `APPLYONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `APPLYONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `UNBLOCKINGSEQUENCE` | DECIMAL(2,0) |  |  |  |  |
| 11 | `UNBLOCKINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `UNBLOCKINGUSER` | CHAR(50) |  |  |  |  |
| 13 | `UNBLOCKINGDATE` | DATE |  |  |  |  |
| 14 | `UNBLOCKINGTIME` | TIME |  |  |  |  |
| 15 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 16 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 17 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 23 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 24 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 25 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 27 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 28 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 30 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGPURCHASEORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGPURCHASEORDER' + known child suffix 'BLOCKS')
  - JOIN predicate: `LOGPURCHASEORDERBLOCKS.FATHERID = LOGPURCHASEORDER.ABSUNIQUEID`

## Starter query

```sql
SELECT t.PURCHASEORDERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.BLOCKSORDERTYPE,
       t.BLOCKSCODE,
       t.BLOCKDESCRIPTION,
       t.APPLICATIONTYPE,
       t.APPLYONCREATE,
       t.APPLYONUPDATE,
       t.APPLYONDELETE,
       t.UNBLOCKINGSEQUENCE,
       t.UNBLOCKINGTYPE
FROM   DB2ADMIN.LOGPURCHASEORDERBLOCKS t
FETCH FIRST 100 ROWS ONLY;
```
