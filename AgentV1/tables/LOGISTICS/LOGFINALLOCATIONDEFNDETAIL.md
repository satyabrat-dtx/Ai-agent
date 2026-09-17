# DB2ADMIN.LOGFINALLOCATIONDEFNDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 49
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 224660

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINALLOCATIONDEFNCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINALLOCATIONDEFNCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `FINALLOCATIONDEFNMAINSEQUENCE` | DECIMAL(8,0) | NOT NULL |  |  |  |
| 3 | `FINALLOCATIONDEFNSUBSEQUENCE` | DECIMAL(8,0) | NOT NULL |  |  |  |
| 4 | `FINALLOCATIONDEFNFROMDATE` | DATE | NOT NULL |  |  |  |
| 5 | `LINESEQUENCE` | DECIMAL(8,0) | NOT NULL |  |  |  |
| 6 | `UGGUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `UGGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `UGGCODE` | CHAR(10) |  |  |  |  |
| 9 | `FACTOR` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 10 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 11 | `PROFITCENTREPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 12 | `COSTCENTRECOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 13 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `GLCODE` | CHAR(20) |  |  |  |  |
| 15 | `FIRSTSEGUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `FIRSTSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `FIRSTSEGCODE` | CHAR(10) |  |  |  |  |
| 18 | `SNDSEGUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `SNDSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `SECONDSEGCODE` | CHAR(10) |  |  |  |  |
| 21 | `THIRDSEGUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `THIRDSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `THIRDSEGCODE` | CHAR(10) |  |  |  |  |
| 24 | `FRSEGUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `FRSEGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 26 | `FOURTHSEGCODE` | CHAR(10) |  |  |  |  |
| 27 | `FIFTHSEGUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `FIFTHSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 29 | `FIFTHSEGCODE` | CHAR(10) |  |  |  |  |
| 30 | `SIXTHSEGUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `SIXTHSEGUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 32 | `SIXTHSEGCODE` | CHAR(10) |  |  |  |  |
| 33 | `SESEGUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 34 | `SESEGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 35 | `SEVENTHSEGCODE` | CHAR(10) |  |  |  |  |
| 36 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 37 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 38 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 39 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 40 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 41 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 42 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 43 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 44 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 45 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 46 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 47 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 48 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINALLOCATIONDEFN**.`ABSUNIQUEID` (high confidence — name = 'LOGFINALLOCATIONDEFN' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGFINALLOCATIONDEFNDETAIL.FATHERID = LOGFINALLOCATIONDEFN.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FINALLOCATIONDEFNCOMPANYCODE,
       t.FINALLOCATIONDEFNCODE,
       t.FINALLOCATIONDEFNMAINSEQUENCE,
       t.FINALLOCATIONDEFNSUBSEQUENCE,
       t.FINALLOCATIONDEFNFROMDATE,
       t.LINESEQUENCE,
       t.UGGUGENGROUPTYPECOMPANYCODE,
       t.UGGUSERGENERICGROUPTYPECODE,
       t.UGGCODE,
       t.FACTOR,
       t.BUSINESSUNITCODE,
       t.PROFITCENTREPROFITCENTERCODE
FROM   DB2ADMIN.LOGFINALLOCATIONDEFNDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
