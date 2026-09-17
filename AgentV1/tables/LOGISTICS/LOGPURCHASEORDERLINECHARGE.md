# DB2ADMIN.LOGPURCHASEORDERLINECHARGE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 33
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 53315

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURORDLINEPURORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PURORDLINEPURORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `PURORDERLINEPURCHASEORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `PURCHASEORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `PURCHASEORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 6 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 7 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 9 | `CHARGETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 11 | `CHARGECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 12 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 15 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 16 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 17 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 18 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 24 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 25 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 26 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 27 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 29 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 30 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 31 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 32 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGPURCHASEORDERLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGPURCHASEORDERLINE' + known child suffix 'CHARGE')
  - JOIN predicate: `LOGPURCHASEORDERLINECHARGE.FATHERID = LOGPURCHASEORDERLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.PURORDLINEPURORDERCOMPANYCODE,
       t.PURORDLINEPURORDERCOUNTERCODE,
       t.PURORDERLINEPURCHASEORDERCODE,
       t.PURCHASEORDERLINEORDERLINE,
       t.PURCHASEORDERLINEORDERSUBLINE,
       t.NUMBERID,
       t.SEQUENCE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE,
       t.VALUE,
       t.CHARGECURRENCYCODE
FROM   DB2ADMIN.LOGPURCHASEORDERLINECHARGE t
FETCH FIRST 100 ROWS ONLY;
```
