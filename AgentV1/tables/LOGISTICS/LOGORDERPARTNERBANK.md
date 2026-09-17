# DB2ADMIN.LOGORDERPARTNERBANK

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 30
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 197533

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ORDPRNCSMSUPPLIERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 2 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 3 | `IDENTIFIER` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 4 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 5 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 6 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 7 | `EXTERNALBANKCODE` | CHAR(15) |  |  |  |  |
| 8 | `CINCODE` | CHAR(2) |  |  |  |  |
| 9 | `CURRENTACCOUNTID` | CHAR(30) |  |  |  |  |
| 10 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 11 | `ACCOUNTOWNER` | CHAR(100) |  |  |  |  |
| 12 | `BBAN` | CHAR(30) |  |  |  |  |
| 13 | `BIC` | CHAR(11) |  |  |  |  |
| 14 | `IBAN` | CHAR(34) |  |  |  |  |
| 15 | `PRIORITY` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 16 | `DIRECTDEBIT` | SMALLINT | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 25 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 26 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 27 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 28 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 29 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGORDERPARTNER**.`ABSUNIQUEID` (medium confidence — name = 'LOGORDERPARTNER' + recurring fragment 'BANK' (seen in 5 tables))
  - JOIN predicate: `LOGORDERPARTNERBANK.FATHERID = LOGORDERPARTNER.ABSUNIQUEID`

## Starter query

```sql
SELECT t.ORDPRNCSMSUPPLIERCOMPANYCODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.IDENTIFIER,
       t.BANKBANKCOUNTRYCODE,
       t.BANKCODE,
       t.BANKBRANCHCODE,
       t.EXTERNALBANKCODE,
       t.CINCODE,
       t.CURRENTACCOUNTID,
       t.CURRENCYCODE,
       t.ACCOUNTOWNER
FROM   DB2ADMIN.LOGORDERPARTNERBANK t
FETCH FIRST 100 ROWS ONLY;
```
