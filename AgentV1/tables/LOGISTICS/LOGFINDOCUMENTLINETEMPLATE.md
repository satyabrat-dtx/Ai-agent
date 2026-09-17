# DB2ADMIN.LOGFINDOCUMENTLINETEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 58
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 174872

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `VALID` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ADVANCEFLAG` | SMALLINT | NOT NULL |  |  |  |
| 7 | `LINETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `SUBLEDGERTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `PROJECTCONTROL` | SMALLINT | NOT NULL |  |  |  |
| 10 | `STATISTICALCONTROL` | SMALLINT | NOT NULL |  |  |  |
| 11 | `PROFITCENTERCONTROL` | INTEGER | NOT NULL |  |  |  |
| 12 | `COSTCENTERCONTROL` | INTEGER | NOT NULL |  |  |  |
| 13 | `CHECKDOCUMENTLINECODE` | CHAR(20) |  |  |  |  |
| 14 | `REVERSALLINETMPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 15 | `REVERSALLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 16 | `TDSLINETEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `TDSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 18 | `REFTEXT1` | CHAR(20) |  |  |  |  |
| 19 | `REFTEXT2` | CHAR(20) |  |  |  |  |
| 20 | `REFTEXT3` | CHAR(20) |  |  |  |  |
| 21 | `REFTEXT4` | CHAR(20) |  |  |  |  |
| 22 | `REFTEXT5` | CHAR(20) |  |  |  |  |
| 23 | `REFAMT1` | CHAR(20) |  |  |  |  |
| 24 | `REFAMT2` | CHAR(20) |  |  |  |  |
| 25 | `REFAMT3` | CHAR(20) |  |  |  |  |
| 26 | `REFAMT4` | CHAR(20) |  |  |  |  |
| 27 | `REFAMT5` | CHAR(20) |  |  |  |  |
| 28 | `FIRSTUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `FIRSTUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 30 | `SECONDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `SECONDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 32 | `THIRDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `THIRDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 34 | `FOURTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `FOURTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 36 | `FIFTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `FIFTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 38 | `SIXTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 39 | `SIXTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 40 | `SEVENTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 41 | `SEVENTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 42 | `INTERCOMPANY` | SMALLINT | NOT NULL |  |  |  |
| 43 | `COMMENTLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 44 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 45 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 46 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 47 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 48 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 49 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 50 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
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

- `FATHERID` → **LOGFINDOCUMENTLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGFINDOCUMENTLINE' + known child suffix 'TEMPLATE')
  - JOIN predicate: `LOGFINDOCUMENTLINETEMPLATE.FATHERID = LOGFINDOCUMENTLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.VALID,
       t.ADVANCEFLAG,
       t.LINETYPE,
       t.SUBLEDGERTYPE,
       t.PROJECTCONTROL,
       t.STATISTICALCONTROL,
       t.PROFITCENTERCONTROL
FROM   DB2ADMIN.LOGFINDOCUMENTLINETEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
