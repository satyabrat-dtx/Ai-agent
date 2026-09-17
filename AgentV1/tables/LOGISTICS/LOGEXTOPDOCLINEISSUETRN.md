# DB2ADMIN.LOGEXTOPDOCLINEISSUETRN

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 38
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216512

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EDLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `EDLPRVCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `EDLPRVCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `EDLLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `EOLCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 5 | `EOLCODE` | CHAR(15) | NOT NULL |  |  |  |
| 6 | `EOLLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 7 | `EOLRESCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 8 | `EOLRESCODE` | CHAR(15) | NOT NULL |  |  |  |
| 9 | `EOLRESLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 10 | `EOLISSUETRANSACTIONNR` | CHAR(15) | NOT NULL |  |  |  |
| 11 | `EOLISSUETRANSDETNR` | INTEGER | NOT NULL |  |  |  |
| 12 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 13 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 15 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 17 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 21 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
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

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEXTOPDOCLINEISSUETRN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.EDLCOMPANYCODE,
       t.EDLPRVCOUNTERCODE,
       t.EDLPRVCODE,
       t.EDLLINE,
       t.EOLCOUNTERCODE,
       t.EOLCODE,
       t.EOLLINE,
       t.EOLRESCOUNTERCODE,
       t.EOLRESCODE,
       t.EOLRESLINE,
       t.EOLISSUETRANSACTIONNR,
       t.EOLISSUETRANSDETNR
FROM   DB2ADMIN.LOGEXTOPDOCLINEISSUETRN t
FETCH FIRST 100 ROWS ONLY;
```
