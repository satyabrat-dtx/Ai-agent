# DB2ADMIN.PRODUCTIONDEMANDSTEPBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 290
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 87464

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 3 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `ROUTINGNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 15 | `RTGSUBCODE01` | CHAR(20) |  |  |  |  |
| 16 | `RTGVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 17 | `RTGSUBCODE02` | CHAR(10) |  |  |  |  |
| 18 | `RTGSUBCODE03` | CHAR(10) |  |  |  |  |
| 19 | `RTGSUBCODE04` | CHAR(10) |  |  |  |  |
| 20 | `RTGSUBCODE05` | CHAR(10) |  |  |  |  |
| 21 | `RTGSUBCODE06` | CHAR(10) |  |  |  |  |
| 22 | `RTGSUBCODE07` | CHAR(10) |  |  |  |  |
| 23 | `RTGSUBCODE08` | CHAR(10) |  |  |  |  |
| 24 | `RTGSUBCODE09` | CHAR(10) |  |  |  |  |
| 25 | `RTGSUBCODE10` | CHAR(10) |  |  |  |  |
| 26 | `RTGSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 27 | `STDROUTINGSTEPNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 28 | `STDROUTINGSTEPSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 29 | `STDROUTINGSTEPSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 30 | `PLANNEDWORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 31 | `PLANNEDOPERATIONCODE` | CHAR(8) |  |  |  |  |
| 32 | `PARTIALSTEP` | SMALLINT | NOT NULL |  |  |  |
| 33 | `WORKCENTERANDOPERATTRIBUTESCOD` | CHAR(20) |  |  |  |  |
| 34 | `WORKCENTERANDOPERATTRCHANGED` | CHAR(2) |  |  |  |  |
| 35 | `RUNMANUALREOPEN` | SMALLINT | NOT NULL |  |  |  |
| 36 | `RUNMANUALCLOSURE` | SMALLINT | NOT NULL |  |  |  |
| 37 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 38 | `STEPTYPE` | CHAR(2) |  |  |  |  |
| 39 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 40 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 41 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 42 | `MAXNUMBEROFRESOURCESALLOWED` | DECIMAL(3,0) |  |  |  |  |
| 43 | `WAREHOUSEWIPCODE` | CHAR(8) |  |  |  |  |
| 44 | `LOCWIPISSUEWHSZONEPHYWHSCODE` | CHAR(8) |  |  |  |  |
| 45 | `LOCWIPISSUEWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 46 | `LOCATIONWIPISSUECODE` | CHAR(10) |  |  |  |  |
| 47 | `LOCWIPENTRYWHSZONEPHYWHSCODE` | CHAR(8) |  |  |  |  |
| 48 | `LOCWIPENTRYWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 49 | `LOCATIONWIPENTRYCODE` | CHAR(10) |  |  |  |  |
| 50 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 51 | `FIRSTISSUEDONE` | CHAR(2) |  |  |  |  |
| 52 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 53 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 54 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 55 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 56 | `VIRTUALSTEPTYPE` | CHAR(2) |  |  |  |  |
| 57 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 58 | `STEPNUMBERLINK` | DECIMAL(5,0) |  |  |  |  |
| 59 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 60 | `CALENDARCODE` | CHAR(3) |  |  |  |  |
| 61 | `INITIALPLANNEDDATETIME` | TIMESTAMP |  |  |  |  |
| 62 | `FINALPLANNEDDATETIME` | TIMESTAMP |  |  |  |  |
| 63 | `INITIALSCHEDULEDDATETIME` | TIMESTAMP |  |  |  |  |
| 64 | `FINALSCHEDULEDDATETIME` | TIMESTAMP |  |  |  |  |
| 65 | `SCHEDULEDSTEP` | SMALLINT | NOT NULL |  |  |  |
| 66 | `UOMTYPE` | CHAR(2) |  |  |  |  |
| 67 | `STANDARDSTEPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 68 | `STANDARDSTEPQUANTITYUOMCODE` | CHAR(3) |  |  |  |  |
| 69 | `STEPEFFICIENCYAPPLY` | CHAR(1) |  |  |  |  |
| 70 | `STEPEFFICIENCY` | DECIMAL(5,2) |  |  |  |  |
| 71 | `NROFMACHINE` | INTEGER | NOT NULL |  |  |  |
| 72 | `REPETITIONNUMBER` | DECIMAL(17,6) |  |  |  |  |
| 73 | `BATHVOLUME` | DECIMAL(17,6) |  |  |  |  |
| 74 | `BATHVOLUMEUOMCODE` | CHAR(3) |  |  |  |  |
| 75 | `CURRENTSTEPPROGRESS` | CHAR(1) |  |  |  |  |
| 76 | `PREVIOUSSTEPPROGRESS` | CHAR(1) |  |  |  |  |
| 77 | `OPSTEPGROUPCODE` | CHAR(8) |  |  |  |  |
| 78 | `OVERLAPPINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 79 | `OVERLAPPINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 80 | `OVERLAPPINGUOMCATEGORY` | CHAR(1) |  |  |  |  |
| 81 | `LOSSINCREASETYPE1CODE` | CHAR(3) |  |  |  |  |
| 82 | `LOSSINCREASE1` | DECIMAL(15,5) |  |  |  |  |
| 83 | `LOSSINCREASEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 84 | `LOSSINCREASETYPE2CODE` | CHAR(3) |  |  |  |  |
| 85 | `LOSSINCREASE2` | DECIMAL(15,5) |  |  |  |  |
| 86 | `LOSSINCREASEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 87 | `LOSSINCREASETYPE3CODE` | CHAR(3) |  |  |  |  |
| 88 | `LOSSINCREASE3` | DECIMAL(15,5) |  |  |  |  |
| 89 | `LOSSINCREASEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 90 | `LOSSINCREASETYPE4CODE` | CHAR(3) |  |  |  |  |
| 91 | `LOSSINCREASE4` | DECIMAL(15,5) |  |  |  |  |
| 92 | `LOSSINCREASEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 93 | `LOSSINCREASETYPE5CODE` | CHAR(3) |  |  |  |  |
| 94 | `LOSSINCREASE5` | DECIMAL(15,5) |  |  |  |  |
| 95 | `LOSSINCREASEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 96 | `LOSSINCREASETYPE6CODE` | CHAR(3) |  |  |  |  |
| 97 | `LOSSINCREASE6` | DECIMAL(15,5) |  |  |  |  |
| 98 | `LOSSINCREASEREFUOM6CODE` | CHAR(3) |  |  |  |  |
| 99 | `LOSSINCREASETYPE7CODE` | CHAR(3) |  |  |  |  |
| 100 | `LOSSINCREASE7` | DECIMAL(15,5) |  |  |  |  |
| 101 | `LOSSINCREASEREFUOM7CODE` | CHAR(3) |  |  |  |  |
| 102 | `LOSSINCREASETYPE8CODE` | CHAR(3) |  |  |  |  |
| 103 | `LOSSINCREASE8` | DECIMAL(15,5) |  |  |  |  |
| 104 | `LOSSINCREASEREFUOM8CODE` | CHAR(3) |  |  |  |  |
| 105 | `LOSSINCREASETYPEPOLICY` | CHAR(3) |  |  |  |  |
| 106 | `PLANNINGLEADTIME` | DECIMAL(15,5) |  |  |  |  |
| 107 | `TIMETYPE1CODE` | CHAR(3) |  |  |  |  |
| 108 | `TIME1` | DECIMAL(10,5) |  |  |  |  |
| 109 | `TIMEUNIT1` | CHAR(2) |  |  |  |  |
| 110 | `TIMEREFQTY1` | DECIMAL(15,5) |  |  |  |  |
| 111 | `TIMEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 112 | `PERCENTAGE1` | DECIMAL(5,2) |  |  |  |  |
| 113 | `LINKEDTIME1` | CHAR(2) |  |  |  |  |
| 114 | `TIMETYPE2CODE` | CHAR(3) |  |  |  |  |
| 115 | `TIME2` | DECIMAL(10,5) |  |  |  |  |
| 116 | `TIMEUNIT2` | CHAR(2) |  |  |  |  |
| 117 | `TIMEREFQTY2` | DECIMAL(15,5) |  |  |  |  |
| 118 | `TIMEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 119 | `PERCENTAGE2` | DECIMAL(5,2) |  |  |  |  |
| 120 | `LINKEDTIME2` | CHAR(2) |  |  |  |  |
| 121 | `TIMETYPE3CODE` | CHAR(3) |  |  |  |  |
| 122 | `TIME3` | DECIMAL(10,5) |  |  |  |  |
| 123 | `TIMEUNIT3` | CHAR(2) |  |  |  |  |
| 124 | `TIMEREFQTY3` | DECIMAL(15,5) |  |  |  |  |
| 125 | `TIMEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 126 | `PERCENTAGE3` | DECIMAL(5,2) |  |  |  |  |
| 127 | `LINKEDTIME3` | CHAR(2) |  |  |  |  |
| 128 | `TIMETYPE4CODE` | CHAR(3) |  |  |  |  |
| 129 | `TIME4` | DECIMAL(10,5) |  |  |  |  |
| 130 | `TIMEUNIT4` | CHAR(2) |  |  |  |  |
| 131 | `TIMEREFQTY4` | DECIMAL(15,5) |  |  |  |  |
| 132 | `TIMEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 133 | `PERCENTAGE4` | DECIMAL(5,2) |  |  |  |  |
| 134 | `LINKEDTIME4` | CHAR(2) |  |  |  |  |
| 135 | `TIMETYPE5CODE` | CHAR(3) |  |  |  |  |
| 136 | `TIME5` | DECIMAL(10,5) |  |  |  |  |
| 137 | `TIMEUNIT5` | CHAR(2) |  |  |  |  |
| 138 | `TIMEREFQTY5` | DECIMAL(15,5) |  |  |  |  |
| 139 | `TIMEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 140 | `PERCENTAGE5` | DECIMAL(5,2) |  |  |  |  |
| 141 | `LINKEDTIME5` | CHAR(2) |  |  |  |  |
| 142 | `CALCULATEDTIME1` | DECIMAL(10,5) |  |  |  |  |
| 143 | `CALCULATEDTIME2` | DECIMAL(10,5) |  |  |  |  |
| 144 | `CALCULATEDTIME3` | DECIMAL(10,5) |  |  |  |  |
| 145 | `CALCULATEDTIME4` | DECIMAL(10,5) |  |  |  |  |
| 146 | `QUEUERECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 147 | `PREPROCESSRECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 148 | `PROCESSRECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 149 | `POSTPROCESSRECORDEDMACHINETIME` | DECIMAL(15,5) |  |  |  |  |
| 150 | `MINBEGINQUEUE` | DATE |  |  |  |  |
| 151 | `MINBEGINQUEUETIME` | TIME |  |  |  |  |
| 152 | `WEEKMINBEGINQUEUE` | INTEGER | NOT NULL |  |  |  |
| 153 | `YEARMINBEGINQUEUE` | INTEGER | NOT NULL |  |  |  |
| 154 | `MINBEGINPRESETUP` | DATE |  |  |  |  |
| 155 | `MINBEGINPRESETUPTIME` | TIME |  |  |  |  |
| 156 | `WEEKMINBEGINPRESETUP` | INTEGER | NOT NULL |  |  |  |
| 157 | `YEARMINBEGINPRESETUP` | INTEGER | NOT NULL |  |  |  |
| 158 | `MINBEGINOPERATION` | DATE |  |  |  |  |
| 159 | `MINBEGINOPERATIONTIME` | TIME |  |  |  |  |
| 160 | `WEEKMINBEGINOPERATION` | INTEGER | NOT NULL |  |  |  |
| 161 | `YEARMINBEGINOPERATION` | INTEGER | NOT NULL |  |  |  |
| 162 | `MINBEGINPOSTSETUP` | DATE |  |  |  |  |
| 163 | `MINBEGINPOSTSETUPTIME` | TIME |  |  |  |  |
| 164 | `WEEKMINBEGINPOSTSETUP` | INTEGER | NOT NULL |  |  |  |
| 165 | `YEARMINBEGINPOSTSETUP` | INTEGER | NOT NULL |  |  |  |
| 166 | `MINENDSTEP` | DATE |  |  |  |  |
| 167 | `MINENDSTEPTIME` | TIME |  |  |  |  |
| 168 | `WEEKMINENDSTEP` | INTEGER | NOT NULL |  |  |  |
| 169 | `YEARMINENDSTEP` | INTEGER | NOT NULL |  |  |  |
| 170 | `ACTUALBEGINQUEUEDATE` | DATE |  |  |  |  |
| 171 | `ACTUALBEGINPREPROCESSDATE` | DATE |  |  |  |  |
| 172 | `ACTUALBEGINPROCESSDATE` | DATE |  |  |  |  |
| 173 | `ACTUALBEGINPOSTPROCESSDATE` | DATE |  |  |  |  |
| 174 | `ACTUALENDDATE` | DATE |  |  |  |  |
| 175 | `STDBEGINQUEUE` | DATE |  |  |  |  |
| 176 | `STDBEGINQUEUETIME` | TIME |  |  |  |  |
| 177 | `WEEKSTDBEGINQUEUE` | INTEGER | NOT NULL |  |  |  |
| 178 | `YEARSTDBEGINQUEUE` | INTEGER | NOT NULL |  |  |  |
| 179 | `STDBEGINPRESETUP` | DATE |  |  |  |  |
| 180 | `STDBEGINPRESETUPTIME` | TIME |  |  |  |  |
| 181 | `WEEKSTDBEGINPRESETUP` | INTEGER | NOT NULL |  |  |  |
| 182 | `YEARSTDBEGINPRESETUP` | INTEGER | NOT NULL |  |  |  |
| 183 | `STDBEGINOPERATION` | DATE |  |  |  |  |
| 184 | `STDBEGINOPERATIONTIME` | TIME |  |  |  |  |
| 185 | `WEEKSTDBEGINOPERATION` | INTEGER | NOT NULL |  |  |  |
| 186 | `YEARSTDBEGINOPERATION` | INTEGER | NOT NULL |  |  |  |
| 187 | `STDBEGINPOSTSETUP` | DATE |  |  |  |  |
| 188 | `STDBEGINPOSTSETUPTIME` | TIME |  |  |  |  |
| 189 | `WEEKSTDBEGINPOSTSETUP` | INTEGER | NOT NULL |  |  |  |
| 190 | `YEARSTDBEGINPOSTSETUP` | INTEGER | NOT NULL |  |  |  |
| 191 | `STDENDSTEP` | DATE |  |  |  |  |
| 192 | `STDENDSTEPTIME` | TIME |  |  |  |  |
| 193 | `WEEKSTDENDSTEP` | INTEGER | NOT NULL |  |  |  |
| 194 | `YEARSTDENDSTEP` | INTEGER | NOT NULL |  |  |  |
| 195 | `RECALCULATEDBEGINQUEUEDATE` | DATE |  |  |  |  |
| 196 | `RECALCULATEDBEGINPREPROCDATE` | DATE |  |  |  |  |
| 197 | `RECALCULATEDBEGINPROCESSDATE` | DATE |  |  |  |  |
| 198 | `RECALCULATEDBEGINPOSTPROCDATE` | DATE |  |  |  |  |
| 199 | `RECALCULATEDENDDATE` | DATE |  |  |  |  |
| 200 | `MAXBEGINQUEUE` | DATE |  |  |  |  |
| 201 | `MAXBEGINQUEUETIME` | TIME |  |  |  |  |
| 202 | `WEEKMAXBEGINQUEUE` | INTEGER | NOT NULL |  |  |  |
| 203 | `YEARMAXBEGINQUEUE` | INTEGER | NOT NULL |  |  |  |
| 204 | `MAXBEGINPRESETUP` | DATE |  |  |  |  |
| 205 | `MAXBEGINPRESETUPTIME` | TIME |  |  |  |  |
| 206 | `WEEKMAXBEGINPRESETUP` | INTEGER | NOT NULL |  |  |  |
| 207 | `YEARMAXBEGINPRESETUP` | INTEGER | NOT NULL |  |  |  |
| 208 | `MAXBEGINOPERATION` | DATE |  |  |  |  |
| 209 | `MAXBEGINOPERATIONTIME` | TIME |  |  |  |  |
| 210 | `WEEKMAXBEGINOPERATION` | INTEGER | NOT NULL |  |  |  |
| 211 | `YEARMAXBEGINOPERATION` | INTEGER | NOT NULL |  |  |  |
| 212 | `MAXBEGINPOSTSETUP` | DATE |  |  |  |  |
| 213 | `MAXBEGINPOSTSETUPTIME` | TIME |  |  |  |  |
| 214 | `WEEKMAXBEGINPOSTSETUP` | INTEGER | NOT NULL |  |  |  |
| 215 | `YEARMAXBEGINPOSTSETUP` | INTEGER | NOT NULL |  |  |  |
| 216 | `MAXENDSTEP` | DATE |  |  |  |  |
| 217 | `MAXENDSTEPTIME` | TIME |  |  |  |  |
| 218 | `WEEKMAXENDSTEP` | INTEGER | NOT NULL |  |  |  |
| 219 | `YEARMAXENDSTEP` | INTEGER | NOT NULL |  |  |  |
| 220 | `BOXHIDEUOM` | SMALLINT | NOT NULL |  |  |  |
| 221 | `INITIALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 222 | `FINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 223 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 224 | `INITIALBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 225 | `FINALBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 226 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 227 | `INITIALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 228 | `FINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 229 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 230 | `INITIALBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 231 | `FINALBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 232 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 233 | `INITIALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 234 | `FINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 235 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 236 | `PROGRESSUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 237 | `PROGRESSBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 238 | `PROGRESSUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 239 | `PROGRESSBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 240 | `PROGRESSUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 241 | `USERPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 242 | `BASEPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 243 | `USERSECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 244 | `BASESECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 245 | `USERPACKAGINGUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 246 | `QTYFORMATRIX` | DECIMAL(15,5) |  |  |  |  |
| 247 | `TIMECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 248 | `LOSSCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 249 | `QUEUELABELFORMATRIX` | CHAR(2) |  |  |  |  |
| 250 | `PREPROCESSLABELFORMATRIX` | CHAR(2) |  |  |  |  |
| 251 | `PROCESSLABELFORMATRIX` | CHAR(2) |  |  |  |  |
| 252 | `POSTPROCESSLABELFORMATRIX` | CHAR(2) |  |  |  |  |
| 253 | `ENDLABELFORMATRIX` | CHAR(2) |  |  |  |  |
| 254 | `PRIMARYLABELFORMATRIX` | CHAR(2) |  |  |  |  |
| 255 | `SECONDARYLABELFORMATRIX` | CHAR(2) |  |  |  |  |
| 256 | `MANUALSTEPFROMDEMAND` | SMALLINT | NOT NULL |  |  |  |
| 257 | `MANUALMODIFIEDSTEP` | SMALLINT | NOT NULL |  |  |  |
| 258 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 259 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 260 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 261 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 262 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 263 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 264 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 265 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 266 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 267 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 268 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 269 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 270 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 271 | `MANUALSTEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 272 | `PARALLELPDNUMBER` | INTEGER | NOT NULL |  |  |  |
| 273 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 274 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 275 | `DYELOTHANDLED` | SMALLINT | NOT NULL |  |  |  |
| 276 | `INITIALPLANSCHEDDATETIME` | TIMESTAMP |  |  |  |  |
| 277 | `FINALPLANSCHEDDATETIME` | TIMESTAMP |  |  |  |  |
| 278 | `GENERATEAUTOMATICQATEST` | SMALLINT | NOT NULL |  |  |  |
| 279 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 280 | `EXCLUDEFINITECAPACITY` | SMALLINT | NOT NULL |  |  |  |
| 281 | `EXCLUDECHECKOVERCAPACITY` | SMALLINT | NOT NULL |  |  |  |
| 282 | `SAVEDSTDBEGINQUEUE` | DATE |  |  |  |  |
| 283 | `SAVEDSTDENDSTEP` | DATE |  |  |  |  |
| 284 | `ORDERINLATE` | SMALLINT | NOT NULL |  |  |  |
| 285 | `OVERLAPPINGWITHPREVSTEPRULE` | INTEGER | NOT NULL |  |  |  |
| 286 | `OVERLAPPINGTONEXTSTEPRULE` | INTEGER | NOT NULL |  |  |  |
| 287 | `NUMBEROFHOURS` | DECIMAL(10,5) |  |  |  |  |
| 288 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 289 | `QUANTITYUOMCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **PRODUCTIONDEMAND**.`ABSUNIQUEID` (high confidence — name = 'PRODUCTIONDEMAND' + known child suffix 'STEP')
  - JOIN predicate: `PRODUCTIONDEMANDSTEPBEAN.FATHERID = PRODUCTIONDEMAND.ABSUNIQUEID`

## Indexes

- `PRODUCTIONDEMANDSTEPBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.STEPNUMBER,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.PRODUCTIONDEMANDSTEPBEAN t
FETCH FIRST 100 ROWS ONLY;
```
