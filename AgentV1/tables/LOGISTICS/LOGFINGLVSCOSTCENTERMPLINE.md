# DB2ADMIN.LOGFINGLVSCOSTCENTERMPLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 20
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 228619

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINGLVSCOSTCENTERMPCMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINGLVSCOSTCENTERMPBUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `FINGLVSCOSTCENTERMPTMPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `FINGLVSCOSTCENTERMAPPINGGLCODE` | CHAR(20) | NOT NULL |  |  |  |
| 4 | `FINGLVSCOSTCENTERMPFROMDATE` | DATE | NOT NULL |  |  |  |
| 5 | `COSTCENTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `COSTCENTERCODE` | CHAR(20) | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 15 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 16 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 17 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 18 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 19 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINGLVSCOSTCENTERMPLINE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINGLVSCOSTCENTERMPCMYCODE,
       t.FINGLVSCOSTCENTERMPBUNITCODE,
       t.FINGLVSCOSTCENTERMPTMPCODE,
       t.FINGLVSCOSTCENTERMAPPINGGLCODE,
       t.FINGLVSCOSTCENTERMPFROMDATE,
       t.COSTCENTERCOMPANYCODE,
       t.COSTCENTERCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.LOGFINGLVSCOSTCENTERMPLINE t
FETCH FIRST 100 ROWS ONLY;
```
