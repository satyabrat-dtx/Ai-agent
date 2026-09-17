# DB2ADMIN.LOGINTERNALORDERLINETEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 127
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 210450

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 2 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `ITEMCODINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `FULLITEMREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `EXTANTITEMREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `EDITABLEITEM` | SMALLINT | NOT NULL |  |  |  |
| 13 | `EDITABLEITEMTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 15 | `ALTERNATIVEITEMCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 16 | `TRANSACTIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 17 | `QUANTITYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 20 | `UPDATEWAREHOUSE` | SMALLINT | NOT NULL |  |  |  |
| 21 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 23 | `STOCKTRNRECEIVINGTMPCMYCODE` | CHAR(3) |  |  |  |  |
| 24 | `STOCKTRNRECEIVINGTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 25 | `STOCKTRNTEMPLATEQCCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `STOCKTRANSACTIONTEMPLATEQCCODE` | CHAR(3) |  |  |  |  |
| 27 | `QUALITYCRITERIA` | CHAR(2) |  |  |  |  |
| 28 | `ALLOCATIONCRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 29 | `ALLOCATIONTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `ALLOCATIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 31 | `ALLOCATIONQUANTITYGREATERORDER` | SMALLINT | NOT NULL |  |  |  |
| 32 | `ALLOCATIONDOCUMENTCRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 33 | `ALLDOCQUANTITYGREATERDOC` | SMALLINT | NOT NULL |  |  |  |
| 34 | `ALLDOCTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `ALLOCATIONDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 36 | `ALLOCATIONRECEIVINGCRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 37 | `ALLRECEIVINGTMPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 38 | `ALLRECEIVINGTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 39 | `DERIVATIONALLTMPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 40 | `DERIVATIONALLTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 41 | `DERIVEDOCALLOCONLYORIGWHS` | SMALLINT | NOT NULL |  |  |  |
| 42 | `FROMORDERTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `FROMORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 44 | `ORIGINALLOCATIONWAREHOUSE` | SMALLINT | NOT NULL |  |  |  |
| 45 | `ALLOCATIONMANAGEMENT` | CHAR(2) |  |  |  |  |
| 46 | `DLTALLAUTOADVICETYPECMYCODE` | CHAR(3) |  |  |  |  |
| 47 | `DLTALLAUTOADVICETYPECODE` | CHAR(3) |  |  |  |  |
| 48 | `COSTHANDLING` | CHAR(1) | NOT NULL |  |  |  |
| 49 | `COSTTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 50 | `COSTCRITERIAFORITEM` | CHAR(2) | NOT NULL |  |  |  |
| 51 | `LINEINORDER` | SMALLINT | NOT NULL |  |  |  |
| 52 | `INTLINETMPFROMOPENORDERCODE` | CHAR(3) |  |  |  |  |
| 53 | `ORDERQUANTITYGREATEROPENORDER` | SMALLINT | NOT NULL |  |  |  |
| 54 | `REPLENISHMENTORDERLINK` | CHAR(2) | NOT NULL |  |  |  |
| 55 | `ORDERRETURNWITHCLOSEDLINEUPD` | SMALLINT | NOT NULL |  |  |  |
| 56 | `COMMENTLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 57 | `LINECOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 58 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 59 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 60 | `COMMENTGROUPCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 61 | `COMMENTGROUPCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 62 | `DERIVATIONLINECMTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 63 | `COMMENTDELIVERYCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 64 | `DELIVERYCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 65 | `DELIVERYCOMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 66 | `DELIVERYCOMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 67 | `BLOCKSLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 68 | `LINEBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 69 | `BLOCKSCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 70 | `BLOCKSCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 71 | `DERIVATIONLINEBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 72 | `BLOCKSDELIVERYCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 73 | `DELIVERYBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 74 | `DELIVERYBLOCKSCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 75 | `DELIVERYBLOCKSCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 76 | `SPREADCHANGEORDERLINECODE` | CHAR(20) |  |  |  |  |
| 77 | `SPREADCHANGEDOCCODE` | CHAR(20) |  |  |  |  |
| 78 | `CHECKORDERLINECODE` | CHAR(20) |  |  |  |  |
| 79 | `CHECKDOCUMENTLINECODE` | CHAR(20) |  |  |  |  |
| 80 | `CLOSURERULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 81 | `DOCUMENTCLOSURERULECODE` | CHAR(20) |  |  |  |  |
| 82 | `COPYDEPENDENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 83 | `FUTUREAVAILABILITYCHECK` | CHAR(2) | NOT NULL |  |  |  |
| 84 | `ORDERSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 85 | `CONFIRMATIONORDERSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 86 | `RESERVATIONSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 87 | `ONLYONEDELIVERYLINE` | SMALLINT | NOT NULL |  |  |  |
| 88 | `REQUIREDDATECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 89 | `REQUIREDDATEPERTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 90 | `REQUIREDDATEPERIODTYPECODE` | CHAR(3) |  |  |  |  |
| 91 | `PLANNEDDATECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 92 | `PLANNEDDATEAUTOMATICPOLICYCODE` | CHAR(20) |  |  |  |  |
| 93 | `CONFIRMEDDATECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 94 | `CONFIRMEDDATEPHASE` | CHAR(2) | NOT NULL |  |  |  |
| 95 | `CONFIRMEDDATEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 96 | `DLVWAREHOUSERESDATEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 97 | `CHECKORDERDELIVERYCODE` | CHAR(20) |  |  |  |  |
| 98 | `LINEINSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 99 | `IMMEDIATEAVAILABILITYCHECK` | CHAR(2) | NOT NULL |  |  |  |
| 100 | `SHIPPINGSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 101 | `RECEIVINGSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 102 | `PARTIALSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 103 | `ORDERLOSSAFTERPARTIALSHIPREC` | SMALLINT | NOT NULL |  |  |  |
| 104 | `RELEASELOSSAFTERPARSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 105 | `ALLLOSSAFTERPARTIALSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 106 | `SHPQTYGREATERDELIVERYDETAIL` | SMALLINT | NOT NULL |  |  |  |
| 107 | `SHIPPINGQTYGREATERORDERLINE` | SMALLINT | NOT NULL |  |  |  |
| 108 | `SHIPPINGEDITABLEUOM` | SMALLINT | NOT NULL |  |  |  |
| 109 | `SHIPPINGEDITABLEWAREHOUSE` | SMALLINT | NOT NULL |  |  |  |
| 110 | `SHIPPINGQUANTITYPOLICYCODE` | CHAR(20) |  |  |  |  |
| 111 | `SHIPPINGSUBSTITUTEITEM` | SMALLINT | NOT NULL |  |  |  |
| 112 | `SHIPPINGSINGLECOMPONENTDEPLINE` | SMALLINT | NOT NULL |  |  |  |
| 113 | `MANDATORYQUANTITYFORUNIT` | SMALLINT | NOT NULL |  |  |  |
| 114 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 115 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 116 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 117 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 118 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 119 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 120 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 121 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 122 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 123 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 124 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 125 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 126 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGINTERNALORDERLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGINTERNALORDERLINE' + known child suffix 'TEMPLATE')
  - JOIN predicate: `LOGINTERNALORDERLINETEMPLATE.FATHERID = LOGINTERNALORDERLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.ITEMNATURE,
       t.ITEMCODINGTYPE,
       t.FULLITEMREQUIRED,
       t.EXTANTITEMREQUIRED
FROM   DB2ADMIN.LOGINTERNALORDERLINETEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
