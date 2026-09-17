# DB2ADMIN.LOGMSEEXTOPLINEINFO

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 37
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216627

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPLINECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `EXTOPLINECOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `EXTOPLINECODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `SUPPLIERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `SUPPLIERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 6 | `CONFIRMEDDATE` | DATE |  |  |  |  |
| 7 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 8 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 10 | `DELIVERYDELAYINWRKDAYS` | INTEGER | NOT NULL |  |  |  |
| 11 | `DELIVERYDELAYINWEEKS` | DECIMAL(12,5) |  |  |  |  |
| 12 | `CONFIRMEDPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `TRANSACTIONPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `PRMDELIVEREDDELTAPERCENTAGE` | DECIMAL(18,3) | NOT NULL |  |  |  |
| 15 | `ORDERDATE` | DATE |  |  |  |  |
| 16 | `COMPLETIONDATE` | DATE |  |  |  |  |
| 17 | `COMPLETIONDAYS` | INTEGER | NOT NULL |  |  |  |
| 18 | `COMPLETIONWRKDAYS` | INTEGER | NOT NULL |  |  |  |
| 19 | `COMPLETIONWEEKS` | DECIMAL(12,5) |  |  |  |  |
| 20 | `CLOSED` | SMALLINT | NOT NULL |  |  |  |
| 21 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 23 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 24 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 25 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 26 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 27 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 28 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 32 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 33 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 34 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 35 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 36 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGMSEEXTOPLINEINFO.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.EXTOPLINECOMPANYCODE,
       t.EXTOPLINECOUNTERCODE,
       t.EXTOPLINECODE,
       t.EXTOPLINEORDERLINE,
       t.SUPPLIERTYPE,
       t.SUPPLIERCODE,
       t.CONFIRMEDDATE,
       t.TRANSACTIONDATE,
       t.TERMSOFDELIVERYCOMPANYCODE,
       t.TERMSOFDELIVERYCODE,
       t.DELIVERYDELAYINWRKDAYS,
       t.DELIVERYDELAYINWEEKS
FROM   DB2ADMIN.LOGMSEEXTOPLINEINFO t
FETCH FIRST 100 ROWS ONLY;
```
