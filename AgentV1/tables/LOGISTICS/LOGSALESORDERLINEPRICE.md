# DB2ADMIN.LOGSALESORDERLINEPRICE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 32
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 55795

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALORDLINESALORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALORDLINESALORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `SALESORDERLINESALESORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `SALESORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `SALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `SALORDLINECOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 6 | `QUALITYLEVELITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `QUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 8 | `SOURCEPRICETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `NUMBERLINEID` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 10 | `COMPOUNDPRICETYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `PRICETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `PRICEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 14 | `PRICESIGN` | CHAR(2) | NOT NULL |  |  |  |
| 15 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 16 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 17 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 23 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 24 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 25 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 26 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 31 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESORDERLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESORDERLINE' + known child suffix 'PRICE')
  - JOIN predicate: `LOGSALESORDERLINEPRICE.FATHERID = LOGSALESORDERLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.SALORDLINESALORDERCOMPANYCODE,
       t.SALORDLINESALORDERCOUNTERCODE,
       t.SALESORDERLINESALESORDERCODE,
       t.SALESORDERLINEORDERLINE,
       t.SALESORDERLINEORDERSUBLINE,
       t.SALORDLINECOMPONENTORDERLINE,
       t.QUALITYLEVELITEMTYPECODE,
       t.QUALITYLEVELCODE,
       t.SOURCEPRICETYPE,
       t.NUMBERLINEID,
       t.COMPOUNDPRICETYPECODE,
       t.PRICETYPE
FROM   DB2ADMIN.LOGSALESORDERLINEPRICE t
FETCH FIRST 100 ROWS ONLY;
```
