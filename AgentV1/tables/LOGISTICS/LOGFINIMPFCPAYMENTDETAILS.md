# DB2ADMIN.LOGFINIMPFCPAYMENTDETAILS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 18
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203250

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINIMPORTFCPAYMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINIMPORTFCPAYMENTCODE` | CHAR(5) | NOT NULL |  |  |  |
| 2 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `BANKREFERENCENUMBER` | CHAR(50) |  |  |  |  |
| 4 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 5 | `DUEDATEFROM` | DATE |  |  |  |  |
| 6 | `FCRATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 7 | `UTILISEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `ADJUSTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `FCNOCODE` | CHAR(5) |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 13 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 14 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 15 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 16 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 17 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINIMPFCPAYMENTDETAILS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINIMPORTFCPAYMENTCOMPANYCODE,
       t.FINIMPORTFCPAYMENTCODE,
       t.LINENO,
       t.BANKREFERENCENUMBER,
       t.CURRENCYCODE,
       t.DUEDATEFROM,
       t.FCRATE,
       t.UTILISEDVALUE,
       t.VALUE,
       t.ADJUSTEDAMOUNT,
       t.FCNOCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.LOGFINIMPFCPAYMENTDETAILS t
FETCH FIRST 100 ROWS ONLY;
```
