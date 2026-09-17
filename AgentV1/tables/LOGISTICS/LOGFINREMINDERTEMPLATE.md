# DB2ADMIN.LOGFINREMINDERTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 35
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 101915

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `COLLECTIONADDRESSNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 8 | `REMINDERLIMITFROMBALANCE` | DECIMAL(5,2) |  |  |  |  |
| 9 | `REMINDERMINIMUMLIMIT` | DECIMAL(11,2) |  |  |  |  |
| 10 | `MAXIMUMDAYSFORLIMITS` | INTEGER | NOT NULL |  |  |  |
| 11 | `REMINDERPROPOSALCODE` | CHAR(20) |  |  |  |  |
| 12 | `REMINDERPROCESSINGCODE` | CHAR(20) |  |  |  |  |
| 13 | `INTERRESTPROCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 14 | `INTERRESTADDITIONALDELAY` | INTEGER | NOT NULL |  |  |  |
| 15 | `POSTINTERRESTS` | SMALLINT | NOT NULL |  |  |  |
| 16 | `VOUCHERTEMPLATEINTERESTCODE` | CHAR(5) |  |  |  |  |
| 17 | `INTERESTACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 18 | `INTJOURNTXTKEYSTDTABLECODE` | CHAR(5) |  |  |  |  |
| 19 | `INTJOURNTXTKEYCODE` | CHAR(10) |  |  |  |  |
| 20 | `POSTCHARGES` | SMALLINT | NOT NULL |  |  |  |
| 21 | `VOUCHERTEMPLATECHARGESCODE` | CHAR(5) |  |  |  |  |
| 22 | `CHARGESACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 23 | `CHRJOURNNOTETEXTKEYSTDTABLECOD` | CHAR(5) |  |  |  |  |
| 24 | `CHARGESJOURNNOTETEXTKEYCODE` | CHAR(10) |  |  |  |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 30 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 31 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 32 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |
| 33 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 34 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINREMINDERTEMPLATE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COLLECTIONADDRESSNUMBERID,
       t.REMINDERLIMITFROMBALANCE,
       t.REMINDERMINIMUMLIMIT,
       t.MAXIMUMDAYSFORLIMITS,
       t.REMINDERPROPOSALCODE
FROM   DB2ADMIN.LOGFINREMINDERTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
