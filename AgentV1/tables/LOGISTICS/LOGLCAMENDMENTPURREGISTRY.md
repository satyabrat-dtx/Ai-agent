# DB2ADMIN.LOGLCAMENDMENTPURREGISTRY

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 33
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 220118

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LCDETAILPURCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `LCDETAILPURDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `LCDETAILPURLCNO` | CHAR(35) | NOT NULL |  |  |  |
| 3 | `LCDETAILPURLCDATE` | DATE | NOT NULL |  |  |  |
| 4 | `LCAMENDMENTNO` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 5 | `LCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 6 | `AMENDMENTDATE` | DATE |  |  |  |  |
| 7 | `LCAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `UTILIZEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `AMENDMARGINAMT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `LCOPENINGCHARGES` | DECIMAL(15,5) |  |  |  |  |
| 11 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 12 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 13 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 14 | `REMARKS` | VARCHAR(100) |  |  |  |  |
| 15 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 16 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 17 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 18 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 19 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 27 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 28 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 29 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 30 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 31 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 32 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGLCAMENDMENTPURREGISTRY.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.LCDETAILPURCOMPANYCODE,
       t.LCDETAILPURDIVISIONCODE,
       t.LCDETAILPURLCNO,
       t.LCDETAILPURLCDATE,
       t.LCAMENDMENTNO,
       t.LCVALUE,
       t.AMENDMENTDATE,
       t.LCAMOUNT,
       t.UTILIZEDAMOUNT,
       t.AMENDMARGINAMT,
       t.LCOPENINGCHARGES,
       t.TAXTEMPLATETEMPLATETYPE
FROM   DB2ADMIN.LOGLCAMENDMENTPURREGISTRY t
FETCH FIRST 100 ROWS ONLY;
```
