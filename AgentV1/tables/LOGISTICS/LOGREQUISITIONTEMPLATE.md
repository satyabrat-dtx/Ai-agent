# DB2ADMIN.LOGREQUISITIONTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 46
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 214370

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
| 7 | `REPLENISHMENTTYPE` | CHAR(2) |  |  |  |  |
| 8 | `COUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `ONLYPRIMARYKEY` | SMALLINT | NOT NULL |  |  |  |
| 11 | `TEMPLATE` | CHAR(3) |  |  |  |  |
| 12 | `RETRIEVEPRICELIST` | SMALLINT | NOT NULL |  |  |  |
| 13 | `LINESGROUPED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `CALCULABLEDATAPRICE` | SMALLINT | NOT NULL |  |  |  |
| 15 | `USETEMPLATEDEFINITION` | SMALLINT | NOT NULL |  |  |  |
| 16 | `MULTILINKHANDLING` | SMALLINT | NOT NULL |  |  |  |
| 17 | `CONVERTORDERITEMUOM` | SMALLINT | NOT NULL |  |  |  |
| 18 | `REPLENISHMENTSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 19 | `ALLOCATIONCRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 20 | `ALLOCATIONTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 21 | `ALLOCATIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 22 | `AUTHORIZATIONCHECKPHASE` | CHAR(90) |  |  |  |  |
| 23 | `REQUISITIONCHECKCODE` | CHAR(20) |  |  |  |  |
| 24 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 25 | `MAXLEVELPURCHASEAPPROVAL` | CHAR(2) |  |  |  |  |
| 26 | `MAXLEVELPURCHASENOTCOMPLETED` | CHAR(2) |  |  |  |  |
| 27 | `SKIPRELEASEATTENDED` | SMALLINT | NOT NULL |  |  |  |
| 28 | `RFQMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 29 | `RRCOMMENTCRITERIA` | CHAR(2) |  |  |  |  |
| 30 | `HEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 31 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 32 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 33 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 34 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 35 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 36 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 37 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 38 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 39 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 40 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 41 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 42 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 43 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 44 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 45 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGREQUISITIONTEMPLATE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.REPLENISHMENTTYPE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.ONLYPRIMARYKEY,
       t.TEMPLATE
FROM   DB2ADMIN.LOGREQUISITIONTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
