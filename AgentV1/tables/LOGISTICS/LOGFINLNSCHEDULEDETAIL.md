# DB2ADMIN.LOGFINLNSCHEDULEDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 21
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 224997

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINLNSFINLMASTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINLNSFINLMLTEUGENGRPTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `FINLNSFINLMASTERLOANTYPECODE` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `FINLNSFINLOANMASTERLOANNO` | CHAR(10) | NOT NULL |  |  |  |
| 4 | `FINLNSCHEDULESCHEDULENO` | INTEGER | NOT NULL |  |  |  |
| 5 | `SNO` | INTEGER | NOT NULL |  |  |  |
| 6 | `SCHEDULEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 7 | `STARTDATE` | DATE |  |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 16 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 17 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 18 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 19 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 20 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINLNSCHEDULE**.`ABSUNIQUEID` (high confidence — name = 'LOGFINLNSCHEDULE' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGFINLNSCHEDULEDETAIL.FATHERID = LOGFINLNSCHEDULE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FINLNSFINLMASTERCOMPANYCODE,
       t.FINLNSFINLMLTEUGENGRPTYPECODE,
       t.FINLNSFINLMASTERLOANTYPECODE,
       t.FINLNSFINLOANMASTERLOANNO,
       t.FINLNSCHEDULESCHEDULENO,
       t.SNO,
       t.SCHEDULEAMOUNT,
       t.STARTDATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.LOGFINLNSCHEDULEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
