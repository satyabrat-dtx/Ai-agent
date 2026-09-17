# DB2ADMIN.LOGCSRM

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 39
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118933

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 1 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 6 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 7 | `CUSTOMERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 8 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 9 | `ORDERPARTNERTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `SUPPLIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 11 | `SUPPLIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 12 | `LETTERTEMPLATECODE` | CHAR(30) |  |  |  |  |
| 13 | `PROPOSALDATE` | DATE | NOT NULL |  |  |  |
| 14 | `PLANNEDSTARTDATE` | DATE |  |  |  |  |
| 15 | `PLANNEDENDDATE` | DATE |  |  |  |  |
| 16 | `OWNERUSERID` | CHAR(50) |  |  |  |  |
| 17 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 18 | `COUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 19 | `CODE` | CHAR(20) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 20 | `PROJECTDATE` | DATE |  |  |  |  |
| 21 | `BRIEF` | VARCHAR(1000) | NOT NULL |  |  |  |
| 22 | `ACTUALSTARTDATE` | DATE |  |  |  |  |
| 23 | `ACTUALENDDATE` | DATE |  |  |  |  |
| 24 | `CLOSINGCOMMENT` | VARCHAR(1000) |  |  |  |  |
| 25 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 26 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 27 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 28 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 29 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 30 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 31 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 33 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 34 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 35 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 36 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 37 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 38 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGCSRM.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGCSRMTEMPLATE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.DEPARTMENTCODE,
       t.CUSTOMERCUSTOMERSUPPLIERTYPE,
       t.CUSTOMERCUSTOMERSUPPLIERCODE,
       t.ORDERPARTNERTYPE,
       t.SUPPLIERCUSTOMERSUPPLIERTYPE,
       t.SUPPLIERCUSTOMERSUPPLIERCODE
FROM   DB2ADMIN.LOGCSRM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
