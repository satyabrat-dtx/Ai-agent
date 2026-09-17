# DB2ADMIN.LOGFINNSUBVENTIONENTRY

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 26
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203583

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINEXPNEGOTIATIONCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINEXPNEGOTIATIONCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `INTERESTRATE` | DECIMAL(5,2) |  |  |  |  |
| 3 | `INTERESTGLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `INTERESTGLCODE` | CHAR(20) | NOT NULL |  |  |  |
| 5 | `INTERESTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `POSTINGDATE` | DATE |  |  |  |  |
| 7 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 8 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 9 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 10 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 11 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 12 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 21 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 22 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 23 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 24 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 25 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINNSUBVENTIONENTRY.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINEXPNEGOTIATIONCOMPANYCODE,
       t.FINEXPNEGOTIATIONCODE,
       t.INTERESTRATE,
       t.INTERESTGLCOMPANYCODE,
       t.INTERESTGLCODE,
       t.INTERESTAMOUNT,
       t.POSTINGDATE,
       t.FINDOCBUSINESSUNITCODE,
       t.FINDOCFINANCIALYEARCODE,
       t.FINDOCTEMPLATECODE,
       t.FINDOCSTATISTICALGROUPCODE,
       t.FINDOCCODE
FROM   DB2ADMIN.LOGFINNSUBVENTIONENTRY t
FETCH FIRST 100 ROWS ONLY;
```
