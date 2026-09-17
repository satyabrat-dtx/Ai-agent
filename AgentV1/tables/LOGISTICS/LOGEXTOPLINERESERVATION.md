# DB2ADMIN.LOGEXTOPLINERESERVATION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 56
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 210914

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPLINECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `EXTOPLINECOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `EXTOPLINECODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `RESERVATIONORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 5 | `RESERVATIONORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 6 | `RESERVATIONRESERVATIONLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 7 | `EXTOPLINECANCELLED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 10 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 12 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 13 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 23 | `VARIANTCODE` | CHAR(20) |  |  |  |  |
| 24 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 25 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 26 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 30 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 32 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 34 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 36 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 37 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 38 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 39 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 40 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 41 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 42 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 43 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 44 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 45 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 46 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 47 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 48 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 49 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 50 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 51 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 52 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 53 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 54 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 55 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGEXTOPLINE**.`ABSUNIQUEID` (medium confidence — name = 'LOGEXTOPLINE' + recurring fragment 'RESERVATION' (seen in 6 tables))
  - JOIN predicate: `LOGEXTOPLINERESERVATION.FATHERID = LOGEXTOPLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.EXTOPLINECOMPANYCODE,
       t.EXTOPLINECOUNTERCODE,
       t.EXTOPLINECODE,
       t.EXTOPLINEORDERLINE,
       t.RESERVATIONORDERCOUNTERCODE,
       t.RESERVATIONORDERCODE,
       t.RESERVATIONRESERVATIONLINE,
       t.EXTOPLINECANCELLED,
       t.WAREHOUSECOMPANYCODE,
       t.WAREHOUSECODE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE
FROM   DB2ADMIN.LOGEXTOPLINERESERVATION t
FETCH FIRST 100 ROWS ONLY;
```
