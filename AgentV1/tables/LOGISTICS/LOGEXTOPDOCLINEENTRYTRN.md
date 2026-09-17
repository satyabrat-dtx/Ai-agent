# DB2ADMIN.LOGEXTOPDOCLINEENTRYTRN

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 35
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216571

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
| 7 | `EOLENTRYTRANSACTIONNR` | CHAR(15) | NOT NULL |  |  |  |
| 8 | `EOLENTRYTRANSDETNR` | INTEGER | NOT NULL |  |  |  |
| 9 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 10 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 12 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 14 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 16 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 18 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 20 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 21 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 29 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 30 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 31 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 32 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 33 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 34 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEXTOPDOCLINEENTRYTRN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.EDLCOMPANYCODE,
       t.EDLPRVCOUNTERCODE,
       t.EDLPRVCODE,
       t.EDLLINE,
       t.EOLCOUNTERCODE,
       t.EOLCODE,
       t.EOLLINE,
       t.EOLENTRYTRANSACTIONNR,
       t.EOLENTRYTRANSDETNR,
       t.USERPRIMARYUOMCODE,
       t.USERPRIMARYQUANTITY,
       t.BASEPRIMARYUOMCODE
FROM   DB2ADMIN.LOGEXTOPDOCLINEENTRYTRN t
FETCH FIRST 100 ROWS ONLY;
```
