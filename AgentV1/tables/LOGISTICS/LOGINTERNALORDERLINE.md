# DB2ADMIN.LOGINTERNALORDERLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 91
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 52158

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTERNALORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `INTERNALORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `INTERNALORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 5 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 7 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 8 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 9 | `ASSORTMENTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 10 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 12 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 14 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 24 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 25 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 26 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 27 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 30 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 32 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 34 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 36 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 37 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `CANCELLEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `CANCELLEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `CANCELLEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 41 | `CANCELLEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 42 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 44 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 46 | `LINESTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 47 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 48 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 49 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 50 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 51 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 52 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 53 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 54 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 55 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 56 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 57 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 58 | `JOINEDORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 59 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 60 | `LINESOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 61 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 62 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 63 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 64 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 65 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 66 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 67 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 68 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 69 | `CONDITIONRETRIEVINGDATE` | DATE | NOT NULL |  |  |  |
| 70 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 71 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 72 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 73 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 74 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 75 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 76 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 77 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 78 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 79 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 80 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 81 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 82 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 83 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 84 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 85 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 86 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 87 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 88 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 89 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 90 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGINTERNALORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGINTERNALORDER' + known child suffix 'LINE')
  - JOIN predicate: `LOGINTERNALORDERLINE.FATHERID = LOGINTERNALORDER.ABSUNIQUEID`
- child `LOGINTERNALORDERLINEBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGINTERNALORDERLINETEMPLATE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.INTERNALORDERCOMPANYCODE,
       t.INTERNALORDERCOUNTERCODE,
       t.INTERNALORDERCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.ASSORTMENTNUMBERID,
       t.LINETEMPLATECODE,
       t.ITEMTYPEAFICODE
FROM   DB2ADMIN.LOGINTERNALORDERLINE t
FETCH FIRST 100 ROWS ONLY;
```
