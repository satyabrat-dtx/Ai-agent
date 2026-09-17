# DB2ADMIN.LOGTOLENTITIES

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 12
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 207153

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TERMSOFLOGCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `TERMSOFLOGORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 2 | `TERMSOFLOGCODE` | CHAR(2) | NOT NULL |  |  |  |
| 3 | `TOLENTITYNAME` | CHAR(50) | NOT NULL |  |  |  |
| 4 | `IGNOREME` | CHAR(1) |  |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 6 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 7 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 8 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 9 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 10 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 11 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGTOLENTITIES.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.TERMSOFLOGCOMPANYCODE,
       t.TERMSOFLOGORDERTYPE,
       t.TERMSOFLOGCODE,
       t.TOLENTITYNAME,
       t.IGNOREME,
       t.ABSUNIQUEID,
       t.LOGTIMESTAMP,
       t.LOGOPERATION,
       t.LOGUSER,
       t.UUID,
       t.FATHERID,
       t.LOGUPDATEDFIELDS
FROM   DB2ADMIN.LOGTOLENTITIES t
FETCH FIRST 100 ROWS ONLY;
```
