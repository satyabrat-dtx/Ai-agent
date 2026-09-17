# DB2ADMIN.LOGSALESORDERTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 144
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 213037

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
| 15 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 16 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 17 | `NONCODIFIEDBUSINESSPRNALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 19 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 20 | `ORDERBOXMANAGEMENT` | CHAR(1) |  |  |  |  |
| 21 | `ORDERBOXPOLICYCODE` | CHAR(20) |  |  |  |  |
| 22 | `LEGALDOCUMENTTYPECODE` | CHAR(4) |  |  |  |  |
| 23 | `INTERCOMPANYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `PURCHASEGENERATIONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 25 | `PURCHASEORDEREDITABLE` | SMALLINT | NOT NULL |  |  |  |
| 26 | `SHIPPINGINFORMATION` | SMALLINT | NOT NULL |  |  |  |
| 27 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 29 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 31 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 33 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 34 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 35 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 36 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 37 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 38 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 39 | `ONLYONESHIPPINGPARAMETERS` | SMALLINT | NOT NULL |  |  |  |
| 40 | `AUTOMATICSHIPPINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 41 | `GOODRETURNNOTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 42 | `VALUATIONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 43 | `DEFAULTPAYMENTMETHODCMYCODE` | CHAR(3) |  |  |  |  |
| 44 | `DEFAULTPAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 45 | `ONLYONEPAYMENTMETHOD` | SMALLINT | NOT NULL |  |  |  |
| 46 | `MINIMUMDOCUMENTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 47 | `MAXIMUMDOCUMENTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 48 | `CASHPAYMENTONDELIVERY` | SMALLINT | NOT NULL |  |  |  |
| 49 | `INVOICINGPARAMETERS` | SMALLINT | NOT NULL |  |  |  |
| 50 | `MINIMUMINVOICEVALUEUSED` | SMALLINT | NOT NULL |  |  |  |
| 51 | `REGISTERTAXCODE` | CHAR(3) |  |  |  |  |
| 52 | `ELECTRONICINVREGISTERTAXCODE` | CHAR(3) |  |  |  |  |
| 53 | `COMPANYBANKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 54 | `PRICELISTCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 55 | `PRICELISTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 56 | `PRICELISTCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 57 | `PRICELISTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 58 | `DISCOUNTHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 59 | `HEADERDISCOUNTSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 60 | `DISCOUNTCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 61 | `DISCOUNTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 62 | `DERIVATIONDISCOUNTSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 63 | `PRICEANDDISCOUNTDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 64 | `TAXHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 65 | `FORCERETRIEVEININVOICE` | SMALLINT | NOT NULL |  |  |  |
| 66 | `HEADERTAXPOLICYCODE` | CHAR(20) |  |  |  |  |
| 67 | `TAXCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 68 | `TAXCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 69 | `CHARGESHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 70 | `HEADERCHARGESPOLICYCODE` | CHAR(20) |  |  |  |  |
| 71 | `CHARGESCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 72 | `CHARGESCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 73 | `DERIVATIONCHARGESPOLICYCODE` | CHAR(20) |  |  |  |  |
| 74 | `PROJECTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 75 | `ONLYONEPROJECT` | SMALLINT | NOT NULL |  |  |  |
| 76 | `AUTOPROJECTASSIGNCODE` | CHAR(20) |  |  |  |  |
| 77 | `STATISTICALGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 78 | `ONLYONESTATISTICALGROUP` | SMALLINT | NOT NULL |  |  |  |
| 79 | `COLLECTIONGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 80 | `ONLYONECOLLECTIONGROUP` | SMALLINT | NOT NULL |  |  |  |
| 81 | `AGENTHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 82 | `HEADERAGENTSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 83 | `AGENTCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 84 | `AGENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 85 | `ONLYONEAGENT` | SMALLINT | NOT NULL |  |  |  |
| 86 | `COMMISSIONCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 87 | `COMMISSIONCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 88 | `COMMISSIONCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 89 | `COMMISSIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 90 | `DERIVATIONCOMMISSIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 91 | `COMMISSIONDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 92 | `ASSORTMENTCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 93 | `ASSORTMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 94 | `ASSORTMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 95 | `LINENOTUPDATABLE` | SMALLINT | NOT NULL |  |  |  |
| 96 | `DERIVATIONASSORTMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 97 | `CREDITCHECKBLOCKCODE` | CHAR(3) |  |  |  |  |
| 98 | `CREDITCHECKBLOCKLEVEL` | CHAR(2) |  |  |  |  |
| 99 | `INTRASTATTRANSACTIONNATURECODE` | CHAR(2) |  |  |  |  |
| 100 | `CARTONMANAGEMENT` | CHAR(2) |  |  |  |  |
| 101 | `MAXLEVELPACKINGGROUPAPPROVAL` | CHAR(2) |  |  |  |  |
| 102 | `CARTONCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 103 | `CARTONCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 104 | `REPLENISHMENTMANAGEMENT` | CHAR(2) |  |  |  |  |
| 105 | `PLANNINGTEMPLATECODE` | CHAR(8) |  |  |  |  |
| 106 | `PLANPERIODIZEDCALENDARCODE` | CHAR(10) |  |  |  |  |
| 107 | `SHIFTORDERDATE` | CHAR(1) |  |  |  |  |
| 108 | `DEFAULTPLANNINGGROUPINGCODE` | CHAR(3) |  |  |  |  |
| 109 | `BLOCKSHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 110 | `HEADERBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 111 | `BLOCKSCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 112 | `BLOCKSCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 113 | `DERIVATIONBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 114 | `COMMENTHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 115 | `HEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 116 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 117 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 118 | `DERIVATIONCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 119 | `COMMENTALWAYSEDITABLE` | SMALLINT | NOT NULL |  |  |  |
| 120 | `SPREADCHANGEORDERCODE` | CHAR(20) |  |  |  |  |
| 121 | `SPREADCHANGEDOCCODE` | CHAR(20) |  |  |  |  |
| 122 | `SPREADCHANGEDOCTODOCCODE` | CHAR(20) |  |  |  |  |
| 123 | `CHECKORDERCODE` | CHAR(20) |  |  |  |  |
| 124 | `CHECKDOCUMENTCODE` | CHAR(20) |  |  |  |  |
| 125 | `COPYDEPENDENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 126 | `DOCUMENTCLOSURERULECODE` | CHAR(20) |  |  |  |  |
| 127 | `CONFIRMATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 128 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 129 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 130 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 131 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 132 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 133 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 134 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 135 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 136 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 137 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 138 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 139 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 140 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 141 | `TNAHEADERCODE` | CHAR(10) |  |  |  |  |
| 142 | `ONLYONEPURCHASEOP` | SMALLINT | NOT NULL |  |  |  |
| 143 | `EIDOCUMENTTYPECODE` | CHAR(4) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESORDER**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESORDER' + known child suffix 'TEMPLATE')
  - JOIN predicate: `LOGSALESORDERTEMPLATE.FATHERID = LOGSALESORDER.ABSUNIQUEID`

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
FROM   DB2ADMIN.LOGSALESORDERTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
