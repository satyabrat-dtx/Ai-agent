# DB2ADMIN.LOGSALESDOCUMENTLINECHARGE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 39
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 54587

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALDOCLINESALDOCCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALDOCLINESALDOCPRVCNTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `SALDOCLINESALDOCPRVCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `SALESDOCUMENTLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `SALESDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `SALDOCLINECOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 6 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 7 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 10 | `CHARGETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 12 | `CHARGECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 13 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 15 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 16 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 17 | `DEFSALCHRDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 18 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 19 | `DOCUMENTLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 20 | `DOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 21 | `DOCUMENTLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 22 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 23 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 24 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 29 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 30 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 31 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 32 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 33 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 34 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 35 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 36 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 37 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 38 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESDOCUMENTLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESDOCUMENTLINE' + known child suffix 'CHARGE')
  - JOIN predicate: `LOGSALESDOCUMENTLINECHARGE.FATHERID = LOGSALESDOCUMENTLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.SALDOCLINESALDOCCOMPANYCODE,
       t.SALDOCLINESALDOCPRVCNTCODE,
       t.SALDOCLINESALDOCPRVCODE,
       t.SALESDOCUMENTLINEORDERLINE,
       t.SALESDOCUMENTLINEORDERSUBLINE,
       t.SALDOCLINECOMPONENTORDERLINE,
       t.NUMBERID,
       t.SEQUENCE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE,
       t.VALUE
FROM   DB2ADMIN.LOGSALESDOCUMENTLINECHARGE t
FETCH FIRST 100 ROWS ONLY;
```
