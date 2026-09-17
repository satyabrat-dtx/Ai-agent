# DB2ADMIN.LOGFINEXPNEXTSUBVENTION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 29
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 224571

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINEXPNEXTFINEXPNCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINEXPNEXTFINEXPNCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `FINEXPNEXTEXTENSIONBANKREFNO` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `FINEXPNEXTEXTENSIONBANKDATE` | DATE | NOT NULL |  |  |  |
| 4 | `FINEXPNEGOTIATIONEXTLINENO` | INTEGER | NOT NULL |  |  |  |
| 5 | `INTERESTRATE` | DECIMAL(5,2) |  |  |  |  |
| 6 | `INTERESTGLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `INTERESTGLCODE` | CHAR(20) | NOT NULL |  |  |  |
| 8 | `INTERESTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `POSTINGDATE` | DATE |  |  |  |  |
| 10 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 11 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 12 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 13 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 14 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 15 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 24 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 25 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 26 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 27 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 28 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINEXPNEXTSUBVENTION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINEXPNEXTFINEXPNCOMPANYCODE,
       t.FINEXPNEXTFINEXPNCODE,
       t.FINEXPNEXTEXTENSIONBANKREFNO,
       t.FINEXPNEXTEXTENSIONBANKDATE,
       t.FINEXPNEGOTIATIONEXTLINENO,
       t.INTERESTRATE,
       t.INTERESTGLCOMPANYCODE,
       t.INTERESTGLCODE,
       t.INTERESTAMOUNT,
       t.POSTINGDATE,
       t.FINDOCBUSINESSUNITCODE,
       t.FINDOCFINANCIALYEARCODE
FROM   DB2ADMIN.LOGFINEXPNEXTSUBVENTION t
FETCH FIRST 100 ROWS ONLY;
```
