# DB2ADMIN.LOGALLOCATIONTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 58
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 214291

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `STOCKTYPEJOINEDCODE` | CHAR(3) |  |  |  |  |
| 9 | `HANDLEEXPIRATIONDATE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `MAINTAINORIGSTOCKTYPEFORDERIV` | SMALLINT | NOT NULL |  |  |  |
| 11 | `DIFFERENTDESTINATIONWHS` | SMALLINT | NOT NULL |  |  |  |
| 12 | `USEDESTINATIONUOM` | SMALLINT | NOT NULL |  |  |  |
| 13 | `HEADERONLYPRIMARYKEY` | SMALLINT | NOT NULL |  |  |  |
| 14 | `DIFFERENCEDESTINATIONITEM` | CHAR(2) | NOT NULL |  |  |  |
| 15 | `ALWELEMENTPARTIALALLOCATION` | SMALLINT | NOT NULL |  |  |  |
| 16 | `IMMEDIATEAVAILABILITYCONTROL` | CHAR(2) | NOT NULL |  |  |  |
| 17 | `AVAILABILITYFORMULACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `AVAILABILITYFORMULACODE` | CHAR(3) |  |  |  |  |
| 19 | `CHECKALLOCATIONCODE` | CHAR(20) |  |  |  |  |
| 20 | `CUSTOMALLOCATIONCODE` | CHAR(20) |  |  |  |  |
| 21 | `EXPANDORIGALLOCTODETAIL` | SMALLINT | NOT NULL |  |  |  |
| 22 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `ITEMDESCRIPTIONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `PROJECTCODEREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 25 | `STATISTICALGROUPREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 26 | `WAREHOUSELOCATIONREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 27 | `DSTWAREHOUSELOCATIONREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 28 | `LOCATIONNATUREMANAGEMENT` | CHAR(90) |  |  |  |  |
| 29 | `LOTREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 30 | `DSTLOTREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 31 | `CONTAINERREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 32 | `DSTCONTAINERREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 33 | `ELEMENTREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 34 | `DSTELEMENTREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 35 | `WEIGHTSREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 36 | `QUALITYLEVELMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 37 | `LOCATIONMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 38 | `ITEMDESCRIPTIONMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 39 | `LOTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 40 | `CONTAINERMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 41 | `CONTAINERELEMENTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 42 | `PROJECTCODEMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 43 | `STATISTICALGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 44 | `PRIMARYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 45 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 46 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 47 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 48 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 49 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 50 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 51 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 52 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 53 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 54 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 55 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 56 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 57 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGALLOCATIONTEMPLATE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.STOCKTYPECODE,
       t.STOCKTYPEJOINEDCODE,
       t.HANDLEEXPIRATIONDATE,
       t.MAINTAINORIGSTOCKTYPEFORDERIV,
       t.DIFFERENTDESTINATIONWHS
FROM   DB2ADMIN.LOGALLOCATIONTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
