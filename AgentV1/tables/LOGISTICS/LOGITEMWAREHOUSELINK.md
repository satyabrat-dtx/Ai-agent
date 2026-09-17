# DB2ADMIN.LOGITEMWAREHOUSELINK

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 53
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 95022

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 4 | `SUBCODE02` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 5 | `SUBCODE03` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 6 | `SUBCODE04` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 7 | `SUBCODE05` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 8 | `SUBCODE06` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 9 | `SUBCODE07` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 10 | `SUBCODE08` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 11 | `SUBCODE09` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 12 | `SUBCODE10` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 13 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 14 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL |  |  |  |
| 15 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 16 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 17 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 18 | `LOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 19 | `ELEMENTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 20 | `CONTAINERCONTROLLED` | CHAR(2) | NOT NULL |  |  |  |
| 21 | `QUALITYCONTROLLED` | CHAR(2) | NOT NULL |  |  |  |
| 22 | `PROJECTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 23 | `STATISTICALGROUPCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `CUSTOMERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 25 | `SUPPLIERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 26 | `ABCCODE` | CHAR(2) |  |  |  |  |
| 27 | `STOCKTAKEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 28 | `STOCKTAKESTDGRPTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 29 | `STOCKTAKESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 30 | `STOCKTAKECODE` | CHAR(3) |  |  |  |  |
| 31 | `TRNNUMBERFROMLASTSTOCKTAKE` | INTEGER | NOT NULL |  |  |  |
| 32 | `INVENTORYTURNOVERFACTOR` | DECIMAL(11,2) | NOT NULL |  |  |  |
| 33 | `REORDERPOINT` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 34 | `SAFETYSTOCK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 35 | `LASTTRANSACTIONDATE` | DATE |  |  |  |  |
| 36 | `LASTENTRYDATE` | DATE |  |  |  |  |
| 37 | `CURRENTSTOCKTAKEDATE` | DATE |  |  |  |  |
| 38 | `LASTSTOCKTAKEDATE` | DATE |  |  |  |  |
| 39 | `UNDERSTOCKTAKE` | CHAR(2) |  |  |  |  |
| 40 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 41 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 42 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 43 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 44 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 45 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 46 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 47 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 48 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 49 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 50 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 51 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 52 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGITEMWAREHOUSELINK.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09
FROM   DB2ADMIN.LOGITEMWAREHOUSELINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
