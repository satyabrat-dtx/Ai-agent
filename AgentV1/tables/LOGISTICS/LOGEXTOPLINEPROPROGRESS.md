# DB2ADMIN.LOGEXTOPLINEPROPROGRESS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 38
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 208768

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EOLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `EOLCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `EOLCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `EOLLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `PROGRESSNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 5 | `PROGRESSDELETED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ISQUEUEPROGRESS` | SMALLINT | NOT NULL |  |  |  |
| 7 | `EXTOPLINECANCELLED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `PDEDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `PDEDEMANDCODE` | CHAR(15) |  |  |  |  |
| 10 | `PDEITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 11 | `PDEELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 12 | `PDEELEMENTCODE` | CHAR(15) |  |  |  |  |
| 13 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `PRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 15 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `SECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 17 | `PACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `PACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `USEDPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `USEDSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `USEDPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 23 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 24 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
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

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEXTOPLINEPROPROGRESS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.EOLCOMPANYCODE,
       t.EOLCOUNTERCODE,
       t.EOLCODE,
       t.EOLLINE,
       t.PROGRESSNUMBER,
       t.PROGRESSDELETED,
       t.ISQUEUEPROGRESS,
       t.EXTOPLINECANCELLED,
       t.PDEDEMANDCOUNTERCODE,
       t.PDEDEMANDCODE,
       t.PDEITEMTYPEAFICODE,
       t.PDEELEMENTSUBCODEKEY
FROM   DB2ADMIN.LOGEXTOPLINEPROPROGRESS t
FETCH FIRST 100 ROWS ONLY;
```
