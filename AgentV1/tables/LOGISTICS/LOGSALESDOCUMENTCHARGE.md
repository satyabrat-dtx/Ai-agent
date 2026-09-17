# DB2ADMIN.LOGSALESDOCUMENTCHARGE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 36
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 54173

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALDOCPROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `SALESDOCUMENTPROVISIONALCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 4 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 7 | `CHARGETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `CHARGECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 10 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 13 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `DEFSALCHRDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 15 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 16 | `SALESDOCUMENTLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 17 | `SALESDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 18 | `SALDOCLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 19 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 20 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 21 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 27 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 28 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 29 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 30 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 32 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 33 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 34 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 35 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESDOCUMENT' + known child suffix 'CHARGE')
  - JOIN predicate: `LOGSALESDOCUMENTCHARGE.FATHERID = LOGSALESDOCUMENT.ABSUNIQUEID`

## Starter query

```sql
SELECT t.SALESDOCUMENTCOMPANYCODE,
       t.SALDOCPROVISIONALCOUNTERCODE,
       t.SALESDOCUMENTPROVISIONALCODE,
       t.NUMBERID,
       t.SEQUENCE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE,
       t.VALUE,
       t.CHARGECURRENCYCODE,
       t.SIGN,
       t.CALCULATIONTYPE
FROM   DB2ADMIN.LOGSALESDOCUMENTCHARGE t
FETCH FIRST 100 ROWS ONLY;
```
