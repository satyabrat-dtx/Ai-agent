# DB2ADMIN.LOGDIRECTDOCUMENTTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 41
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 219259

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(8) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `BOOKINGFOR` | CHAR(10) |  |  |  |  |
| 3 | `DOCUMENTTYPE` | CHAR(1) |  |  |  |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `COUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 10 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `POSTINGBY` | CHAR(1) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 19 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 20 | `FIRSTUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 21 | `FIRSTUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 22 | `SECONDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `SECONDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 24 | `THIRDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `THIRDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 26 | `FOURTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `FOURTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 28 | `FIFTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `FIFTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 30 | `SIXTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `SIXTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 32 | `SEVENTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `SEVENTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 34 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 35 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 36 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 37 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 38 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 39 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 40 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGDIRECTDOCUMENTTEMPLATE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.BOOKINGFOR,
       t.DOCUMENTTYPE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.POSTINGBY
FROM   DB2ADMIN.LOGDIRECTDOCUMENTTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
