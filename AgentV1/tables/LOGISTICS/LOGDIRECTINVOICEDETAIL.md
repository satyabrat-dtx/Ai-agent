# DB2ADMIN.LOGDIRECTINVOICEDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 69
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216979

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIRECTINVOICECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `DIRECTINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `DIRECTINVOICECOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 3 | `DIRECTINVOICECODE` | CHAR(15) | NOT NULL |  |  |  |
| 4 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 5 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 20 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 22 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 23 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 24 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 25 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 27 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 28 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |
| 29 | `REFERENCETEXT2` | CHAR(20) |  |  |  |  |
| 30 | `REFERENCETEXT3` | CHAR(20) |  |  |  |  |
| 31 | `REFERENCETEXT4` | CHAR(20) |  |  |  |  |
| 32 | `REFERENCETEXT5` | CHAR(20) |  |  |  |  |
| 33 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 34 | `FIRSTUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 35 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 36 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 37 | `SNDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 39 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 40 | `THIRDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 41 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 42 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 43 | `FRUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 44 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 45 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 46 | `FIFTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 47 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 48 | `SIXTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 49 | `SIXTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 50 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 51 | `SEVENTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 52 | `SEUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 53 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 54 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 55 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 56 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 57 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 58 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 59 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 60 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 61 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 62 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 63 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 64 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 65 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 66 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 67 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 68 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGDIRECTINVOICE**.`ABSUNIQUEID` (high confidence — name = 'LOGDIRECTINVOICE' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGDIRECTINVOICEDETAIL.FATHERID = LOGDIRECTINVOICE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.DIRECTINVOICECOMPANYCODE,
       t.DIRECTINVOICEDIVISIONCODE,
       t.DIRECTINVOICECOUNTERCODE,
       t.DIRECTINVOICECODE,
       t.LINENO,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.LOGDIRECTINVOICEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
