# DB2ADMIN.LOGITEMSTLINKALLOWEDVALUE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 35
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 210394

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ITEMSTLINKLINKITEMTYPECMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `ITEMSTLINKLINKITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `ITEMSTLINKLINKPOSITION` | INTEGER | NOT NULL |  |  |  |
| 3 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 14 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 15 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 16 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 17 | `SAMPLE` | SMALLINT | NOT NULL |  |  |  |
| 18 | `OBSOLETE` | SMALLINT | NOT NULL |  |  |  |
| 19 | `PROTOTYPETEMPORARY` | SMALLINT | NOT NULL |  |  |  |
| 20 | `APPROVALSTATUS` | INTEGER | NOT NULL |  |  |  |
| 21 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
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

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGITEMSTLINKALLOWEDVALUE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.ITEMSTLINKLINKITEMTYPECMYCODE,
       t.ITEMSTLINKLINKITEMTYPECODE,
       t.ITEMSTLINKLINKPOSITION,
       t.PROTOTYPE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.LOGITEMSTLINKALLOWEDVALUE t
FETCH FIRST 100 ROWS ONLY;
```
