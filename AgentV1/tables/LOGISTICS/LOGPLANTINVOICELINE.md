# DB2ADMIN.LOGPLANTINVOICELINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 79
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 141657

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PLANTINVOICECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `PLANTINVOICECODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `INVOICEDATE` | DATE |  |  |  |  |
| 4 | `INVOICELINENO` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 17 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 18 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 19 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 20 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 21 | `INPUTCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 22 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 23 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 27 | `SECONDARYUMCODE` | CHAR(3) |  |  |  |  |
| 28 | `PACKINGUMCODE` | CHAR(3) |  |  |  |  |
| 29 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `BASESECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `BASEPRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 32 | `BASESECONDARYUMCODE` | CHAR(3) |  |  |  |  |
| 33 | `WIDTH` | DECIMAL(18,5) |  |  |  |  |
| 34 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 35 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 36 | `NUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 37 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 38 | `ORDERPRICE` | DECIMAL(18,5) |  |  |  |  |
| 39 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 40 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 41 | `PRICELISTORDERTYPE` | CHAR(1) |  |  |  |  |
| 42 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 43 | `INVOICECURRENCYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 44 | `COMPANYCURRENCYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 45 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 46 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 47 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 48 | `SIONCODE` | CHAR(15) |  |  |  |  |
| 49 | `SOLINEABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 50 | `LCORDERLINELINENO` | INTEGER | NOT NULL |  |  |  |
| 51 | `LCORDERLINELCDETAILLCNO` | CHAR(35) |  |  |  |  |
| 52 | `LCORDERLINELCDETAILLCDATE` | DATE |  |  |  |  |
| 53 | `ARTICLERATE1` | DECIMAL(18,5) |  |  |  |  |
| 54 | `ARTICLERATE2` | DECIMAL(18,5) |  |  |  |  |
| 55 | `ARTICLERATE3` | DECIMAL(18,5) |  |  |  |  |
| 56 | `ALCODE` | CHAR(30) |  |  |  |  |
| 57 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 58 | `ADVANCELICENSENO` | CHAR(30) |  |  |  |  |
| 59 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 60 | `EPCGEPCGAPPLICATIONCODE` | CHAR(30) |  |  |  |  |
| 61 | `EPCGAPPLICATIONDATE` | DATE |  |  |  |  |
| 62 | `EPCGLICENSENO` | CHAR(30) |  |  |  |  |
| 63 | `EPCGLICENSEDATE` | DATE |  |  |  |  |
| 64 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 65 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 66 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 67 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 68 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 69 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 70 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 71 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 72 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 73 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 74 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 75 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 76 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 77 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 78 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGPLANTINVOICE**.`ABSUNIQUEID` (high confidence — name = 'LOGPLANTINVOICE' + known child suffix 'LINE')
  - JOIN predicate: `LOGPLANTINVOICELINE.FATHERID = LOGPLANTINVOICE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.PLANTINVOICECOMPANYCODE,
       t.PLANTINVOICEDIVISIONCODE,
       t.PLANTINVOICECODE,
       t.INVOICEDATE,
       t.INVOICELINENO,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.LOGPLANTINVOICELINE t
FETCH FIRST 100 ROWS ONLY;
```
