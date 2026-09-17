# DB2ADMIN.LOGDEVELOPMENTREQUESTDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 97
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 213202

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DEVELOPMENTREQUESTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `DEVELOPMENTREQUESTCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `DEVELOPMENTREQUESTCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `LINENR` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 4 | `MAIN` | SMALLINT | NOT NULL |  |  |  |
| 5 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `DRDETAILLINKLINENR` | DECIMAL(5,0) |  |  |  |  |
| 7 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `CODINGSUBCODE01` | CHAR(20) |  |  |  |  |
| 10 | `CODINGSUBCODE02` | CHAR(10) |  |  |  |  |
| 11 | `CODINGSUBCODE03` | CHAR(10) |  |  |  |  |
| 12 | `CODINGSUBCODE04` | CHAR(10) |  |  |  |  |
| 13 | `CODINGSUBCODE05` | CHAR(10) |  |  |  |  |
| 14 | `CODINGSUBCODE06` | CHAR(10) |  |  |  |  |
| 15 | `CODINGSUBCODE07` | CHAR(10) |  |  |  |  |
| 16 | `CODINGSUBCODE08` | CHAR(10) |  |  |  |  |
| 17 | `CODINGSUBCODE09` | CHAR(10) |  |  |  |  |
| 18 | `CODINGSUBCODE10` | CHAR(10) |  |  |  |  |
| 19 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 20 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 21 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 22 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `BASEUOMCODE` | CHAR(3) |  |  |  |  |
| 24 | `REQUESTEDDUEDATE` | DATE |  |  |  |  |
| 25 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 26 | `MAKEORBUY` | INTEGER | NOT NULL |  |  |  |
| 27 | `SUPPLIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 28 | `SUPPLIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 29 | `NOTE` | VARCHAR(200) |  |  |  |  |
| 30 | `CUSTOMERUNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 31 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 32 | `NEWBARCODE` | SMALLINT | NOT NULL |  |  |  |
| 33 | `EXTERNALBARCODEORIGIN` | SMALLINT | NOT NULL |  |  |  |
| 34 | `CUSTOMERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 35 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 36 | `BARTYPECODE` | CHAR(2) |  |  |  |  |
| 37 | `BARCODE` | VARCHAR(50) |  |  |  |  |
| 38 | `QRCODE` | CHAR(200) |  |  |  |  |
| 39 | `GRAPHICSINSTRUCTIONS` | VARCHAR(200) |  |  |  |  |
| 40 | `GRAPHICSSTATUS` | INTEGER | NOT NULL |  |  |  |
| 41 | `GRAPHICSAPPROVAL` | SMALLINT | NOT NULL |  |  |  |
| 42 | `GRAPHICSREJECT` | SMALLINT | NOT NULL |  |  |  |
| 43 | `GRAPHICSSUSPEND` | SMALLINT | NOT NULL |  |  |  |
| 44 | `PACKAGINGDETAIL` | VARCHAR(200) |  |  |  |  |
| 45 | `PACKAGINGSTATUS` | INTEGER | NOT NULL |  |  |  |
| 46 | `PACKAGINGAPPROVAL` | SMALLINT | NOT NULL |  |  |  |
| 47 | `PACKAGINGREJECT` | SMALLINT | NOT NULL |  |  |  |
| 48 | `PACKAGINGSUSPEND` | SMALLINT | NOT NULL |  |  |  |
| 49 | `REPLACEITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 50 | `REPLACEITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 51 | `REPLACESUBCODE01` | CHAR(20) |  |  |  |  |
| 52 | `REPLACESUBCODE02` | CHAR(10) |  |  |  |  |
| 53 | `REPLACESUBCODE03` | CHAR(10) |  |  |  |  |
| 54 | `REPLACESUBCODE04` | CHAR(10) |  |  |  |  |
| 55 | `REPLACESUBCODE05` | CHAR(10) |  |  |  |  |
| 56 | `REPLACESUBCODE06` | CHAR(10) |  |  |  |  |
| 57 | `REPLACESUBCODE07` | CHAR(10) |  |  |  |  |
| 58 | `REPLACESUBCODE08` | CHAR(10) |  |  |  |  |
| 59 | `REPLACESUBCODE09` | CHAR(10) |  |  |  |  |
| 60 | `REPLACESUBCODE10` | CHAR(10) |  |  |  |  |
| 61 | `GRAPHICSCOMPONENTKEY` | VARCHAR(250) |  |  |  |  |
| 62 | `GRAPHICSREASONKEY` | VARCHAR(250) |  |  |  |  |
| 63 | `PACKAGINGDEVELOPMENTKEY` | VARCHAR(250) |  |  |  |  |
| 64 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 65 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 66 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 67 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 68 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 69 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 70 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 71 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 72 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 73 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 74 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 75 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 76 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 77 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 78 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 79 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 80 | `PROTSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 81 | `PROTSUBCODE02` | CHAR(10) |  |  |  |  |
| 82 | `PROTSUBCODE03` | CHAR(10) |  |  |  |  |
| 83 | `PROTSUBCODE04` | CHAR(10) |  |  |  |  |
| 84 | `PROTSUBCODE05` | CHAR(10) |  |  |  |  |
| 85 | `PROTSUBCODE06` | CHAR(10) |  |  |  |  |
| 86 | `PROTSUBCODE07` | CHAR(10) |  |  |  |  |
| 87 | `PROTSUBCODE08` | CHAR(10) |  |  |  |  |
| 88 | `PROTSUBCODE09` | CHAR(10) |  |  |  |  |
| 89 | `PROTSUBCODE10` | CHAR(10) |  |  |  |  |
| 90 | `STRUCTURALINSTRUCTIONS` | VARCHAR(200) |  |  |  |  |
| 91 | `STRUCTURALSTATUS` | INTEGER | NOT NULL |  |  |  |
| 92 | `STRUCTURALAPPROVAL` | SMALLINT | NOT NULL |  |  |  |
| 93 | `STRUCTURALREJECT` | SMALLINT | NOT NULL |  |  |  |
| 94 | `STRUCTURALSUSPEND` | SMALLINT | NOT NULL |  |  |  |
| 95 | `STRUCTURALCOMPONENTKEY` | VARCHAR(250) |  |  |  |  |
| 96 | `STRUCTURALREASONKEY` | VARCHAR(250) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGDEVELOPMENTREQUEST**.`ABSUNIQUEID` (high confidence — name = 'LOGDEVELOPMENTREQUEST' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGDEVELOPMENTREQUESTDETAIL.FATHERID = LOGDEVELOPMENTREQUEST.ABSUNIQUEID`

## Starter query

```sql
SELECT t.DEVELOPMENTREQUESTCOMPANYCODE,
       t.DEVELOPMENTREQUESTCOUNTERCODE,
       t.DEVELOPMENTREQUESTCODE,
       t.LINENR,
       t.MAIN,
       t.PROTOTYPE,
       t.DRDETAILLINKLINENR,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.CODINGSUBCODE01,
       t.CODINGSUBCODE02,
       t.CODINGSUBCODE03
FROM   DB2ADMIN.LOGDEVELOPMENTREQUESTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
