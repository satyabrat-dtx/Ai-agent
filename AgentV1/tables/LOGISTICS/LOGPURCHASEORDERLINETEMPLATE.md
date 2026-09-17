# DB2ADMIN.LOGPURCHASEORDERLINETEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 128
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 208862

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
| 9 | `NEVERUSEMATRIX` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ITEMCODINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `FULLITEMREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `SECONDARYSUBCODESALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `EXTANTITEMREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `EDITABLEITEM` | SMALLINT | NOT NULL |  |  |  |
| 15 | `EDITABLEITEMTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 16 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 17 | `ALTERNATIVEITEMCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 18 | `QUANTITYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 19 | `EXTERNALOPERATIONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 20 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 21 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 22 | `UPDATEWAREHOUSE` | SMALLINT | NOT NULL |  |  |  |
| 23 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 25 | `STOCKTRNTEMPLATEQCCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `STOCKTRANSACTIONTEMPLATEQCCODE` | CHAR(3) |  |  |  |  |
| 27 | `SERVICETRNTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `SERVICETRANSACTIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 29 | `QUALITYCRITERIA` | CHAR(2) |  |  |  |  |
| 30 | `ALLOCATIONCRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 31 | `ALLOCATIONTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `ALLOCATIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 33 | `DERIVATIONALLTMPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 34 | `DERIVATIONALLTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 35 | `ALLOCATIONQUANTITYGREATERORDER` | SMALLINT | NOT NULL |  |  |  |
| 36 | `ALLOCFROMPURTOSAL` | SMALLINT | NOT NULL |  |  |  |
| 37 | `ALLOCFROMPURTOSALTMPCMYCODE` | CHAR(3) |  |  |  |  |
| 38 | `ALLOCFROMPURTOSALTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 39 | `DLTALLAUTOADVICETYPECMYCODE` | CHAR(3) |  |  |  |  |
| 40 | `DLTALLAUTOADVICETYPECODE` | CHAR(3) |  |  |  |  |
| 41 | `AMOUNTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 42 | `UPDATEVALUE` | SMALLINT | NOT NULL |  |  |  |
| 43 | `CURRENCYPOOLMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 44 | `PRICELINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 45 | `PRICEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 46 | `PRICECHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 47 | `PRICECHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 48 | `MANUALPRICEALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 49 | `EMPTYPRICEALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 50 | `DISCOUNTLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 51 | `DISCOUNTCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 52 | `DISCOUNTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 53 | `DERIVATIONLINEDSCPOLICYCODE` | CHAR(20) |  |  |  |  |
| 54 | `APPLYDISCOUNTHEADER` | CHAR(2) |  |  |  |  |
| 55 | `TAXLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 56 | `TAXPOLICYCODE` | CHAR(20) |  |  |  |  |
| 57 | `TAXCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 58 | `TAXCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 59 | `PRICEAMOUNTINCLUDESTAX` | SMALLINT | NOT NULL |  |  |  |
| 60 | `TOTALAMOUNTINCLUDESTAX` | SMALLINT | NOT NULL |  |  |  |
| 61 | `ORDERVALUEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 62 | `CHARGESLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 63 | `CHARGESCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 64 | `CHARGESCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 65 | `DERIVATIONLINECHRPOLICYCODE` | CHAR(20) |  |  |  |  |
| 66 | `COSTHANDLING` | CHAR(1) | NOT NULL |  |  |  |
| 67 | `COSTTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 68 | `COSTCRITERIAFORITEM` | CHAR(2) | NOT NULL |  |  |  |
| 69 | `CONTROLTYPE` | INTEGER | NOT NULL |  |  |  |
| 70 | `QTYRECEIVED` | DECIMAL(15,5) |  |  |  |  |
| 71 | `APPLIEDON` | INTEGER | NOT NULL |  |  |  |
| 72 | `LINEINORDER` | SMALLINT | NOT NULL |  |  |  |
| 73 | `LINETEMPLATEFROMOPENORDERCODE` | CHAR(3) |  |  |  |  |
| 74 | `ORDERQUANTITYGREATERQUOTATION` | SMALLINT | NOT NULL |  |  |  |
| 75 | `ORDERQUANTITYGREATEROPENORDER` | SMALLINT | NOT NULL |  |  |  |
| 76 | `ORDERRETURNWITHCLOSEDLINEUPD` | SMALLINT | NOT NULL |  |  |  |
| 77 | `COMMENTLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 78 | `LINECOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 79 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 80 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 81 | `COMMENTGROUPCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 82 | `COMMENTGROUPCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 83 | `DERIVATIONLINECMTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 84 | `COMMENTDELIVERYCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 85 | `DELIVERYCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 86 | `DELIVERYCOMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 87 | `DELIVERYCOMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 88 | `BLOCKSLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 89 | `LINEBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 90 | `BLOCKSCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 91 | `BLOCKSCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 92 | `DERIVATIONLINEBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 93 | `BLOCKSDELIVERYCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 94 | `DELIVERYBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 95 | `DELIVERYBLOCKSCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 96 | `DELIVERYBLOCKSCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 97 | `SPREADCHANGEORDERLINECODE` | CHAR(20) |  |  |  |  |
| 98 | `CHECKORDERLINECODE` | CHAR(20) |  |  |  |  |
| 99 | `CLOSURERULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 100 | `COPYDEPENDENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 101 | `ORDERSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 102 | `CONFIRMATIONORDERSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 103 | `ONLYONEDELIVERYLINE` | SMALLINT | NOT NULL |  |  |  |
| 104 | `REQUIREDDATECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 105 | `REQUIREDDATEPERTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 106 | `REQUIREDDATEPERIODTYPECODE` | CHAR(3) |  |  |  |  |
| 107 | `DLVWAREHOUSERESDATEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 108 | `LINEINSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 109 | `PARTIALSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 110 | `ORDERLOSSAFTERPARTIALSHIPREC` | SMALLINT | NOT NULL |  |  |  |
| 111 | `RECEIVINGQTYGREATERDLVDETAIL` | SMALLINT | NOT NULL |  |  |  |
| 112 | `LINEININVOICE` | SMALLINT | NOT NULL |  |  |  |
| 113 | `CHECKORDERDELIVERYCODE` | CHAR(20) |  |  |  |  |
| 114 | `INTERCOMPANYRECEIPT` | SMALLINT | NOT NULL |  |  |  |
| 115 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 116 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 117 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 118 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 119 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 120 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 121 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 122 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 123 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 124 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 125 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 126 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 127 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGPURCHASEORDERLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGPURCHASEORDERLINE' + known child suffix 'TEMPLATE')
  - JOIN predicate: `LOGPURCHASEORDERLINETEMPLATE.FATHERID = LOGPURCHASEORDERLINE.ABSUNIQUEID`

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
       t.NEVERUSEMATRIX,
       t.ITEMCODINGTYPE,
       t.FULLITEMREQUIRED
FROM   DB2ADMIN.LOGPURCHASEORDERLINETEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
