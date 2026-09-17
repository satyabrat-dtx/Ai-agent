# DB2ADMIN.LOGNETTOLOG

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 36
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 219530

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(2) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `UPDATEREASONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `VALID` | SMALLINT | NOT NULL |  |  |  |
| 7 | `PLANTINVOICELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 8 | `PLANTINVOICELINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 9 | `CUSTOMINVOICELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 10 | `CUSTOMINVOICELINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 11 | `COMMERCIALINVOICELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 12 | `COMINVLINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 13 | `MRNHEADERLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 14 | `MRNDETAILLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 15 | `MRNREJECTIONLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 16 | `EXPENSEINVOICELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 17 | `EMPLOYEELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 18 | `GATEENTRYLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 19 | `FINDOCUMENTLOGOPTION` | INTEGER | NOT NULL |  |  |  |
| 20 | `FINDOCUMENTLINELOGOPTION` | INTEGER | NOT NULL |  |  |  |
| 21 | `DIRECTINVOICELOGOPTION` | INTEGER | NOT NULL |  |  |  |
| 22 | `DIRECTINVOICEDETAILLOGOPTION` | INTEGER | NOT NULL |  |  |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 30 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 31 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 32 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 33 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 34 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 35 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGNETTOLOG.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.UPDATEREASONREQUIRED,
       t.VALID,
       t.PLANTINVOICELOGOPTIONS,
       t.PLANTINVOICELINELOGOPTIONS,
       t.CUSTOMINVOICELOGOPTIONS,
       t.CUSTOMINVOICELINELOGOPTIONS,
       t.COMMERCIALINVOICELOGOPTIONS
FROM   DB2ADMIN.LOGNETTOLOG t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
