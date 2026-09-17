# DB2ADMIN.LOGSALESORDERLINETEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 215
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 211129

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
| 18 | `BOMANALYSISWHSGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `BOMANALYSISWHSGROUPCODE` | CHAR(3) |  |  |  |  |
| 20 | `APPROVALREQUESTMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 21 | `TRANSACTIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 22 | `QUANTITYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 23 | `EXCLUSIVEHANDLED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `RULEEXCLUSIVEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 25 | `RULECODE` | CHAR(10) |  |  |  |  |
| 26 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 28 | `UPDATEWAREHOUSE` | SMALLINT | NOT NULL |  |  |  |
| 29 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 31 | `STOCKTRNTEMPLATEQCCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `STOCKTRANSACTIONTEMPLATEQCCODE` | CHAR(3) |  |  |  |  |
| 33 | `STOCKTRNTMPRETURNCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 34 | `STOCKTRNTEMPLATERETURNCODE` | CHAR(3) |  |  |  |  |
| 35 | `QUALITYCRITERIA` | CHAR(2) |  |  |  |  |
| 36 | `ALLOCATIONCRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 37 | `ALLOCATIONTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 38 | `ALLOCATIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 39 | `ALLOCATIONQUANTITYGREATERORDER` | SMALLINT | NOT NULL |  |  |  |
| 40 | `DERIVEORDALLOCONLYORIGWHS` | SMALLINT | NOT NULL |  |  |  |
| 41 | `ALLOCATIONRELEASECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 42 | `ALLRELEASETEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `ALLOCATIONRELEASETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 44 | `ALLRELEASEQUANTITYGREATERORD` | SMALLINT | NOT NULL |  |  |  |
| 45 | `DERIVERELALLOCONLYORIGWHS` | SMALLINT | NOT NULL |  |  |  |
| 46 | `ALLOCATIONDOCUMENTCRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 47 | `ALLDOCTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 48 | `ALLOCATIONDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 49 | `ALLDOCQUANTITYGREATERDOC` | SMALLINT | NOT NULL |  |  |  |
| 50 | `DERIVEDOCALLOCONLYORIGWHS` | SMALLINT | NOT NULL |  |  |  |
| 51 | `ALLOCATIONMANAGEMENT` | CHAR(2) |  |  |  |  |
| 52 | `DLTALLAUTOADVICETYPECMYCODE` | CHAR(3) |  |  |  |  |
| 53 | `DLTALLAUTOADVICETYPECODE` | CHAR(3) |  |  |  |  |
| 54 | `AVLWAREHOUSEGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 55 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 56 | `ORIGINALLOCATIONWAREHOUSE` | SMALLINT | NOT NULL |  |  |  |
| 57 | `CONSIGNMENT` | CHAR(1) | NOT NULL |  |  |  |
| 58 | `INTRASTATBEFOREACCTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 59 | `CONSIGNMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 60 | `CONSIGNMENTWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 61 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 62 | `ISSUECONSIGNMENTTRNTMPCMYCODE` | CHAR(3) |  |  |  |  |
| 63 | `ISSUECONSIGNMENTTRNTMPCODE` | CHAR(3) |  |  |  |  |
| 64 | `ENTRYCONSIGNMENTTRNTMPCMYCODE` | CHAR(3) |  |  |  |  |
| 65 | `ENTRYCONSIGNMENTTRNTMPCODE` | CHAR(3) |  |  |  |  |
| 66 | `RETURNISSUETEMPLATECMYCODE` | CHAR(3) |  |  |  |  |
| 67 | `RETURNISSUECONSIGNMENTTMPCODE` | CHAR(3) |  |  |  |  |
| 68 | `SHPINVOICELINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 69 | `EDITABLECONSIGNMENTTEMPLATE` | SMALLINT | NOT NULL |  |  |  |
| 70 | `AMOUNTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 71 | `UPDATEVALUE` | SMALLINT | NOT NULL |  |  |  |
| 72 | `AMOUNTGREATERDELIVERYDETAIL` | SMALLINT | NOT NULL |  |  |  |
| 73 | `PRICELINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 74 | `PRICEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 75 | `PRICECHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 76 | `PRICECHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 77 | `MANUALPRICEALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 78 | `EMPTYPRICEALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 79 | `OTHERPRICEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 80 | `DISCOUNTLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 81 | `DISCOUNTSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 82 | `DISCOUNTCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 83 | `DISCOUNTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 84 | `DERIVATIONLINEDSCPOLICYCODE` | CHAR(20) |  |  |  |  |
| 85 | `APPLYDISCOUNTHEADER` | CHAR(2) |  |  |  |  |
| 86 | `TAXLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 87 | `TAXPOLICYCODE` | CHAR(20) |  |  |  |  |
| 88 | `TAXCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 89 | `TAXCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 90 | `PRICEAMOUNTINCLUDESTAX` | SMALLINT | NOT NULL |  |  |  |
| 91 | `TOTALAMOUNTINCLUDESTAX` | SMALLINT | NOT NULL |  |  |  |
| 92 | `ORDERVALUEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 93 | `CHARGESLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 94 | `FORCERETRIEVEININVOICE` | SMALLINT | NOT NULL |  |  |  |
| 95 | `LINECHARGESPOLICYCODE` | CHAR(20) |  |  |  |  |
| 96 | `CHARGESCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 97 | `CHARGESCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 98 | `DERIVATIONLINECHRPOLICYCODE` | CHAR(20) |  |  |  |  |
| 99 | `COSTHANDLING` | CHAR(1) | NOT NULL |  |  |  |
| 100 | `COSTTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 101 | `COSTCRITERIAFORITEM` | CHAR(2) | NOT NULL |  |  |  |
| 102 | `PRICINGHANDLING` | CHAR(1) | NOT NULL |  |  |  |
| 103 | `PRICINGCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 104 | `LINEINORDER` | SMALLINT | NOT NULL |  |  |  |
| 105 | `SAMPLESTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 106 | `SALLINETMPFROMOPENORDERCODE` | CHAR(3) |  |  |  |  |
| 107 | `ORDERQUANTITYGREATEROFFER` | SMALLINT | NOT NULL |  |  |  |
| 108 | `ORDERQUANTITYGREATEROPENORDER` | SMALLINT | NOT NULL |  |  |  |
| 109 | `REPLENISHMENTORDERLINK` | CHAR(2) | NOT NULL |  |  |  |
| 110 | `ORDERRETURNWITHCLOSEDLINEUPD` | SMALLINT | NOT NULL |  |  |  |
| 111 | `COMMENTLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 112 | `LINECOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 113 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 114 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 115 | `COMMENTGROUPCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 116 | `COMMENTGROUPCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 117 | `DERIVATIONLINECMTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 118 | `COMMENTDELIVERYCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 119 | `DELIVERYCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 120 | `DELIVERYCOMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 121 | `DELIVERYCOMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 122 | `BLOCKSLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 123 | `LINEBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 124 | `BLOCKSCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 125 | `BLOCKSCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 126 | `DERIVATIONLINEBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 127 | `BLOCKSDELIVERYCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 128 | `DELIVERYBLOCKSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 129 | `DELIVERYBLOCKSCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 130 | `DELIVERYBLOCKSCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 131 | `SPREADCHANGEORDERLINECODE` | CHAR(20) |  |  |  |  |
| 132 | `SPREADCHANGEDOCCODE` | CHAR(20) |  |  |  |  |
| 133 | `SPREADCHANGEDOCTODOCCODE` | CHAR(20) |  |  |  |  |
| 134 | `CHECKORDERLINECODE` | CHAR(20) |  |  |  |  |
| 135 | `CHECKDOCUMENTLINECODE` | CHAR(20) |  |  |  |  |
| 136 | `CLOSURERULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 137 | `DOCUMENTCLOSURERULECODE` | CHAR(20) |  |  |  |  |
| 138 | `COPYDEPENDENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 139 | `FUTUREAVAILABILITYCHECK` | CHAR(2) | NOT NULL |  |  |  |
| 140 | `ORDERSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 141 | `CONFIRMATIONORDERSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 142 | `ONLYONEDELIVERYLINE` | SMALLINT | NOT NULL |  |  |  |
| 143 | `REQUIREDDATECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 144 | `REQUIREDDATEPERTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 145 | `REQUIREDDATEPERIODTYPECODE` | CHAR(3) |  |  |  |  |
| 146 | `PLANNEDDATECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 147 | `PLANNEDDATEAUTOMATICPOLICYCODE` | CHAR(20) |  |  |  |  |
| 148 | `CONFIRMEDDATECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 149 | `CONFIRMEDDATEPHASE` | CHAR(2) | NOT NULL |  |  |  |
| 150 | `CONFIRMEDDATEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 151 | `DLVWAREHOUSERESDATEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 152 | `PROCONFIRMEDDATEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 153 | `SHIPPINGDATECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 154 | `CUSTOMERDELIVERYDATECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 155 | `SHIPPINGDATEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 156 | `CHECKORDERDELIVERYCODE` | CHAR(20) |  |  |  |  |
| 157 | `SHIPPINGQUANTITYPOLICYCODE` | CHAR(20) |  |  |  |  |
| 158 | `DISTRIBUTIONWAREHOUSEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 159 | `DISTRIBUTIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 160 | `DISTRIBUTIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 161 | `LINETEMINTDOCCODE` | CHAR(3) |  |  |  |  |
| 162 | `CONSIDERREADYTOSHIP` | SMALLINT | NOT NULL |  |  |  |
| 163 | `LINEINSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 164 | `ONLYMANUALRELEASE` | SMALLINT | NOT NULL |  |  |  |
| 165 | `IMMEDIATEAVAILABILITYCHECK` | CHAR(2) | NOT NULL |  |  |  |
| 166 | `RELEASESTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 167 | `SHIPPINGSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 168 | `RECEIVINGSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 169 | `RELEASERESTRICTIONCHECK` | CHAR(1) | NOT NULL |  |  |  |
| 170 | `SHIPPEDQTYFORCRNOTEVALUATION` | SMALLINT | NOT NULL |  |  |  |
| 171 | `UPDATEQTYFROMSHIPPED` | CHAR(2) |  |  |  |  |
| 172 | `PARTIALSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 173 | `ORDERLOSSAFTERPARTIALSHIPREC` | SMALLINT | NOT NULL |  |  |  |
| 174 | `RELEASELOSSAFTERPARSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 175 | `RELEASEONLYAVAILABLE` | SMALLINT | NOT NULL |  |  |  |
| 176 | `ALLLOSSAFTERPARTIALSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 177 | `SHPQTYGREATERDELIVERYDETAIL` | SMALLINT | NOT NULL |  |  |  |
| 178 | `SHIPPINGQTYGREATERORDERLINE` | SMALLINT | NOT NULL |  |  |  |
| 179 | `BILLINGQTYGREATERRELEASE` | SMALLINT | NOT NULL |  |  |  |
| 180 | `SHIPPINGEDITABLEUOM` | SMALLINT | NOT NULL |  |  |  |
| 181 | `SHIPPINGEDITABLEWAREHOUSE` | SMALLINT | NOT NULL |  |  |  |
| 182 | `SHIPPINGSUBSTITUTEITEM` | SMALLINT | NOT NULL |  |  |  |
| 183 | `MAINTAINLINEUOM` | SMALLINT | NOT NULL |  |  |  |
| 184 | `EVOLVEORIGALLOCWHSONLY` | SMALLINT | NOT NULL |  |  |  |
| 185 | `SHIPPINGSINGLECOMPONENTDEPLINE` | SMALLINT | NOT NULL |  |  |  |
| 186 | `MANDATORYQUANTITYFORUNIT` | SMALLINT | NOT NULL |  |  |  |
| 187 | `SHIPPINGRESTRICTIONCHECK` | CHAR(1) | NOT NULL |  |  |  |
| 188 | `LINEININVOICE` | SMALLINT | NOT NULL |  |  |  |
| 189 | `CREDITQUANTITYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 190 | `THIRDPARTMANUFACTORING` | SMALLINT | NOT NULL |  |  |  |
| 191 | `AGENTLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 192 | `LINEAGENTSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 193 | `AGENTCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 194 | `AGENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 195 | `COMMISSIONLINECRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 196 | `COMMISSIONSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 197 | `COMMISSIONCHOOSEKEYSTYPE` | CHAR(2) |  |  |  |  |
| 198 | `COMMISSIONCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 199 | `DERIVATIONLINECMSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 200 | `INTRATRANSACTIONNATURECODE` | CHAR(2) |  |  |  |  |
| 201 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 202 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 203 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 204 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 205 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 206 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 207 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 208 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 209 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 210 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 211 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 212 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 213 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 214 | `CONSIDERCANCELLEDQTYFORDRV` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESORDERLINE**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESORDERLINE' + known child suffix 'TEMPLATE')
  - JOIN predicate: `LOGSALESORDERLINETEMPLATE.FATHERID = LOGSALESORDERLINE.ABSUNIQUEID`

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
FROM   DB2ADMIN.LOGSALESORDERLINETEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
