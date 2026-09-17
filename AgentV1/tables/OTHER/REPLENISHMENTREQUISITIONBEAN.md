# DB2ADMIN.REPLENISHMENTREQUISITIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 168
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 73545

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
| 14 | `COMPLETED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `RELEASEATTENDED` | SMALLINT | NOT NULL |  |  |  |
| 16 | `REJECTED` | SMALLINT | NOT NULL |  |  |  |
| 17 | `TEMPLATEREQUISITIONRESULTCODE` | CHAR(3) |  |  |  |  |
| 18 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 19 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 20 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 30 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 31 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 32 | `ORDERUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 33 | `ORDERUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 34 | `ORDERBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 35 | `ORDERBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `ORDERUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 37 | `ORDERUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `ORDERBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 39 | `ORDERBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `ORDERUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 41 | `ORDERUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 42 | `DELIVERYDATE` | DATE |  |  |  |  |
| 43 | `STATISTICALGROUPINGCODE` | CHAR(6) |  |  |  |  |
| 44 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 45 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 46 | `PURCHASEORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 47 | `PURCHASEORDERLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 48 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 49 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 50 | `CUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 51 | `CUSTOMERSUPPLIERLEGALNAME` | VARCHAR(200) |  |  |  |  |
| 52 | `DESTINATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 53 | `ORIGINWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 54 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 55 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 56 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 57 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 58 | `TOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 59 | `OPENPURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 60 | `OPENPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 61 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 62 | `PRICERETRIEVED` | DECIMAL(18,5) |  |  |  |  |
| 63 | `ORDERLINKTYPE` | CHAR(2) |  |  |  |  |
| 64 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 65 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 66 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 67 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 68 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 69 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 70 | `LINEPURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 71 | `LINEPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 72 | `LINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 73 | `LINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 74 | `INTDLVINTORDLINEINTORDCNTCODE` | CHAR(8) |  |  |  |  |
| 75 | `INTDLVINTORDLINEINTORDERCODE` | CHAR(15) |  |  |  |  |
| 76 | `INTDLVINTORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 77 | `INTDLVINTORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 78 | `INTDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 79 | `INTDOCINTDOCPRVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 80 | `INTDOCINTDOCPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 81 | `INTDOCUMENTORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 82 | `INTDOCUMENTORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 83 | `INSERTEDDATETIME` | TIMESTAMP |  |  |  |  |
| 84 | `INSERTEDUSER` | CHAR(50) |  |  |  |  |
| 85 | `FIRSTLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 86 | `FIRSTLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 87 | `SECONDLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 88 | `SECONDLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 89 | `COMPLETEDDATE` | DATE |  |  |  |  |
| 90 | `COMPLETEDUSER` | CHAR(50) |  |  |  |  |
| 91 | `RELEASEATTENDEDDATE` | DATE |  |  |  |  |
| 92 | `RELEASEATTENDEDUSER` | CHAR(50) |  |  |  |  |
| 93 | `RELEASEDDATE` | DATE |  |  |  |  |
| 94 | `RELEASEDUSER` | CHAR(50) |  |  |  |  |
| 95 | `REJECTEDDATE` | DATE |  |  |  |  |
| 96 | `REJECTEDUSER` | CHAR(50) |  |  |  |  |
| 97 | `RELEASEATTENDEDOK` | SMALLINT | NOT NULL |  |  |  |
| 98 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 99 | `HEADERCODE` | CHAR(15) |  |  |  |  |
| 100 | `HEADERLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 101 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 102 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 103 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 104 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 105 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 106 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 107 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 108 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 109 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 110 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 111 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 112 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 113 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 114 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 115 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 116 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 117 | `PMWORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 118 | `PMWORKORDERCODE` | CHAR(15) |  |  |  |  |
| 119 | `PMMACHINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 120 | `PMMACHINECODE` | CHAR(15) |  |  |  |  |
| 121 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 122 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 123 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 124 | `RFQDETAILRFQHEADERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 125 | `RFQDETAILRFQHEADERCODE` | CHAR(15) |  |  |  |  |
| 126 | `RFQDETAILLINENO` | INTEGER | NOT NULL |  |  |  |
| 127 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 128 | `REMARK` | VARCHAR(200) |  |  |  |  |
| 129 | `ORDERPRIORITY` | CHAR(2) |  |  |  |  |
| 130 | `REQUESTREASON` | VARCHAR(200) |  |  |  |  |
| 131 | `SUGGESTEDSUPPLIER` | CHAR(100) |  |  |  |  |
| 132 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 133 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 134 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 135 | `CALLEDFROM` | CHAR(30) |  |  |  |  |
| 136 | `PREVIOUSRELEASELEVEL` | CHAR(2) |  |  |  |  |
| 137 | `ORIGINALREQREQUISITIONTMPCODE` | CHAR(3) |  |  |  |  |
| 138 | `ORIGINALREQCODE` | CHAR(15) |  |  |  |  |
| 139 | `COMPLETIONPHASEFROMHEADER` | SMALLINT | NOT NULL |  |  |  |
| 140 | `PREVIOUSITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 141 | `PREVIOUSBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 142 | `PREVIOUSBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 143 | `PREVIOUSBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 144 | `PREVIOUSBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 145 | `PREVIOUSUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 146 | `PREVIOUSUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 147 | `PREVIOUSUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 148 | `PREVIOUSUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 149 | `PREVIOUSUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 150 | `PREVIOUSUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 151 | `PREVIOUSPROJECTCODE` | CHAR(20) |  |  |  |  |
| 152 | `PREVIOUSDESTINATIONWHSCODE` | CHAR(8) |  |  |  |  |
| 153 | `PREVIOUSORDERLINKTYPE` | CHAR(2) |  |  |  |  |
| 154 | `PREVIOUSFULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 155 | `SKIPRELEASELEVELCONTROL` | SMALLINT | NOT NULL |  |  |  |
| 156 | `CANBEDELETEDBYPLANNING` | SMALLINT | NOT NULL |  |  |  |
| 157 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 158 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 159 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 160 | `SAVEDDELIVERYDATE` | DATE |  |  |  |  |
| 161 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 162 | `ORIGINALREOPENLEVEL` | CHAR(2) |  |  |  |  |
| 163 | `ENABLEDRLINE` | SMALLINT | NOT NULL |  |  |  |
| 164 | `DRCOUNTER` | CHAR(8) |  |  |  |  |
| 165 | `DRCODE` | CHAR(15) |  |  |  |  |
| 166 | `DRLINE` | DECIMAL(5,0) |  |  |  |  |
| 167 | `RESETDRLINE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LENISHMENTREQUISITIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.REPLENISHMENTREQUISITIONBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
