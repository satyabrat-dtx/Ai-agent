# DB2ADMIN.PRODUCTIBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'PRODUCT')
- **Roles**: `staging_mirror`
- **Columns**: 254
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147948

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
| 51 | `TAKEALLQADEFINITIONS` | SMALLINT | NOT NULL |  |  |  |
| 52 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 53 | `BARTYPECODE` | CHAR(2) |  |  |  |  |
| 54 | `BARCODE` | VARCHAR(50) |  |  |  |  |
| 55 | `DRAWINGNUMBER` | CHAR(100) |  |  |  |  |
| 56 | `MANUFACTURERCODE` | CHAR(15) |  |  |  |  |
| 57 | `COMPOSITIONCODE` | CHAR(10) |  |  |  |  |
| 58 | `INTRASTATCODE` | CHAR(11) |  |  |  |  |
| 59 | `LIFOGRPCODE` | CHAR(3) |  |  |  |  |
| 60 | `FOREUSESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 61 | `FOREUSECODE` | CHAR(3) |  |  |  |  |
| 62 | `STOCKTAKESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 63 | `STOCKTAKECODE` | CHAR(3) |  |  |  |  |
| 64 | `REPLENSTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 65 | `REPLENCODE` | CHAR(3) |  |  |  |  |
| 66 | `FAMILYGRPCODE` | CHAR(3) |  |  |  |  |
| 67 | `QAITEMGROUPCODE` | CHAR(10) |  |  |  |  |
| 68 | `STATUS` | CHAR(1) |  |  |  |  |
| 69 | `APPROVALDATE` | DATE |  |  |  |  |
| 70 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 71 | `RELEASEDATE` | DATE |  |  |  |  |
| 72 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 73 | `VALIDITYSTATUS` | CHAR(2) |  |  |  |  |
| 74 | `INITIALDATE` | DATE |  |  |  |  |
| 75 | `FINALDATE` | DATE |  |  |  |  |
| 76 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 77 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 78 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 79 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 80 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 81 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 82 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 83 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 84 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 85 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 86 | `PRODUCTIONUOMTYPE` | CHAR(2) |  |  |  |  |
| 87 | `PRODUCTIONUNITCODE` | CHAR(3) |  |  |  |  |
| 88 | `STDPRODUCTIONBATCH` | DECIMAL(15,5) |  |  |  |  |
| 89 | `SUBCONTRACTORSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 90 | `CUSTOMERSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 91 | `COSTCATEGORYCODE` | CHAR(20) |  |  |  |  |
| 92 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |
| 93 | `WASTEPRODUCT` | CHAR(2) |  |  |  |  |
| 94 | `PRODUCTIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 95 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 96 | `BOMVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 97 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 98 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 99 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 100 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 101 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 102 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 103 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 104 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 105 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 106 | `RTGSUBCODE01` | CHAR(20) |  |  |  |  |
| 107 | `RTGVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 108 | `RTGSUBCODE02` | CHAR(10) |  |  |  |  |
| 109 | `RTGSUBCODE03` | CHAR(10) |  |  |  |  |
| 110 | `RTGSUBCODE04` | CHAR(10) |  |  |  |  |
| 111 | `RTGSUBCODE05` | CHAR(10) |  |  |  |  |
| 112 | `RTGSUBCODE06` | CHAR(10) |  |  |  |  |
| 113 | `RTGSUBCODE07` | CHAR(10) |  |  |  |  |
| 114 | `RTGSUBCODE08` | CHAR(10) |  |  |  |  |
| 115 | `RTGSUBCODE09` | CHAR(10) |  |  |  |  |
| 116 | `RTGSUBCODE10` | CHAR(10) |  |  |  |  |
| 117 | `PICKUPPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 118 | `CONSUMPTIONFACTOR` | DECIMAL(5,2) |  |  |  |  |
| 119 | `KEEPOLDPRICE` | SMALLINT | NOT NULL |  |  |  |
| 120 | `INTERNALPRICE` | DECIMAL(18,5) |  |  |  |  |
| 121 | `INTERNALPRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 122 | `VALIDFROMDATE` | DATE |  |  |  |  |
| 123 | `VALIDTODATE` | DATE |  |  |  |  |
| 124 | `INTPRICELISTCODE` | CHAR(8) |  |  |  |  |
| 125 | `INTPRICECOSTGROUPCODE` | CHAR(8) |  |  |  |  |
| 126 | `INTPRICEPLANTCODE` | CHAR(8) |  |  |  |  |
| 127 | `NUMBEROFKEYSTOINPUT` | INTEGER | NOT NULL |  |  |  |
| 128 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 129 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 130 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 131 | `PRODWASHSYMBOL01CODE` | CHAR(10) |  |  |  |  |
| 132 | `PRODWASHSYMBOL02CODE` | CHAR(10) |  |  |  |  |
| 133 | `PRODWASHSYMBOL03CODE` | CHAR(10) |  |  |  |  |
| 134 | `PRODWASHSYMBOL04CODE` | CHAR(10) |  |  |  |  |
| 135 | `PRODWASHSYMBOL05CODE` | CHAR(10) |  |  |  |  |
| 136 | `PRODWASHSYMBOL06CODE` | CHAR(10) |  |  |  |  |
| 137 | `MAXLAYLENGTH` | DECIMAL(8,3) |  |  |  |  |
| 138 | `MAXNOLAYERS` | INTEGER | NOT NULL |  |  |  |
| 139 | `WIDTHRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 140 | `WIDTHRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 141 | `GSMRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 142 | `GSMRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 143 | `SHRINKAGE` | DECIMAL(5,2) |  |  |  |  |
| 144 | `SIITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 145 | `SISUBCODE01` | CHAR(20) |  |  |  |  |
| 146 | `SISUBCODE02` | CHAR(10) |  |  |  |  |
| 147 | `SISUBCODE03` | CHAR(10) |  |  |  |  |
| 148 | `SISUBCODE04` | CHAR(10) |  |  |  |  |
| 149 | `SISUBCODE05` | CHAR(10) |  |  |  |  |
| 150 | `SISUBCODE06` | CHAR(10) |  |  |  |  |
| 151 | `SISUBCODE07` | CHAR(10) |  |  |  |  |
| 152 | `SISUBCODE08` | CHAR(10) |  |  |  |  |
| 153 | `SISUBCODE09` | CHAR(10) |  |  |  |  |
| 154 | `SISUBCODE10` | CHAR(10) |  |  |  |  |
| 155 | `FNCSTANDARDORDERGROUPCODE` | CHAR(3) |  |  |  |  |
| 156 | `NETWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 157 | `GROSSWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 158 | `REALNETWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 159 | `WEIGHTUOMCODE` | CHAR(3) |  |  |  |  |
| 160 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 161 | `ALLOWEDDIVISIONSSTR` | VARCHAR(100) |  |  |  |  |
| 162 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 163 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 164 | `TAXTEMPLATEDETAILTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 165 | `TAXTEMPLATEDETAILCODE` | CHAR(3) |  |  |  |  |
| 166 | `GSTWITHINSTATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 167 | `GSTWITHINSTATECODE` | CHAR(3) |  |  |  |  |
| 168 | `GSTINTERSTATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 169 | `GSTINTERSTATECODE` | CHAR(3) |  |  |  |  |
| 170 | `SHIPMENTARTICLECODE` | CHAR(5) |  |  |  |  |
| 171 | `TAXTEMPLATEHEADERTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 172 | `TAXTEMPLATEHEADERCODE` | CHAR(3) |  |  |  |  |
| 173 | `INPUTCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 174 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 175 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 176 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 177 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 178 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 179 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 180 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 181 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 182 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 183 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 184 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 185 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 186 | `BUDGETUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 187 | `BUDGETUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 188 | `ARTICLESTATUSCODE` | CHAR(8) |  |  |  |  |
| 189 | `TNAHEADERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 190 | `TNAHEADERCODE` | CHAR(10) |  |  |  |  |
| 191 | `ACTIVITYDATE` | TIMESTAMP |  |  |  |  |
| 192 | `TNASTARTDATE` | TIMESTAMP |  |  |  |  |
| 193 | `TNAENDDATE` | TIMESTAMP |  |  |  |  |
| 194 | `TNARECALCULATIONENDDATE` | TIMESTAMP |  |  |  |  |
| 195 | `TNASTATUS` | INTEGER | NOT NULL |  |  |  |
| 196 | `CHECKELEMENTSCODE` | CHAR(20) |  |  |  |  |
| 197 | `ORIGINCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 198 | `PRODUCTIONBOMRULECODE` | CHAR(10) |  |  |  |  |
| 199 | `PRODUCTIONBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 200 | `COSTINGBOMRULECODE` | CHAR(10) |  |  |  |  |
| 201 | `COSTINGBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 202 | `TECHNICALBOMRULECODE` | CHAR(10) |  |  |  |  |
| 203 | `TECHNICALBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 204 | `PLANNINGBOMRULECODE` | CHAR(10) |  |  |  |  |
| 205 | `PLANNINGBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 206 | `PRODUCTIONROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 207 | `PROROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 208 | `COSTINGROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 209 | `COSTINGROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 210 | `TECHNICALROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 211 | `TECHNICALROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 212 | `PLANNINGROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 213 | `PLANNINGROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 214 | `PRODUCTIONTRANSACTIONERROR` | SMALLINT | NOT NULL |  |  |  |
| 215 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 216 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 217 | `PROTOTYPECOPYCONTEXT` | INTEGER | NOT NULL |  |  |  |
| 218 | `ORIGINPROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 219 | `ORIGINPROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 220 | `ORIGINVERSIONCHANGEREASONCODE` | CHAR(8) |  |  |  |  |
| 221 | `ENABLEDRLINE` | SMALLINT | NOT NULL |  |  |  |
| 222 | `DRCOUNTER` | CHAR(8) |  |  |  |  |
| 223 | `DRCODE` | CHAR(15) |  |  |  |  |
| 224 | `DRLINE` | DECIMAL(5,0) |  |  |  |  |
| 225 | `RESETDRLINE` | SMALLINT | NOT NULL |  |  |  |
| 226 | `MARKERLENGTHUOMCODE` | CHAR(3) |  |  |  |  |
| 227 | `AUTONETWEIGHTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 228 | `REALIGNTNA` | SMALLINT | NOT NULL |  |  |  |
| 229 | `BARCODEOUTPUT` | CHAR(1) |  |  |  |  |
| 230 | `QRCODE` | CHAR(200) |  |  |  |  |
| 231 | `QRBARCODE` | CHAR(1) |  |  |  |  |
| 232 | `MAKEORBUY` | INTEGER | NOT NULL |  |  |  |
| 233 | `ALLOWEDPRODUCTSKETCHGROUPKEY` | VARCHAR(250) |  |  |  |  |
| 234 | `NOTTRANSACTIONABLE` | SMALLINT | NOT NULL |  |  |  |
| 235 | `TIMETYPE` | INTEGER | NOT NULL |  |  |  |
| 236 | `FIXEDHOURS` | DECIMAL(10,5) |  |  |  |  |
| 237 | `SPEED` | DECIMAL(15,5) |  |  |  |  |
| 238 | `SPEEDUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 239 | `PROTOTYPEBOMPROJECT` | CHAR(16) |  |  |  |  |
| 240 | `PROTOTYPEBOMVERSION` | CHAR(3) |  |  |  |  |
| 241 | `PROTOTYPEROUTINGPROJECT` | CHAR(16) |  |  |  |  |
| 242 | `PROTOTYPEROUTINGVERSION` | CHAR(3) |  |  |  |  |
| 243 | `PRODWASHSYMBOLLABELCODE` | CHAR(10) |  |  |  |  |
| 244 | `PRODWASHFINALLABEL` | VARCHAR(500) |  |  |  |  |
| 245 | `ORIGINPROTOTYPE` | CHAR(20) |  |  |  |  |
| 246 | `GANTTMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 247 | `TNAGANTTRESOURCEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 248 | `TNAGANTTMARKERREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 249 | `TNAGANTTLINKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 250 | `TNAGANTTSUBTASKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 251 | `TNAACTIVITYGANTT` | CLOB(1000000) |  |  |  |  |
| 252 | `BARCODECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 253 | `QRCODECHANGED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTIBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.PRODUCTIBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
