# DB2ADMIN.LOGLINEREPORTDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 49
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 102868

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINEREPORTCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `CODE` | CHAR(4) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(100) |  |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `REPORTTYPE` | CHAR(3) |  |  |  |  |
| 6 | `LINETYPE` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `SUMMARIZATIONCODE` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `DIALOGCODE` | CHAR(1) |  |  |  |  |
| 9 | `PRINTCODE` | CHAR(2) |  |  |  |  |
| 10 | `ALTERNATIVELINECODE` | CHAR(4) |  |  |  |  |
| 11 | `ALTLINEBASEONSUM` | SMALLINT | NOT NULL |  |  |  |
| 12 | `HUNDREDPERCENTLINE` | SMALLINT | NOT NULL |  |  |  |
| 13 | `LEVEL1` | CHAR(2) |  |  |  |  |
| 14 | `LEVEL2` | CHAR(2) |  |  |  |  |
| 15 | `LEVEL3` | CHAR(2) |  |  |  |  |
| 16 | `LEVEL4` | CHAR(2) |  |  |  |  |
| 17 | `LEVEL5` | CHAR(2) |  |  |  |  |
| 18 | `LINELEVEL` | CHAR(10) |  |  |  |  |
| 19 | `OPERATOR01` | CHAR(1) |  |  |  |  |
| 20 | `LINE01CODE` | CHAR(4) |  |  |  |  |
| 21 | `OPERATOR02` | CHAR(1) |  |  |  |  |
| 22 | `LINE02CODE` | CHAR(4) |  |  |  |  |
| 23 | `OPERATOR03` | CHAR(1) |  |  |  |  |
| 24 | `LINE03CODE` | CHAR(4) |  |  |  |  |
| 25 | `OPERATOR04` | CHAR(1) |  |  |  |  |
| 26 | `LINE04CODE` | CHAR(4) |  |  |  |  |
| 27 | `OPERATOR05` | CHAR(1) |  |  |  |  |
| 28 | `LINE05CODE` | CHAR(4) |  |  |  |  |
| 29 | `OPERATOR06` | CHAR(1) |  |  |  |  |
| 30 | `LINE06CODE` | CHAR(4) |  |  |  |  |
| 31 | `OPERATOR07` | CHAR(1) |  |  |  |  |
| 32 | `LINE07CODE` | CHAR(4) |  |  |  |  |
| 33 | `OPERATOR08` | CHAR(1) |  |  |  |  |
| 34 | `LINE08CODE` | CHAR(4) |  |  |  |  |
| 35 | `OPERATOR09` | CHAR(1) |  |  |  |  |
| 36 | `LINE09CODE` | CHAR(4) |  |  |  |  |
| 37 | `OPERATOR10` | CHAR(1) |  |  |  |  |
| 38 | `LINE10CODE` | CHAR(4) |  |  |  |  |
| 39 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 40 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 41 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 42 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 43 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 44 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 45 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 46 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |
| 47 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 48 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGLINEREPORT**.`ABSUNIQUEID` (high confidence — name = 'LOGLINEREPORT' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGLINEREPORTDETAIL.FATHERID = LOGLINEREPORT.ABSUNIQUEID`

## Starter query

```sql
SELECT t.LINEREPORTCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.REPORTTYPE,
       t.LINETYPE,
       t.SUMMARIZATIONCODE,
       t.DIALOGCODE,
       t.PRINTCODE,
       t.ALTERNATIVELINECODE,
       t.ALTLINEBASEONSUM
FROM   DB2ADMIN.LOGLINEREPORTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
