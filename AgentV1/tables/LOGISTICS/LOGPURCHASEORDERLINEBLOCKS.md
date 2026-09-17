# DB2ADMIN.LOGPURCHASEORDERLINEBLOCKS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 33
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 53261

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURORDLINEPURORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PURORDLINEPURORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `PURORDERLINEPURCHASEORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `PURCHASEORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `PURCHASEORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `BLOCKSORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `BLOCKSCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `BLOCKDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 8 | `APPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `APPLYONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `APPLYONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 11 | `APPLYONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `UNBLOCKINGSEQUENCE` | DECIMAL(2,0) |  |  |  |  |
| 13 | `UNBLOCKINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `UNBLOCKINGUSER` | CHAR(50) |  |  |  |  |
| 15 | `UNBLOCKINGDATE` | DATE |  |  |  |  |
| 16 | `UNBLOCKINGTIME` | TIME |  |  |  |  |
| 17 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 18 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 19 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 25 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 26 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 27 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 29 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 30 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 31 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 32 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGPURCHASEORDERLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGPURCHASEORDERLINE' + known child suffix 'BLOCKS')
  - JOIN predicate: `LOGPURCHASEORDERLINEBLOCKS.FATHERID = LOGPURCHASEORDERLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.PURORDLINEPURORDERCOMPANYCODE,
       t.PURORDLINEPURORDERCOUNTERCODE,
       t.PURORDERLINEPURCHASEORDERCODE,
       t.PURCHASEORDERLINEORDERLINE,
       t.PURCHASEORDERLINEORDERSUBLINE,
       t.BLOCKSORDERTYPE,
       t.BLOCKSCODE,
       t.BLOCKDESCRIPTION,
       t.APPLICATIONTYPE,
       t.APPLYONCREATE,
       t.APPLYONUPDATE,
       t.APPLYONDELETE
FROM   DB2ADMIN.LOGPURCHASEORDERLINEBLOCKS t
FETCH FIRST 100 ROWS ONLY;
```
