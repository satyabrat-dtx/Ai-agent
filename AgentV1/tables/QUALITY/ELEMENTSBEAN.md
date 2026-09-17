# DB2ADMIN.ELEMENTSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `QUALITY` (low confidence — table name starts with 'ELEMENT')
- **Roles**: `staging_mirror`
- **Columns**: 168
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 106226

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CATSSEQ` | BIGINT | NOT NULL |  |  |  |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `SUBCODEKEY` | CHAR(20) |  |  |  |  |
| 5 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 6 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 7 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 8 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 9 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 10 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 11 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 12 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 13 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 14 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 15 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 16 | `DEFINITIVEELEMENTCODE` | CHAR(15) |  |  |  |  |
| 17 | `AUTOMATICCREATIONELEMENT` | SMALLINT | NOT NULL |  |  |  |
| 18 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 19 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 20 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 21 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 22 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 23 | `ELEMENTNATURE` | CHAR(2) |  |  |  |  |
| 24 | `STATUSCODE` | CHAR(3) |  |  |  |  |
| 25 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `ENTRYDATE` | DATE |  |  |  |  |
| 27 | `FIRST` | SMALLINT | NOT NULL |  |  |  |
| 28 | `ENTRYDOCUMENTDATE` | DATE |  |  |  |  |
| 29 | `ENTRYDOCUMENTTYPE` | CHAR(2) |  |  |  |  |
| 30 | `ENTRYDOCUMENTCOUNTER` | CHAR(8) |  |  |  |  |
| 31 | `ENTRYDOCUMENTNUMBER` | CHAR(50) |  |  |  |  |
| 32 | `ISSUEDOCUMENTDATE` | DATE |  |  |  |  |
| 33 | `ISSUEDOCUMENTTYPE` | CHAR(2) |  |  |  |  |
| 34 | `ISSUEDOCUMENTCOUNTER` | CHAR(8) |  |  |  |  |
| 35 | `ISSUEDOCUMENTNUMBER` | CHAR(50) |  |  |  |  |
| 36 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 37 | `CUSTOMERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 38 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 39 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 40 | `SUPPLIERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 41 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 42 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 43 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 44 | `CUTITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 45 | `CUTITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 46 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 47 | `FIRSTQUALITYCONTROLDATE` | DATE |  |  |  |  |
| 48 | `FIRSTQUALITYCONTROLCOUNTER` | CHAR(8) |  |  |  |  |
| 49 | `FIRSTQUALITYCONTROLNUMBER` | CHAR(15) |  |  |  |  |
| 50 | `BASEPRIMARYUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 51 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `BASESECONDARYUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 53 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 54 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 55 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 56 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 57 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 58 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 59 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 60 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 61 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 62 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 63 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 64 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 65 | `QUANTITY1` | DECIMAL(15,5) |  |  |  |  |
| 66 | `UNITOFMEASURE1CODE` | CHAR(3) |  |  |  |  |
| 67 | `QUANTITY12` | DECIMAL(15,5) |  |  |  |  |
| 68 | `UNITOFMEASURE12CODE` | CHAR(3) |  |  |  |  |
| 69 | `QUANTITY13` | DECIMAL(15,5) |  |  |  |  |
| 70 | `UNITOFMEASURE13CODE` | CHAR(3) |  |  |  |  |
| 71 | `QUANTITY2` | DECIMAL(15,5) |  |  |  |  |
| 72 | `UNITOFMEASURE2CODE` | CHAR(3) |  |  |  |  |
| 73 | `QUANTITY3` | DECIMAL(15,5) |  |  |  |  |
| 74 | `UNITOFMEASURE3CODE` | CHAR(3) |  |  |  |  |
| 75 | `QUANTITY4` | DECIMAL(15,5) |  |  |  |  |
| 76 | `UNITOFMEASURE4CODE` | CHAR(3) |  |  |  |  |
| 77 | `QUANTITY5` | DECIMAL(15,5) |  |  |  |  |
| 78 | `UNITOFMEASURE5CODE` | CHAR(3) |  |  |  |  |
| 79 | `QUANTITY21` | DECIMAL(15,5) |  |  |  |  |
| 80 | `UNITOFMEASURE21CODE` | CHAR(3) |  |  |  |  |
| 81 | `QUANTITY22` | DECIMAL(15,5) |  |  |  |  |
| 82 | `UNITOFMEASURE22CODE` | CHAR(3) |  |  |  |  |
| 83 | `QUANTITY23` | DECIMAL(15,5) |  |  |  |  |
| 84 | `UNITOFMEASURE23CODE` | CHAR(3) |  |  |  |  |
| 85 | `QUANTITY24` | DECIMAL(15,5) |  |  |  |  |
| 86 | `UNITOFMEASURE24CODE` | CHAR(3) |  |  |  |  |
| 87 | `QUANTITY25` | DECIMAL(15,5) |  |  |  |  |
| 88 | `UNITOFMEASURE25CODE` | CHAR(3) |  |  |  |  |
| 89 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 90 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 91 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 92 | `IMPORTCODE` | CHAR(15) |  |  |  |  |
| 93 | `ELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 94 | `ELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 95 | `ELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 96 | `ELEMENTCODE` | CHAR(15) |  |  |  |  |
| 97 | `INSPECTIONINDEX` | INTEGER | NOT NULL |  |  |  |
| 98 | `EVENTSLINK` | CHAR(15) |  |  |  |  |
| 99 | `NUMBERGROUPSHIFT` | INTEGER | NOT NULL |  |  |  |
| 100 | `NUMBERSHIFT` | INTEGER | NOT NULL |  |  |  |
| 101 | `OPERATORCODE` | CHAR(50) |  |  |  |  |
| 102 | `WEAVERCODE` | CHAR(50) |  |  |  |  |
| 103 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 104 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 105 | `DLVPURORDLINEPURORDCNTCODE` | CHAR(8) |  |  |  |  |
| 106 | `DLVPURORDLINEPURORDERCODE` | CHAR(15) |  |  |  |  |
| 107 | `DLVPURCHASEORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 108 | `DLVPURORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 109 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 110 | `PACKINGTYPECODE` | CHAR(3) |  |  |  |  |
| 111 | `LENGTHUOMCODE` | CHAR(3) |  |  |  |  |
| 112 | `LENGTHINITIAL` | DECIMAL(7,2) |  |  |  |  |
| 113 | `LENGTHGROSS` | DECIMAL(7,2) |  |  |  |  |
| 114 | `WEIGHTUOMCODE` | CHAR(3) |  |  |  |  |
| 115 | `WEIGHTGROSS` | DECIMAL(7,2) |  |  |  |  |
| 116 | `WEIGHTNET` | DECIMAL(7,2) |  |  |  |  |
| 117 | `WEIGHTREALNET` | DECIMAL(7,2) |  |  |  |  |
| 118 | `WIDTHUOMCODE` | CHAR(3) |  |  |  |  |
| 119 | `WIDTHGROSS` | DECIMAL(7,2) |  |  |  |  |
| 120 | `WIDTHNET` | DECIMAL(7,2) |  |  |  |  |
| 121 | `QUALITYINSPECTIONCODE` | DECIMAL(2,0) |  |  |  |  |
| 122 | `QUALITYREASONINSPECTIONCODE` | CHAR(3) |  |  |  |  |
| 123 | `TOTALPOINTS` | DECIMAL(5,0) |  |  |  |  |
| 124 | `TOTALCREDITS` | DECIMAL(7,2) |  |  |  |  |
| 125 | `NUMBEROFPIECES` | DECIMAL(5,0) |  |  |  |  |
| 126 | `NUMBEROFDEFECTS` | DECIMAL(5,0) |  |  |  |  |
| 127 | `NUMBEROFDEFECTSINCALC` | DECIMAL(5,2) |  |  |  |  |
| 128 | `SHORTESTPIECELENGHT` | DECIMAL(7,2) |  |  |  |  |
| 129 | `PREDOMINANTDEFECTEVENTCODE` | CHAR(3) |  |  |  |  |
| 130 | `PREDEFECTGRPSTDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 131 | `PREDOMINANTDEFECTGROUPCODE` | CHAR(3) |  |  |  |  |
| 132 | `POINTTABLESTDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 133 | `POINTTABLECODE` | CHAR(3) |  |  |  |  |
| 134 | `VARIABLE` | VARCHAR(250) |  |  |  |  |
| 135 | `INSPECTIONSTARTDATETIME` | TIMESTAMP |  |  |  |  |
| 136 | `INSPECTIONENDDATETIME` | TIMESTAMP |  |  |  |  |
| 137 | `INSPECTIONTIME` | TIME |  |  |  |  |
| 138 | `INSPECTIONSTOPTIME` | TIME |  |  |  |  |
| 139 | `LOOMNUMBER` | CHAR(10) |  |  |  |  |
| 140 | `INSPECTIONSTATION` | CHAR(10) |  |  |  |  |
| 141 | `WINDINGMACHINE` | CHAR(10) |  |  |  |  |
| 142 | `ORIGINALELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 143 | `ORIGINALELEMENTCODE` | CHAR(15) |  |  |  |  |
| 144 | `ORIGINALELELMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 145 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 146 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 147 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 148 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 149 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 150 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 151 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 152 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 153 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 154 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 155 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 156 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 157 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 158 | `FATHERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 159 | `REUNIFICATE` | SMALLINT | NOT NULL |  |  |  |
| 160 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 161 | `ENTRYDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 162 | `ISSUEDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 163 | `ORIGINCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 164 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 165 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 166 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 167 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ELEMENTSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.CATSSEQ,
       t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODEKEY,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05,
       t.DECOSUBCODE06,
       t.DECOSUBCODE07
FROM   DB2ADMIN.ELEMENTSBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
