# DB2ADMIN.LOGFINLOANREPAYMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 23
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 230678

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINLOANMASTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINLMLTEUGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `FINLOANMASTERLOANTYPECODE` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `FINLOANMASTERLOANNO` | CHAR(10) | NOT NULL |  |  |  |
| 4 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 5 | `SLNO` | INTEGER | NOT NULL |  |  |  |
| 6 | `NUMBEROFREPAYMENTS` | DECIMAL(3,0) |  |  |  |  |
| 7 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `STARTDATE` | DATE |  |  |  |  |
| 9 | `ENDDATE` | DATE |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 18 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 19 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 20 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 21 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 22 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINLOANREPAYMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINLOANMASTERCOMPANYCODE,
       t.FINLMLTEUGENERICGROUPTYPECODE,
       t.FINLOANMASTERLOANTYPECODE,
       t.FINLOANMASTERLOANNO,
       t.ABSVERSIONNUMBER,
       t.SLNO,
       t.NUMBEROFREPAYMENTS,
       t.AMOUNT,
       t.STARTDATE,
       t.ENDDATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.LOGFINLOANREPAYMENT t
FETCH FIRST 100 ROWS ONLY;
```
