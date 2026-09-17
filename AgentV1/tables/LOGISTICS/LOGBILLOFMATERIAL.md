# DB2ADMIN.LOGBILLOFMATERIAL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 89
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 56493

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 16 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 17 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 18 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 19 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 20 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 21 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 22 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 23 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 24 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 25 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 26 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 27 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 28 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 29 | `REFBOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 30 | `REFBOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 31 | `PRODUCTIONBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 32 | `PRODBOMSTARTDATE` | DATE |  |  |  |  |
| 33 | `PRODBOMENDDATE` | DATE |  |  |  |  |
| 34 | `PRODUCTIONREFERENCEBOM` | SMALLINT | NOT NULL |  |  |  |
| 35 | `PRODREFBOMSTARTDATE` | DATE |  |  |  |  |
| 36 | `PRODREFBOMENDDATE` | DATE |  |  |  |  |
| 37 | `COSTCALCULATIONBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 38 | `COSTCALCBOMSTARTDATE` | DATE |  |  |  |  |
| 39 | `COSTCALCBOMENDDATE` | DATE |  |  |  |  |
| 40 | `TECHNICALBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 41 | `TECHBOMSTARTDATE` | DATE |  |  |  |  |
| 42 | `TECHBOMENDDATE` | DATE |  |  |  |  |
| 43 | `PLANNINGBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 44 | `PLANBOMSTARTDATE` | DATE |  |  |  |  |
| 45 | `PLANBOMENDDATE` | DATE |  |  |  |  |
| 46 | `BOMTYPECODE` | CHAR(6) |  |  |  |  |
| 47 | `CHECKCODE` | CHAR(2) |  |  |  |  |
| 48 | `USERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 49 | `GENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 50 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 51 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 52 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 53 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 54 | `BOMUOMTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 55 | `BOMUOMCODE` | CHAR(3) |  |  |  |  |
| 56 | `BOMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `BOMINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 58 | `BOMCOMMENTCRITERIA` | CHAR(2) |  |  |  |  |
| 59 | `HEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 60 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 61 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 62 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 63 | `APPROVALDATE` | DATE |  |  |  |  |
| 64 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 65 | `RELEASEDATE` | DATE |  |  |  |  |
| 66 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 67 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 68 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 69 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 70 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 71 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 72 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 73 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 74 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 75 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 76 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 77 | `USERGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 78 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 79 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 80 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 81 | `IMPORTEDBOM` | SMALLINT | NOT NULL |  |  |  |
| 82 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 83 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 84 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 85 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 86 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 87 | `ORIGINPROTOTYPE` | CHAR(20) |  |  |  |  |
| 88 | `ORIGINSUFFIXCODE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGBILLOFMATERIAL.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.NUMBERID,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.LOGBILLOFMATERIAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
