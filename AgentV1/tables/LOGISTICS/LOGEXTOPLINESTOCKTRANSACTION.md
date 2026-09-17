# DB2ADMIN.LOGEXTOPLINESTOCKTRANSACTION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 49
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 208325

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EOLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `EOLCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `EOLCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `EOLLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `EOLRESCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 5 | `EOLRESCODE` | CHAR(15) | NOT NULL |  |  |  |
| 6 | `EOLRESLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 7 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 8 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 9 | `EXTOPLINECANCELLED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `UPDEOLCANCELLEDQUANTITIES` | SMALLINT | NOT NULL |  |  |  |
| 11 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 12 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 14 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 16 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 18 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 20 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `ORGTRANSTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 27 | `ORGTRANSTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 28 | `RESSTUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `RESSTBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `RESSTUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `RESSTBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 32 | `RESSTUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 34 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 35 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
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

- `FATHERID` → **LOGEXTOPLINE**.`ABSUNIQUEID` (medium confidence — name = 'LOGEXTOPLINE' + recurring fragment 'STOCKTRANSACTION' (seen in 5 tables))
  - JOIN predicate: `LOGEXTOPLINESTOCKTRANSACTION.FATHERID = LOGEXTOPLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.EOLCOMPANYCODE,
       t.EOLCOUNTERCODE,
       t.EOLCODE,
       t.EOLLINE,
       t.EOLRESCOUNTERCODE,
       t.EOLRESCODE,
       t.EOLRESLINE,
       t.STOCKTRNTRANSACTIONNUMBER,
       t.STOCKTRNTRNDETAILNUMBER,
       t.EXTOPLINECANCELLED,
       t.UPDEOLCANCELLEDQUANTITIES,
       t.USERPRIMARYUOMCODE
FROM   DB2ADMIN.LOGEXTOPLINESTOCKTRANSACTION t
FETCH FIRST 100 ROWS ONLY;
```
