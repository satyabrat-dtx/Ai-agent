# DB2ADMIN.LOGSALESORDERLINEDISCOUNT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 53
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 55721

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
| 6 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 7 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 8 | `DISCOUNTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 11 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `TAXAPPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 15 | `EXCLUDEDINCMSCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 16 | `EXCLUDEDINCOMMISSIONRETRIEVING` | SMALLINT | NOT NULL |  |  |  |
| 17 | `DISCOUNTGROUPCODE` | CHAR(3) |  |  |  |  |
| 18 | `PAYMENTDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 19 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `FREEGIFTDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 21 | `FREEGIFTDISCOUNTEQUALITEMSOLD` | SMALLINT | NOT NULL |  |  |  |
| 22 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 23 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 24 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 34 | `DEFSALDSCDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 35 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 36 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 37 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 38 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 39 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 40 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 41 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 42 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 43 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 44 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 45 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 46 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 47 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 48 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 49 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 50 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 51 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 52 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESORDERLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESORDERLINE' + known child suffix 'DISCOUNT')
  - JOIN predicate: `LOGSALESORDERLINEDISCOUNT.FATHERID = LOGSALESORDERLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.SALORDLINESALORDERCOMPANYCODE,
       t.SALORDLINESALORDERCOUNTERCODE,
       t.SALESORDERLINESALESORDERCODE,
       t.SALESORDERLINEORDERLINE,
       t.SALESORDERLINEORDERSUBLINE,
       t.SALORDLINECOMPONENTORDERLINE,
       t.NUMBERID,
       t.SEQUENCE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN
FROM   DB2ADMIN.LOGSALESORDERLINEDISCOUNT t
FETCH FIRST 100 ROWS ONLY;
```
