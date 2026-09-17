# DB2ADMIN.LOGPROJECT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 44
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 211618

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(20) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 8 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 9 | `BUDGETMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `BUDGETPROGRESSSTATUS` | INTEGER | NOT NULL |  |  |  |
| 11 | `BUDGETSTATUS` | CHAR(1) | NOT NULL |  |  |  |
| 12 | `PROJECTBUDGETBYPLANNINGRUN` | INTEGER | NOT NULL |  |  |  |
| 13 | `BUDGETTOBEUPDONPLANNINGRUN` | SMALLINT | NOT NULL |  |  |  |
| 14 | `BUDGETAPPROVALDATE` | DATE |  |  |  |  |
| 15 | `BUDGETAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 16 | `BUDGETUNAPPROVALDATE` | DATE |  |  |  |  |
| 17 | `BUDGETUNAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 18 | `PLANNERANNOTATION` | VARCHAR(250) |  |  |  |  |
| 19 | `PLANRUNNING` | SMALLINT | NOT NULL |  |  |  |
| 20 | `CANBEEXPLODED` | SMALLINT | NOT NULL |  |  |  |
| 21 | `PLANNINGTEMPLATECODE` | CHAR(8) |  |  |  |  |
| 22 | `PROGRESSSTATUS` | INTEGER | NOT NULL |  |  |  |
| 23 | `LINESCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `ERRORS` | VARCHAR(960) |  |  |  |  |
| 25 | `WARNINGS` | VARCHAR(960) |  |  |  |  |
| 26 | `TRACECREATIONID` | DECIMAL(11,0) |  |  |  |  |
| 27 | `TRACELINE` | INTEGER | NOT NULL |  |  |  |
| 28 | `SUBMITTEDJOBJOBNUMBER` | BIGINT | NOT NULL |  |  |  |
| 29 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 30 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 31 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 32 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 33 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 34 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 35 | `WFMSTATUS` | INTEGER | NOT NULL |  |  |  |
| 36 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 38 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 39 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 40 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 41 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 42 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 43 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPROJECT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CUSTOMERTYPE,
       t.CUSTOMERCODE,
       t.BUDGETMANAGED,
       t.BUDGETPROGRESSSTATUS,
       t.BUDGETSTATUS
FROM   DB2ADMIN.LOGPROJECT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
