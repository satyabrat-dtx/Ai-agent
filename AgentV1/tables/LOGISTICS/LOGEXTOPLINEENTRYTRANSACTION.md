# DB2ADMIN.LOGEXTOPLINEENTRYTRANSACTION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 46
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 212970

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPLINECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `EXTOPLINECOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `EXTOPLINECODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 5 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 6 | `EXTOPLINECANCELLED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SERVTRENTRYTRLINK` | DECIMAL(11,0) |  |  |  |  |
| 8 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 9 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 11 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 13 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 15 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 17 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `ORGTRANSTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 24 | `ORGTRANSTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 25 | `RESSTUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `RESSTBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `RESSTUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 28 | `RESSTBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `RESSTUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 31 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 32 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 33 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 34 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 35 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 36 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 37 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 38 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 39 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 40 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 41 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 42 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 43 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 44 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 45 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGEXTOPLINE**.`ABSUNIQUEID` (medium confidence — name = 'LOGEXTOPLINE' + recurring fragment 'ENTRYTRANSACTION' (seen in 4 tables))
  - JOIN predicate: `LOGEXTOPLINEENTRYTRANSACTION.FATHERID = LOGEXTOPLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.EXTOPLINECOMPANYCODE,
       t.EXTOPLINECOUNTERCODE,
       t.EXTOPLINECODE,
       t.EXTOPLINEORDERLINE,
       t.STOCKTRNTRANSACTIONNUMBER,
       t.STOCKTRNTRNDETAILNUMBER,
       t.EXTOPLINECANCELLED,
       t.SERVTRENTRYTRLINK,
       t.USERPRIMARYUOMCODE,
       t.USERPRIMARYQUANTITY,
       t.BASEPRIMARYUOMCODE,
       t.BASEPRIMARYQUANTITY
FROM   DB2ADMIN.LOGEXTOPLINEENTRYTRANSACTION t
FETCH FIRST 100 ROWS ONLY;
```
