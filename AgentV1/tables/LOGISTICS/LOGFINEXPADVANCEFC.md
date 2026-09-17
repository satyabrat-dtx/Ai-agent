# DB2ADMIN.LOGFINEXPADVANCEFC

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 30
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 202248

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINEXPADVANCECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINEXPADVANCECODE` | CHAR(5) | NOT NULL |  |  |  |
| 2 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `ADVANCENO` | CHAR(5) |  |  |  |  |
| 4 | `BANKREFNO` | CHAR(20) |  |  |  |  |
| 5 | `DUEDATE` | DATE |  |  |  |  |
| 6 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 7 | `FCUNUTILISED` | DECIMAL(18,5) |  |  |  |  |
| 8 | `ADJUSTBILL` | DECIMAL(18,5) |  |  |  |  |
| 9 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `FCAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `FCNO` | CHAR(10) |  |  |  |  |
| 12 | `MARKETRATE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `BANKCHARGESUSD` | DECIMAL(18,5) |  |  |  |  |
| 14 | `INRVALUE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `TOTALUSD` | DECIMAL(18,5) |  |  |  |  |
| 16 | `TOTALINR` | DECIMAL(18,5) |  |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 25 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 26 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 27 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 28 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 29 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINEXPADVANCEFC.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINEXPADVANCECOMPANYCODE,
       t.FINEXPADVANCECODE,
       t.LINENO,
       t.ADVANCENO,
       t.BANKREFNO,
       t.DUEDATE,
       t.RATE,
       t.FCUNUTILISED,
       t.ADJUSTBILL,
       t.AMOUNT,
       t.FCAMOUNT,
       t.FCNO
FROM   DB2ADMIN.LOGFINEXPADVANCEFC t
FETCH FIRST 100 ROWS ONLY;
```
