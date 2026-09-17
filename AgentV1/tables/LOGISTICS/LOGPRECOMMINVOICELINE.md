# DB2ADMIN.LOGPRECOMMINVOICELINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 72
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 217069

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PRECOMMINVOICECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PRECOMMINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `PRECOMMINVOICECODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `PIREFNO` | BIGINT | NOT NULL |  |  |  |
| 4 | `PILINE` | INTEGER | NOT NULL |  |  |  |
| 5 | `INVOICEDATE` | DATE |  |  |  |  |
| 6 | `INVOICELINENO` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 7 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 10 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `BUYERSPOREFNO` | CHAR(100) |  |  |  |  |
| 15 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 21 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 22 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 23 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 25 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `SECONDARYUMCODE` | CHAR(3) |  |  |  |  |
| 27 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 28 | `PACKINGUMCODE` | CHAR(3) |  |  |  |  |
| 29 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 30 | `ORDERPRICE` | DECIMAL(18,5) |  |  |  |  |
| 31 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 33 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 34 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 35 | `PRICELISTORDERTYPE` | CHAR(1) |  |  |  |  |
| 36 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 37 | `INVOICECURRENCYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 38 | `COMPANYCURRENCYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 39 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 40 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 41 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 42 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 43 | `INPUTCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 44 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 45 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 46 | `WIDTH` | DECIMAL(18,5) |  |  |  |  |
| 47 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 48 | `SIONCODE` | CHAR(15) |  |  |  |  |
| 49 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 50 | `SOLINEABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 51 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 52 | `CBM` | DECIMAL(15,5) |  |  |  |  |
| 53 | `NUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 54 | `LCORDERLINELINENO` | INTEGER | NOT NULL |  |  |  |
| 55 | `LCORDERLINELCDETAILLCNO` | CHAR(35) |  |  |  |  |
| 56 | `LCORDERLINELCDETAILLCDATE` | DATE |  |  |  |  |
| 57 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 58 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 59 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 60 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 61 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 62 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 63 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 64 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 65 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 66 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 67 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 68 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 69 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 70 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 71 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGPRECOMMINVOICE**.`ABSUNIQUEID` (high confidence — name = 'LOGPRECOMMINVOICE' + known child suffix 'LINE')
  - JOIN predicate: `LOGPRECOMMINVOICELINE.FATHERID = LOGPRECOMMINVOICE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.PRECOMMINVOICECOMPANYCODE,
       t.PRECOMMINVOICEDIVISIONCODE,
       t.PRECOMMINVOICECODE,
       t.PIREFNO,
       t.PILINE,
       t.INVOICEDATE,
       t.INVOICELINENO,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03
FROM   DB2ADMIN.LOGPRECOMMINVOICELINE t
FETCH FIRST 100 ROWS ONLY;
```
