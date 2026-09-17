# DB2ADMIN.LOGSALESRELEASELINECHARGE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 35
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 56106

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESRELEASELINECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALESRELEASELINECODE` | CHAR(15) | NOT NULL |  |  |  |
| 2 | `SALESRELEASELINELINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 3 | `SALESRELEASELINESUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 4 | `SALRELEASELINECMPRELEASELINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 6 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 7 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 9 | `CHARGETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 11 | `CHARGECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 12 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 15 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 16 | `DEFSALCHRDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 17 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 18 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 19 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 20 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 26 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 27 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 28 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 29 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 32 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 33 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 34 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESRELEASELINE**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESRELEASELINE' + known child suffix 'CHARGE')
  - JOIN predicate: `LOGSALESRELEASELINECHARGE.FATHERID = LOGSALESRELEASELINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.SALESRELEASELINECOMPANYCODE,
       t.SALESRELEASELINECODE,
       t.SALESRELEASELINELINE,
       t.SALESRELEASELINESUBLINE,
       t.SALRELEASELINECMPRELEASELINE,
       t.NUMBERID,
       t.SEQUENCE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE,
       t.VALUE,
       t.CHARGECURRENCYCODE
FROM   DB2ADMIN.LOGSALESRELEASELINECHARGE t
FETCH FIRST 100 ROWS ONLY;
```
