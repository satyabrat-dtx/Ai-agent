# DB2ADMIN.LOGAPPROVALREQUESTDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 43
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 206021

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `APPROVALREQUESTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `APPROVALREQUESTREQUESTCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `APPROVALREQUESTVERSION` | INTEGER | NOT NULL |  |  |  |
| 3 | `LINENR` | INTEGER | NOT NULL |  |  |  |
| 4 | `SAMPLEREFERENCE` | CHAR(50) |  |  |  |  |
| 5 | `COLORDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 6 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `DEFINITIVECOLORCODE` | CHAR(10) |  |  |  |  |
| 19 | `DEFINITIVECOLORCODEDESCR` | VARCHAR(200) |  |  |  |  |
| 20 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 21 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 22 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 23 | `RESULT` | INTEGER | NOT NULL |  |  |  |
| 24 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 25 | `APPROVALDATE` | DATE |  |  |  |  |
| 26 | `APPROVALUSERUSERID` | CHAR(50) |  |  |  |  |
| 27 | `COMPANY` | CHAR(3) |  |  |  |  |
| 28 | `TYPE` | CHAR(3) |  |  |  |  |
| 29 | `CODE` | CHAR(10) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 30 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 31 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 32 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 33 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 34 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 35 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 36 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 37 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 38 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 39 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 40 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 41 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 42 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGAPPROVALREQUEST**.`ABSUNIQUEID` (high confidence — name = 'LOGAPPROVALREQUEST' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGAPPROVALREQUESTDETAIL.FATHERID = LOGAPPROVALREQUEST.ABSUNIQUEID`

## Starter query

```sql
SELECT t.APPROVALREQUESTCOMPANYCODE,
       t.APPROVALREQUESTREQUESTCODE,
       t.APPROVALREQUESTVERSION,
       t.LINENR,
       t.SAMPLEREFERENCE,
       t.COLORDESCRIPTION,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.LOGAPPROVALREQUESTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
