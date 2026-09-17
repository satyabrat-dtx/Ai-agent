# DB2ADMIN.LOGEXTOPLINESUPWHSTRN

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 40
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 210145

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPLINECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `EXTOPLINECOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `EXTOPLINECODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 5 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 6 | `ORGSTOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 7 | `ORGSTOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 8 | `EXTOPLINECANCELLED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ENTITYTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `ENTITYNUMBER` | CHAR(15) |  |  |  |  |
| 11 | `ENTITYDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 12 | `ORGENTITYNUMBER` | CHAR(15) |  |  |  |  |
| 13 | `ORGENTITYDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 14 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 15 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 17 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 21 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 23 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 25 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 26 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 27 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 28 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 29 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 30 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 31 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 32 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 34 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 35 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 36 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 37 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 38 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 39 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEXTOPLINESUPWHSTRN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.EXTOPLINECOMPANYCODE,
       t.EXTOPLINECOUNTERCODE,
       t.EXTOPLINECODE,
       t.EXTOPLINEORDERLINE,
       t.STOCKTRNTRANSACTIONNUMBER,
       t.STOCKTRNTRNDETAILNUMBER,
       t.ORGSTOCKTRNTRANSACTIONNUMBER,
       t.ORGSTOCKTRNTRNDETAILNUMBER,
       t.EXTOPLINECANCELLED,
       t.ENTITYTYPE,
       t.ENTITYNUMBER,
       t.ENTITYDETAILNUMBER
FROM   DB2ADMIN.LOGEXTOPLINESUPWHSTRN t
FETCH FIRST 100 ROWS ONLY;
```
