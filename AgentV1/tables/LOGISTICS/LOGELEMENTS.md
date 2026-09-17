# DB2ADMIN.LOGELEMENTS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 93
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 63473

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CATSSEQ` | BIGINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `SUBCODEKEY` | CHAR(20) | NOT NULL |  |  |  |
| 4 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 5 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 6 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 7 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 8 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 9 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 10 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 11 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 12 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 13 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 14 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 15 | `DEFINITIVEELEMENTCODE` | CHAR(15) |  |  |  |  |
| 16 | `AUTOMATICCREATIONELEMENT` | SMALLINT | NOT NULL |  |  |  |
| 17 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 18 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 19 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 20 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 21 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 22 | `ELEMENTNATURE` | CHAR(2) |  |  |  |  |
| 23 | `STATUSCODE` | CHAR(3) |  |  |  |  |
| 24 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `ENTRYDATE` | DATE |  |  |  |  |
| 26 | `ENTRYDOCUMENTDATE` | DATE |  |  |  |  |
| 27 | `ENTRYDOCUMENTTYPE` | CHAR(2) |  |  |  |  |
| 28 | `ENTRYDOCUMENTCOUNTER` | CHAR(8) |  |  |  |  |
| 29 | `ENTRYDOCUMENTNUMBER` | CHAR(50) |  |  |  |  |
| 30 | `ISSUEDOCUMENTDATE` | DATE |  |  |  |  |
| 31 | `ISSUEDOCUMENTTYPE` | CHAR(2) |  |  |  |  |
| 32 | `ISSUEDOCUMENTCOUNTER` | CHAR(8) |  |  |  |  |
| 33 | `ISSUEDOCUMENTNUMBER` | CHAR(50) |  |  |  |  |
| 34 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 35 | `CUSTOMERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 36 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 37 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 38 | `SUPPLIERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 39 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 40 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 41 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 42 | `CUTITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 43 | `CUTITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 44 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 45 | `FIRSTQUALITYCONTROLDATE` | DATE |  |  |  |  |
| 46 | `FIRSTQUALITYCONTROLCOUNTER` | CHAR(8) |  |  |  |  |
| 47 | `FIRSTQUALITYCONTROLNUMBER` | CHAR(15) |  |  |  |  |
| 48 | `BASEPRIMARYUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 49 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `BASESECONDARYUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 51 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 53 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 54 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 55 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 56 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 57 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 58 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 59 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 60 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 61 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 62 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 63 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 64 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 65 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 66 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 67 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 68 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 69 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 70 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 71 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 72 | `STATUSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 73 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 74 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 75 | `CUTITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 76 | `QUALITYREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 77 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 78 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 79 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 80 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 81 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 82 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 83 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 84 | `FATHERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 85 | `FATHERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 86 | `REUNIFICATE` | SMALLINT | NOT NULL |  |  |  |
| 87 | `ENTRYDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 88 | `ISSUEDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 89 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 90 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 91 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 92 | `ORIGINCOUNTRYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGELEMENTS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.CATSSEQ,
       t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODEKEY,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05,
       t.DECOSUBCODE06,
       t.DECOSUBCODE07,
       t.DECOSUBCODE08
FROM   DB2ADMIN.LOGELEMENTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
