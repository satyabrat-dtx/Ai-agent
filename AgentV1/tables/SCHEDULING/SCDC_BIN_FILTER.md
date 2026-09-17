# DB2ADMIN.SCDC_BIN_FILTER

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 350
- **Primary key**: `BF_IDENTIFIER`, `BF_WKST_CODE`, `BF_TABCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188804

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BF_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `BF_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `BF_TABCODE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `BF_TABDESC` | VARCHAR(40) |  |  |  |  |
| 4 | `BF_TABVIS` | SMALLINT |  |  |  |  |
| 5 | `BF_MINQTY` | DECIMAL(11,2) |  |  |  |  |
| 6 | `BF_MAXQTY` | DECIMAL(11,2) |  |  |  |  |
| 7 | `BF_RSC_CODE` | VARCHAR(8) |  |  |  |  |
| 8 | `BF_RSC_CODE_TO` | VARCHAR(8) |  |  |  |  |
| 9 | `BF_TYPE_PROD` | VARCHAR(3) |  |  |  |  |
| 10 | `BF_PRODLOWDATA_FROM` | TIMESTAMP |  |  |  |  |
| 11 | `BF_PRODLOWDATA_TO` | TIMESTAMP |  |  |  |  |
| 12 | `BF_DELIVDATE_FROM` | TIMESTAMP |  |  |  |  |
| 13 | `BF_DELIVDATE_TO` | TIMESTAMP |  |  |  |  |
| 14 | `BF_PLANSTARTDATE_FROM` | TIMESTAMP |  |  |  |  |
| 15 | `BF_PLANSTARTDATE_TO` | TIMESTAMP |  |  |  |  |
| 16 | `BF_PLANSTARTDATETODAY_FROM` | SMALLINT |  |  |  |  |
| 17 | `BF_PLANSTARTDATETODAY_TO` | SMALLINT |  |  |  |  |
| 18 | `BF_PLANENDDATE_FROM` | TIMESTAMP |  |  |  |  |
| 19 | `BF_PLANENDTDATE_TO` | TIMESTAMP |  |  |  |  |
| 20 | `BF_PLANENDDATETODAY_FROM` | SMALLINT |  |  |  |  |
| 21 | `BF_PLANENDDATETODAY_TO` | SMALLINT |  |  |  |  |
| 22 | `BF_NEXTSTARTDATE_FROM` | TIMESTAMP |  |  |  |  |
| 23 | `BF_NEXTSTARTDATE_TO` | TIMESTAMP |  |  |  |  |
| 24 | `BF_NEXTSTARTDATETODAY_FROM` | SMALLINT |  |  |  |  |
| 25 | `BF_NEXTSTARTDATETODAY_TO` | SMALLINT |  |  |  |  |
| 26 | `BF_PREVENDDATE_FROM` | TIMESTAMP |  |  |  |  |
| 27 | `BF_PREVENDDATE_TO` | TIMESTAMP |  |  |  |  |
| 28 | `BF_PREVENDDATETODAY_FROM` | SMALLINT |  |  |  |  |
| 29 | `BF_PREVENDDATETODAY_TO` | SMALLINT |  |  |  |  |
| 30 | `BF_LOWSTARTDATE_FROM` | TIMESTAMP |  |  |  |  |
| 31 | `BF_LOWSTARTDATE_TO` | TIMESTAMP |  |  |  |  |
| 32 | `BF_SCHEDSTARTDATE_FROM` | TIMESTAMP |  |  |  |  |
| 33 | `BF_SCHEDSTARTDATE_TO` | TIMESTAMP |  |  |  |  |
| 34 | `BF_DAYSFROMTODAY_FROM` | SMALLINT |  |  |  |  |
| 35 | `BF_DAYSFROMTODAY_TO` | SMALLINT |  |  |  |  |
| 36 | `BF_SCHEDCROSSDATE_FROM` | TIMESTAMP |  |  |  |  |
| 37 | `BF_SCHEDCROSSDATE_TO` | TIMESTAMP |  |  |  |  |
| 38 | `BF_FILTTEMPORARY` | SMALLINT |  |  |  |  |
| 39 | `BF_PREQ_NO` | VARCHAR(30) |  |  |  |  |
| 40 | `BF_READ_ONLY` | SMALLINT |  |  |  |  |
| 41 | `BF_WKCNTER` | VARCHAR(8) |  |  |  |  |
| 42 | `BF_WKCNTER_TO` | VARCHAR(8) |  |  |  |  |
| 43 | `BF_WKCT_PROC` | VARCHAR(8) |  |  |  |  |
| 44 | `BF_WKCT_PROC_TO` | VARCHAR(8) |  |  |  |  |
| 45 | `BF_SHOW_ALTERNATIVE` | SMALLINT |  |  |  |  |
| 46 | `BF_WC_FROM_PLAN` | SMALLINT |  |  |  |  |
| 47 | `BF_STEP_TYP` | CHAR(1) |  |  |  |  |
| 48 | `BF_PREQ_NO_TO` | VARCHAR(30) |  |  |  |  |
| 49 | `BF_PROD_FAMILY` | VARCHAR(120) |  |  |  |  |
| 50 | `BF_MATERIAL_FAMILY` | VARCHAR(120) |  |  |  |  |
| 51 | `BF_SCHED_JOBS` | SMALLINT |  |  |  |  |
| 52 | `BF_FLTJOBSONGANTT` | SMALLINT |  |  |  |  |
| 53 | `BF_CLOSED_JOBS` | SMALLINT |  |  |  |  |
| 54 | `BF_ONLY_READONLY` | SMALLINT |  |  |  |  |
| 55 | `BF_ONLY_SCHED` | SMALLINT |  |  |  |  |
| 56 | `BF_ONLY_CLOSED` | SMALLINT |  |  |  |  |
| 57 | `BF_GROUPS` | SMALLINT |  |  |  |  |
| 58 | `BF_ONLY_GROUPS` | SMALLINT |  |  |  |  |
| 59 | `BF_PRIORITIES` | SMALLINT |  |  |  |  |
| 60 | `BF_PROGRESS` | SMALLINT |  |  |  |  |
| 61 | `BF_ONLYPROGRESS` | SMALLINT |  |  |  |  |
| 62 | `BF_AFTERDELIVERYDAY` | SMALLINT |  |  |  |  |
| 63 | `BF_AFTERDELIVERYINDAYS` | SMALLINT |  |  |  |  |
| 64 | `BF_BEFOREEARLIESTSTART` | SMALLINT |  |  |  |  |
| 65 | `BF_BEFOREEARLIESTSTARTINDAYS` | SMALLINT |  |  |  |  |
| 66 | `BF_AFTERLATESTEND` | SMALLINT |  |  |  |  |
| 67 | `BF_AFTERLATESTENDINDAYS` | SMALLINT |  |  |  |  |
| 68 | `BF_SHOULDBESCHEDULED` | SMALLINT |  |  |  |  |
| 69 | `BF_SHOULDBESCHEDULEDINDAYS` | SMALLINT |  |  |  |  |
| 70 | `BF_MISSINGMATERIALS` | SMALLINT |  |  |  |  |
| 71 | `BF_MISSINGADDRES` | SMALLINT |  |  |  |  |
| 72 | `BF_OVERIDEPREVIOUS` | SMALLINT |  |  |  |  |
| 73 | `BF_OVERIDENEXT` | SMALLINT |  |  |  |  |
| 74 | `BF_COMPWITHPREVJOB` | SMALLINT |  |  |  |  |
| 75 | `BF_COMPWITHPREVJOBINCASE` | SMALLINT |  |  |  |  |
| 76 | `BF_COMPWITHRES` | SMALLINT |  |  |  |  |
| 77 | `BF_COMPWITHRESINCASE` | SMALLINT |  |  |  |  |
| 78 | `BF_LATESTENDINGDATE_FROM` | TIMESTAMP |  |  |  |  |
| 79 | `BF_LATESTENDINGDATE_TO` | TIMESTAMP |  |  |  |  |
| 80 | `BF_JOBMSG` | CHAR(1) |  |  |  |  |
| 81 | `BF_IMBALANCEDSTEP` | CHAR(1) |  |  |  |  |
| 82 | `BF_PSTEP_ID` | SMALLINT |  |  |  |  |
| 83 | `BF_PSTEP_ID_TO` | SMALLINT |  |  |  |  |
| 84 | `BF_ST_GROUP_FROM` | INTEGER |  |  |  |  |
| 85 | `BF_ST_GROUP_TO` | INTEGER |  |  |  |  |
| 86 | `BF_PSUBST_ID` | SMALLINT |  |  |  |  |
| 87 | `BF_PSUBST_ID_TO` | SMALLINT |  |  |  |  |
| 88 | `BF_CONF_LVL_FINAL` | CHAR(1) |  |  |  |  |
| 89 | `BF_CONF_LVL_INI` | CHAR(1) |  |  |  |  |
| 90 | `BF_CONF_LVL_1` | CHAR(1) |  |  |  |  |
| 91 | `BF_CONF_LVL_2` | CHAR(1) |  |  |  |  |
| 92 | `BF_CONF_LVL_3` | CHAR(1) |  |  |  |  |
| 93 | `BF_CONF_LVL_4` | CHAR(1) |  |  |  |  |
| 94 | `BF_CONF_LVL_5` | CHAR(1) |  |  |  |  |
| 95 | `BF_CUSTOMER_DATE_CONF` | CHAR(1) |  |  |  |  |
| 96 | `BF_CUSTOMER_DATE_CALC` | CHAR(1) |  |  |  |  |
| 97 | `BF_CUSTOMER_DATE_REQUESTD` | CHAR(1) |  |  |  |  |
| 98 | `BF_CONF_CONLVL_NEW` | CHAR(1) |  |  |  |  |
| 99 | `BF_GROUPEDBY_CODE` | VARCHAR(20) |  |  |  |  |
| 100 | `BF_SHOWFIRSTGRPLINEINBIN` | CHAR(1) |  |  |  |  |
| 101 | `BF_AUTOGRPSINGLEJOB` | CHAR(1) |  |  |  |  |
| 102 | `BF_SHOWBTCGRPLINESINBIN` | CHAR(1) |  |  |  |  |
| 103 | `BF_SHOWCONTINUEGRPLINESINBIN` | CHAR(1) |  |  |  |  |
| 104 | `BF_OVERRIDDEN_TAB` | CHAR(1) |  |  |  |  |
| 105 | `BF_DEPENDONNEXTHANDLEDSTEP` | SMALLINT |  |  |  |  |
| 106 | `BF_DEPENDONPREVHANDLEDSTEP` | SMALLINT |  |  |  |  |
| 107 | `BF_DEPENDONNXTHANDLEDLINKEDREQ` | SMALLINT |  |  |  |  |
| 108 | `BF_DEPENDONPRVHANDLEDLINKEDREQ` | SMALLINT |  |  |  |  |
| 109 | `BF_PROPCODE1` | VARCHAR(5) |  |  |  |  |
| 110 | `BF_PROPRES1` | VARCHAR(6) |  |  |  |  |
| 111 | `BF_PROPVAL_FROM1` | VARCHAR(90) |  |  |  |  |
| 112 | `BF_PROPVAL_TO1` | VARCHAR(90) |  |  |  |  |
| 113 | `BF_PROPCODE2` | VARCHAR(5) |  |  |  |  |
| 114 | `BF_PROPRES2` | VARCHAR(6) |  |  |  |  |
| 115 | `BF_PROPVAL_FROM2` | VARCHAR(90) |  |  |  |  |
| 116 | `BF_PROPVAL_TO2` | VARCHAR(90) |  |  |  |  |
| 117 | `BF_PROPCODE3` | VARCHAR(5) |  |  |  |  |
| 118 | `BF_PROPRES3` | VARCHAR(6) |  |  |  |  |
| 119 | `BF_PROPVAL_FROM3` | VARCHAR(90) |  |  |  |  |
| 120 | `BF_PROPVAL_TO3` | VARCHAR(90) |  |  |  |  |
| 121 | `BF_PROPCODE4` | VARCHAR(5) |  |  |  |  |
| 122 | `BF_PROPRES4` | VARCHAR(6) |  |  |  |  |
| 123 | `BF_PROPVAL_FROM4` | VARCHAR(90) |  |  |  |  |
| 124 | `BF_PROPVAL_TO4` | VARCHAR(90) |  |  |  |  |
| 125 | `BF_PROPCODE5` | VARCHAR(5) |  |  |  |  |
| 126 | `BF_PROPRES5` | VARCHAR(6) |  |  |  |  |
| 127 | `BF_PROPVAL_FROM5` | VARCHAR(90) |  |  |  |  |
| 128 | `BF_PROPVAL_TO5` | VARCHAR(90) |  |  |  |  |
| 129 | `BF_PROPCODE6` | VARCHAR(5) |  |  |  |  |
| 130 | `BF_PROPRES6` | VARCHAR(6) |  |  |  |  |
| 131 | `BF_PROPVAL_FROM6` | VARCHAR(90) |  |  |  |  |
| 132 | `BF_PROPVAL_TO6` | VARCHAR(90) |  |  |  |  |
| 133 | `BF_PROPCODE7` | VARCHAR(5) |  |  |  |  |
| 134 | `BF_PROPRES7` | VARCHAR(6) |  |  |  |  |
| 135 | `BF_PROPVAL_FROM7` | VARCHAR(90) |  |  |  |  |
| 136 | `BF_PROPVAL_TO7` | VARCHAR(90) |  |  |  |  |
| 137 | `BF_PROPCODE8` | VARCHAR(5) |  |  |  |  |
| 138 | `BF_PROPRES8` | VARCHAR(6) |  |  |  |  |
| 139 | `BF_PROPVAL_FROM8` | VARCHAR(90) |  |  |  |  |
| 140 | `BF_PROPVAL_TO8` | VARCHAR(90) |  |  |  |  |
| 141 | `BF_PROPCODE9` | VARCHAR(5) |  |  |  |  |
| 142 | `BF_PROPRES9` | VARCHAR(6) |  |  |  |  |
| 143 | `BF_PROPVAL_FROM9` | VARCHAR(90) |  |  |  |  |
| 144 | `BF_PROPVAL_TO9` | VARCHAR(90) |  |  |  |  |
| 145 | `BF_PROPCODE10` | VARCHAR(5) |  |  |  |  |
| 146 | `BF_PROPRES10` | VARCHAR(6) |  |  |  |  |
| 147 | `BF_PROPVAL_FROM10` | VARCHAR(90) |  |  |  |  |
| 148 | `BF_PROPVAL_TO10` | VARCHAR(90) |  |  |  |  |
| 149 | `BF_PROPCODE11` | VARCHAR(5) |  |  |  |  |
| 150 | `BF_PROPRES11` | VARCHAR(6) |  |  |  |  |
| 151 | `BF_PROPVAL_FROM11` | VARCHAR(90) |  |  |  |  |
| 152 | `BF_PROPVAL_TO11` | VARCHAR(90) |  |  |  |  |
| 153 | `BF_PROPCODE12` | VARCHAR(5) |  |  |  |  |
| 154 | `BF_PROPRES12` | VARCHAR(6) |  |  |  |  |
| 155 | `BF_PROPVAL_FROM12` | VARCHAR(90) |  |  |  |  |
| 156 | `BF_PROPVAL_TO12` | VARCHAR(90) |  |  |  |  |
| 157 | `BF_PROPCODE13` | VARCHAR(5) |  |  |  |  |
| 158 | `BF_PROPRES13` | VARCHAR(6) |  |  |  |  |
| 159 | `BF_PROPVAL_FROM13` | VARCHAR(90) |  |  |  |  |
| 160 | `BF_PROPVAL_TO13` | VARCHAR(90) |  |  |  |  |
| 161 | `BF_PROPCODE14` | VARCHAR(5) |  |  |  |  |
| 162 | `BF_PROPRES14` | VARCHAR(6) |  |  |  |  |
| 163 | `BF_PROPVAL_FROM14` | VARCHAR(90) |  |  |  |  |
| 164 | `BF_PROPVAL_TO14` | VARCHAR(90) |  |  |  |  |
| 165 | `BF_PROPCODE15` | VARCHAR(5) |  |  |  |  |
| 166 | `BF_PROPRES15` | VARCHAR(6) |  |  |  |  |
| 167 | `BF_PROPVAL_FROM15` | VARCHAR(90) |  |  |  |  |
| 168 | `BF_PROPVAL_TO15` | VARCHAR(90) |  |  |  |  |
| 169 | `BF_PROPCODE16` | VARCHAR(5) |  |  |  |  |
| 170 | `BF_PROPRES16` | VARCHAR(6) |  |  |  |  |
| 171 | `BF_PROPVAL_FROM16` | VARCHAR(90) |  |  |  |  |
| 172 | `BF_PROPVAL_TO16` | VARCHAR(90) |  |  |  |  |
| 173 | `BF_PROPCODE17` | VARCHAR(5) |  |  |  |  |
| 174 | `BF_PROPRES17` | VARCHAR(6) |  |  |  |  |
| 175 | `BF_PROPVAL_FROM17` | VARCHAR(90) |  |  |  |  |
| 176 | `BF_PROPVAL_TO17` | VARCHAR(90) |  |  |  |  |
| 177 | `BF_PROPCODE18` | VARCHAR(5) |  |  |  |  |
| 178 | `BF_PROPRES18` | VARCHAR(6) |  |  |  |  |
| 179 | `BF_PROPVAL_FROM18` | VARCHAR(90) |  |  |  |  |
| 180 | `BF_PROPVAL_TO18` | VARCHAR(90) |  |  |  |  |
| 181 | `BF_PROPCODE19` | VARCHAR(5) |  |  |  |  |
| 182 | `BF_PROPRES19` | VARCHAR(6) |  |  |  |  |
| 183 | `BF_PROPVAL_FROM19` | VARCHAR(90) |  |  |  |  |
| 184 | `BF_PROPVAL_TO19` | VARCHAR(90) |  |  |  |  |
| 185 | `BF_PROPCODE20` | VARCHAR(5) |  |  |  |  |
| 186 | `BF_PROPRES20` | VARCHAR(6) |  |  |  |  |
| 187 | `BF_PROPVAL_FROM20` | VARCHAR(90) |  |  |  |  |
| 188 | `BF_PROPVAL_TO20` | VARCHAR(90) |  |  |  |  |
| 189 | `BF_PROPCODE21` | VARCHAR(5) |  |  |  |  |
| 190 | `BF_PROPRES21` | VARCHAR(6) |  |  |  |  |
| 191 | `BF_PROPVAL_FROM21` | VARCHAR(90) |  |  |  |  |
| 192 | `BF_PROPVAL_TO21` | VARCHAR(90) |  |  |  |  |
| 193 | `BF_PROPCODE22` | VARCHAR(5) |  |  |  |  |
| 194 | `BF_PROPRES22` | VARCHAR(6) |  |  |  |  |
| 195 | `BF_PROPVAL_FROM22` | VARCHAR(90) |  |  |  |  |
| 196 | `BF_PROPVAL_TO22` | VARCHAR(90) |  |  |  |  |
| 197 | `BF_PROPCODE23` | VARCHAR(5) |  |  |  |  |
| 198 | `BF_PROPRES23` | VARCHAR(6) |  |  |  |  |
| 199 | `BF_PROPVAL_FROM23` | VARCHAR(90) |  |  |  |  |
| 200 | `BF_PROPVAL_TO23` | VARCHAR(90) |  |  |  |  |
| 201 | `BF_PROPCODE24` | VARCHAR(5) |  |  |  |  |
| 202 | `BF_PROPRES24` | VARCHAR(6) |  |  |  |  |
| 203 | `BF_PROPVAL_FROM24` | VARCHAR(90) |  |  |  |  |
| 204 | `BF_PROPVAL_TO24` | VARCHAR(90) |  |  |  |  |
| 205 | `BF_PROPCODE25` | VARCHAR(5) |  |  |  |  |
| 206 | `BF_PROPRES25` | VARCHAR(6) |  |  |  |  |
| 207 | `BF_PROPVAL_FROM25` | VARCHAR(90) |  |  |  |  |
| 208 | `BF_PROPVAL_TO25` | VARCHAR(90) |  |  |  |  |
| 209 | `BF_PROPCODE26` | VARCHAR(5) |  |  |  |  |
| 210 | `BF_PROPRES26` | VARCHAR(6) |  |  |  |  |
| 211 | `BF_PROPVAL_FROM26` | VARCHAR(90) |  |  |  |  |
| 212 | `BF_PROPVAL_TO26` | VARCHAR(90) |  |  |  |  |
| 213 | `BF_PROPCODE27` | VARCHAR(5) |  |  |  |  |
| 214 | `BF_PROPRES27` | VARCHAR(6) |  |  |  |  |
| 215 | `BF_PROPVAL_FROM27` | VARCHAR(90) |  |  |  |  |
| 216 | `BF_PROPVAL_TO27` | VARCHAR(90) |  |  |  |  |
| 217 | `BF_PROPCODE28` | VARCHAR(5) |  |  |  |  |
| 218 | `BF_PROPRES28` | VARCHAR(6) |  |  |  |  |
| 219 | `BF_PROPVAL_FROM28` | VARCHAR(90) |  |  |  |  |
| 220 | `BF_PROPVAL_TO28` | VARCHAR(90) |  |  |  |  |
| 221 | `BF_PROPCODE29` | VARCHAR(5) |  |  |  |  |
| 222 | `BF_PROPRES29` | VARCHAR(6) |  |  |  |  |
| 223 | `BF_PROPVAL_FROM29` | VARCHAR(90) |  |  |  |  |
| 224 | `BF_PROPVAL_TO29` | VARCHAR(90) |  |  |  |  |
| 225 | `BF_PROPCODE30` | VARCHAR(5) |  |  |  |  |
| 226 | `BF_PROPRES30` | VARCHAR(6) |  |  |  |  |
| 227 | `BF_PROPVAL_FROM30` | VARCHAR(90) |  |  |  |  |
| 228 | `BF_PROPVAL_TO30` | VARCHAR(90) |  |  |  |  |
| 229 | `BF_PROPCODE31` | VARCHAR(5) |  |  |  |  |
| 230 | `BF_PROPRES31` | VARCHAR(6) |  |  |  |  |
| 231 | `BF_PROPVAL_FROM31` | VARCHAR(90) |  |  |  |  |
| 232 | `BF_PROPVAL_TO31` | VARCHAR(90) |  |  |  |  |
| 233 | `BF_PROPCODE32` | VARCHAR(5) |  |  |  |  |
| 234 | `BF_PROPRES32` | VARCHAR(6) |  |  |  |  |
| 235 | `BF_PROPVAL_FROM32` | VARCHAR(90) |  |  |  |  |
| 236 | `BF_PROPVAL_TO32` | VARCHAR(90) |  |  |  |  |
| 237 | `BF_PROPCODE33` | VARCHAR(5) |  |  |  |  |
| 238 | `BF_PROPRES33` | VARCHAR(6) |  |  |  |  |
| 239 | `BF_PROPVAL_FROM33` | VARCHAR(90) |  |  |  |  |
| 240 | `BF_PROPVAL_TO33` | VARCHAR(90) |  |  |  |  |
| 241 | `BF_PROPCODE34` | VARCHAR(5) |  |  |  |  |
| 242 | `BF_PROPRES34` | VARCHAR(6) |  |  |  |  |
| 243 | `BF_PROPVAL_FROM34` | VARCHAR(90) |  |  |  |  |
| 244 | `BF_PROPVAL_TO34` | VARCHAR(90) |  |  |  |  |
| 245 | `BF_PROPCODE35` | VARCHAR(5) |  |  |  |  |
| 246 | `BF_PROPRES35` | VARCHAR(6) |  |  |  |  |
| 247 | `BF_PROPVAL_FROM35` | VARCHAR(90) |  |  |  |  |
| 248 | `BF_PROPVAL_TO35` | VARCHAR(90) |  |  |  |  |
| 249 | `BF_PROPCODE36` | VARCHAR(5) |  |  |  |  |
| 250 | `BF_PROPRES36` | VARCHAR(6) |  |  |  |  |
| 251 | `BF_PROPVAL_FROM36` | VARCHAR(90) |  |  |  |  |
| 252 | `BF_PROPVAL_TO36` | VARCHAR(90) |  |  |  |  |
| 253 | `BF_PROPCODE37` | VARCHAR(5) |  |  |  |  |
| 254 | `BF_PROPRES37` | VARCHAR(6) |  |  |  |  |
| 255 | `BF_PROPVAL_FROM37` | VARCHAR(90) |  |  |  |  |
| 256 | `BF_PROPVAL_TO37` | VARCHAR(90) |  |  |  |  |
| 257 | `BF_PROPCODE38` | VARCHAR(5) |  |  |  |  |
| 258 | `BF_PROPRES38` | VARCHAR(6) |  |  |  |  |
| 259 | `BF_PROPVAL_FROM38` | VARCHAR(90) |  |  |  |  |
| 260 | `BF_PROPVAL_TO38` | VARCHAR(90) |  |  |  |  |
| 261 | `BF_PROPCODE39` | VARCHAR(5) |  |  |  |  |
| 262 | `BF_PROPRES39` | VARCHAR(6) |  |  |  |  |
| 263 | `BF_PROPVAL_FROM39` | VARCHAR(90) |  |  |  |  |
| 264 | `BF_PROPVAL_TO39` | VARCHAR(90) |  |  |  |  |
| 265 | `BF_PROPCODE40` | VARCHAR(5) |  |  |  |  |
| 266 | `BF_PROPRES40` | VARCHAR(6) |  |  |  |  |
| 267 | `BF_PROPVAL_FROM40` | VARCHAR(90) |  |  |  |  |
| 268 | `BF_PROPVAL_TO40` | VARCHAR(90) |  |  |  |  |
| 269 | `BF_PROPCODE41` | VARCHAR(5) |  |  |  |  |
| 270 | `BF_PROPRES41` | VARCHAR(6) |  |  |  |  |
| 271 | `BF_PROPVAL_FROM41` | VARCHAR(90) |  |  |  |  |
| 272 | `BF_PROPVAL_TO41` | VARCHAR(90) |  |  |  |  |
| 273 | `BF_PROPCODE42` | VARCHAR(5) |  |  |  |  |
| 274 | `BF_PROPRES42` | VARCHAR(6) |  |  |  |  |
| 275 | `BF_PROPVAL_FROM42` | VARCHAR(90) |  |  |  |  |
| 276 | `BF_PROPVAL_TO42` | VARCHAR(90) |  |  |  |  |
| 277 | `BF_PROPCODE43` | VARCHAR(5) |  |  |  |  |
| 278 | `BF_PROPRES43` | VARCHAR(6) |  |  |  |  |
| 279 | `BF_PROPVAL_FROM43` | VARCHAR(90) |  |  |  |  |
| 280 | `BF_PROPVAL_TO43` | VARCHAR(90) |  |  |  |  |
| 281 | `BF_PROPCODE44` | VARCHAR(5) |  |  |  |  |
| 282 | `BF_PROPRES44` | VARCHAR(6) |  |  |  |  |
| 283 | `BF_PROPVAL_FROM44` | VARCHAR(90) |  |  |  |  |
| 284 | `BF_PROPVAL_TO44` | VARCHAR(90) |  |  |  |  |
| 285 | `BF_PROPCODE45` | VARCHAR(5) |  |  |  |  |
| 286 | `BF_PROPRES45` | VARCHAR(6) |  |  |  |  |
| 287 | `BF_PROPVAL_FROM45` | VARCHAR(90) |  |  |  |  |
| 288 | `BF_PROPVAL_TO45` | VARCHAR(90) |  |  |  |  |
| 289 | `BF_PROPCODE46` | VARCHAR(5) |  |  |  |  |
| 290 | `BF_PROPRES46` | VARCHAR(6) |  |  |  |  |
| 291 | `BF_PROPVAL_FROM46` | VARCHAR(90) |  |  |  |  |
| 292 | `BF_PROPVAL_TO46` | VARCHAR(90) |  |  |  |  |
| 293 | `BF_PROPCODE47` | VARCHAR(5) |  |  |  |  |
| 294 | `BF_PROPRES47` | VARCHAR(6) |  |  |  |  |
| 295 | `BF_PROPVAL_FROM47` | VARCHAR(90) |  |  |  |  |
| 296 | `BF_PROPVAL_TO47` | VARCHAR(90) |  |  |  |  |
| 297 | `BF_PROPCODE48` | VARCHAR(5) |  |  |  |  |
| 298 | `BF_PROPRES48` | VARCHAR(6) |  |  |  |  |
| 299 | `BF_PROPVAL_FROM48` | VARCHAR(90) |  |  |  |  |
| 300 | `BF_PROPVAL_TO48` | VARCHAR(90) |  |  |  |  |
| 301 | `BF_PROPCODE49` | VARCHAR(5) |  |  |  |  |
| 302 | `BF_PROPRES49` | VARCHAR(6) |  |  |  |  |
| 303 | `BF_PROPVAL_FROM49` | VARCHAR(90) |  |  |  |  |
| 304 | `BF_PROPVAL_TO49` | VARCHAR(90) |  |  |  |  |
| 305 | `BF_PROPCODE50` | VARCHAR(5) |  |  |  |  |
| 306 | `BF_PROPRES50` | VARCHAR(6) |  |  |  |  |
| 307 | `BF_PROPVAL_FROM50` | VARCHAR(90) |  |  |  |  |
| 308 | `BF_PROPVAL_TO50` | VARCHAR(90) |  |  |  |  |
| 309 | `BF_PROPCODE51` | VARCHAR(5) |  |  |  |  |
| 310 | `BF_PROPRES51` | VARCHAR(6) |  |  |  |  |
| 311 | `BF_PROPVAL_FROM51` | VARCHAR(90) |  |  |  |  |
| 312 | `BF_PROPVAL_TO51` | VARCHAR(90) |  |  |  |  |
| 313 | `BF_PROPCODE52` | VARCHAR(5) |  |  |  |  |
| 314 | `BF_PROPRES52` | VARCHAR(6) |  |  |  |  |
| 315 | `BF_PROPVAL_FROM52` | VARCHAR(90) |  |  |  |  |
| 316 | `BF_PROPVAL_TO52` | VARCHAR(90) |  |  |  |  |
| 317 | `BF_PROPCODE53` | VARCHAR(5) |  |  |  |  |
| 318 | `BF_PROPRES53` | VARCHAR(6) |  |  |  |  |
| 319 | `BF_PROPVAL_FROM53` | VARCHAR(90) |  |  |  |  |
| 320 | `BF_PROPVAL_TO53` | VARCHAR(90) |  |  |  |  |
| 321 | `BF_PROPCODE54` | VARCHAR(5) |  |  |  |  |
| 322 | `BF_PROPRES54` | VARCHAR(6) |  |  |  |  |
| 323 | `BF_PROPVAL_FROM54` | VARCHAR(90) |  |  |  |  |
| 324 | `BF_PROPVAL_TO54` | VARCHAR(90) |  |  |  |  |
| 325 | `BF_PROPCODE55` | VARCHAR(5) |  |  |  |  |
| 326 | `BF_PROPRES55` | VARCHAR(6) |  |  |  |  |
| 327 | `BF_PROPVAL_FROM55` | VARCHAR(90) |  |  |  |  |
| 328 | `BF_PROPVAL_TO55` | VARCHAR(90) |  |  |  |  |
| 329 | `BF_PROPCODE56` | VARCHAR(5) |  |  |  |  |
| 330 | `BF_PROPRES56` | VARCHAR(6) |  |  |  |  |
| 331 | `BF_PROPVAL_FROM56` | VARCHAR(90) |  |  |  |  |
| 332 | `BF_PROPVAL_TO56` | VARCHAR(90) |  |  |  |  |
| 333 | `BF_PROPCODE57` | VARCHAR(5) |  |  |  |  |
| 334 | `BF_PROPRES57` | VARCHAR(6) |  |  |  |  |
| 335 | `BF_PROPVAL_FROM57` | VARCHAR(90) |  |  |  |  |
| 336 | `BF_PROPVAL_TO57` | VARCHAR(90) |  |  |  |  |
| 337 | `BF_PROPCODE58` | VARCHAR(5) |  |  |  |  |
| 338 | `BF_PROPRES58` | VARCHAR(6) |  |  |  |  |
| 339 | `BF_PROPVAL_FROM58` | VARCHAR(90) |  |  |  |  |
| 340 | `BF_PROPVAL_TO58` | VARCHAR(90) |  |  |  |  |
| 341 | `BF_PROPCODE59` | VARCHAR(5) |  |  |  |  |
| 342 | `BF_PROPRES59` | VARCHAR(6) |  |  |  |  |
| 343 | `BF_PROPVAL_FROM59` | VARCHAR(90) |  |  |  |  |
| 344 | `BF_PROPVAL_TO59` | VARCHAR(90) |  |  |  |  |
| 345 | `BF_PROPCODE60` | VARCHAR(5) |  |  |  |  |
| 346 | `BF_PROPRES60` | VARCHAR(6) |  |  |  |  |
| 347 | `BF_PROPVAL_FROM60` | VARCHAR(90) |  |  |  |  |
| 348 | `BF_PROPVAL_TO60` | VARCHAR(90) |  |  |  |  |
| 349 | `BF_DAYSFROMTODAY_TO_TIME` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.BF_IDENTIFIER,
       t.BF_WKST_CODE,
       t.BF_TABCODE,
       t.BF_TABDESC,
       t.BF_TABVIS,
       t.BF_MINQTY,
       t.BF_MAXQTY,
       t.BF_RSC_CODE,
       t.BF_RSC_CODE_TO,
       t.BF_TYPE_PROD,
       t.BF_PRODLOWDATA_FROM,
       t.BF_PRODLOWDATA_TO
FROM   DB2ADMIN.SCDC_BIN_FILTER t
FETCH FIRST 100 ROWS ONLY;
```
