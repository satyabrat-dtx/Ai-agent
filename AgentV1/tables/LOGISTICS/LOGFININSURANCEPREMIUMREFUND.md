# DB2ADMIN.LOGFININSURANCEPREMIUMREFUND

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 38
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 223366

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
| 9 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 10 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 11 | `FISCALYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 12 | `FISCALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 13 | `EXCESSPREMIUMAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 14 | `INSURANCEEXPGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 15 | `INSURANCEEXPGLCODE` | CHAR(20) |  |  |  |  |
| 16 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 18 | `POSTINGDATE` | DATE |  |  |  |  |
| 19 | `REMARKS` | CHAR(100) |  |  |  |  |
| 20 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 21 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 22 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 23 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 24 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 32 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 33 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 34 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 35 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 36 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 37 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFININSURANCEPREMIUMREFUND.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

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
       t.PROFITCENTERPROFITCENTERCODE,
       t.COSTCENTERCOSTCENTERCODE,
       t.FISCALYEARCOMPANYCODE
FROM   DB2ADMIN.LOGFININSURANCEPREMIUMREFUND t
FETCH FIRST 100 ROWS ONLY;
```
