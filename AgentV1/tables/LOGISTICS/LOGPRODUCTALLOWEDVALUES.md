# DB2ADMIN.LOGPRODUCTALLOWEDVALUES

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 23
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 210067

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PRDSPCSIZEPRODUCTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PRDSPCSIZEPRODUCTITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `PRDSPCSIZEPRODUCTSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 3 | `PRDSPCSIZEPRODUCTSUBCODE02` | CHAR(10) | NOT NULL |  |  |  |
| 4 | `PRDSPCSIZEPRODUCTSUBCODE03` | CHAR(10) | NOT NULL |  |  |  |
| 5 | `PRDSPCSIZEPRODUCTSUBCODE04` | CHAR(10) | NOT NULL |  |  |  |
| 6 | `PRDSPCSIZEPRODUCTSUBCODE05` | CHAR(10) | NOT NULL |  |  |  |
| 7 | `PRDSPCSIZEPRODUCTSUBCODE06` | CHAR(10) | NOT NULL |  |  |  |
| 8 | `PRDSPCSIZEPRODUCTSUBCODE07` | CHAR(10) | NOT NULL |  |  |  |
| 9 | `PRDSPCSIZEPRODUCTSUBCODE08` | CHAR(10) | NOT NULL |  |  |  |
| 10 | `PRDSPCSIZEPRODUCTSUBCODE09` | CHAR(10) | NOT NULL |  |  |  |
| 11 | `PRDSPCSIZEPRODUCTSUBCODE10` | CHAR(10) | NOT NULL |  |  |  |
| 12 | `HORIZONTALVALUE` | CHAR(10) | NOT NULL |  |  |  |
| 13 | `VERTICALVALUE` | CHAR(10) | NOT NULL |  |  |  |
| 14 | `ALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 18 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 19 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 20 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 21 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 22 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGPRODUCT**.`ABSUNIQUEID` (medium confidence — name = 'LOGPRODUCT' + recurring fragment 'ALLOWEDVALUES' (seen in 4 tables))
  - JOIN predicate: `LOGPRODUCTALLOWEDVALUES.FATHERID = LOGPRODUCT.ABSUNIQUEID`

## Starter query

```sql
SELECT t.PRDSPCSIZEPRODUCTCOMPANYCODE,
       t.PRDSPCSIZEPRODUCTITEMTYPECODE,
       t.PRDSPCSIZEPRODUCTSUBCODE01,
       t.PRDSPCSIZEPRODUCTSUBCODE02,
       t.PRDSPCSIZEPRODUCTSUBCODE03,
       t.PRDSPCSIZEPRODUCTSUBCODE04,
       t.PRDSPCSIZEPRODUCTSUBCODE05,
       t.PRDSPCSIZEPRODUCTSUBCODE06,
       t.PRDSPCSIZEPRODUCTSUBCODE07,
       t.PRDSPCSIZEPRODUCTSUBCODE08,
       t.PRDSPCSIZEPRODUCTSUBCODE09,
       t.PRDSPCSIZEPRODUCTSUBCODE10
FROM   DB2ADMIN.LOGPRODUCTALLOWEDVALUES t
FETCH FIRST 100 ROWS ONLY;
```
