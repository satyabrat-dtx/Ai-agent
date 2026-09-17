# DB2ADMIN.LOGSALESDOCUMENTLINEDISCOUNT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 57
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 54647

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
| 34 | `DOCUMENTLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 35 | `DOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 36 | `DOCUMENTLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 37 | `DEFSALDSCDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 38 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 39 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 40 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 41 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 42 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 43 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 44 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 45 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 46 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 47 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 48 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 49 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 50 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 51 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 52 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 53 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 54 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 55 | `ADVANCEINVOICEDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 56 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESDOCUMENTLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESDOCUMENTLINE' + known child suffix 'DISCOUNT')
  - JOIN predicate: `LOGSALESDOCUMENTLINEDISCOUNT.FATHERID = LOGSALESDOCUMENTLINE.ABSUNIQUEID`

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
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN
FROM   DB2ADMIN.LOGSALESDOCUMENTLINEDISCOUNT t
FETCH FIRST 100 ROWS ONLY;
```
