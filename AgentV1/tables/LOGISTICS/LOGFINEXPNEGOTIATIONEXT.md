# DB2ADMIN.LOGFINEXPNEGOTIATIONEXT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 38
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 202766

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINEXPNEGOTIATIONCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINEXPNEGOTIATIONCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `EXTENSIONBANKREFNO` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `EXTENSIONBANKDATE` | DATE | NOT NULL |  |  |  |
| 4 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 5 | `NOOFDAYSEXTENDED` | INTEGER | NOT NULL |  |  |  |
| 6 | `DUEDATE` | DATE |  |  |  |  |
| 7 | `EXTENSIONINTERESTRATE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `NEGOTIATEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `EXTENSTIONINTERESTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `EXTENSIONINTERESTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `EXTENSIONINTERESTGLCODE` | CHAR(20) |  |  |  |  |
| 12 | `BANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 13 | `BANKCHARGESGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `BANKCHARGESGLCODE` | CHAR(20) |  |  |  |  |
| 15 | `OTHERCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 16 | `OTHERCHARGESGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `OTHERCHARGESGLCODE` | CHAR(20) |  |  |  |  |
| 18 | `CGST` | DECIMAL(18,5) |  |  |  |  |
| 19 | `CGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `CGSTGLCODE` | CHAR(20) |  |  |  |  |
| 21 | `SGST` | DECIMAL(18,5) |  |  |  |  |
| 22 | `SCGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `SCGSTGLCODE` | CHAR(20) |  |  |  |  |
| 24 | `POSTINGDATE` | DATE |  |  |  |  |
| 25 | `REMARKS` | VARCHAR(255) |  |  |  |  |
| 26 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 27 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 28 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 29 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 30 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
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

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINEXPNEGOTIATIONEXT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINEXPNEGOTIATIONCOMPANYCODE,
       t.FINEXPNEGOTIATIONCODE,
       t.EXTENSIONBANKREFNO,
       t.EXTENSIONBANKDATE,
       t.LINENO,
       t.NOOFDAYSEXTENDED,
       t.DUEDATE,
       t.EXTENSIONINTERESTRATE,
       t.NEGOTIATEDVALUE,
       t.EXTENSTIONINTERESTAMOUNT,
       t.EXTENSIONINTERESTGLCOMPANYCODE,
       t.EXTENSIONINTERESTGLCODE
FROM   DB2ADMIN.LOGFINEXPNEGOTIATIONEXT t
FETCH FIRST 100 ROWS ONLY;
```
