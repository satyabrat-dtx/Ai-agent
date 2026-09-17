# DB2ADMIN.LOGFINBLNSLINETMPCALCULATION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 28
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 226064

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PARENTFINBLNSTMPCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PARENTFINBLNSHEETTEMPLATECODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `PARENTCODE` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `SERIALNUMBER` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 4 | `RESULTVARIABLE` | CHAR(10) | NOT NULL |  |  |  |
| 5 | `OPERATOR1TYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `OPERATORVARIABLE1C` | CHAR(10) |  |  |  |  |
| 7 | `OPERATORVARIABLE1N` | DECIMAL(11,4) |  |  |  |  |
| 8 | `OPERATORVARIABLE1RCODE` | CHAR(10) |  |  |  |  |
| 9 | `OPERATOR2TYPE` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `OPERATORVARIABLE2C` | CHAR(10) |  |  |  |  |
| 11 | `OPERATORVARIABLE2N` | DECIMAL(11,4) |  |  |  |  |
| 12 | `OPERATORVARIABLE2RCODE` | CHAR(10) |  |  |  |  |
| 13 | `OPERATOR` | INTEGER | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `STEP` | CHAR(1) |  |  |  |  |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 23 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 24 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 25 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 26 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 27 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINBLNSLINETMPCALCULATION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.PARENTFINBLNSTMPCOMPANYCODE,
       t.PARENTFINBLNSHEETTEMPLATECODE,
       t.PARENTCODE,
       t.SERIALNUMBER,
       t.RESULTVARIABLE,
       t.OPERATOR1TYPE,
       t.OPERATORVARIABLE1C,
       t.OPERATORVARIABLE1N,
       t.OPERATORVARIABLE1RCODE,
       t.OPERATOR2TYPE,
       t.OPERATORVARIABLE2C,
       t.OPERATORVARIABLE2N
FROM   DB2ADMIN.LOGFINBLNSLINETMPCALCULATION t
FETCH FIRST 100 ROWS ONLY;
```
