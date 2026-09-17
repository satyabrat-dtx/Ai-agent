# DB2ADMIN.LOGTOLATTRIBUTES

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 13
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 210111

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TOLENTITIESTERMSOFLOGCMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `TOLENTITIESTERMSOFLOGORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 2 | `TOLENTITIESTERMSOFLOGCODE` | CHAR(2) | NOT NULL |  |  |  |
| 3 | `TOLENTITIESTOLENTITYNAME` | CHAR(50) | NOT NULL |  |  |  |
| 4 | `TOLATTRIBUTEFIELDNAME` | VARCHAR(120) | NOT NULL |  |  |  |
| 5 | `IGNOREME` | CHAR(1) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 7 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 8 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 9 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 10 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 11 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 12 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGTOLATTRIBUTES.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.TOLENTITIESTERMSOFLOGCMYCODE,
       t.TOLENTITIESTERMSOFLOGORDERTYPE,
       t.TOLENTITIESTERMSOFLOGCODE,
       t.TOLENTITIESTOLENTITYNAME,
       t.TOLATTRIBUTEFIELDNAME,
       t.IGNOREME,
       t.ABSUNIQUEID,
       t.LOGTIMESTAMP,
       t.LOGOPERATION,
       t.LOGUSER,
       t.UUID,
       t.FATHERID
FROM   DB2ADMIN.LOGTOLATTRIBUTES t
FETCH FIRST 100 ROWS ONLY;
```
