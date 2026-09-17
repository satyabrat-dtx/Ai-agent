# DB2ADMIN.LOGFINTRANSITDETAILOUT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 31
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 227012

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINPOLICYMASTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINPOLICYMBUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `FINPOLICYMPOLICYTEUGENGRPTECOD` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `FINPOLICYMASTERPOLICYTYPECODE` | CHAR(10) | NOT NULL |  |  |  |
| 4 | `FINPOLICYMINCMYCSMSUPTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `FINPOLICYMINCMYCSMSUPCODE` | CHAR(8) | NOT NULL |  |  |  |
| 6 | `FINPOLICYMASTERPOLICYNO` | CHAR(20) | NOT NULL |  |  |  |
| 7 | `FINPOLICYMASTERPOLICYDATE` | DATE | NOT NULL |  |  |  |
| 8 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 9 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 10 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 11 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `TYPE` | CHAR(1) |  |  |  |  |
| 13 | `INVOICENO` | CHAR(15) |  |  |  |  |
| 14 | `INVOICEDATE` | DATE |  |  |  |  |
| 15 | `ITEMTYPE` | CHAR(3) |  |  |  |  |
| 16 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `NETAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 25 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 26 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 27 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 28 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 29 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 30 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINTRANSITDETAILOUT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINPOLICYMASTERCOMPANYCODE,
       t.FINPOLICYMBUSINESSUNITCODE,
       t.FINPOLICYMPOLICYTEUGENGRPTECOD,
       t.FINPOLICYMASTERPOLICYTYPECODE,
       t.FINPOLICYMINCMYCSMSUPTYPE,
       t.FINPOLICYMINCMYCSMSUPCODE,
       t.FINPOLICYMASTERPOLICYNO,
       t.FINPOLICYMASTERPOLICYDATE,
       t.LINENO,
       t.FROMDATE,
       t.TODATE,
       t.AMOUNT
FROM   DB2ADMIN.LOGFINTRANSITDETAILOUT t
FETCH FIRST 100 ROWS ONLY;
```
