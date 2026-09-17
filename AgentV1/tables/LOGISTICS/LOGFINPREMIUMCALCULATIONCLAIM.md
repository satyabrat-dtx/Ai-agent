# DB2ADMIN.LOGFINPREMIUMCALCULATIONCLAIM

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 39
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 223425

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINPREMIUMCLCCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINPREMIUMCLCEMPLOYEETYPE` | CHAR(5) | NOT NULL |  |  |  |
| 2 | `FINPREMIUMCALCULATIONRISKTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `FINPREMIUMCALCULATIONENTRYDATE` | DATE | NOT NULL |  |  |  |
| 4 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 5 | `BUGROUPCODE` | CHAR(10) |  |  |  |  |
| 6 | `CLAIMAPPLIED` | DECIMAL(18,5) |  |  |  |  |
| 7 | `CLAIMRECEIVED` | DECIMAL(18,5) |  |  |  |  |
| 8 | `NCBPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 9 | `RECEIVEDDATE` | DATE |  |  |  |  |
| 10 | `REMARKS` | VARCHAR(500) |  |  |  |  |
| 11 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 12 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 13 | `CLAIMAPPLIEDGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `CLAIMAPPLIEDGLCODE` | CHAR(20) |  |  |  |  |
| 15 | `CLAIMRECIEVEDGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `CLAIMRECIEVEDGLCODE` | CHAR(20) |  |  |  |  |
| 17 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 18 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 19 | `FLAG` | CHAR(15) |  |  |  |  |
| 20 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 27 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 28 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 29 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 30 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 31 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 33 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 34 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 35 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 36 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 37 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 38 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINPREMIUMCALCULATION**.`ABSUNIQUEID` (medium confidence — name = 'LOGFINPREMIUMCALCULATION' + recurring fragment 'CLAIM' (seen in 7 tables))
  - JOIN predicate: `LOGFINPREMIUMCALCULATIONCLAIM.FATHERID = LOGFINPREMIUMCALCULATION.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FINPREMIUMCLCCOMPANYCODE,
       t.FINPREMIUMCLCEMPLOYEETYPE,
       t.FINPREMIUMCALCULATIONRISKTYPE,
       t.FINPREMIUMCALCULATIONENTRYDATE,
       t.LINENO,
       t.BUGROUPCODE,
       t.CLAIMAPPLIED,
       t.CLAIMRECEIVED,
       t.NCBPERCENTAGE,
       t.RECEIVEDDATE,
       t.REMARKS,
       t.PROFITCENTERPROFITCENTERCODE
FROM   DB2ADMIN.LOGFINPREMIUMCALCULATIONCLAIM t
FETCH FIRST 100 ROWS ONLY;
```
