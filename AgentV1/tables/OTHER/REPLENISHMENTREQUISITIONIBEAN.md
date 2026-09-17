# DB2ADMIN.REPLENISHMENTREQUISITIONIBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 156
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 220593

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `REQUISITIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `PROPOSALORIGIN` | CHAR(2) |  |  |  |  |
| 6 | `REPLENISHMENTTYPE` | CHAR(2) |  |  |  |  |
| 7 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `PROPOSALDATE` | DATE |  |  |  |  |
| 10 | `APPLICANTCODE` | CHAR(50) |  |  |  |  |
| 11 | `PLANNERCODE` | CHAR(50) |  |  |  |  |
| 12 | `APPROVALLEVEL` | CHAR(2) |  |  |  |  |
| 13 | `RELEASELEVEL` | CHAR(2) |  |  |  |  |
| 14 | `SKIPRELEASELEVELCONTROL` | SMALLINT | NOT NULL |  |  |  |
| 15 | `COMPLETED` | SMALLINT | NOT NULL |  |  |  |
| 16 | `RELEASEATTENDED` | SMALLINT | NOT NULL |  |  |  |
| 17 | `REJECTED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `TEMPLATEREQUISITIONRESULTCODE` | CHAR(3) |  |  |  |  |
| 19 | `CANBEDELETEDBYPLANNING` | SMALLINT | NOT NULL |  |  |  |
| 20 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 21 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 22 | `ITEMDESC` | CHAR(80) |  |  |  |  |
| 23 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 24 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 25 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 26 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 27 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 37 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 38 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 39 | `PREVIOUSBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 40 | `PREVIOUSUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 41 | `PREVIOUSUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `PREVIOUSUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `ORDERUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 44 | `ORDERUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `ORDERBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 46 | `ORDERBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `ORDERUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 48 | `ORDERUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `ORDERBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `ORDERBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `ORDERUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 52 | `ORDERUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `DELIVERYDATE` | DATE |  |  |  |  |
| 54 | `SAVEDDELIVERYDATE` | DATE |  |  |  |  |
| 55 | `STATISTICALGROUPINGCODE` | CHAR(6) |  |  |  |  |
| 56 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 57 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 58 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 59 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 60 | `RFQDETAILRFQHEADERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 61 | `RFQDETAILRFQHEADERCODE` | CHAR(15) |  |  |  |  |
| 62 | `RFQDETAILLINENO` | INTEGER | NOT NULL |  |  |  |
| 63 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 64 | `REMARK` | VARCHAR(200) |  |  |  |  |
| 65 | `ORDERPRIORITY` | CHAR(2) |  |  |  |  |
| 66 | `REQUESTREASON` | VARCHAR(200) |  |  |  |  |
| 67 | `SUGGESTEDSUPPLIER` | CHAR(100) |  |  |  |  |
| 68 | `PURCHASEORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 69 | `PURCHASEORDERLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 70 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 71 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 72 | `CUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 73 | `CUSTOMERSUPPLIERLEGALNAME` | VARCHAR(200) |  |  |  |  |
| 74 | `DESTINATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 75 | `ORIGINWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 76 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 77 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 78 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 79 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 80 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 81 | `TOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 82 | `OPENPURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 83 | `OPENPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 84 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 85 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 86 | `ORDERLINKTYPE` | CHAR(2) |  |  |  |  |
| 87 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 88 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 89 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 90 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 91 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 92 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 93 | `LINEPURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 94 | `LINEPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 95 | `LINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 96 | `LINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 97 | `INTDLVINTORDLINEINTORDCNTCODE` | CHAR(8) |  |  |  |  |
| 98 | `INTDLVINTORDLINEINTORDERCODE` | CHAR(15) |  |  |  |  |
| 99 | `INTDLVINTORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 100 | `INTDLVINTORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 101 | `INTDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 102 | `INTDOCINTDOCPRVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 103 | `INTDOCINTDOCPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 104 | `INTDOCUMENTORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 105 | `INTDOCUMENTORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 106 | `PMWORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 107 | `PMWORKORDERCODE` | CHAR(15) |  |  |  |  |
| 108 | `PMMACHINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 109 | `PMMACHINECODE` | CHAR(15) |  |  |  |  |
| 110 | `ORIGINALREQREQUISITIONTMPCODE` | CHAR(3) |  |  |  |  |
| 111 | `ORIGINALREQCODE` | CHAR(15) |  |  |  |  |
| 112 | `INSERTEDDATETIME` | TIMESTAMP |  |  |  |  |
| 113 | `INSERTEDUSER` | CHAR(50) |  |  |  |  |
| 114 | `FIRSTLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 115 | `FIRSTLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 116 | `SECONDLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 117 | `SECONDLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 118 | `COMPLETEDDATE` | DATE |  |  |  |  |
| 119 | `COMPLETEDUSER` | CHAR(50) |  |  |  |  |
| 120 | `RELEASEATTENDEDDATE` | DATE |  |  |  |  |
| 121 | `RELEASEATTENDEDUSER` | CHAR(50) |  |  |  |  |
| 122 | `RELEASEDDATE` | DATE |  |  |  |  |
| 123 | `RELEASEDUSER` | CHAR(50) |  |  |  |  |
| 124 | `REJECTEDDATE` | DATE |  |  |  |  |
| 125 | `REJECTEDUSER` | CHAR(50) |  |  |  |  |
| 126 | `RELEASEATTENDEDOK` | SMALLINT | NOT NULL |  |  |  |
| 127 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 128 | `HEADERCODE` | CHAR(15) |  |  |  |  |
| 129 | `HEADERLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 130 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 131 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 132 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 133 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 134 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 135 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 136 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 137 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 138 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 139 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 140 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 141 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 142 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 143 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 144 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 145 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 146 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 147 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 148 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 149 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 150 | `ORIGINALREOPENLEVEL` | CHAR(2) |  |  |  |  |
| 151 | `ENABLEDRLINE` | SMALLINT | NOT NULL |  |  |  |
| 152 | `DRCOUNTER` | CHAR(8) |  |  |  |  |
| 153 | `DRCODE` | CHAR(15) |  |  |  |  |
| 154 | `DRLINE` | DECIMAL(5,0) |  |  |  |  |
| 155 | `RESETDRLINE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LENISHMENTREQUISITIONIBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.REQUISITIONTEMPLATECODE,
       t.PROPOSALORIGIN,
       t.REPLENISHMENTTYPE,
       t.COUNTERCODE,
       t.CODE,
       t.PROPOSALDATE,
       t.APPLICANTCODE,
       t.PLANNERCODE
FROM   DB2ADMIN.REPLENISHMENTREQUISITIONIBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
