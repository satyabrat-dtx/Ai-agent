# DB2ADMIN.LOGEXTOPLINEDISCOUNT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 30
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 206333

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPLINECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `EXTOPLINECOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `EXTOPLINECODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 5 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 6 | `DISCOUNTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 8 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 9 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `TAXAPPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 13 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 15 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 16 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
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

- `FATHERID` → **LOGEXTOPLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGEXTOPLINE' + known child suffix 'DISCOUNT')
  - JOIN predicate: `LOGEXTOPLINEDISCOUNT.FATHERID = LOGEXTOPLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.EXTOPLINECOMPANYCODE,
       t.EXTOPLINECOUNTERCODE,
       t.EXTOPLINECODE,
       t.EXTOPLINEORDERLINE,
       t.NUMBERID,
       t.SEQUENCE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN,
       t.TAXAPPLICATIONTYPE,
       t.CALCULATIONTYPE
FROM   DB2ADMIN.LOGEXTOPLINEDISCOUNT t
FETCH FIRST 100 ROWS ONLY;
```
