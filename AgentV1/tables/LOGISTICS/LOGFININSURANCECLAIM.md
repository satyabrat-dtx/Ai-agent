# DB2ADMIN.LOGFININSURANCECLAIM

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 42
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 225662

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
| 9 | `CLAIMAPPLIED` | DECIMAL(18,5) |  |  |  |  |
| 10 | `CLAIMRECEIVED` | DECIMAL(18,5) |  |  |  |  |
| 11 | `NCBPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 12 | `RECEIVEDDATE` | DATE |  |  |  |  |
| 13 | `REMARKS` | VARCHAR(500) |  |  |  |  |
| 14 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 15 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 16 | `CLAIMAPPLIEDGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `CLAIMAPPLIEDGLCODE` | CHAR(20) |  |  |  |  |
| 18 | `CLAIMRECIEVEDGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `CLAIMRECIEVEDGLCODE` | CHAR(20) |  |  |  |  |
| 20 | `POSTINGDATE` | DATE |  |  |  |  |
| 21 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 22 | `FLAG` | CHAR(15) |  |  |  |  |
| 23 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 24 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 25 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 26 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 27 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 28 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 30 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 31 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 32 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 33 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 34 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 36 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 37 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 38 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 39 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 40 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 41 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFININSURANCECLAIM.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

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
       t.CLAIMAPPLIED,
       t.CLAIMRECEIVED,
       t.NCBPERCENTAGE
FROM   DB2ADMIN.LOGFININSURANCECLAIM t
FETCH FIRST 100 ROWS ONLY;
```
