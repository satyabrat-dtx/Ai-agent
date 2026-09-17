# DB2ADMIN.LOGCUSTOMINVOICELINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 77
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 136451

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CUSTOMINVOICECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `CUSTOMINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `CUSTOMINVOICECODE` | CHAR(20) | NOT NULL |  |  |  |
| 3 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 4 | `PLANTINVOICELINEINVOICELINENO` | DECIMAL(3,0) |  |  |  |  |
| 5 | `INVOICEDATE` | DATE |  |  |  |  |
| 6 | `INVOICELINENO` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 7 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `SUBCODE1` | CHAR(20) |  |  |  |  |
| 10 | `SUBCODE2` | CHAR(10) |  |  |  |  |
| 11 | `SUBCODE3` | CHAR(10) |  |  |  |  |
| 12 | `SUBCODE4` | CHAR(10) |  |  |  |  |
| 13 | `SUBCODE5` | CHAR(10) |  |  |  |  |
| 14 | `SUBCODE6` | CHAR(10) |  |  |  |  |
| 15 | `SUBCODE7` | CHAR(10) |  |  |  |  |
| 16 | `SUBCODE8` | CHAR(10) |  |  |  |  |
| 17 | `SUBCODE9` | CHAR(10) |  |  |  |  |
| 18 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 20 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 21 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 22 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 24 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `SECONDARYUMCODE` | CHAR(3) |  |  |  |  |
| 26 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `PACKINGUMCODE` | CHAR(3) |  |  |  |  |
| 28 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `BASEPRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 30 | `BASESECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `BASESECONDARYUMCODE` | CHAR(3) |  |  |  |  |
| 32 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 33 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 34 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 35 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 36 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 37 | `INVOICECURRENCYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 38 | `COMPANYCURRENCYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 39 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 40 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 41 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 42 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 43 | `INPUTCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 44 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 45 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 46 | `WIDTH` | DECIMAL(18,5) |  |  |  |  |
| 47 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 48 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 49 | `SOLINEABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 50 | `NUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 51 | `LCORDERLINELINENO` | INTEGER | NOT NULL |  |  |  |
| 52 | `LCORDERLINELCDETAILLCNO` | CHAR(35) |  |  |  |  |
| 53 | `LCORDERLINELCDETAILLCDATE` | DATE |  |  |  |  |
| 54 | `ALCODE` | CHAR(30) |  |  |  |  |
| 55 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 56 | `ADVANCELICENSENO` | CHAR(30) |  |  |  |  |
| 57 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 58 | `EPCGEPCGAPPLICATIONCODE` | CHAR(30) |  |  |  |  |
| 59 | `EPCGAPPLICATIONDATE` | DATE |  |  |  |  |
| 60 | `EPCGLICENSENO` | CHAR(30) |  |  |  |  |
| 61 | `EPCGLICENSEDATE` | DATE |  |  |  |  |
| 62 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 63 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 64 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 65 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 66 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 67 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 68 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 69 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 70 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 71 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 72 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 73 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 74 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 75 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 76 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGCUSTOMINVOICE**.`ABSUNIQUEID` (high confidence — name = 'LOGCUSTOMINVOICE' + known child suffix 'LINE')
  - JOIN predicate: `LOGCUSTOMINVOICELINE.FATHERID = LOGCUSTOMINVOICE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.CUSTOMINVOICECOMPANYCODE,
       t.CUSTOMINVOICEDIVISIONCODE,
       t.CUSTOMINVOICECODE,
       t.PLANTINVOICECODE,
       t.PLANTINVOICELINEINVOICELINENO,
       t.INVOICEDATE,
       t.INVOICELINENO,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE1,
       t.SUBCODE2,
       t.SUBCODE3
FROM   DB2ADMIN.LOGCUSTOMINVOICELINE t
FETCH FIRST 100 ROWS ONLY;
```
