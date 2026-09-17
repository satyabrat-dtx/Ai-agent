# DB2ADMIN.LOGINTERNALDOCUMENTBLOCKS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 32
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 51499

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTERNALDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `INTDOCPROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `INTDOCUMENTPROVISIONALCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `BLOCKSORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 4 | `BLOCKSCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `BLOCKDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 6 | `APPLICATIONDOCUMENTTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `APPLICATIONDOCUMENTACTIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `APPLYONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `APPLYONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `APPLYONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 11 | `UNBLOCKINGSEQUENCE` | DECIMAL(2,0) |  |  |  |  |
| 12 | `UNBLOCKINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `UNBLOCKINGUSER` | CHAR(50) |  |  |  |  |
| 14 | `UNBLOCKINGDATE` | DATE |  |  |  |  |
| 15 | `UNBLOCKINGTIME` | TIME |  |  |  |  |
| 16 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 17 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 18 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 24 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 25 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 26 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 31 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGINTERNALDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'LOGINTERNALDOCUMENT' + known child suffix 'BLOCKS')
  - JOIN predicate: `LOGINTERNALDOCUMENTBLOCKS.FATHERID = LOGINTERNALDOCUMENT.ABSUNIQUEID`

## Starter query

```sql
SELECT t.INTERNALDOCUMENTCOMPANYCODE,
       t.INTDOCPROVISIONALCOUNTERCODE,
       t.INTDOCUMENTPROVISIONALCODE,
       t.BLOCKSORDERTYPE,
       t.BLOCKSCODE,
       t.BLOCKDESCRIPTION,
       t.APPLICATIONDOCUMENTTYPE,
       t.APPLICATIONDOCUMENTACTIONCODE,
       t.APPLYONCREATE,
       t.APPLYONUPDATE,
       t.APPLYONDELETE,
       t.UNBLOCKINGSEQUENCE
FROM   DB2ADMIN.LOGINTERNALDOCUMENTBLOCKS t
FETCH FIRST 100 ROWS ONLY;
```
