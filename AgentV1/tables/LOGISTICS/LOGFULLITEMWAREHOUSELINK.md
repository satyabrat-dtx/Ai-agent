# DB2ADMIN.LOGFULLITEMWAREHOUSELINK

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 45
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 94956

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL |  |  |  |
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
| 18 | `ABCCODE` | CHAR(2) |  |  |  |  |
| 19 | `STOCKTAKEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 20 | `STOCKTAKESTDGRPTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 21 | `STOCKTAKESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 22 | `STOCKTAKECODE` | CHAR(3) |  |  |  |  |
| 23 | `TRNNUMBERFROMLASTSTOCKTAKE` | INTEGER | NOT NULL |  |  |  |
| 24 | `INVENTORYTURNOVERFACTOR` | DECIMAL(11,2) | NOT NULL |  |  |  |
| 25 | `REORDERPOINT` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 26 | `SAFETYSTOCK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 27 | `LASTTRANSACTIONDATE` | DATE |  |  |  |  |
| 28 | `LASTENTRYDATE` | DATE |  |  |  |  |
| 29 | `CURRENTSTOCKTAKEDATE` | DATE |  |  |  |  |
| 30 | `LASTSTOCKTAKEDATE` | DATE |  |  |  |  |
| 31 | `UNDERSTOCKTAKE` | CHAR(2) |  |  |  |  |
| 32 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 33 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 34 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 35 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 36 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 37 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 38 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 39 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 40 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 41 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 42 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 43 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 44 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFULLITEMWAREHOUSELINK.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09
FROM   DB2ADMIN.LOGFULLITEMWAREHOUSELINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
