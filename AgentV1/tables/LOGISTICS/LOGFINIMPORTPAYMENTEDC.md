# DB2ADMIN.LOGFINIMPORTPAYMENTEDC

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 21
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203541

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINIMPORTEDCHARGESCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINIMPORTEDCHARGESCODE` | CHAR(15) | NOT NULL |  |  |  |
| 2 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `BANKREFERENCENUMBER` | CHAR(50) |  |  |  |  |
| 4 | `DUEDATEFROM` | DATE |  |  |  |  |
| 5 | `FCNO` | CHAR(3) |  |  |  |  |
| 6 | `RATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 7 | `ADJUSTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `UTILISEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `RATEDIFF` | DECIMAL(18,5) |  |  |  |  |
| 11 | `IMPORTPAYMENT` | CHAR(8) | NOT NULL |  |  |  |
| 12 | `BANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 13 | `POSTED` | SMALLINT | NOT NULL |  |  |  |
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

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINIMPORTPAYMENTEDC.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINIMPORTEDCHARGESCOMPANYCODE,
       t.FINIMPORTEDCHARGESCODE,
       t.LINENO,
       t.BANKREFERENCENUMBER,
       t.DUEDATEFROM,
       t.FCNO,
       t.RATE,
       t.ADJUSTEDAMOUNT,
       t.UTILISEDVALUE,
       t.VALUE,
       t.RATEDIFF,
       t.IMPORTPAYMENT
FROM   DB2ADMIN.LOGFINIMPORTPAYMENTEDC t
FETCH FIRST 100 ROWS ONLY;
```
