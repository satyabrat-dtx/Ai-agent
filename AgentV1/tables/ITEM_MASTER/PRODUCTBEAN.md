# DB2ADMIN.PRODUCTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'PRODUCT')
- **Roles**: `staging_mirror`
- **Columns**: 239
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 66429

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `PREVIOUSDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 4 | `LOGINCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `DESCRIPTIONCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 18 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 19 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 20 | `EXTERNALCODE` | CHAR(30) |  |  |  |  |
| 21 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 22 | `BASECOSTUNITCODE` | CHAR(3) |  |  |  |  |
| 23 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 24 | `SECONDARYUNSTEADYCVSFACTOR` | DECIMAL(11,5) |  |  |  |  |
| 25 | `CONVERSIONFACTORTYPE` | CHAR(2) |  |  |  |  |
| 26 | `MULTIPLIER` | DECIMAL(11,5) |  |  |  |  |
| 27 | `CONVERSIONFACTORPOLICYCODE` | CHAR(20) |  |  |  |  |
| 28 | `CREATESELLINGITEM` | SMALLINT | NOT NULL |  |  |  |
| 29 | `CREATEPURCHASEORDERITEM` | SMALLINT | NOT NULL |  |  |  |
| 30 | `CREATEINTERNALORDERITEM` | SMALLINT | NOT NULL |  |  |  |
| 31 | `LOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 32 | `EXISTENTLOTSLOADING` | CHAR(2) |  |  |  |  |
| 33 | `LOTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 34 | `CHOOSELOTCODE` | CHAR(20) |  |  |  |  |
| 35 | `CHECKLOTCODE` | CHAR(20) |  |  |  |  |
| 36 | `LOTEXPIRATIONCODE` | CHAR(20) |  |  |  |  |
| 37 | `CONTAINERCONTROLLED` | CHAR(2) |  |  |  |  |
| 38 | `SEVERALCONTAINERTYPEALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 39 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 40 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 41 | `CHOOSECONTAINERCODE` | CHAR(20) |  |  |  |  |
| 42 | `ELEMENTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 43 | `ELEMENTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 44 | `CHOOSEELEMENTSCODE` | CHAR(20) |  |  |  |  |
| 45 | `QUALITYCONTROLLED` | CHAR(2) |  |  |  |  |
| 46 | `QUALITYGROUPCODE` | CHAR(3) |  |  |  |  |
| 47 | `PROJECTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 48 | `STATISTICALGROUPCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 49 | `CUSTOMERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 50 | `SUPPLIERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 51 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 52 | `BARTYPECODE` | CHAR(2) |  |  |  |  |
| 53 | `BARCODE` | VARCHAR(50) |  |  |  |  |
| 54 | `DRAWINGNUMBER` | CHAR(100) |  |  |  |  |
| 55 | `MANUFACTURERCODE` | CHAR(15) |  |  |  |  |
| 56 | `COMPOSITIONCODE` | CHAR(10) |  |  |  |  |
| 57 | `INTRASTATCODE` | CHAR(11) |  |  |  |  |
| 58 | `LIFOGRPCODE` | CHAR(3) |  |  |  |  |
| 59 | `FOREUSESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 60 | `FOREUSECODE` | CHAR(3) |  |  |  |  |
| 61 | `STOCKTAKESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 62 | `STOCKTAKECODE` | CHAR(3) |  |  |  |  |
| 63 | `REPLENSTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 64 | `REPLENCODE` | CHAR(3) |  |  |  |  |
| 65 | `FAMILYGRPCODE` | CHAR(3) |  |  |  |  |
| 66 | `STATUS` | CHAR(1) |  |  |  |  |
| 67 | `APPROVALDATE` | DATE |  |  |  |  |
| 68 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 69 | `RELEASEDATE` | DATE |  |  |  |  |
| 70 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 71 | `VALIDITYSTATUS` | CHAR(2) |  |  |  |  |
| 72 | `INITIALDATE` | DATE |  |  |  |  |
| 73 | `FINALDATE` | DATE |  |  |  |  |
| 74 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 75 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 76 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 77 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 78 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 79 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 80 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 81 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 82 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 83 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 84 | `PRODUCTIONUOMTYPE` | CHAR(2) |  |  |  |  |
| 85 | `PRODUCTIONUNITCODE` | CHAR(3) |  |  |  |  |
| 86 | `STDPRODUCTIONBATCH` | DECIMAL(15,5) |  |  |  |  |
| 87 | `SUBCONTRACTORSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 88 | `CUSTOMERSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 89 | `COSTCATEGORYCODE` | CHAR(20) |  |  |  |  |
| 90 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |
| 91 | `WASTEPRODUCT` | CHAR(2) |  |  |  |  |
| 92 | `PRODUCTIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 93 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 94 | `BOMVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 95 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 96 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 97 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 98 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 99 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 100 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 101 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 102 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 103 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 104 | `RTGSUBCODE01` | CHAR(20) |  |  |  |  |
| 105 | `RTGVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 106 | `RTGSUBCODE02` | CHAR(10) |  |  |  |  |
| 107 | `RTGSUBCODE03` | CHAR(10) |  |  |  |  |
| 108 | `RTGSUBCODE04` | CHAR(10) |  |  |  |  |
| 109 | `RTGSUBCODE05` | CHAR(10) |  |  |  |  |
| 110 | `RTGSUBCODE06` | CHAR(10) |  |  |  |  |
| 111 | `RTGSUBCODE07` | CHAR(10) |  |  |  |  |
| 112 | `RTGSUBCODE08` | CHAR(10) |  |  |  |  |
| 113 | `RTGSUBCODE09` | CHAR(10) |  |  |  |  |
| 114 | `RTGSUBCODE10` | CHAR(10) |  |  |  |  |
| 115 | `PICKUPPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 116 | `CONSUMPTIONFACTOR` | DECIMAL(5,2) |  |  |  |  |
| 117 | `SIITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 118 | `SISUBCODE01` | CHAR(20) |  |  |  |  |
| 119 | `SISUBCODE02` | CHAR(10) |  |  |  |  |
| 120 | `SISUBCODE03` | CHAR(10) |  |  |  |  |
| 121 | `SISUBCODE04` | CHAR(10) |  |  |  |  |
| 122 | `SISUBCODE05` | CHAR(10) |  |  |  |  |
| 123 | `SISUBCODE06` | CHAR(10) |  |  |  |  |
| 124 | `SISUBCODE07` | CHAR(10) |  |  |  |  |
| 125 | `SISUBCODE08` | CHAR(10) |  |  |  |  |
| 126 | `SISUBCODE09` | CHAR(10) |  |  |  |  |
| 127 | `SISUBCODE10` | CHAR(10) |  |  |  |  |
| 128 | `FNCSTANDARDORDERGROUPCODE` | CHAR(3) |  |  |  |  |
| 129 | `NETWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 130 | `GROSSWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 131 | `REALNETWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 132 | `WEIGHTUOMCODE` | CHAR(3) |  |  |  |  |
| 133 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 134 | `ALLOWEDDIVISIONSSTR` | VARCHAR(100) |  |  |  |  |
| 135 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 136 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 137 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 138 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 139 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 140 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 141 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 142 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 143 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 144 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 145 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 146 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 147 | `PRODWASHSYMBOL01CODE` | CHAR(10) |  |  |  |  |
| 148 | `PRODWASHSYMBOL02CODE` | CHAR(10) |  |  |  |  |
| 149 | `PRODWASHSYMBOL03CODE` | CHAR(10) |  |  |  |  |
| 150 | `PRODWASHSYMBOL04CODE` | CHAR(10) |  |  |  |  |
| 151 | `PRODWASHSYMBOL05CODE` | CHAR(10) |  |  |  |  |
| 152 | `PRODWASHSYMBOL06CODE` | CHAR(10) |  |  |  |  |
| 153 | `KEEPOLDPRICE` | SMALLINT | NOT NULL |  |  |  |
| 154 | `INTERNALPRICE` | DECIMAL(18,5) |  |  |  |  |
| 155 | `INTERNALPRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 156 | `VALIDFROMDATE` | DATE |  |  |  |  |
| 157 | `VALIDTODATE` | DATE |  |  |  |  |
| 158 | `INTPRICELISTCODE` | CHAR(8) |  |  |  |  |
| 159 | `INTPRICECOSTGROUPCODE` | CHAR(8) |  |  |  |  |
| 160 | `INTPRICEPLANTCODE` | CHAR(8) |  |  |  |  |
| 161 | `NUMBEROFKEYSTOINPUT` | INTEGER | NOT NULL |  |  |  |
| 162 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 163 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 164 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 165 | `QAITEMGROUPCODE` | CHAR(10) |  |  |  |  |
| 166 | `MAXLAYLENGTH` | DECIMAL(8,3) |  |  |  |  |
| 167 | `MAXNOLAYERS` | INTEGER | NOT NULL |  |  |  |
| 168 | `WIDTHRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 169 | `WIDTHRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 170 | `GSMRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 171 | `GSMRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 172 | `SHRINKAGE` | DECIMAL(5,2) |  |  |  |  |
| 173 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 174 | `TAKEALLQADEFINITIONS` | SMALLINT | NOT NULL |  |  |  |
| 175 | `BUDGETUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 176 | `BUDGETUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 177 | `ARTICLESTATUSCODE` | CHAR(8) |  |  |  |  |
| 178 | `TNAHEADERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 179 | `TNAHEADERCODE` | CHAR(10) |  |  |  |  |
| 180 | `ACTIVITYDATE` | TIMESTAMP |  |  |  |  |
| 181 | `CHECKELEMENTSCODE` | CHAR(20) |  |  |  |  |
| 182 | `ORIGINCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 183 | `PRODUCTIONBOMRULECODE` | CHAR(10) |  |  |  |  |
| 184 | `PRODUCTIONBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 185 | `COSTINGBOMRULECODE` | CHAR(10) |  |  |  |  |
| 186 | `COSTINGBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 187 | `TECHNICALBOMRULECODE` | CHAR(10) |  |  |  |  |
| 188 | `TECHNICALBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 189 | `PLANNINGBOMRULECODE` | CHAR(10) |  |  |  |  |
| 190 | `PLANNINGBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 191 | `PRODUCTIONROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 192 | `PROROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 193 | `COSTINGROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 194 | `COSTINGROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 195 | `TECHNICALROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 196 | `TECHNICALROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 197 | `PLANNINGROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 198 | `PLANNINGROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 199 | `PRODUCTIONTRANSACTIONERROR` | SMALLINT | NOT NULL |  |  |  |
| 200 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 201 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 202 | `PROTOTYPECOPYCONTEXT` | INTEGER | NOT NULL |  |  |  |
| 203 | `ORIGINPROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 204 | `ORIGINPROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 205 | `ORIGINVERSIONCHANGEREASONCODE` | CHAR(8) |  |  |  |  |
| 206 | `ENABLEDRLINE` | SMALLINT | NOT NULL |  |  |  |
| 207 | `DRCOUNTER` | CHAR(8) |  |  |  |  |
| 208 | `DRCODE` | CHAR(15) |  |  |  |  |
| 209 | `DRLINE` | DECIMAL(5,0) |  |  |  |  |
| 210 | `RESETDRLINE` | SMALLINT | NOT NULL |  |  |  |
| 211 | `MARKERLENGTHUOMCODE` | CHAR(3) |  |  |  |  |
| 212 | `AUTONETWEIGHTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 213 | `REALIGNTNA` | SMALLINT | NOT NULL |  |  |  |
| 214 | `BARCODEOUTPUT` | CHAR(1) |  |  |  |  |
| 215 | `QRCODE` | CHAR(200) |  |  |  |  |
| 216 | `QRBARCODE` | CHAR(1) |  |  |  |  |
| 217 | `MAKEORBUY` | INTEGER | NOT NULL |  |  |  |
| 218 | `ALLOWEDPRODUCTSKETCHGROUPKEY` | VARCHAR(250) |  |  |  |  |
| 219 | `NOTTRANSACTIONABLE` | SMALLINT | NOT NULL |  |  |  |
| 220 | `TIMETYPE` | INTEGER | NOT NULL |  |  |  |
| 221 | `FIXEDHOURS` | DECIMAL(10,5) |  |  |  |  |
| 222 | `SPEED` | DECIMAL(15,5) |  |  |  |  |
| 223 | `SPEEDUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 224 | `PROTOTYPEBOMPROJECT` | CHAR(16) |  |  |  |  |
| 225 | `PROTOTYPEBOMVERSION` | CHAR(3) |  |  |  |  |
| 226 | `PROTOTYPEROUTINGPROJECT` | CHAR(16) |  |  |  |  |
| 227 | `PROTOTYPEROUTINGVERSION` | CHAR(3) |  |  |  |  |
| 228 | `PRODWASHSYMBOLLABELCODE` | CHAR(10) |  |  |  |  |
| 229 | `PRODWASHFINALLABEL` | VARCHAR(500) |  |  |  |  |
| 230 | `ORIGINPROTOTYPE` | CHAR(20) |  |  |  |  |
| 231 | `GANTTMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 232 | `TNAGANTTRESOURCEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 233 | `TNAGANTTMARKERREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 234 | `TNAGANTTLINKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 235 | `TNAGANTTSUBTASKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 236 | `TNAACTIVITYGANTT` | CLOB(1000000) |  |  |  |  |
| 237 | `BARCODECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 238 | `QRCODECHANGED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.PREVIOUSDESCRIPTION,
       t.LOGINCOMPANYCODE,
       t.DESCRIPTIONCHANGED,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.PRODUCTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
