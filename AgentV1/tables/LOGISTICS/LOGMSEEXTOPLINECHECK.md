# DB2ADMIN.LOGMSEEXTOPLINECHECK

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 26
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 212694

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPLINECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `EXTOPLINECOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `EXTOPLINECODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `SPECIFICATIONTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `SPECMASTERDEFINITIONCODE` | CHAR(3) |  |  |  |  |
| 6 | `ONTIMECHECK` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ONTIMEPOINTS` | INTEGER | NOT NULL |  |  |  |
| 8 | `COMPLETECHECK` | SMALLINT | NOT NULL |  |  |  |
| 9 | `COMPLETEPOINTS` | INTEGER | NOT NULL |  |  |  |
| 10 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 11 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 12 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 21 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 22 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 23 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 24 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 25 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGMSEEXTOPLINECHECK.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.EXTOPLINECOMPANYCODE,
       t.EXTOPLINECOUNTERCODE,
       t.EXTOPLINECODE,
       t.EXTOPLINEORDERLINE,
       t.SPECIFICATIONTEMPLATECODE,
       t.SPECMASTERDEFINITIONCODE,
       t.ONTIMECHECK,
       t.ONTIMEPOINTS,
       t.COMPLETECHECK,
       t.COMPLETEPOINTS,
       t.TERMSOFLOGORDERTYPE,
       t.TERMSOFLOGCODE
FROM   DB2ADMIN.LOGMSEEXTOPLINECHECK t
FETCH FIRST 100 ROWS ONLY;
```
