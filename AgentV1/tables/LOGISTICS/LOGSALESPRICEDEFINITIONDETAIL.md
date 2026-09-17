# DB2ADMIN.LOGSALESPRICEDEFINITIONDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 26
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 116510

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALPRICEDEFINITIONCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALESPRICEDEFINITIONNUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 2 | `QUALITYLEVELITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 4 | `BREAKDOWNLIMIT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 5 | `SOURCEPRICETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `NUMBERLINEID` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 7 | `COMPOUNDPRICETYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `PRICETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `PRICEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 11 | `PRICESIGN` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 19 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 20 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 21 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 22 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 25 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESPRICEDEFINITION**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESPRICEDEFINITION' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGSALESPRICEDEFINITIONDETAIL.FATHERID = LOGSALESPRICEDEFINITION.ABSUNIQUEID`

## Starter query

```sql
SELECT t.SALPRICEDEFINITIONCOMPANYCODE,
       t.SALESPRICEDEFINITIONNUMBERID,
       t.QUALITYLEVELITEMTYPECODE,
       t.QUALITYLEVELCODE,
       t.BREAKDOWNLIMIT,
       t.SOURCEPRICETYPE,
       t.NUMBERLINEID,
       t.COMPOUNDPRICETYPECODE,
       t.PRICETYPE,
       t.PRICE,
       t.PRICEPERCENTAGE,
       t.PRICESIGN
FROM   DB2ADMIN.LOGSALESPRICEDEFINITIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
