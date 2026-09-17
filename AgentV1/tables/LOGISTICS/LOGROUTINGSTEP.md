# DB2ADMIN.LOGROUTINGSTEP

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 69
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 56849

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ROUTINGCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `ROUTINGNUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 2 | `ROUTINGITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `ROUTINGSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 4 | `ROUTINGSUBCODE02` | CHAR(10) |  |  |  |  |
| 5 | `ROUTINGSUBCODE03` | CHAR(10) |  |  |  |  |
| 6 | `ROUTINGSUBCODE04` | CHAR(10) |  |  |  |  |
| 7 | `ROUTINGSUBCODE05` | CHAR(10) |  |  |  |  |
| 8 | `ROUTINGSUBCODE06` | CHAR(10) |  |  |  |  |
| 9 | `ROUTINGSUBCODE07` | CHAR(10) |  |  |  |  |
| 10 | `ROUTINGSUBCODE08` | CHAR(10) |  |  |  |  |
| 11 | `ROUTINGSUBCODE09` | CHAR(10) |  |  |  |  |
| 12 | `ROUTINGSUBCODE10` | CHAR(10) |  |  |  |  |
| 13 | `ROUTINGSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 14 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 15 | `SUBSEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 16 | `STEPINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 17 | `REFROUTINGSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 18 | `REFROUTINGSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 19 | `REFROUTINGSTATUS` | CHAR(2) |  |  |  |  |
| 20 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 21 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 22 | `WORKCENTERANDOPERATTRIBUTESCOD` | CHAR(20) |  |  |  |  |
| 23 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 24 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 25 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 26 | `STANDARDSTEPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `STANDARDSTEPQTYUOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 29 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 30 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 40 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 41 | `PRERULECODE` | CHAR(10) |  |  |  |  |
| 42 | `RULECODE` | CHAR(10) |  |  |  |  |
| 43 | `RULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 44 | `OVERLAPPINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 45 | `OVERLAPPINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `OVERLAPPINGUOMCATEGORY` | CHAR(1) |  |  |  |  |
| 47 | `INITIALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 48 | `FINALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 49 | `INITIALDATE` | DATE |  |  |  |  |
| 50 | `FINALDATE` | DATE |  |  |  |  |
| 51 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 52 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 53 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 54 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 55 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 56 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 57 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 58 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 59 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 60 | `ROUTINGITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 61 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 62 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 63 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 64 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 65 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 66 | `PROVISIONAL` | SMALLINT | NOT NULL |  |  |  |
| 67 | `RULEAPPLICABILITY` | INTEGER | NOT NULL |  |  |  |
| 68 | `PROTOTYPEBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGROUTING**.`ABSUNIQUEID` (high confidence — name = 'LOGROUTING' + known child suffix 'STEP')
  - JOIN predicate: `LOGROUTINGSTEP.FATHERID = LOGROUTING.ABSUNIQUEID`

## Starter query

```sql
SELECT t.ROUTINGCOMPANYCODE,
       t.ROUTINGNUMBERID,
       t.ROUTINGITEMTYPECODE,
       t.ROUTINGSUBCODE01,
       t.ROUTINGSUBCODE02,
       t.ROUTINGSUBCODE03,
       t.ROUTINGSUBCODE04,
       t.ROUTINGSUBCODE05,
       t.ROUTINGSUBCODE06,
       t.ROUTINGSUBCODE07,
       t.ROUTINGSUBCODE08,
       t.ROUTINGSUBCODE09
FROM   DB2ADMIN.LOGROUTINGSTEP t
FETCH FIRST 100 ROWS ONLY;
```
