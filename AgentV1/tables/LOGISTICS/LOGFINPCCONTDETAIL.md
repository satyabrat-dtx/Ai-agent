# DB2ADMIN.LOGFINPCCONTDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 27
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 228451

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINPACKINGCREDITCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINPACKINGCREDITLETTERNO` | CHAR(5) | NOT NULL |  |  |  |
| 2 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `CONTRACTTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `CONTRACTNUMBERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `CONTRACTNUMBERCODE` | CHAR(15) |  |  |  |  |
| 6 | `SALESORDERITEMNOORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `SALESORDERITEMNOORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `SALORDINOCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `SUBLEDGERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `SUBLEDGERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `SCHDATE` | DATE |  |  |  |  |
| 12 | `CONTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `CONTRACTSTATUS` | CHAR(1) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 22 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 23 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 24 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 25 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 26 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINPCCONTDETAIL.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINPACKINGCREDITCOMPANYCODE,
       t.FINPACKINGCREDITLETTERNO,
       t.LINENO,
       t.CONTRACTTYPECODE,
       t.CONTRACTNUMBERCOUNTERCODE,
       t.CONTRACTNUMBERCODE,
       t.SALESORDERITEMNOORDERLINE,
       t.SALESORDERITEMNOORDERSUBLINE,
       t.SALORDINOCOMPONENTORDERLINE,
       t.SUBLEDGERCUSTOMERSUPPLIERTYPE,
       t.SUBLEDGERCUSTOMERSUPPLIERCODE,
       t.SCHDATE
FROM   DB2ADMIN.LOGFINPCCONTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
