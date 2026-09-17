# DB2ADMIN.LOGSALESRELEASELINEDISCOUNT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 52
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 56216

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESRELEASELINECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALESRELEASELINECODE` | CHAR(15) | NOT NULL |  |  |  |
| 2 | `SALESRELEASELINELINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 3 | `SALESRELEASELINESUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 4 | `SALRELEASELINECMPRELEASELINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 6 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 7 | `DISCOUNTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 10 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `TAXAPPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 14 | `EXCLUDEDINCMSCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 15 | `EXCLUDEDINCOMMISSIONRETRIEVING` | SMALLINT | NOT NULL |  |  |  |
| 16 | `DISCOUNTGROUPCODE` | CHAR(3) |  |  |  |  |
| 17 | `PAYMENTDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 18 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 19 | `FREEGIFTDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 20 | `FREEGIFTDISCOUNTEQUALITEMSOLD` | SMALLINT | NOT NULL |  |  |  |
| 21 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 22 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 23 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 33 | `DEFSALDSCDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 34 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 35 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 36 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 37 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 38 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 39 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 40 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 41 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 42 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 43 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 44 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 45 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 46 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 47 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 48 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 49 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 50 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 51 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESRELEASELINE**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESRELEASELINE' + known child suffix 'DISCOUNT')
  - JOIN predicate: `LOGSALESRELEASELINEDISCOUNT.FATHERID = LOGSALESRELEASELINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.SALESRELEASELINECOMPANYCODE,
       t.SALESRELEASELINECODE,
       t.SALESRELEASELINELINE,
       t.SALESRELEASELINESUBLINE,
       t.SALRELEASELINECMPRELEASELINE,
       t.NUMBERID,
       t.SEQUENCE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN,
       t.TAXAPPLICATIONTYPE
FROM   DB2ADMIN.LOGSALESRELEASELINEDISCOUNT t
FETCH FIRST 100 ROWS ONLY;
```
