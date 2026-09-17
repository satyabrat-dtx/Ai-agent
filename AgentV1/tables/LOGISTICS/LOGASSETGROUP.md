# DB2ADMIN.LOGASSETGROUP

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 33
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 100695

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `TYPEOFASSET` | CHAR(2) |  |  |  |  |
| 6 | `TYPEOFASSETMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 7 | `INFOTYPECODE` | CHAR(2) |  |  |  |  |
| 8 | `INFOTYPEMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ASSETACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 10 | `ASSETACCOUNTMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 11 | `COUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 12 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 13 | `CIPACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 14 | `CIPACCOUNTMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 15 | `LOCATIONSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 16 | `LOCATIONCODE` | CHAR(10) |  |  |  |  |
| 17 | `TYPEOFUSESTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 18 | `TYPEOFUSECODE` | CHAR(10) |  |  |  |  |
| 19 | `TYPEOFPURCHASINGSTDTABLECODE` | CHAR(5) |  |  |  |  |
| 20 | `TYPEOFPURCHASINGCODE` | CHAR(10) |  |  |  |  |
| 21 | `TYPEOFPROPERTYSTDTABLECODE` | CHAR(5) |  |  |  |  |
| 22 | `TYPEOFPROPERTYCODE` | CHAR(10) |  |  |  |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 29 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 30 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |
| 31 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 32 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGASSETGROUP.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TYPEOFASSET,
       t.TYPEOFASSETMANDATORY,
       t.INFOTYPECODE,
       t.INFOTYPEMANDATORY,
       t.ASSETACCOUNTCODE,
       t.ASSETACCOUNTMANDATORY,
       t.COUNTERCOMPANYCODE
FROM   DB2ADMIN.LOGASSETGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
