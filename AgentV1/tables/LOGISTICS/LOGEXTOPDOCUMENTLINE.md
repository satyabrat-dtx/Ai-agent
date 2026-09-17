# DB2ADMIN.LOGEXTOPDOCUMENTLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 89
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 207576

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `EXTOPDOCUMENTPROVCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `EXTOPDOCUMENTPROVISIONALCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 5 | `ORIGINTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 9 | `EXTERNOPLINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `EXTERNOPLINECODE` | CHAR(15) |  |  |  |  |
| 11 | `EXTERNOPLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 12 | `PRDRESERVATIONORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 13 | `PRDRESERVATIONORDERCODE` | CHAR(15) |  |  |  |  |
| 14 | `PRDRESERVATIONRESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 15 | `ELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `ELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 17 | `ELEMENTCODE` | CHAR(15) |  |  |  |  |
| 18 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 19 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 20 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 21 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 22 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 24 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 25 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 26 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 36 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 37 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 38 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 40 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 41 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 44 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 46 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `RECEIVEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 48 | `RECEIVEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `RECEIVEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `RECEIVEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `RECEIVEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `ORIGINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 54 | `ORIGINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `RECEIVINGDATE` | DATE |  |  |  |  |
| 56 | `LINESTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 57 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 58 | `RECEIVINGSTATUS` | CHAR(2) |  |  |  |  |
| 59 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 60 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 61 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 62 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 63 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 64 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 65 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 66 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 67 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 68 | `ISSUEMATERIALCOST` | DECIMAL(18,5) |  |  |  |  |
| 69 | `ISSUEMATERIALCOSTUOMCODE` | CHAR(3) |  |  |  |  |
| 70 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 71 | `QUANTITYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 72 | `LINESOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 73 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 74 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 75 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 76 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 77 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 78 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 79 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 80 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 81 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 82 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 83 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 84 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 85 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 86 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 87 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 88 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGEXTOPDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'LOGEXTOPDOCUMENT' + known child suffix 'LINE')
  - JOIN predicate: `LOGEXTOPDOCUMENTLINE.FATHERID = LOGEXTOPDOCUMENT.ABSUNIQUEID`

## Starter query

```sql
SELECT t.EXTOPDOCUMENTCOMPANYCODE,
       t.EXTOPDOCUMENTPROVCOUNTERCODE,
       t.EXTOPDOCUMENTPROVISIONALCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ORIGINTYPE,
       t.LINETEMPLATECODE,
       t.ORDERTYPE,
       t.ORDERLINE,
       t.EXTERNOPLINECOUNTERCODE,
       t.EXTERNOPLINECODE,
       t.EXTERNOPLINEORDERLINE
FROM   DB2ADMIN.LOGEXTOPDOCUMENTLINE t
FETCH FIRST 100 ROWS ONLY;
```
