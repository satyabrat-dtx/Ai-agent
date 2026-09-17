# DB2ADMIN.LOGCOSTELEMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 36
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 61846

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `COSTCATEGORYCODE` | CHAR(20) |  |  |  |  |
| 9 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |
| 10 | `VALUATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `PRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 12 | `INDUSTRIALACCOUNTINGCODE` | CHAR(20) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 20 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 21 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 22 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 23 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 24 | `COSTCATEGORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `COSTLEVELCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 27 | `COSTTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 28 | `SERVICECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `SERVICEITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 30 | `SERVICESUBCODE01` | CHAR(20) |  |  |  |  |
| 31 | `MAINCOSTELEFORSERVICEEXTOP` | SMALLINT | NOT NULL |  |  |  |
| 32 | `SELLINGCOST` | SMALLINT | NOT NULL |  |  |  |
| 33 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 34 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 35 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGCOSTELEMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COSTCATEGORYCODE,
       t.COSTLEVELCODE,
       t.VALUATIONTYPE,
       t.PRIMARYUOMCODE
FROM   DB2ADMIN.LOGCOSTELEMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
