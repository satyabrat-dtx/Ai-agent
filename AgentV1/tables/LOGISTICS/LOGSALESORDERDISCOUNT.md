# DB2ADMIN.LOGSALESORDERDISCOUNT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 35
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 55319

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `SALESORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 4 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `DISCOUNTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 7 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 8 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `TAXAPPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 12 | `EXCLUDEDINCMSCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 13 | `EXCLUDEDINCOMMISSIONRETRIEVING` | SMALLINT | NOT NULL |  |  |  |
| 14 | `DISCOUNTGROUPCODE` | CHAR(3) |  |  |  |  |
| 15 | `PAYMENTDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 17 | `DEFSALDSCDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 18 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
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
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 32 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 33 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 34 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESORDER' + known child suffix 'DISCOUNT')
  - JOIN predicate: `LOGSALESORDERDISCOUNT.FATHERID = LOGSALESORDER.ABSUNIQUEID`

## Starter query

```sql
SELECT t.SALESORDERCOMPANYCODE,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.NUMBERID,
       t.SEQUENCE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN,
       t.TAXAPPLICATIONTYPE,
       t.CALCULATIONTYPE,
       t.AMOUNTCALCULATIONTYPE
FROM   DB2ADMIN.LOGSALESORDERDISCOUNT t
FETCH FIRST 100 ROWS ONLY;
```
