# DB2ADMIN.LOGREPLENISHMENTREQUISITION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 147
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 67909

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `REQUISITIONTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `PROPOSALORIGIN` | CHAR(2) |  |  |  |  |
| 5 | `REPLENISHMENTTYPE` | CHAR(2) |  |  |  |  |
| 6 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `PROPOSALDATE` | DATE |  |  |  |  |
| 9 | `APPLICANTCODE` | CHAR(50) |  |  |  |  |
| 10 | `PLANNERCODE` | CHAR(50) |  |  |  |  |
| 11 | `APPROVALLEVEL` | CHAR(2) |  |  |  |  |
| 12 | `RELEASELEVEL` | CHAR(2) |  |  |  |  |
| 13 | `COMPLETED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `RELEASEATTENDED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `REJECTED` | SMALLINT | NOT NULL |  |  |  |
| 16 | `TEMPLATEREQUISITIONRESULTCODE` | CHAR(3) |  |  |  |  |
| 17 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 18 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 19 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 29 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 30 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 31 | `ORDERUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 32 | `ORDERUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `ORDERBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 34 | `ORDERBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `ORDERUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 36 | `ORDERUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 37 | `ORDERBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 38 | `ORDERBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `ORDERUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 40 | `ORDERUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 41 | `DELIVERYDATE` | DATE |  |  |  |  |
| 42 | `STATISTICALGROUPINGCODE` | CHAR(6) |  |  |  |  |
| 43 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 44 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 45 | `PURCHASEORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 46 | `PURCHASEORDERLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 47 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 48 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 49 | `CUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 50 | `DESTINATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 51 | `ORIGINWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 52 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 53 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 54 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 55 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 56 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 57 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 58 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 59 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 60 | `TOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 61 | `OPENPURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 62 | `OPENPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 63 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 64 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 65 | `ORDERLINKTYPE` | CHAR(2) |  |  |  |  |
| 66 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 67 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 68 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 69 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 70 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 71 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 72 | `LINEPURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 73 | `LINEPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 74 | `LINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 75 | `LINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 76 | `INTDLVINTORDLINEINTORDCNTCODE` | CHAR(8) |  |  |  |  |
| 77 | `INTDLVINTORDLINEINTORDERCODE` | CHAR(15) |  |  |  |  |
| 78 | `INTDLVINTORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 79 | `INTDLVINTORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 80 | `INTDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 81 | `INTDOCINTDOCPRVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 82 | `INTDOCINTDOCPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 83 | `INTDOCUMENTORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 84 | `INTDOCUMENTORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 85 | `INSERTEDDATETIME` | TIMESTAMP |  |  |  |  |
| 86 | `INSERTEDUSER` | CHAR(50) |  |  |  |  |
| 87 | `FIRSTLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 88 | `FIRSTLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 89 | `SECONDLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 90 | `SECONDLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 91 | `COMPLETEDDATE` | DATE |  |  |  |  |
| 92 | `COMPLETEDUSER` | CHAR(50) |  |  |  |  |
| 93 | `RELEASEATTENDEDDATE` | DATE |  |  |  |  |
| 94 | `RELEASEATTENDEDUSER` | CHAR(50) |  |  |  |  |
| 95 | `RELEASEDDATE` | DATE |  |  |  |  |
| 96 | `RELEASEDUSER` | CHAR(50) |  |  |  |  |
| 97 | `REJECTEDDATE` | DATE |  |  |  |  |
| 98 | `REJECTEDUSER` | CHAR(50) |  |  |  |  |
| 99 | `RELEASEATTENDEDOK` | SMALLINT | NOT NULL |  |  |  |
| 100 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 101 | `HEADERCODE` | CHAR(15) |  |  |  |  |
| 102 | `HEADERLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 103 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 104 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 105 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 106 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 107 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 108 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 109 | `COUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 110 | `APPLICANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 111 | `PLANNERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 112 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 113 | `STATISTICALGROUPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 114 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 115 | `DESTINATIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 116 | `ORIGINWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 117 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 118 | `ORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 119 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 120 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 121 | `PMWORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 122 | `PMWORKORDERCODE` | CHAR(15) |  |  |  |  |
| 123 | `PMMACHINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 124 | `PMMACHINECODE` | CHAR(15) |  |  |  |  |
| 125 | `RFQDETAILRFQHEADERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 126 | `RFQDETAILRFQHEADERCODE` | CHAR(15) |  |  |  |  |
| 127 | `RFQDETAILLINENO` | INTEGER | NOT NULL |  |  |  |
| 128 | `BUYERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 129 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 130 | `REMARK` | VARCHAR(200) |  |  |  |  |
| 131 | `ORDERPRIORITY` | CHAR(2) |  |  |  |  |
| 132 | `REQUESTREASON` | VARCHAR(200) |  |  |  |  |
| 133 | `SUGGESTEDSUPPLIER` | CHAR(100) |  |  |  |  |
| 134 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 135 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 136 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 137 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 138 | `ORIGINALREQREQUISITIONTMPCODE` | CHAR(3) |  |  |  |  |
| 139 | `ORIGINALREQCODE` | CHAR(15) |  |  |  |  |
| 140 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 141 | `CANBEDELETEDBYPLANNING` | SMALLINT | NOT NULL |  |  |  |
| 142 | `SAVEDDELIVERYDATE` | DATE |  |  |  |  |
| 143 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 144 | `DRCOUNTER` | CHAR(8) |  |  |  |  |
| 145 | `DRCODE` | CHAR(15) |  |  |  |  |
| 146 | `DRLINE` | DECIMAL(5,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGREPLENISHMENTREQUISITION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.REQUISITIONTEMPLATECODE,
       t.PROPOSALORIGIN,
       t.REPLENISHMENTTYPE,
       t.COUNTERCODE,
       t.CODE,
       t.PROPOSALDATE,
       t.APPLICANTCODE,
       t.PLANNERCODE,
       t.APPROVALLEVEL
FROM   DB2ADMIN.LOGREPLENISHMENTREQUISITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
