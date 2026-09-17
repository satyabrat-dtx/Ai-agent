# DB2ADMIN.LOGADVANCEDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 30
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 219123

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ADVANCECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `ADVANCEPURORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `ADVANCEPURCHASEORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `ADVANCELINENO` | INTEGER | NOT NULL |  |  |  |
| 4 | `LINENO` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 5 | `PURINVDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 6 | `PURINVORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `PURINVORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 8 | `PURINVCODE` | CHAR(25) |  |  |  |  |
| 9 | `PURINVINVOICEDATE` | DATE |  |  |  |  |
| 10 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 11 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 12 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 13 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 14 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 15 | `TDSAPPLICABLEAMT` | DECIMAL(15,5) |  |  |  |  |
| 16 | `TDSAMT` | DECIMAL(15,5) |  |  |  |  |
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

- `FATHERID` → **LOGADVANCE**.`ABSUNIQUEID` (high confidence — name = 'LOGADVANCE' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGADVANCEDETAIL.FATHERID = LOGADVANCE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.ADVANCECOMPANYCODE,
       t.ADVANCEPURORDERCOUNTERCODE,
       t.ADVANCEPURCHASEORDERCODE,
       t.ADVANCELINENO,
       t.LINENO,
       t.PURINVDIVISIONCODE,
       t.PURINVORDPRNCSMSUPPLIERTYPE,
       t.PURINVORDPRNCSMSUPPLIERCODE,
       t.PURINVCODE,
       t.PURINVINVOICEDATE,
       t.FINDOCBUSINESSUNITCODE,
       t.FINDOCFINANCIALYEARCODE
FROM   DB2ADMIN.LOGADVANCEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
