# DB2ADMIN.LOGADSTORAGE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 22
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 106588

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 1 | `NAMEENTITYNAME` | CHAR(50) | NOT NULL |  |  |  |
| 2 | `NAMENAME` | CHAR(50) | NOT NULL |  |  |  |
| 3 | `FIELDNAME` | VARCHAR(120) | NOT NULL |  |  |  |
| 4 | `KEYSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 5 | `SHARED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `DATATYPE` | INTEGER | NOT NULL |  |  |  |
| 7 | `VALUESTRING` | VARCHAR(250) |  |  |  |  |
| 8 | `VALUEINT` | INTEGER | NOT NULL |  |  |  |
| 9 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 10 | `VALUEDATE` | DATE |  |  |  |  |
| 11 | `VALUEDECIMAL` | DECIMAL(18,5) |  |  |  |  |
| 12 | `VALUELONG` | BIGINT | NOT NULL |  |  |  |
| 13 | `VALUETIME` | TIME |  |  |  |  |
| 14 | `VALUETIMESTAMP` | TIMESTAMP |  |  |  |  |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 16 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 17 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 18 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 19 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 20 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 21 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGADSTORAGE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.UNIQUEID,
       t.NAMEENTITYNAME,
       t.NAMENAME,
       t.FIELDNAME,
       t.KEYSEQUENCE,
       t.SHARED,
       t.DATATYPE,
       t.VALUESTRING,
       t.VALUEINT,
       t.VALUEBOOLEAN,
       t.VALUEDATE,
       t.VALUEDECIMAL
FROM   DB2ADMIN.LOGADSTORAGE t
FETCH FIRST 100 ROWS ONLY;
```
