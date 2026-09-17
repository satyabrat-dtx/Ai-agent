# DB2ADMIN.LOGSALESORDERASSORTMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 52
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 54883

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `SALESORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 4 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 6 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 18 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 19 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `ORDERUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 21 | `ORDERUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `ORDERBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 23 | `ORDERBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `ORDERUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 25 | `ORDERUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `ORDERBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 27 | `ORDERBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 28 | `ORDERUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 29 | `ORDERUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 31 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 32 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 33 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 34 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 35 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 36 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 37 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 38 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 39 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 40 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 41 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 42 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 43 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 44 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 45 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 46 | `PREVIOUSUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `PREVIOUSUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 48 | `PREVIOUSUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `PREVIOUSUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `PREVIOUSUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `PREVIOUSUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESORDER' + known child suffix 'ASSORTMENT')
  - JOIN predicate: `LOGSALESORDERASSORTMENT.FATHERID = LOGSALESORDER.ABSUNIQUEID`

## Starter query

```sql
SELECT t.SALESORDERCOMPANYCODE,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.NUMBERID,
       t.LINETEMPLATECODE,
       t.SEQUENCE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.LOGSALESORDERASSORTMENT t
FETCH FIRST 100 ROWS ONLY;
```
