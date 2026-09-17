# DB2ADMIN.LOGFINPCEXTLETTER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 19
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 224151

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINPACKINGCREDITCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINPACKINGCREDITLETTERNO` | CHAR(5) | NOT NULL |  |  |  |
| 2 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `EXTENDEDDUEDATE` | DATE |  |  |  |  |
| 4 | `EXTENDEDINTERESTRATE` | DECIMAL(5,2) |  |  |  |  |
| 5 | `NARRATION` | CHAR(50) |  |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 14 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 15 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 16 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 17 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 18 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINPCEXTLETTER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINPACKINGCREDITCOMPANYCODE,
       t.FINPACKINGCREDITLETTERNO,
       t.LINENO,
       t.EXTENDEDDUEDATE,
       t.EXTENDEDINTERESTRATE,
       t.NARRATION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.LOGFINPCEXTLETTER t
FETCH FIRST 100 ROWS ONLY;
```
