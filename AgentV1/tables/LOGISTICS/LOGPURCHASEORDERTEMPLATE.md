# DB2ADMIN.LOGPURCHASEORDERTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 113
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216685

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
| 10 | `EFFECTIVITYDATESMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 11 | `EFFECTIVITYDATETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `LINESMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 13 | `AUTOINSERTFORVOIDLINES` | SMALLINT | NOT NULL |  |  |  |
| 14 | `LINESCOUNTERRATE` | INTEGER | NOT NULL |  |  |  |
| 15 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 16 | `NONCODIFIEDBUSINESSPRNALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 17 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 18 | `BUDGETCONTROL` | INTEGER | NOT NULL |  |  |  |
| 19 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 20 | `ORDERBOXMANAGEMENT` | CHAR(1) |  |  |  |  |
| 21 | `ORDERBOXPOLICYCODE` | CHAR(20) |  |  |  |  |
| 22 | `MULTILINKHANDLING` | SMALLINT | NOT NULL |  |  |  |
| 23 | `LINKEDSTOCKTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 24 | `INTERCOMPANYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 25 | `SHIPPINGINFORMATION` | SMALLINT | NOT NULL |  |  |  |
| 26 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 28 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 30 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 32 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 33 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 34 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 35 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 36 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 37 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 38 | `ONLYONESHIPPINGPARAMETERS` | SMALLINT | NOT NULL |  |  |  |
| 39 | `PRODUCTIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 40 | `TEMPLATEFORORDERCODE` | CHAR(3) |  |  |  |  |
| 41 | `CONTAINERELEMENTMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 42 | `ONLYONEBUYER` | SMALLINT | NOT NULL |  |  |  |
| 43 | `REFERENCEDATEAPPLY` | CHAR(2) |  |  |  |  |
| 44 | `VALUATIONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 45 | `DEFAULTPAYMENTMETHODCMYCODE` | CHAR(3) |  |  |  |  |
| 46 | `DEFAULTPAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 47 | `ONLYONEPAYMENTMETHOD` | SMALLINT | NOT NULL |  |  |  |
| 48 | `MINIMUMDOCUMENTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 49 | `MAXIMUMDOCUMENTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 50 | `CASHPAYMENTONDELIVERY` | SMALLINT | NOT NULL |  |  |  |
| 51 | `EXHANGERATEAPPLICATIONDOCTYPE` | CHAR(3) |  |  |  |  |
| 52 | `REGISTERTAXCODE` | CHAR(3) |  |  |  |  |
| 53 | `ELECTRONICINVREGISTERTAXCODE` | CHAR(3) |  |  |  |  |
| 54 | `PRICELISTCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 55 | `PRICELISTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 56 | `PRICELISTCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 57 | `PRICELISTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 58 | `DISCOUNTHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 59 | `DISCOUNTCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 60 | `DISCOUNTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 61 | `PRCANDDISCOUNTAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 62 | `DERIVATIONDISCOUNTSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 63 | `CHARGESHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 64 | `CHARGESCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 65 | `CHARGESCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 66 | `DERIVATIONCHARGESPOLICYCODE` | CHAR(20) |  |  |  |  |
| 67 | `TAXHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 68 | `HEADERTAXPOLICYCODE` | CHAR(20) |  |  |  |  |
| 69 | `TAXCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 70 | `TAXCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 71 | `PROJECTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 72 | `ONLYONEPROJECT` | SMALLINT | NOT NULL |  |  |  |
| 73 | `STATISTICALGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 74 | `ONLYONESTATISTICALGROUP` | SMALLINT | NOT NULL |  |  |  |
| 75 | `COLLECTIONGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 76 | `ONLYONECOLLECTIONGROUP` | SMALLINT | NOT NULL |  |  |  |
| 77 | `CUSTOMERMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 78 | `ONLYONECUSTOMER` | SMALLINT | NOT NULL |  |  |  |
| 79 | `ASSORTMENTCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 80 | `ASSORTMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 81 | `ASSORTMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 82 | `LINENOTUPDATABLE` | SMALLINT | NOT NULL |  |  |  |
| 83 | `DERIVATIONASSORTMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 84 | `INTRASTATTRANSACTIONNATURECODE` | CHAR(2) |  |  |  |  |
| 85 | `POMODIFYFLAG` | INTEGER | NOT NULL |  |  |  |
| 86 | `BLOCKSHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 87 | `HEADERBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 88 | `BLOCKSCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 89 | `BLOCKSCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 90 | `DERIVATIONBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 91 | `COMMENTHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 92 | `HEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 93 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 94 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 95 | `DERIVATIONCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 96 | `SPREADCHANGEORDERCODE` | CHAR(20) |  |  |  |  |
| 97 | `CHECKORDERCODE` | CHAR(20) |  |  |  |  |
| 98 | `COPYDEPENDENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 99 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 100 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 101 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 102 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 103 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 104 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 105 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 106 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 107 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 108 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 109 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 110 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 111 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 112 | `TNAHEADERCODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGPURCHASEORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGPURCHASEORDER' + known child suffix 'TEMPLATE')
  - JOIN predicate: `LOGPURCHASEORDERTEMPLATE.FATHERID = LOGPURCHASEORDER.ABSUNIQUEID`

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
       t.EFFECTIVITYDATESMANAGEMENT,
       t.EFFECTIVITYDATETYPE
FROM   DB2ADMIN.LOGPURCHASEORDERTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
