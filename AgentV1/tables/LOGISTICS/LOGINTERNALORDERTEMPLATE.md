# DB2ADMIN.LOGINTERNALORDERTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 80
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 211761

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 4 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `DOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `DIRECTENTRYALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `DESTINATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `EFFECTIVITYDATESMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 12 | `EFFECTIVITYDATETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `LINESMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 14 | `AUTOINSERTFORVOIDLINES` | SMALLINT | NOT NULL |  |  |  |
| 15 | `LINESCOUNTERRATE` | INTEGER | NOT NULL |  |  |  |
| 16 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 17 | `NONCODIFIEDBUSINESSPRNALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 19 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 20 | `LEGALDOCUMENTTYPECODE` | CHAR(4) |  |  |  |  |
| 21 | `SHIPPINGINFORMATION` | SMALLINT | NOT NULL |  |  |  |
| 22 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 24 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 26 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 28 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 29 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 30 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 31 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 32 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 33 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 34 | `ONLYONESHIPPINGPARAMETERS` | SMALLINT | NOT NULL |  |  |  |
| 35 | `AUTOMATICSHIPPINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 36 | `TERMOFSHIPPINGANDRECEIVINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 37 | `AUTOMATICALLOCATION` | SMALLINT | NOT NULL |  |  |  |
| 38 | `REQUESTMATERIAL` | SMALLINT | NOT NULL |  |  |  |
| 39 | `PROJECTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 40 | `ONLYONEPROJECT` | SMALLINT | NOT NULL |  |  |  |
| 41 | `STATISTICALGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 42 | `ONLYONESTATISTICALGROUP` | SMALLINT | NOT NULL |  |  |  |
| 43 | `COLLECTIONGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 44 | `ONLYONECOLLECTIONGROUP` | SMALLINT | NOT NULL |  |  |  |
| 45 | `ASSORTMENTCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 46 | `ASSORTMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 47 | `ASSORTMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 48 | `LINENOTUPDATABLE` | SMALLINT | NOT NULL |  |  |  |
| 49 | `DERIVATIONASSORTMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 50 | `BLOCKSHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 51 | `HEADERBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 52 | `BLOCKSCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 53 | `BLOCKSCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 54 | `DERIVATIONBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 55 | `COMMENTHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 56 | `HEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 57 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 58 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 59 | `DERIVATIONCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 60 | `COMMENTALWAYSEDITABLE` | SMALLINT | NOT NULL |  |  |  |
| 61 | `SPREADCHANGEORDERCODE` | CHAR(20) |  |  |  |  |
| 62 | `SPREADCHANGEDOCCODE` | CHAR(20) |  |  |  |  |
| 63 | `CHECKORDERCODE` | CHAR(20) |  |  |  |  |
| 64 | `CHECKDOCUMENTCODE` | CHAR(20) |  |  |  |  |
| 65 | `COPYDEPENDENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 66 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 67 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 68 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 69 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 70 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 71 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 72 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 73 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 74 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 75 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 76 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 77 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 78 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 79 | `TNAHEADERCODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGINTERNALORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGINTERNALORDER' + known child suffix 'TEMPLATE')
  - JOIN predicate: `LOGINTERNALORDERTEMPLATE.FATHERID = LOGINTERNALORDER.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ORDERTYPE,
       t.CODE,
       t.DOCUMENTTYPE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DIRECTENTRYALLOWED,
       t.DESTINATIONTYPE,
       t.EFFECTIVITYDATESMANAGEMENT
FROM   DB2ADMIN.LOGINTERNALORDERTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
