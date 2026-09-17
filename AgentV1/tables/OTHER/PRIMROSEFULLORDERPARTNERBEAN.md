# DB2ADMIN.PRIMROSEFULLORDERPARTNERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 388
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 73745

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `BUSINESSPARTNERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `CUSTOMERSUPPLIERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 5 | `CUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 6 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 7 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 8 | `ORDERLOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 9 | `ORIGININFORMATIONTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `ENDDATE` | DATE |  |  |  |  |
| 11 | `SUBSTITUTEBPNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 12 | `LEGALNAME1` | VARCHAR(270) |  |  |  |  |
| 13 | `LEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 14 | `SHORTNAME` | VARCHAR(80) |  |  |  |  |
| 15 | `SEARCHNAME` | VARCHAR(120) |  |  |  |  |
| 16 | `GROUPBPNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 17 | `SUNDRY` | SMALLINT | NOT NULL |  |  |  |
| 18 | `FISCALTYPECODE` | CHAR(2) |  |  |  |  |
| 19 | `FISCALCODE` | CHAR(16) |  |  |  |  |
| 20 | `TAXREGISTRATIONNUMBER` | CHAR(15) |  |  |  |  |
| 21 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 22 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 23 | `REPRESENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `COMPANYSUPPLIERCODE` | CHAR(10) |  |  |  |  |
| 25 | `TAXSTAMPREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 26 | `TAXSTAMPREQUIREDFORCREDIT` | SMALLINT | NOT NULL |  |  |  |
| 27 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 28 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 29 | `FINANCIALPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 30 | `FINANCIALPARTNERCODE` | CHAR(8) |  |  |  |  |
| 31 | `COMPANYBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 32 | `ACKNOWLEDGEMENTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 33 | `ACKNOWLEDGEMENTTYPE` | CHAR(2) |  |  |  |  |
| 34 | `CREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 35 | `ENDDATECREDITLIMIT` | DATE |  |  |  |  |
| 36 | `INSURANCECREDITLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 37 | `INSURANCECMYCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 38 | `INSURANCECMYCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 39 | `ENDDATEINSURANCECREDITLIMIT` | DATE |  |  |  |  |
| 40 | `AREACODE` | CHAR(3) |  |  |  |  |
| 41 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 42 | `ORDERALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 43 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 44 | `BLOCKCONTROLREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 45 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 46 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 47 | `WORKINGCALENDARCODE` | CHAR(3) |  |  |  |  |
| 48 | `DATECALCULATIONCODE` | CHAR(3) |  |  |  |  |
| 49 | `COMPANYLIABLEINITIALSCODE` | CHAR(50) |  |  |  |  |
| 50 | `MINIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 51 | `MAXIMUMORDERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 52 | `MINIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 53 | `MAXIMUMORDERDELIVERYVALUE` | DECIMAL(18,5) |  |  |  |  |
| 54 | `MINIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 55 | `MAXIMUMORDERINVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 56 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 57 | `GROUPORDERSONSHIPPING` | INTEGER | NOT NULL |  |  |  |
| 58 | `GROUPSHIPPINGSONINVOICE` | INTEGER | NOT NULL |  |  |  |
| 59 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 60 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 61 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 62 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 63 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 64 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 65 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 66 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 67 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 68 | `AGTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 69 | `AGENTGRPCODE` | CHAR(3) |  |  |  |  |
| 70 | `ASSORTGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 71 | `ASSORTGRPCODE` | CHAR(3) |  |  |  |  |
| 72 | `EXSGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 73 | `EXCLUSIVEGRPCODE` | CHAR(3) |  |  |  |  |
| 74 | `BLOCKGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 75 | `BLOCKGRPCODE` | CHAR(3) |  |  |  |  |
| 76 | `PRCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 77 | `PRICEGRPCODE` | CHAR(3) |  |  |  |  |
| 78 | `DSCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 79 | `DISCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 80 | `CHARGEGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 81 | `CHARGEGRPCODE` | CHAR(3) |  |  |  |  |
| 82 | `RESTRICGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 83 | `RESTRICGRPCODE` | CHAR(3) |  |  |  |  |
| 84 | `CMTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 85 | `COMMENTGRPCODE` | CHAR(3) |  |  |  |  |
| 86 | `TAXGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 87 | `TAXGRPCODE` | CHAR(3) |  |  |  |  |
| 88 | `MNGACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 89 | `MANAGEMENTACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 90 | `FNCACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 91 | `FINANCIALACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 92 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 93 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 94 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 95 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 96 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 97 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 98 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 99 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 100 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 101 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 102 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 103 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 104 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 105 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 106 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 107 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 108 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 109 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 110 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 111 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 112 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 113 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 114 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 115 | `PERSON` | VARCHAR(200) |  |  |  |  |
| 116 | `ROLEINTHECOMPANY` | VARCHAR(200) |  |  |  |  |
| 117 | `PHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 118 | `FAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 119 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 120 | `BOOKLINE01` | VARCHAR(200) |  |  |  |  |
| 121 | `BOOKLINE02` | VARCHAR(200) |  |  |  |  |
| 122 | `BOOKLINE03` | VARCHAR(200) |  |  |  |  |
| 123 | `BOOKLINE04` | VARCHAR(200) |  |  |  |  |
| 124 | `BOOKLINE05` | VARCHAR(200) |  |  |  |  |
| 125 | `DOCUMENTTYPEFORMAIL` | CHAR(90) |  |  |  |  |
| 126 | `PRIMROSEDISTRICTCODE` | CHAR(5) |  |  |  |  |
| 127 | `INITIALDATE` | DATE |  |  |  |  |
| 128 | `FINALDATE` | DATE |  |  |  |  |
| 129 | `EDICODE` | CHAR(20) |  |  |  |  |
| 130 | `TELEXNUMBER` | CHAR(20) |  |  |  |  |
| 131 | `SITOADDRESS` | CHAR(60) |  |  |  |  |
| 132 | `PERSONTYPE` | CHAR(1) |  |  |  |  |
| 133 | `SURNAME` | CHAR(35) |  |  |  |  |
| 134 | `NAME` | CHAR(35) |  |  |  |  |
| 135 | `DOMICILEADDRESSLINE1` | CHAR(35) |  |  |  |  |
| 136 | `DOMICILEADDRESSLINE2` | CHAR(35) |  |  |  |  |
| 137 | `DOMICILETOWN` | CHAR(35) |  |  |  |  |
| 138 | `DOMICILEPOSTALCODE` | CHAR(9) |  |  |  |  |
| 139 | `FOREIGNFISCALCODE` | CHAR(20) |  |  |  |  |
| 140 | `DOMICILECOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 141 | `DOMICILEDISTRICTCODE` | CHAR(5) |  |  |  |  |
| 142 | `PROFESSIONAL` | CHAR(1) | NOT NULL |  |  |  |
| 143 | `FORCFEST` | CHAR(15) |  |  |  |  |
| 144 | `T05CD` | CHAR(3) |  |  |  |  |
| 145 | `T41CD` | CHAR(3) |  |  |  |  |
| 146 | `T17CD` | CHAR(3) |  |  |  |  |
| 147 | `FORDTINI` | DATE |  |  |  |  |
| 148 | `FORDTFIN` | DATE |  |  |  |  |
| 149 | `FORGGEM1` | DECIMAL(2,0) |  |  |  |  |
| 150 | `FORGGEM2` | DECIMAL(2,0) |  |  |  |  |
| 151 | `FORGGEM3` | DECIMAL(2,0) |  |  |  |  |
| 152 | `FORGGEM4` | DECIMAL(2,0) |  |  |  |  |
| 153 | `FORGGEM5` | DECIMAL(2,0) |  |  |  |  |
| 154 | `FORIPES1` | CHAR(4) |  |  |  |  |
| 155 | `FORIPES2` | CHAR(4) |  |  |  |  |
| 156 | `FORIPES3` | CHAR(4) |  |  |  |  |
| 157 | `FORIPES4` | CHAR(4) |  |  |  |  |
| 158 | `FORIPES5` | CHAR(4) |  |  |  |  |
| 159 | `FORFPES1` | CHAR(4) |  |  |  |  |
| 160 | `FORFPES2` | CHAR(4) |  |  |  |  |
| 161 | `FORFPES3` | CHAR(4) |  |  |  |  |
| 162 | `FORFPES4` | CHAR(4) |  |  |  |  |
| 163 | `FORFPES5` | CHAR(4) |  |  |  |  |
| 164 | `FORDTRI1` | CHAR(4) |  |  |  |  |
| 165 | `FORDTRI2` | CHAR(4) |  |  |  |  |
| 166 | `FORDTRI3` | CHAR(4) |  |  |  |  |
| 167 | `FORDTRI4` | CHAR(4) |  |  |  |  |
| 168 | `FORDTRI5` | CHAR(4) |  |  |  |  |
| 169 | `T25CD` | CHAR(3) |  |  |  |  |
| 170 | `FORCCPCH` | CHAR(1) | NOT NULL |  |  |  |
| 171 | `FORGAPAP` | CHAR(1) |  |  |  |  |
| 172 | `VOCCD` | CHAR(12) |  |  |  |  |
| 173 | `FORCOCO2` | CHAR(12) |  |  |  |  |
| 174 | `FORCOCO3` | CHAR(12) |  |  |  |  |
| 175 | `FORCOCO4` | CHAR(12) |  |  |  |  |
| 176 | `FORCOCO5` | CHAR(12) |  |  |  |  |
| 177 | `T02CD` | CHAR(3) |  |  |  |  |
| 178 | `T18CD` | CHAR(5) |  |  |  |  |
| 179 | `FORTPVAL` | CHAR(1) |  |  |  |  |
| 180 | `FORIPPFO` | DECIMAL(1,0) |  |  |  |  |
| 181 | `FORCFINT` | CHAR(1) |  |  |  |  |
| 182 | `FORCLDIP` | CHAR(1) | NOT NULL |  |  |  |
| 183 | `FORDOGAN` | CHAR(1) | NOT NULL |  |  |  |
| 184 | `FORSOCFA` | CHAR(1) | NOT NULL |  |  |  |
| 185 | `FORIVADF` | CHAR(1) | NOT NULL |  |  |  |
| 186 | `T40CD` | CHAR(5) |  |  |  |  |
| 187 | `CLICFEST` | CHAR(15) |  |  |  |  |
| 188 | `T42CD` | CHAR(3) |  |  |  |  |
| 189 | `T16CD` | CHAR(3) |  |  |  |  |
| 190 | `CLIDTINI` | DATE |  |  |  |  |
| 191 | `CLIDTFIN` | DATE |  |  |  |  |
| 192 | `CLIGGEM1` | DECIMAL(2,0) |  |  |  |  |
| 193 | `CLIGGEM2` | DECIMAL(2,0) |  |  |  |  |
| 194 | `CLIGGEM3` | DECIMAL(2,0) |  |  |  |  |
| 195 | `CLIGGEM4` | DECIMAL(2,0) |  |  |  |  |
| 196 | `CLIGGEM5` | DECIMAL(2,0) |  |  |  |  |
| 197 | `CLIIPES1` | CHAR(4) |  |  |  |  |
| 198 | `CLIIPES2` | CHAR(4) |  |  |  |  |
| 199 | `CLIIPES3` | CHAR(4) |  |  |  |  |
| 200 | `CLIIPES4` | CHAR(4) |  |  |  |  |
| 201 | `CLIIPES5` | CHAR(4) |  |  |  |  |
| 202 | `CLIFPES1` | CHAR(4) |  |  |  |  |
| 203 | `CLIFPES2` | CHAR(4) |  |  |  |  |
| 204 | `CLIFPES3` | CHAR(4) |  |  |  |  |
| 205 | `CLIFPES4` | CHAR(4) |  |  |  |  |
| 206 | `CLIFPES5` | CHAR(4) |  |  |  |  |
| 207 | `CLIDTRI1` | CHAR(4) |  |  |  |  |
| 208 | `CLIDTRI2` | CHAR(4) |  |  |  |  |
| 209 | `CLIDTRI3` | CHAR(4) |  |  |  |  |
| 210 | `CLIDTRI4` | CHAR(4) |  |  |  |  |
| 211 | `CLIDTRI5` | CHAR(4) |  |  |  |  |
| 212 | `T30CD` | CHAR(3) |  |  |  |  |
| 213 | `CLICCPCH` | CHAR(1) | NOT NULL |  |  |  |
| 214 | `CLIGAPAP` | CHAR(1) |  |  |  |  |
| 215 | `CLICORI2` | CHAR(12) |  |  |  |  |
| 216 | `CLICORI3` | CHAR(12) |  |  |  |  |
| 217 | `CLICORI4` | CHAR(12) |  |  |  |  |
| 218 | `CLICORI5` | CHAR(12) |  |  |  |  |
| 219 | `CLITPVAL` | CHAR(1) |  |  |  |  |
| 220 | `CLICFINT` | CHAR(1) |  |  |  |  |
| 221 | `CLICLDIP` | CHAR(1) | NOT NULL |  |  |  |
| 222 | `CLIGGCAS` | DECIMAL(3,0) |  |  |  |  |
| 223 | `CLIRAEFF` | CHAR(1) |  |  |  |  |
| 224 | `CLISCOCL` | CHAR(1) |  |  |  |  |
| 225 | `CLIIVADF` | CHAR(1) |  |  |  |  |
| 226 | `T31CD` | CHAR(3) |  |  |  |  |
| 227 | `T60CD` | CHAR(5) |  |  |  |  |
| 228 | `T21TRACF` | CHAR(3) |  |  |  |  |
| 229 | `T21CD` | CHAR(5) |  |  |  |  |
| 230 | `FORTIRA2` | CHAR(3) |  |  |  |  |
| 231 | `FORSPRA2` | CHAR(5) |  |  |  |  |
| 232 | `FORTIRA3` | CHAR(3) |  |  |  |  |
| 233 | `FORSPRA3` | CHAR(5) |  |  |  |  |
| 234 | `FORTIRA4` | CHAR(3) |  |  |  |  |
| 235 | `FORSPRA4` | CHAR(5) |  |  |  |  |
| 236 | `FORTIRA5` | CHAR(3) |  |  |  |  |
| 237 | `FORSPRA5` | CHAR(5) |  |  |  |  |
| 238 | `FORESTEC` | CHAR(1) | NOT NULL |  |  |  |
| 239 | `ANICD` | DECIMAL(7,0) |  |  |  |  |
| 240 | `ANRCD` | DECIMAL(3,0) |  |  |  |  |
| 241 | `T27CD` | CHAR(4) |  |  |  |  |
| 242 | `T28CD` | CHAR(3) |  |  |  |  |
| 243 | `T66TPCNT` | CHAR(5) |  |  |  |  |
| 244 | `FORNDINT` | CHAR(10) |  |  |  |  |
| 245 | `FORDDIIN` | DATE |  |  |  |  |
| 246 | `FORNPDIN` | CHAR(10) |  |  |  |  |
| 247 | `FORIVDIN` | DATE |  |  |  |  |
| 248 | `FORFVDIN` | DATE |  |  |  |  |
| 249 | `FORCAP` | CHAR(9) |  |  |  |  |
| 250 | `FORDSRIC` | CHAR(15) |  |  |  |  |
| 251 | `FORCOFIS` | CHAR(16) |  |  |  |  |
| 252 | `FORINDIR` | CHAR(35) |  |  |  |  |
| 253 | `FORLOCAL` | CHAR(35) |  |  |  |  |
| 254 | `FORT34CD` | CHAR(3) |  |  |  |  |
| 255 | `FORPAIVA` | CHAR(15) |  |  |  |  |
| 256 | `FORT35CD` | CHAR(5) |  |  |  |  |
| 257 | `FORRASOC` | CHAR(35) |  |  |  |  |
| 258 | `FORDSRID` | CHAR(15) |  |  |  |  |
| 259 | `FORPROFE` | CHAR(1) | NOT NULL |  |  |  |
| 260 | `FORPRAGE` | CHAR(1) | NOT NULL |  |  |  |
| 261 | `FORTICER` | CHAR(1) |  |  |  |  |
| 262 | `FORCDATT` | DECIMAL(2,0) |  |  |  |  |
| 263 | `T54CD` | CHAR(5) |  |  |  |  |
| 264 | `T20TRACF` | CHAR(3) |  |  |  |  |
| 265 | `T20CD` | CHAR(5) |  |  |  |  |
| 266 | `CLITIRA2` | CHAR(3) |  |  |  |  |
| 267 | `CLISPRA2` | CHAR(5) |  |  |  |  |
| 268 | `CLITIRA3` | CHAR(3) |  |  |  |  |
| 269 | `CLISPRA3` | CHAR(5) |  |  |  |  |
| 270 | `CLITIRA4` | CHAR(3) |  |  |  |  |
| 271 | `CLISPRA4` | CHAR(5) |  |  |  |  |
| 272 | `CLITIRA5` | CHAR(3) |  |  |  |  |
| 273 | `CLISPRA5` | CHAR(5) |  |  |  |  |
| 274 | `CLIINSSO` | DECIMAL(7,0) |  |  |  |  |
| 275 | `CLIINSRI` | DECIMAL(7,0) |  |  |  |  |
| 276 | `CLICORSO` | DECIMAL(3,0) |  |  |  |  |
| 277 | `CLICORRI` | DECIMAL(3,0) |  |  |  |  |
| 278 | `CLINDINT` | CHAR(10) |  |  |  |  |
| 279 | `CLIDDIIN` | DATE |  |  |  |  |
| 280 | `CLINPDIN` | CHAR(10) |  |  |  |  |
| 281 | `CLIIVDIN` | DATE |  |  |  |  |
| 282 | `CLIFVDIN` | DATE |  |  |  |  |
| 283 | `CLIDTPRI` | DATE |  |  |  |  |
| 284 | `CLICAP` | CHAR(9) |  |  |  |  |
| 285 | `CLIDSRIC` | CHAR(15) |  |  |  |  |
| 286 | `CLICOFIS` | CHAR(16) |  |  |  |  |
| 287 | `CLIINDIR` | CHAR(35) |  |  |  |  |
| 288 | `CLILOCAL` | CHAR(35) |  |  |  |  |
| 289 | `CLIT34CD` | CHAR(3) |  |  |  |  |
| 290 | `CLIPAIVA` | CHAR(15) |  |  |  |  |
| 291 | `CLIT35CD` | CHAR(5) |  |  |  |  |
| 292 | `CLIRASOC` | CHAR(35) |  |  |  |  |
| 293 | `CLIDSRID` | CHAR(15) |  |  |  |  |
| 294 | `T19CD` | CHAR(3) |  |  |  |  |
| 295 | `CLIESTSO` | CHAR(1) | NOT NULL |  |  |  |
| 296 | `CLIERIBA` | CHAR(1) | NOT NULL |  |  |  |
| 297 | `CREATIONDATETIME2` | TIMESTAMP |  |  |  |  |
| 298 | `CREATIONUSER2` | CHAR(50) |  |  |  |  |
| 299 | `LASTUPDATEDATETIME2` | TIMESTAMP |  |  |  |  |
| 300 | `LASTUPDATEUSER2` | CHAR(50) |  |  |  |  |
| 301 | `USECREATIONUSER2` | SMALLINT | NOT NULL |  |  |  |
| 302 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 303 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 304 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 305 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 306 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 307 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 308 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 309 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 310 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 311 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 312 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 313 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 314 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 315 | `RISKCATEGORYSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 316 | `RISKCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 317 | `RISKNUMBER` | CHAR(30) |  |  |  |  |
| 318 | `TYPEOFINSURANCESYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 319 | `TYPEOFINSURANCECODE` | CHAR(10) |  |  |  |  |
| 320 | `CREDITREPORTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 321 | `CREDITREPORTCODE` | CHAR(10) |  |  |  |  |
| 322 | `CREDITREQUEST` | SMALLINT | NOT NULL |  |  |  |
| 323 | `CREDITREQUESTDATE` | DATE |  |  |  |  |
| 324 | `FINTABLENBRACCOUNTGROUP` | CHAR(5) |  |  |  |  |
| 325 | `GLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 326 | `FINANCEACCOUNTGROUPCODE` | CHAR(10) |  |  |  |  |
| 327 | `VARFORACCSTATEMENTSTDTABLECOD` | CHAR(5) |  |  |  |  |
| 328 | `VARIANTFORACCOUNTSTATEMENTCODE` | CHAR(10) |  |  |  |  |
| 329 | `VARFORBLNCNFSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 330 | `VARFORBALANCECONFIRMATIONCODE` | CHAR(10) |  |  |  |  |
| 331 | `FININITIALDATE` | DATE |  |  |  |  |
| 332 | `FINFINALDATE` | DATE |  |  |  |  |
| 333 | `FININACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 334 | `NOTEFORBOOKING` | VARCHAR(100) |  |  |  |  |
| 335 | `REMINDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 336 | `REMINDERDELIVERY` | CHAR(1) |  |  |  |  |
| 337 | `REMBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 338 | `REMBLOCKCODE` | CHAR(2) |  |  |  |  |
| 339 | `REMINDERBLOCKDATE` | DATE |  |  |  |  |
| 340 | `BUSINESSPRNFORREMINDERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 341 | `COLLECTIONDIFFERENT` | SMALLINT | NOT NULL |  |  |  |
| 342 | `COLLECTIONADDRESSNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 343 | `BADDEBTSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 344 | `BADDEBTSCODE` | CHAR(10) |  |  |  |  |
| 345 | `VALUEADJUSTMENTSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 346 | `VALUEADJUSTMENTCODE` | CHAR(10) |  |  |  |  |
| 347 | `VALUEADJUSTMENTRATE` | DECIMAL(5,2) |  |  |  |  |
| 348 | `CSMSUPSTATUSSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 349 | `CUSTOMERSUPPLIERSTATUSCODE` | CHAR(10) |  |  |  |  |
| 350 | `NOTEFORREMINDER` | VARCHAR(100) |  |  |  |  |
| 351 | `PAYMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 352 | `PAYMENTBLOCKBLOCKTYPE` | CHAR(1) |  |  |  |  |
| 353 | `PAYMENTBLOCKCODE` | CHAR(2) |  |  |  |  |
| 354 | `PAYMENTHOLDDATE` | DATE |  |  |  |  |
| 355 | `VARFORPAYMENTADVICESTDTABLECOD` | CHAR(5) |  |  |  |  |
| 356 | `VARIANTFORPAYMENTADVICECODE` | CHAR(10) |  |  |  |  |
| 357 | `BUSINESSPRNFORPAYMENTNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 358 | `NOTEFORPAYMENT` | VARCHAR(100) |  |  |  |  |
| 359 | `INTERCOMPANYDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 360 | `VATTAXCODE` | CHAR(5) |  |  |  |  |
| 361 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 362 | `CREATIONDATETIMEUTC2` | TIMESTAMP |  |  |  |  |
| 363 | `CREATIONDATETIMECMPDIV2` | TIMESTAMP |  |  |  |  |
| 364 | `CREATIONDATETIMEUSER2` | TIMESTAMP |  |  |  |  |
| 365 | `LASTUPDATEDATETIMEUTC2` | TIMESTAMP |  |  |  |  |
| 366 | `LASTUPDATEDATETIMECMPDIV2` | TIMESTAMP |  |  |  |  |
| 367 | `LASTUPDATEDATETIMEUSER2` | TIMESTAMP |  |  |  |  |
| 368 | `ASSOCIATIONMARK` | SMALLINT | NOT NULL |  |  |  |
| 369 | `ASSOCIATIONPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 370 | `ASSOCIATIONMEMBER` | CHAR(20) |  |  |  |  |
| 371 | `FISCALREPRESENTATIVENUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 372 | `PERMESTABLISHMENTCODE` | CHAR(8) |  |  |  |  |
| 373 | `FISCALREPRESENTATIVEUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 374 | `GENDER` | CHAR(1) |  |  |  |  |
| 375 | `DATEOFBIRTH` | DATE |  |  |  |  |
| 376 | `COUNTRYOFBIRTHCODE` | CHAR(3) |  |  |  |  |
| 377 | `DISTRICTOFBIRTH` | VARCHAR(200) |  |  |  |  |
| 378 | `PLACEOFBIRTH` | VARCHAR(200) |  |  |  |  |
| 379 | `EDATATRANSFERTYPE` | CHAR(1) |  |  |  |  |
| 380 | `EDATATRANSFERUNIQUEID` | CHAR(50) |  |  |  |  |
| 381 | `EDATATRANSFEREMAIL` | CHAR(150) |  |  |  |  |
| 382 | `INTERDIVISIONLINKCODE` | CHAR(10) |  |  |  |  |
| 383 | `RFPARTNERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 384 | `INSURANCESELFRETENTION` | DECIMAL(5,2) |  |  |  |  |
| 385 | `ACTIONBUTTON` | CHAR(20) |  |  |  |  |
| 386 | `NATIONALITY` | CHAR(20) |  |  |  |  |
| 387 | `DUEDATEEXCEPTIONCODE` | CHAR(6) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRIMROSEFULLORDPRNBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.BUSINESSPARTNERNUMBERID,
       t.COMPANYCODE,
       t.CUSTOMERSUPPLIERCOMPANYCODE,
       t.CUSTOMERSUPPLIERTYPE,
       t.CUSTOMERSUPPLIERCODE,
       t.SUPPLIERCODE,
       t.WAREHOUSECODE,
       t.ORDERLOGICALWAREHOUSECODE,
       t.ORIGININFORMATIONTYPECODE,
       t.ENDDATE,
       t.SUBSTITUTEBPNUMBERID
FROM   DB2ADMIN.PRIMROSEFULLORDERPARTNERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
