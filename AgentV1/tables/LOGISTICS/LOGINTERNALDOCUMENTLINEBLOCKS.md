# DB2ADMIN.LOGINTERNALDOCUMENTLINEBLOCKS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 34
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 51707

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTDOCLINEINTDOCCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `INTDOCLINEINTDOCPRVCNTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `INTDOCLINEINTDOCPRVCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `INTERNALDOCUMENTLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `INTDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `BLOCKSORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `BLOCKSCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `BLOCKDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 8 | `APPLICATIONDOCUMENTTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 9 | `APPLICATIONDOCUMENTACTIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 10 | `APPLYONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 11 | `APPLYONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `APPLYONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 13 | `UNBLOCKINGSEQUENCE` | DECIMAL(2,0) |  |  |  |  |
| 14 | `UNBLOCKINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 15 | `UNBLOCKINGUSER` | CHAR(50) |  |  |  |  |
| 16 | `UNBLOCKINGDATE` | DATE |  |  |  |  |
| 17 | `UNBLOCKINGTIME` | TIME |  |  |  |  |
| 18 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 19 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 20 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 26 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 27 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 28 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 30 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 31 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 32 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 33 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGINTERNALDOCUMENTLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGINTERNALDOCUMENTLINE' + known child suffix 'BLOCKS')
  - JOIN predicate: `LOGINTERNALDOCUMENTLINEBLOCKS.FATHERID = LOGINTERNALDOCUMENTLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.INTDOCLINEINTDOCCOMPANYCODE,
       t.INTDOCLINEINTDOCPRVCNTCODE,
       t.INTDOCLINEINTDOCPRVCODE,
       t.INTERNALDOCUMENTLINEORDERLINE,
       t.INTDOCUMENTLINEORDERSUBLINE,
       t.BLOCKSORDERTYPE,
       t.BLOCKSCODE,
       t.BLOCKDESCRIPTION,
       t.APPLICATIONDOCUMENTTYPE,
       t.APPLICATIONDOCUMENTACTIONCODE,
       t.APPLYONCREATE,
       t.APPLYONUPDATE
FROM   DB2ADMIN.LOGINTERNALDOCUMENTLINEBLOCKS t
FETCH FIRST 100 ROWS ONLY;
```
