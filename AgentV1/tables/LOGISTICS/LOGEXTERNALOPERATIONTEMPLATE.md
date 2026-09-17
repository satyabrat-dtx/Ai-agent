# DB2ADMIN.LOGEXTERNALOPERATIONTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 132
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 213753

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `INTERCOMPANYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `WIPISSUETEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `WIPISSUETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 10 | `WIPENTRYTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `WIPENTRYTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `STATISTICALGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `COLLECTIONGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `PROJECTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 15 | `EXTOPLINERESMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 16 | `EXTOPLINEPRODENTRYMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 17 | `SUPPLIERWAREHOUSEMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 18 | `SUPWHSENTRYTMPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `SUPWAREHOUSEENTRYTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 20 | `SUPWHSISSUETMPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 21 | `SUPWAREHOUSEISSUETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 22 | `DEFAULTSUPWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `DEFAULTSUPPLIERWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 24 | `SHPPROGRESSTMPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `SHIPPINGPROGRESSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 26 | `RECEIVINGPROGRESSTMPCMYCODE` | CHAR(3) |  |  |  |  |
| 27 | `RECEIVINGPROGRESSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 28 | `DATERECALCPROGRESSTMPCMYCODE` | CHAR(3) |  |  |  |  |
| 29 | `DATERECALCPROGRESSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 30 | `SERVICETRNTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `SERVICETRANSACTIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 32 | `SERVICETRNREVOKETMPCMYCODE` | CHAR(3) |  |  |  |  |
| 33 | `SERVICETRNREVOKETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 34 | `LINESCOUNTERRATE` | INTEGER | NOT NULL |  |  |  |
| 35 | `BUDGETCONTROL` | INTEGER | NOT NULL |  |  |  |
| 36 | `WFMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 37 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 38 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 39 | `EDITABLEITEM` | SMALLINT | NOT NULL |  |  |  |
| 40 | `EDITABLEITEMTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 41 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 42 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 43 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 44 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 45 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 46 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 47 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 48 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 49 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 50 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 51 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 52 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 53 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 54 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 55 | `ORDERCATEGORYORDERTYPE` | CHAR(1) |  |  |  |  |
| 56 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 57 | `VALUATIONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 58 | `DEFAULTPAYMENTMETHODCMYCODE` | CHAR(3) |  |  |  |  |
| 59 | `DEFAULTPAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 60 | `ONLYONEPAYMENTMETHOD` | SMALLINT | NOT NULL |  |  |  |
| 61 | `MAXIMUMDOCUMENTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 62 | `MINIMUMDOCUMENTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 63 | `CASHPAYMENTONDELIVERY` | SMALLINT | NOT NULL |  |  |  |
| 64 | `REGISTERTAXCODE` | CHAR(3) |  |  |  |  |
| 65 | `AMOUNTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 66 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 67 | `QUANTITYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 68 | `PRICELINECRITERIA` | CHAR(1) |  |  |  |  |
| 69 | `PRICELISTRULECODE` | CHAR(10) |  |  |  |  |
| 70 | `RETRIEVEPRICELISTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 71 | `PRICEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 72 | `PRICECHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 73 | `PRICECHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 74 | `MANUALPRICEALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 75 | `DISCOUNTLINECRITERIA` | CHAR(1) |  |  |  |  |
| 76 | `DISCOUNTCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 77 | `DISCOUNTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 78 | `CHARGESLINECRITERIA` | CHAR(1) |  |  |  |  |
| 79 | `CHARGESCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 80 | `CHARGESCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 81 | `PRICEAMOUNTINCLUDESTAX` | SMALLINT | NOT NULL |  |  |  |
| 82 | `TOTALAMOUNTINCLUDESTAX` | SMALLINT | NOT NULL |  |  |  |
| 83 | `ORDERVALUEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 84 | `CONTROLTYPE` | INTEGER | NOT NULL |  |  |  |
| 85 | `QTYRECEIVED` | DECIMAL(15,5) |  |  |  |  |
| 86 | `APPLIEDON` | INTEGER | NOT NULL |  |  |  |
| 87 | `TAXLINECRITERIA` | CHAR(1) |  |  |  |  |
| 88 | `TAXPOLICYCODE` | CHAR(20) |  |  |  |  |
| 89 | `TAXCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 90 | `TAXCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 91 | `SERVICERULECODE` | CHAR(10) |  |  |  |  |
| 92 | `SERVICECODE` | CHAR(20) |  |  |  |  |
| 93 | `ORDERPARTNERRULECODE` | CHAR(10) |  |  |  |  |
| 94 | `RETRIEVEORDERPARTNERCODE` | CHAR(20) |  |  |  |  |
| 95 | `ENTRYITEMRULECODE` | CHAR(10) |  |  |  |  |
| 96 | `ENTRYITEMCODE` | CHAR(20) |  |  |  |  |
| 97 | `ISSUEITEMRULECODE` | CHAR(10) |  |  |  |  |
| 98 | `RETRIEVEISSUEITEMCODE` | CHAR(20) |  |  |  |  |
| 99 | `SERVICECHKCODE` | CHAR(20) |  |  |  |  |
| 100 | `ENTRYITEMCHKCODE` | CHAR(20) |  |  |  |  |
| 101 | `CHECKEXTDOCUMENTCODE` | CHAR(20) |  |  |  |  |
| 102 | `CUSTOMEXTDOCUMENTCODE` | CHAR(20) |  |  |  |  |
| 103 | `CUSTOMEXTOPERATIONCODE` | CHAR(20) |  |  |  |  |
| 104 | `SKIPCONTROLFORCANCELLED` | SMALLINT | NOT NULL |  |  |  |
| 105 | `CHECKEXTOPERATIONCODE` | CHAR(20) |  |  |  |  |
| 106 | `CLOSURERULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 107 | `CLOSINGSTEPPOLICYCODE` | CHAR(20) |  |  |  |  |
| 108 | `COMMENTHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 109 | `HEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 110 | `COMMENTCHOOSEKEYSORDERTYPE` | CHAR(1) |  |  |  |  |
| 111 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 112 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 113 | `DERIVATIONCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 114 | `ISSUEMATERIALCOSTPOLICYCODE` | CHAR(20) |  |  |  |  |
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
| 128 | `STOPPAGEUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 129 | `STOPPAGEUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 130 | `PREVENTIONUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 131 | `PREVENTIONUSERGRPCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEXTERNALOPERATIONTEMPLATE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.INTERCOMPANYREQUIRED,
       t.WIPISSUETEMPLATECOMPANYCODE,
       t.WIPISSUETEMPLATECODE,
       t.WIPENTRYTEMPLATECOMPANYCODE,
       t.WIPENTRYTEMPLATECODE
FROM   DB2ADMIN.LOGEXTERNALOPERATIONTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
