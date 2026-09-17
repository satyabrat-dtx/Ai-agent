# DB2ADMIN.LOGCOMMERCIALINVOICELINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 81
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 135902

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMMERCIALINVOICECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `COMMERCIALINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `COMMERCIALINVOICECODE` | CHAR(20) | NOT NULL |  |  |  |
| 3 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 4 | `PLANTINVOICELINEINVOICELINENO` | DECIMAL(3,0) |  |  |  |  |
| 5 | `CUSTOMINVOICECODE` | CHAR(20) |  |  |  |  |
| 6 | `CUSTOMINVOICELINEINVOICELINENO` | DECIMAL(3,0) |  |  |  |  |
| 7 | `INVOICEDATE` | DATE |  |  |  |  |
| 8 | `INVOICELINENO` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 9 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `SUBCODE1` | CHAR(20) |  |  |  |  |
| 12 | `SUBCODE2` | CHAR(10) |  |  |  |  |
| 13 | `SUBCODE3` | CHAR(10) |  |  |  |  |
| 14 | `SUBCODE4` | CHAR(10) |  |  |  |  |
| 15 | `SUBCODE5` | CHAR(10) |  |  |  |  |
| 16 | `SUBCODE6` | CHAR(10) |  |  |  |  |
| 17 | `SUBCODE7` | CHAR(10) |  |  |  |  |
| 18 | `SUBCODE8` | CHAR(10) |  |  |  |  |
| 19 | `SUBCODE9` | CHAR(10) |  |  |  |  |
| 20 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 22 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 23 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 24 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 26 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `SECONDARYUMCODE` | CHAR(3) |  |  |  |  |
| 28 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `PACKINGUMCODE` | CHAR(3) |  |  |  |  |
| 30 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `BASEPRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 32 | `BASESECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `BASESECONDARYUMCODE` | CHAR(3) |  |  |  |  |
| 34 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 35 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 36 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 37 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 38 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 39 | `INVOICECURRENCYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 40 | `COMPANYCURRENCYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 41 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 42 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 43 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 44 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 45 | `INPUTCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 46 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 47 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 48 | `WIDTH` | DECIMAL(18,5) |  |  |  |  |
| 49 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 50 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 51 | `SOLINEABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 52 | `NUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 53 | `LCORDERLINELINENO` | INTEGER | NOT NULL |  |  |  |
| 54 | `LCORDERLINELCDETAILLCNO` | CHAR(35) |  |  |  |  |
| 55 | `LCORDERLINELCDETAILLCDATE` | DATE |  |  |  |  |
| 56 | `POLPOLICYNO` | CHAR(20) |  |  |  |  |
| 57 | `POLPOLICYDATE` | DATE |  |  |  |  |
| 58 | `ALCODE` | CHAR(30) |  |  |  |  |
| 59 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 60 | `ADVANCELICENSENO` | CHAR(30) |  |  |  |  |
| 61 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 62 | `EPCGEPCGAPPLICATIONCODE` | CHAR(30) |  |  |  |  |
| 63 | `EPCGAPPLICATIONDATE` | DATE |  |  |  |  |
| 64 | `EPCGLICENSENO` | CHAR(30) |  |  |  |  |
| 65 | `EPCGLICENSEDATE` | DATE |  |  |  |  |
| 66 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 67 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 68 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 69 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 70 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 71 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 72 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 73 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 74 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 75 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 76 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 77 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 78 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 79 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 80 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGCOMMERCIALINVOICE**.`ABSUNIQUEID` (high confidence — name = 'LOGCOMMERCIALINVOICE' + known child suffix 'LINE')
  - JOIN predicate: `LOGCOMMERCIALINVOICELINE.FATHERID = LOGCOMMERCIALINVOICE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMMERCIALINVOICECOMPANYCODE,
       t.COMMERCIALINVOICEDIVISIONCODE,
       t.COMMERCIALINVOICECODE,
       t.PLANTINVOICECODE,
       t.PLANTINVOICELINEINVOICELINENO,
       t.CUSTOMINVOICECODE,
       t.CUSTOMINVOICELINEINVOICELINENO,
       t.INVOICEDATE,
       t.INVOICELINENO,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE1
FROM   DB2ADMIN.LOGCOMMERCIALINVOICELINE t
FETCH FIRST 100 ROWS ONLY;
```
