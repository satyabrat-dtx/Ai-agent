# DB2ADMIN.LOGFINLOANSCHEDULE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 24
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 223782

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINLRFINLOANMASTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINLRFINLMLTEUGENGRPTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `FINLRFINLMASTERLOANTYPECODE` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `FINLRFINLOANMASTERLOANNO` | CHAR(10) | NOT NULL |  |  |  |
| 4 | `FINLOANREPAYMENTSLNO` | INTEGER | NOT NULL |  |  |  |
| 5 | `SLNO` | INTEGER | NOT NULL |  |  |  |
| 6 | `STARTDATE` | DATE |  |  |  |  |
| 7 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `SANCTIONSCHEDULE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `PAIDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `PENDINGAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 19 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 20 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 21 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 22 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 23 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINLOANSCHEDULE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINLRFINLOANMASTERCOMPANYCODE,
       t.FINLRFINLMLTEUGENGRPTYPECODE,
       t.FINLRFINLMASTERLOANTYPECODE,
       t.FINLRFINLOANMASTERLOANNO,
       t.FINLOANREPAYMENTSLNO,
       t.SLNO,
       t.STARTDATE,
       t.AMOUNT,
       t.SANCTIONSCHEDULE,
       t.PAIDAMOUNT,
       t.PENDINGAMOUNT,
       t.CREATIONDATETIME
FROM   DB2ADMIN.LOGFINLOANSCHEDULE t
FETCH FIRST 100 ROWS ONLY;
```
