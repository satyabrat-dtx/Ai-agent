# DB2ADMIN.LOGPLANNINGTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 595
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 209298

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(8) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `RULECODE` | CHAR(10) |  |  |  |  |
| 3 | `RULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 4 | `PLANNINGBY` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `MULTILINKSPLANNING` | SMALLINT | NOT NULL |  |  |  |
| 6 | `PROJECTMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 7 | `USEBASEQUANTITIES` | SMALLINT | NOT NULL |  |  |  |
| 8 | `USEORDERONLOWERLEVELRULE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `USESPLITTEDPDFORORDER` | SMALLINT | NOT NULL |  |  |  |
| 10 | `FINITECAPACITYPLANNING` | SMALLINT | NOT NULL |  |  |  |
| 11 | `LEVEL1ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 12 | `LEVEL1ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 13 | `LEVEL1SUBCODE01` | CHAR(20) |  |  |  |  |
| 14 | `LEVEL1SUBCODE02` | CHAR(10) |  |  |  |  |
| 15 | `LEVEL1SUBCODE03` | CHAR(10) |  |  |  |  |
| 16 | `LEVEL1SUBCODE04` | CHAR(10) |  |  |  |  |
| 17 | `LEVEL1SUBCODE05` | CHAR(10) |  |  |  |  |
| 18 | `LEVEL1SUBCODE06` | CHAR(10) |  |  |  |  |
| 19 | `LEVEL1SUBCODE07` | CHAR(10) |  |  |  |  |
| 20 | `LEVEL1SUBCODE08` | CHAR(10) |  |  |  |  |
| 21 | `LEVEL1SUBCODE09` | CHAR(10) |  |  |  |  |
| 22 | `LEVEL1SUBCODE10` | CHAR(10) |  |  |  |  |
| 23 | `PLANNINGAVLFORMULA1CMYCODE` | CHAR(3) |  |  |  |  |
| 24 | `PLANNINGAVLFORMULA1CODE` | CHAR(3) |  |  |  |  |
| 25 | `AVAILABILITYCONDITION` | CHAR(1) |  |  |  |  |
| 26 | `AVAILABILITYBYGROUP` | SMALLINT | NOT NULL |  |  |  |
| 27 | `PERIODIZEDCALENDARTYPE1CODE` | CHAR(10) |  |  |  |  |
| 28 | `LOGICALWAREHOUSE1COMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `LOGICALWAREHOUSE1CODE` | CHAR(8) |  |  |  |  |
| 30 | `AVLWAREHOUSEGROUP1COMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `AVLWAREHOUSEGROUP1CODE` | CHAR(3) |  |  |  |  |
| 32 | `TOLERANCEQTY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `FORCERECALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 34 | `AVQUALITYGROUP1CODE` | CHAR(3) |  |  |  |  |
| 35 | `ONETOONERELATION1` | SMALLINT | NOT NULL |  |  |  |
| 36 | `ADDNEWRESERVATIONSAFTERPO1` | SMALLINT | NOT NULL |  |  |  |
| 37 | `LEVEL2MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 38 | `LEVEL2ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 39 | `LEVEL2ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 40 | `LEVEL2SUBCODE01` | CHAR(20) |  |  |  |  |
| 41 | `LEVEL2SUBCODE02` | CHAR(10) |  |  |  |  |
| 42 | `LEVEL2SUBCODE03` | CHAR(10) |  |  |  |  |
| 43 | `LEVEL2SUBCODE04` | CHAR(10) |  |  |  |  |
| 44 | `LEVEL2SUBCODE05` | CHAR(10) |  |  |  |  |
| 45 | `LEVEL2SUBCODE06` | CHAR(10) |  |  |  |  |
| 46 | `LEVEL2SUBCODE07` | CHAR(10) |  |  |  |  |
| 47 | `LEVEL2SUBCODE08` | CHAR(10) |  |  |  |  |
| 48 | `LEVEL2SUBCODE09` | CHAR(10) |  |  |  |  |
| 49 | `LEVEL2SUBCODE10` | CHAR(10) |  |  |  |  |
| 50 | `RULE2CODE` | CHAR(10) |  |  |  |  |
| 51 | `RULEPOLICY2CODE` | CHAR(20) |  |  |  |  |
| 52 | `ONETOONERELATION2` | SMALLINT | NOT NULL |  |  |  |
| 53 | `ADDNEWRESERVATIONSAFTERPO2` | SMALLINT | NOT NULL |  |  |  |
| 54 | `PLANNINGAVLFORMULA2CMYCODE` | CHAR(3) |  |  |  |  |
| 55 | `PLANNINGAVLFORMULA2CODE` | CHAR(3) |  |  |  |  |
| 56 | `AVAILABILITYCONDITION2` | CHAR(1) |  |  |  |  |
| 57 | `AVAILABILITYBYGROUP2` | SMALLINT | NOT NULL |  |  |  |
| 58 | `PERIODIZEDCALENDARTYPE2CODE` | CHAR(10) |  |  |  |  |
| 59 | `LOGICALWAREHOUSE2COMPANYCODE` | CHAR(3) |  |  |  |  |
| 60 | `LOGICALWAREHOUSE2CODE` | CHAR(8) |  |  |  |  |
| 61 | `AVLWAREHOUSEGROUP2COMPANYCODE` | CHAR(3) |  |  |  |  |
| 62 | `AVLWAREHOUSEGROUP2CODE` | CHAR(3) |  |  |  |  |
| 63 | `TOLERANCEQTY2` | DECIMAL(15,5) |  |  |  |  |
| 64 | `FORCERECALCULATION2` | SMALLINT | NOT NULL |  |  |  |
| 65 | `AVQUALITYGROUP2CODE` | CHAR(3) |  |  |  |  |
| 66 | `LEVEL3MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 67 | `LEVEL3ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 68 | `LEVEL3ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 69 | `LEVEL3SUBCODE01` | CHAR(20) |  |  |  |  |
| 70 | `LEVEL3SUBCODE02` | CHAR(10) |  |  |  |  |
| 71 | `LEVEL3SUBCODE03` | CHAR(10) |  |  |  |  |
| 72 | `LEVEL3SUBCODE04` | CHAR(10) |  |  |  |  |
| 73 | `LEVEL3SUBCODE05` | CHAR(10) |  |  |  |  |
| 74 | `LEVEL3SUBCODE06` | CHAR(10) |  |  |  |  |
| 75 | `LEVEL3SUBCODE07` | CHAR(10) |  |  |  |  |
| 76 | `LEVEL3SUBCODE08` | CHAR(10) |  |  |  |  |
| 77 | `LEVEL3SUBCODE09` | CHAR(10) |  |  |  |  |
| 78 | `LEVEL3SUBCODE10` | CHAR(10) |  |  |  |  |
| 79 | `RULE3CODE` | CHAR(10) |  |  |  |  |
| 80 | `RULEPOLICY3CODE` | CHAR(20) |  |  |  |  |
| 81 | `ONETOONERELATION3` | SMALLINT | NOT NULL |  |  |  |
| 82 | `ADDNEWRESERVATIONSAFTERPO3` | SMALLINT | NOT NULL |  |  |  |
| 83 | `PLANNINGAVLFORMULA3CMYCODE` | CHAR(3) |  |  |  |  |
| 84 | `PLANNINGAVLFORMULA3CODE` | CHAR(3) |  |  |  |  |
| 85 | `AVAILABILITYCONDITION3` | CHAR(1) |  |  |  |  |
| 86 | `AVAILABILITYBYGROUP3` | SMALLINT | NOT NULL |  |  |  |
| 87 | `PERIODIZEDCALENDARTYPE3CODE` | CHAR(10) |  |  |  |  |
| 88 | `LOGICALWAREHOUSE3COMPANYCODE` | CHAR(3) |  |  |  |  |
| 89 | `LOGICALWAREHOUSE3CODE` | CHAR(8) |  |  |  |  |
| 90 | `AVLWAREHOUSEGROUP3COMPANYCODE` | CHAR(3) |  |  |  |  |
| 91 | `AVLWAREHOUSEGROUP3CODE` | CHAR(3) |  |  |  |  |
| 92 | `TOLERANCEQTY3` | DECIMAL(15,5) |  |  |  |  |
| 93 | `FORCERECALCULATION3` | SMALLINT | NOT NULL |  |  |  |
| 94 | `AVQUALITYGROUP3CODE` | CHAR(3) |  |  |  |  |
| 95 | `LEVEL4MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 96 | `LEVEL4ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 97 | `LEVEL4ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 98 | `LEVEL4SUBCODE01` | CHAR(20) |  |  |  |  |
| 99 | `LEVEL4SUBCODE02` | CHAR(10) |  |  |  |  |
| 100 | `LEVEL4SUBCODE03` | CHAR(10) |  |  |  |  |
| 101 | `LEVEL4SUBCODE04` | CHAR(10) |  |  |  |  |
| 102 | `LEVEL4SUBCODE05` | CHAR(10) |  |  |  |  |
| 103 | `LEVEL4SUBCODE06` | CHAR(10) |  |  |  |  |
| 104 | `LEVEL4SUBCODE07` | CHAR(10) |  |  |  |  |
| 105 | `LEVEL4SUBCODE08` | CHAR(10) |  |  |  |  |
| 106 | `LEVEL4SUBCODE09` | CHAR(10) |  |  |  |  |
| 107 | `LEVEL4SUBCODE10` | CHAR(10) |  |  |  |  |
| 108 | `RULE4CODE` | CHAR(10) |  |  |  |  |
| 109 | `RULEPOLICY4CODE` | CHAR(20) |  |  |  |  |
| 110 | `ONETOONERELATION4` | SMALLINT | NOT NULL |  |  |  |
| 111 | `ADDNEWRESERVATIONSAFTERPO4` | SMALLINT | NOT NULL |  |  |  |
| 112 | `PLANNINGAVLFORMULA4CMYCODE` | CHAR(3) |  |  |  |  |
| 113 | `PLANNINGAVLFORMULA4CODE` | CHAR(3) |  |  |  |  |
| 114 | `AVAILABILITYCONDITION4` | CHAR(1) |  |  |  |  |
| 115 | `AVAILABILITYBYGROUP4` | SMALLINT | NOT NULL |  |  |  |
| 116 | `PERIODIZEDCALENDARTYPE4CODE` | CHAR(10) |  |  |  |  |
| 117 | `LOGICALWAREHOUSE4COMPANYCODE` | CHAR(3) |  |  |  |  |
| 118 | `LOGICALWAREHOUSE4CODE` | CHAR(8) |  |  |  |  |
| 119 | `AVLWAREHOUSEGROUP4COMPANYCODE` | CHAR(3) |  |  |  |  |
| 120 | `AVLWAREHOUSEGROUP4CODE` | CHAR(3) |  |  |  |  |
| 121 | `TOLERANCEQTY4` | DECIMAL(15,5) |  |  |  |  |
| 122 | `FORCERECALCULATION4` | SMALLINT | NOT NULL |  |  |  |
| 123 | `AVQUALITYGROUP4CODE` | CHAR(3) |  |  |  |  |
| 124 | `LEVEL5MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 125 | `LEVEL5ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 126 | `LEVEL5ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 127 | `LEVEL5SUBCODE01` | CHAR(20) |  |  |  |  |
| 128 | `LEVEL5SUBCODE02` | CHAR(10) |  |  |  |  |
| 129 | `LEVEL5SUBCODE03` | CHAR(10) |  |  |  |  |
| 130 | `LEVEL5SUBCODE04` | CHAR(10) |  |  |  |  |
| 131 | `LEVEL5SUBCODE05` | CHAR(10) |  |  |  |  |
| 132 | `LEVEL5SUBCODE06` | CHAR(10) |  |  |  |  |
| 133 | `LEVEL5SUBCODE07` | CHAR(10) |  |  |  |  |
| 134 | `LEVEL5SUBCODE08` | CHAR(10) |  |  |  |  |
| 135 | `LEVEL5SUBCODE09` | CHAR(10) |  |  |  |  |
| 136 | `LEVEL5SUBCODE10` | CHAR(10) |  |  |  |  |
| 137 | `RULE5CODE` | CHAR(10) |  |  |  |  |
| 138 | `RULEPOLICY5CODE` | CHAR(20) |  |  |  |  |
| 139 | `ONETOONERELATION5` | SMALLINT | NOT NULL |  |  |  |
| 140 | `ADDNEWRESERVATIONSAFTERPO5` | SMALLINT | NOT NULL |  |  |  |
| 141 | `PLANNINGAVLFORMULA5CMYCODE` | CHAR(3) |  |  |  |  |
| 142 | `PLANNINGAVLFORMULA5CODE` | CHAR(3) |  |  |  |  |
| 143 | `AVAILABILITYCONDITION5` | CHAR(1) |  |  |  |  |
| 144 | `AVAILABILITYBYGROUP5` | SMALLINT | NOT NULL |  |  |  |
| 145 | `PERIODIZEDCALENDARTYPE5CODE` | CHAR(10) |  |  |  |  |
| 146 | `LOGICALWAREHOUSE5COMPANYCODE` | CHAR(3) |  |  |  |  |
| 147 | `LOGICALWAREHOUSE5CODE` | CHAR(8) |  |  |  |  |
| 148 | `AVLWAREHOUSEGROUP5COMPANYCODE` | CHAR(3) |  |  |  |  |
| 149 | `AVLWAREHOUSEGROUP5CODE` | CHAR(3) |  |  |  |  |
| 150 | `TOLERANCEQTY5` | DECIMAL(15,5) |  |  |  |  |
| 151 | `FORCERECALCULATION5` | SMALLINT | NOT NULL |  |  |  |
| 152 | `AVQUALITYGROUP5CODE` | CHAR(3) |  |  |  |  |
| 153 | `LEVEL6MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 154 | `LEVEL6ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 155 | `LEVEL6ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 156 | `LEVEL6SUBCODE01` | CHAR(20) |  |  |  |  |
| 157 | `LEVEL6SUBCODE02` | CHAR(10) |  |  |  |  |
| 158 | `LEVEL6SUBCODE03` | CHAR(10) |  |  |  |  |
| 159 | `LEVEL6SUBCODE04` | CHAR(10) |  |  |  |  |
| 160 | `LEVEL6SUBCODE05` | CHAR(10) |  |  |  |  |
| 161 | `LEVEL6SUBCODE06` | CHAR(10) |  |  |  |  |
| 162 | `LEVEL6SUBCODE07` | CHAR(10) |  |  |  |  |
| 163 | `LEVEL6SUBCODE08` | CHAR(10) |  |  |  |  |
| 164 | `LEVEL6SUBCODE09` | CHAR(10) |  |  |  |  |
| 165 | `LEVEL6SUBCODE10` | CHAR(10) |  |  |  |  |
| 166 | `RULE6CODE` | CHAR(10) |  |  |  |  |
| 167 | `RULEPOLICY6CODE` | CHAR(20) |  |  |  |  |
| 168 | `ONETOONERELATION6` | SMALLINT | NOT NULL |  |  |  |
| 169 | `ADDNEWRESERVATIONSAFTERPO6` | SMALLINT | NOT NULL |  |  |  |
| 170 | `PLANNINGAVLFORMULA6CMYCODE` | CHAR(3) |  |  |  |  |
| 171 | `PLANNINGAVLFORMULA6CODE` | CHAR(3) |  |  |  |  |
| 172 | `AVAILABILITYCONDITION6` | CHAR(1) |  |  |  |  |
| 173 | `AVAILABILITYBYGROUP6` | SMALLINT | NOT NULL |  |  |  |
| 174 | `PERIODIZEDCALENDARTYPE6CODE` | CHAR(10) |  |  |  |  |
| 175 | `LOGICALWAREHOUSE6COMPANYCODE` | CHAR(3) |  |  |  |  |
| 176 | `LOGICALWAREHOUSE6CODE` | CHAR(8) |  |  |  |  |
| 177 | `AVLWAREHOUSEGROUP6COMPANYCODE` | CHAR(3) |  |  |  |  |
| 178 | `AVLWAREHOUSEGROUP6CODE` | CHAR(3) |  |  |  |  |
| 179 | `TOLERANCEQTY6` | DECIMAL(15,5) |  |  |  |  |
| 180 | `FORCERECALCULATION6` | SMALLINT | NOT NULL |  |  |  |
| 181 | `AVQUALITYGROUP6CODE` | CHAR(3) |  |  |  |  |
| 182 | `LEVEL7MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 183 | `LEVEL7ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 184 | `LEVEL7ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 185 | `LEVEL7SUBCODE01` | CHAR(20) |  |  |  |  |
| 186 | `LEVEL7SUBCODE02` | CHAR(10) |  |  |  |  |
| 187 | `LEVEL7SUBCODE03` | CHAR(10) |  |  |  |  |
| 188 | `LEVEL7SUBCODE04` | CHAR(10) |  |  |  |  |
| 189 | `LEVEL7SUBCODE05` | CHAR(10) |  |  |  |  |
| 190 | `LEVEL7SUBCODE06` | CHAR(10) |  |  |  |  |
| 191 | `LEVEL7SUBCODE07` | CHAR(10) |  |  |  |  |
| 192 | `LEVEL7SUBCODE08` | CHAR(10) |  |  |  |  |
| 193 | `LEVEL7SUBCODE09` | CHAR(10) |  |  |  |  |
| 194 | `LEVEL7SUBCODE10` | CHAR(10) |  |  |  |  |
| 195 | `RULE7CODE` | CHAR(10) |  |  |  |  |
| 196 | `RULEPOLICY7CODE` | CHAR(20) |  |  |  |  |
| 197 | `ONETOONERELATION7` | SMALLINT | NOT NULL |  |  |  |
| 198 | `ADDNEWRESERVATIONSAFTERPO7` | SMALLINT | NOT NULL |  |  |  |
| 199 | `PLANNINGAVLFORMULA7CMYCODE` | CHAR(3) |  |  |  |  |
| 200 | `PLANNINGAVLFORMULA7CODE` | CHAR(3) |  |  |  |  |
| 201 | `AVAILABILITYCONDITION7` | CHAR(1) |  |  |  |  |
| 202 | `AVAILABILITYBYGROUP7` | SMALLINT | NOT NULL |  |  |  |
| 203 | `PERIODIZEDCALENDARTYPE7CODE` | CHAR(10) |  |  |  |  |
| 204 | `LOGICALWAREHOUSE7COMPANYCODE` | CHAR(3) |  |  |  |  |
| 205 | `LOGICALWAREHOUSE7CODE` | CHAR(8) |  |  |  |  |
| 206 | `AVLWAREHOUSEGROUP7COMPANYCODE` | CHAR(3) |  |  |  |  |
| 207 | `AVLWAREHOUSEGROUP7CODE` | CHAR(3) |  |  |  |  |
| 208 | `TOLERANCEQTY7` | DECIMAL(15,5) |  |  |  |  |
| 209 | `FORCERECALCULATION7` | SMALLINT | NOT NULL |  |  |  |
| 210 | `AVQUALITYGROUP7CODE` | CHAR(3) |  |  |  |  |
| 211 | `LEVEL8MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 212 | `LEVEL8ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 213 | `LEVEL8ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 214 | `LEVEL8SUBCODE01` | CHAR(20) |  |  |  |  |
| 215 | `LEVEL8SUBCODE02` | CHAR(10) |  |  |  |  |
| 216 | `LEVEL8SUBCODE03` | CHAR(10) |  |  |  |  |
| 217 | `LEVEL8SUBCODE04` | CHAR(10) |  |  |  |  |
| 218 | `LEVEL8SUBCODE05` | CHAR(10) |  |  |  |  |
| 219 | `LEVEL8SUBCODE06` | CHAR(10) |  |  |  |  |
| 220 | `LEVEL8SUBCODE07` | CHAR(10) |  |  |  |  |
| 221 | `LEVEL8SUBCODE08` | CHAR(10) |  |  |  |  |
| 222 | `LEVEL8SUBCODE09` | CHAR(10) |  |  |  |  |
| 223 | `LEVEL8SUBCODE10` | CHAR(10) |  |  |  |  |
| 224 | `RULE8CODE` | CHAR(10) |  |  |  |  |
| 225 | `RULEPOLICY8CODE` | CHAR(20) |  |  |  |  |
| 226 | `ONETOONERELATION8` | SMALLINT | NOT NULL |  |  |  |
| 227 | `ADDNEWRESERVATIONSAFTERPO8` | SMALLINT | NOT NULL |  |  |  |
| 228 | `PLANNINGAVLFORMULA8CMYCODE` | CHAR(3) |  |  |  |  |
| 229 | `PLANNINGAVLFORMULA8CODE` | CHAR(3) |  |  |  |  |
| 230 | `AVAILABILITYCONDITION8` | CHAR(1) |  |  |  |  |
| 231 | `AVAILABILITYBYGROUP8` | SMALLINT | NOT NULL |  |  |  |
| 232 | `PERIODIZEDCALENDARTYPE8CODE` | CHAR(10) |  |  |  |  |
| 233 | `LOGICALWAREHOUSE8COMPANYCODE` | CHAR(3) |  |  |  |  |
| 234 | `LOGICALWAREHOUSE8CODE` | CHAR(8) |  |  |  |  |
| 235 | `AVLWAREHOUSEGROUP8COMPANYCODE` | CHAR(3) |  |  |  |  |
| 236 | `AVLWAREHOUSEGROUP8CODE` | CHAR(3) |  |  |  |  |
| 237 | `TOLERANCEQTY8` | DECIMAL(15,5) |  |  |  |  |
| 238 | `FORCERECALCULATION8` | SMALLINT | NOT NULL |  |  |  |
| 239 | `AVQUALITYGROUP8CODE` | CHAR(3) |  |  |  |  |
| 240 | `LEVEL9MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 241 | `LEVEL9ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 242 | `LEVEL9ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 243 | `LEVEL9SUBCODE01` | CHAR(20) |  |  |  |  |
| 244 | `LEVEL9SUBCODE02` | CHAR(10) |  |  |  |  |
| 245 | `LEVEL9SUBCODE03` | CHAR(10) |  |  |  |  |
| 246 | `LEVEL9SUBCODE04` | CHAR(10) |  |  |  |  |
| 247 | `LEVEL9SUBCODE05` | CHAR(10) |  |  |  |  |
| 248 | `LEVEL9SUBCODE06` | CHAR(10) |  |  |  |  |
| 249 | `LEVEL9SUBCODE07` | CHAR(10) |  |  |  |  |
| 250 | `LEVEL9SUBCODE08` | CHAR(10) |  |  |  |  |
| 251 | `LEVEL9SUBCODE09` | CHAR(10) |  |  |  |  |
| 252 | `LEVEL9SUBCODE10` | CHAR(10) |  |  |  |  |
| 253 | `RULE9CODE` | CHAR(10) |  |  |  |  |
| 254 | `RULEPOLICY9CODE` | CHAR(20) |  |  |  |  |
| 255 | `ONETOONERELATION9` | SMALLINT | NOT NULL |  |  |  |
| 256 | `ADDNEWRESERVATIONSAFTERPO9` | SMALLINT | NOT NULL |  |  |  |
| 257 | `PLANNINGAVLFORMULA9CMYCODE` | CHAR(3) |  |  |  |  |
| 258 | `PLANNINGAVLFORMULA9CODE` | CHAR(3) |  |  |  |  |
| 259 | `AVAILABILITYCONDITION9` | CHAR(1) |  |  |  |  |
| 260 | `AVAILABILITYBYGROUP9` | SMALLINT | NOT NULL |  |  |  |
| 261 | `PERIODIZEDCALENDARTYPE9CODE` | CHAR(10) |  |  |  |  |
| 262 | `LOGICALWAREHOUSE9COMPANYCODE` | CHAR(3) |  |  |  |  |
| 263 | `LOGICALWAREHOUSE9CODE` | CHAR(8) |  |  |  |  |
| 264 | `AVLWAREHOUSEGROUP9COMPANYCODE` | CHAR(3) |  |  |  |  |
| 265 | `AVLWAREHOUSEGROUP9CODE` | CHAR(3) |  |  |  |  |
| 266 | `TOLERANCEQTY9` | DECIMAL(15,5) |  |  |  |  |
| 267 | `FORCERECALCULATION9` | SMALLINT | NOT NULL |  |  |  |
| 268 | `AVQUALITYGROUP9CODE` | CHAR(3) |  |  |  |  |
| 269 | `LEVEL10MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 270 | `LEVEL10ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 271 | `LEVEL10ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 272 | `LEVEL10SUBCODE01` | CHAR(20) |  |  |  |  |
| 273 | `LEVEL10SUBCODE02` | CHAR(10) |  |  |  |  |
| 274 | `LEVEL10SUBCODE03` | CHAR(10) |  |  |  |  |
| 275 | `LEVEL10SUBCODE04` | CHAR(10) |  |  |  |  |
| 276 | `LEVEL10SUBCODE05` | CHAR(10) |  |  |  |  |
| 277 | `LEVEL10SUBCODE06` | CHAR(10) |  |  |  |  |
| 278 | `LEVEL10SUBCODE07` | CHAR(10) |  |  |  |  |
| 279 | `LEVEL10SUBCODE08` | CHAR(10) |  |  |  |  |
| 280 | `LEVEL10SUBCODE09` | CHAR(10) |  |  |  |  |
| 281 | `LEVEL10SUBCODE10` | CHAR(10) |  |  |  |  |
| 282 | `RULE10CODE` | CHAR(10) |  |  |  |  |
| 283 | `RULEPOLICY10CODE` | CHAR(20) |  |  |  |  |
| 284 | `ONETOONERELATION10` | SMALLINT | NOT NULL |  |  |  |
| 285 | `ADDNEWRESERVATIONSAFTERPO10` | SMALLINT | NOT NULL |  |  |  |
| 286 | `PLANNINGAVLFORMULA10CMYCODE` | CHAR(3) |  |  |  |  |
| 287 | `PLANNINGAVLFORMULA10CODE` | CHAR(3) |  |  |  |  |
| 288 | `AVAILABILITYCONDITION10` | CHAR(1) |  |  |  |  |
| 289 | `AVAILABILITYBYGROUP10` | SMALLINT | NOT NULL |  |  |  |
| 290 | `PERIODIZEDCALENDARTYPE10CODE` | CHAR(10) |  |  |  |  |
| 291 | `LOGICALWAREHOUSE10COMPANYCODE` | CHAR(3) |  |  |  |  |
| 292 | `LOGICALWAREHOUSE10CODE` | CHAR(8) |  |  |  |  |
| 293 | `AVLWHSGROUP10COMPANYCODE` | CHAR(3) |  |  |  |  |
| 294 | `AVLWAREHOUSEGROUP10CODE` | CHAR(3) |  |  |  |  |
| 295 | `TOLERANCEQTY10` | DECIMAL(15,5) |  |  |  |  |
| 296 | `FORCERECALCULATION10` | SMALLINT | NOT NULL |  |  |  |
| 297 | `AVQUALITYGROUP10CODE` | CHAR(3) |  |  |  |  |
| 298 | `LEVEL11MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 299 | `LEVEL11ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 300 | `LEVEL11ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 301 | `LEVEL11SUBCODE01` | CHAR(20) |  |  |  |  |
| 302 | `LEVEL11SUBCODE02` | CHAR(10) |  |  |  |  |
| 303 | `LEVEL11SUBCODE03` | CHAR(10) |  |  |  |  |
| 304 | `LEVEL11SUBCODE04` | CHAR(10) |  |  |  |  |
| 305 | `LEVEL11SUBCODE05` | CHAR(10) |  |  |  |  |
| 306 | `LEVEL11SUBCODE06` | CHAR(10) |  |  |  |  |
| 307 | `LEVEL11SUBCODE07` | CHAR(10) |  |  |  |  |
| 308 | `LEVEL11SUBCODE08` | CHAR(10) |  |  |  |  |
| 309 | `LEVEL11SUBCODE09` | CHAR(10) |  |  |  |  |
| 310 | `LEVEL11SUBCODE10` | CHAR(10) |  |  |  |  |
| 311 | `RULE11CODE` | CHAR(10) |  |  |  |  |
| 312 | `RULEPOLICY11CODE` | CHAR(20) |  |  |  |  |
| 313 | `ONETOONERELATION11` | SMALLINT | NOT NULL |  |  |  |
| 314 | `ADDNEWRESERVATIONSAFTERPO11` | SMALLINT | NOT NULL |  |  |  |
| 315 | `PLANNINGAVLFORMULA11CMYCODE` | CHAR(3) |  |  |  |  |
| 316 | `PLANNINGAVLFORMULA11CODE` | CHAR(3) |  |  |  |  |
| 317 | `AVAILABILITYCONDITION11` | CHAR(1) |  |  |  |  |
| 318 | `AVAILABILITYBYGROUP11` | SMALLINT | NOT NULL |  |  |  |
| 319 | `PERIODIZEDCALENDARTYPE11CODE` | CHAR(10) |  |  |  |  |
| 320 | `LOGICALWAREHOUSE11COMPANYCODE` | CHAR(3) |  |  |  |  |
| 321 | `LOGICALWAREHOUSE11CODE` | CHAR(8) |  |  |  |  |
| 322 | `AVLWHSGROUP11COMPANYCODE` | CHAR(3) |  |  |  |  |
| 323 | `AVLWAREHOUSEGROUP11CODE` | CHAR(3) |  |  |  |  |
| 324 | `TOLERANCEQTY11` | DECIMAL(15,5) |  |  |  |  |
| 325 | `FORCERECALCULATION11` | SMALLINT | NOT NULL |  |  |  |
| 326 | `AVQUALITYGROUP11CODE` | CHAR(3) |  |  |  |  |
| 327 | `LEVEL12MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 328 | `LEVEL12ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 329 | `LEVEL12ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 330 | `LEVEL12SUBCODE01` | CHAR(20) |  |  |  |  |
| 331 | `LEVEL12SUBCODE02` | CHAR(10) |  |  |  |  |
| 332 | `LEVEL12SUBCODE03` | CHAR(10) |  |  |  |  |
| 333 | `LEVEL12SUBCODE04` | CHAR(10) |  |  |  |  |
| 334 | `LEVEL12SUBCODE05` | CHAR(10) |  |  |  |  |
| 335 | `LEVEL12SUBCODE06` | CHAR(10) |  |  |  |  |
| 336 | `LEVEL12SUBCODE07` | CHAR(10) |  |  |  |  |
| 337 | `LEVEL12SUBCODE08` | CHAR(10) |  |  |  |  |
| 338 | `LEVEL12SUBCODE09` | CHAR(10) |  |  |  |  |
| 339 | `LEVEL12SUBCODE10` | CHAR(10) |  |  |  |  |
| 340 | `RULE12CODE` | CHAR(10) |  |  |  |  |
| 341 | `RULEPOLICY12CODE` | CHAR(20) |  |  |  |  |
| 342 | `ONETOONERELATION12` | SMALLINT | NOT NULL |  |  |  |
| 343 | `ADDNEWRESERVATIONSAFTERPO12` | SMALLINT | NOT NULL |  |  |  |
| 344 | `PLANNINGAVLFORMULA12CMYCODE` | CHAR(3) |  |  |  |  |
| 345 | `PLANNINGAVLFORMULA12CODE` | CHAR(3) |  |  |  |  |
| 346 | `AVAILABILITYCONDITION12` | CHAR(1) |  |  |  |  |
| 347 | `AVAILABILITYBYGROUP12` | SMALLINT | NOT NULL |  |  |  |
| 348 | `PERIODIZEDCALENDARTYPE12CODE` | CHAR(10) |  |  |  |  |
| 349 | `LOGICALWAREHOUSE12COMPANYCODE` | CHAR(3) |  |  |  |  |
| 350 | `LOGICALWAREHOUSE12CODE` | CHAR(8) |  |  |  |  |
| 351 | `AVLWHSGROUP12COMPANYCODE` | CHAR(3) |  |  |  |  |
| 352 | `AVLWAREHOUSEGROUP12CODE` | CHAR(3) |  |  |  |  |
| 353 | `TOLERANCEQTY12` | DECIMAL(15,5) |  |  |  |  |
| 354 | `FORCERECALCULATION12` | SMALLINT | NOT NULL |  |  |  |
| 355 | `AVQUALITYGROUP12CODE` | CHAR(3) |  |  |  |  |
| 356 | `LEVEL13MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 357 | `LEVEL13ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 358 | `LEVEL13ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 359 | `LEVEL13SUBCODE01` | CHAR(20) |  |  |  |  |
| 360 | `LEVEL13SUBCODE02` | CHAR(10) |  |  |  |  |
| 361 | `LEVEL13SUBCODE03` | CHAR(10) |  |  |  |  |
| 362 | `LEVEL13SUBCODE04` | CHAR(10) |  |  |  |  |
| 363 | `LEVEL13SUBCODE05` | CHAR(10) |  |  |  |  |
| 364 | `LEVEL13SUBCODE06` | CHAR(10) |  |  |  |  |
| 365 | `LEVEL13SUBCODE07` | CHAR(10) |  |  |  |  |
| 366 | `LEVEL13SUBCODE08` | CHAR(10) |  |  |  |  |
| 367 | `LEVEL13SUBCODE09` | CHAR(10) |  |  |  |  |
| 368 | `LEVEL13SUBCODE10` | CHAR(10) |  |  |  |  |
| 369 | `RULE13CODE` | CHAR(10) |  |  |  |  |
| 370 | `RULEPOLICY13CODE` | CHAR(20) |  |  |  |  |
| 371 | `ONETOONERELATION13` | SMALLINT | NOT NULL |  |  |  |
| 372 | `ADDNEWRESERVATIONSAFTERPO13` | SMALLINT | NOT NULL |  |  |  |
| 373 | `PLANNINGAVLFORMULA13CMYCODE` | CHAR(3) |  |  |  |  |
| 374 | `PLANNINGAVLFORMULA13CODE` | CHAR(3) |  |  |  |  |
| 375 | `AVAILABILITYCONDITION13` | CHAR(1) |  |  |  |  |
| 376 | `AVAILABILITYBYGROUP13` | SMALLINT | NOT NULL |  |  |  |
| 377 | `PERIODIZEDCALENDARTYPE13CODE` | CHAR(10) |  |  |  |  |
| 378 | `LOGICALWAREHOUSE13COMPANYCODE` | CHAR(3) |  |  |  |  |
| 379 | `LOGICALWAREHOUSE13CODE` | CHAR(8) |  |  |  |  |
| 380 | `AVLWHSGROUP13COMPANYCODE` | CHAR(3) |  |  |  |  |
| 381 | `AVLWAREHOUSEGROUP13CODE` | CHAR(3) |  |  |  |  |
| 382 | `TOLERANCEQTY13` | DECIMAL(15,5) |  |  |  |  |
| 383 | `FORCERECALCULATION13` | SMALLINT | NOT NULL |  |  |  |
| 384 | `AVQUALITYGROUP13CODE` | CHAR(3) |  |  |  |  |
| 385 | `LEVEL14MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 386 | `LEVEL14ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 387 | `LEVEL14ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 388 | `LEVEL14SUBCODE01` | CHAR(20) |  |  |  |  |
| 389 | `LEVEL14SUBCODE02` | CHAR(10) |  |  |  |  |
| 390 | `LEVEL14SUBCODE03` | CHAR(10) |  |  |  |  |
| 391 | `LEVEL14SUBCODE04` | CHAR(10) |  |  |  |  |
| 392 | `LEVEL14SUBCODE05` | CHAR(10) |  |  |  |  |
| 393 | `LEVEL14SUBCODE06` | CHAR(10) |  |  |  |  |
| 394 | `LEVEL14SUBCODE07` | CHAR(10) |  |  |  |  |
| 395 | `LEVEL14SUBCODE08` | CHAR(10) |  |  |  |  |
| 396 | `LEVEL14SUBCODE09` | CHAR(10) |  |  |  |  |
| 397 | `LEVEL14SUBCODE10` | CHAR(10) |  |  |  |  |
| 398 | `RULE14CODE` | CHAR(10) |  |  |  |  |
| 399 | `RULEPOLICY14CODE` | CHAR(20) |  |  |  |  |
| 400 | `ONETOONERELATION14` | SMALLINT | NOT NULL |  |  |  |
| 401 | `ADDNEWRESERVATIONSAFTERPO14` | SMALLINT | NOT NULL |  |  |  |
| 402 | `PLANNINGAVLFORMULA14CMYCODE` | CHAR(3) |  |  |  |  |
| 403 | `PLANNINGAVLFORMULA14CODE` | CHAR(3) |  |  |  |  |
| 404 | `AVAILABILITYCONDITION14` | CHAR(1) |  |  |  |  |
| 405 | `AVAILABILITYBYGROUP14` | SMALLINT | NOT NULL |  |  |  |
| 406 | `PERIODIZEDCALENDARTYPE14CODE` | CHAR(10) |  |  |  |  |
| 407 | `LOGICALWAREHOUSE14COMPANYCODE` | CHAR(3) |  |  |  |  |
| 408 | `LOGICALWAREHOUSE14CODE` | CHAR(8) |  |  |  |  |
| 409 | `AVLWHSGROUP14COMPANYCODE` | CHAR(3) |  |  |  |  |
| 410 | `AVLWAREHOUSEGROUP14CODE` | CHAR(3) |  |  |  |  |
| 411 | `TOLERANCEQTY14` | DECIMAL(15,5) |  |  |  |  |
| 412 | `FORCERECALCULATION14` | SMALLINT | NOT NULL |  |  |  |
| 413 | `AVQUALITYGROUP14CODE` | CHAR(3) |  |  |  |  |
| 414 | `LEVEL15MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 415 | `LEVEL15ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 416 | `LEVEL15ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 417 | `LEVEL15SUBCODE01` | CHAR(20) |  |  |  |  |
| 418 | `LEVEL15SUBCODE02` | CHAR(10) |  |  |  |  |
| 419 | `LEVEL15SUBCODE03` | CHAR(10) |  |  |  |  |
| 420 | `LEVEL15SUBCODE04` | CHAR(10) |  |  |  |  |
| 421 | `LEVEL15SUBCODE05` | CHAR(10) |  |  |  |  |
| 422 | `LEVEL15SUBCODE06` | CHAR(10) |  |  |  |  |
| 423 | `LEVEL15SUBCODE07` | CHAR(10) |  |  |  |  |
| 424 | `LEVEL15SUBCODE08` | CHAR(10) |  |  |  |  |
| 425 | `LEVEL15SUBCODE09` | CHAR(10) |  |  |  |  |
| 426 | `LEVEL15SUBCODE10` | CHAR(10) |  |  |  |  |
| 427 | `RULE15CODE` | CHAR(10) |  |  |  |  |
| 428 | `RULEPOLICY15CODE` | CHAR(20) |  |  |  |  |
| 429 | `ONETOONERELATION15` | SMALLINT | NOT NULL |  |  |  |
| 430 | `ADDNEWRESERVATIONSAFTERPO15` | SMALLINT | NOT NULL |  |  |  |
| 431 | `PLANNINGAVLFORMULA15CMYCODE` | CHAR(3) |  |  |  |  |
| 432 | `PLANNINGAVLFORMULA15CODE` | CHAR(3) |  |  |  |  |
| 433 | `AVAILABILITYCONDITION15` | CHAR(1) |  |  |  |  |
| 434 | `AVAILABILITYBYGROUP15` | SMALLINT | NOT NULL |  |  |  |
| 435 | `PERIODIZEDCALENDARTYPE15CODE` | CHAR(10) |  |  |  |  |
| 436 | `LOGICALWAREHOUSE15COMPANYCODE` | CHAR(3) |  |  |  |  |
| 437 | `LOGICALWAREHOUSE15CODE` | CHAR(8) |  |  |  |  |
| 438 | `AVLWHSGROUP15COMPANYCODE` | CHAR(3) |  |  |  |  |
| 439 | `AVLWAREHOUSEGROUP15CODE` | CHAR(3) |  |  |  |  |
| 440 | `TOLERANCEQTY15` | DECIMAL(15,5) |  |  |  |  |
| 441 | `FORCERECALCULATION15` | SMALLINT | NOT NULL |  |  |  |
| 442 | `AVQUALITYGROUP15CODE` | CHAR(3) |  |  |  |  |
| 443 | `LEVEL16MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 444 | `LEVEL16ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 445 | `LEVEL16ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 446 | `LEVEL16SUBCODE01` | CHAR(20) |  |  |  |  |
| 447 | `LEVEL16SUBCODE02` | CHAR(10) |  |  |  |  |
| 448 | `LEVEL16SUBCODE03` | CHAR(10) |  |  |  |  |
| 449 | `LEVEL16SUBCODE04` | CHAR(10) |  |  |  |  |
| 450 | `LEVEL16SUBCODE05` | CHAR(10) |  |  |  |  |
| 451 | `LEVEL16SUBCODE06` | CHAR(10) |  |  |  |  |
| 452 | `LEVEL16SUBCODE07` | CHAR(10) |  |  |  |  |
| 453 | `LEVEL16SUBCODE08` | CHAR(10) |  |  |  |  |
| 454 | `LEVEL16SUBCODE09` | CHAR(10) |  |  |  |  |
| 455 | `LEVEL16SUBCODE10` | CHAR(10) |  |  |  |  |
| 456 | `RULE16CODE` | CHAR(10) |  |  |  |  |
| 457 | `RULEPOLICY16CODE` | CHAR(20) |  |  |  |  |
| 458 | `ONETOONERELATION16` | SMALLINT | NOT NULL |  |  |  |
| 459 | `ADDNEWRESERVATIONSAFTERPO16` | SMALLINT | NOT NULL |  |  |  |
| 460 | `PLANNINGAVLFORMULA16CMYCODE` | CHAR(3) |  |  |  |  |
| 461 | `PLANNINGAVLFORMULA16CODE` | CHAR(3) |  |  |  |  |
| 462 | `AVAILABILITYCONDITION16` | CHAR(1) |  |  |  |  |
| 463 | `AVAILABILITYBYGROUP16` | SMALLINT | NOT NULL |  |  |  |
| 464 | `PERIODIZEDCALENDARTYPE16CODE` | CHAR(10) |  |  |  |  |
| 465 | `LOGICALWAREHOUSE16COMPANYCODE` | CHAR(3) |  |  |  |  |
| 466 | `LOGICALWAREHOUSE16CODE` | CHAR(8) |  |  |  |  |
| 467 | `AVLWHSGROUP16COMPANYCODE` | CHAR(3) |  |  |  |  |
| 468 | `AVLWAREHOUSEGROUP16CODE` | CHAR(3) |  |  |  |  |
| 469 | `TOLERANCEQTY16` | DECIMAL(15,5) |  |  |  |  |
| 470 | `FORCERECALCULATION16` | SMALLINT | NOT NULL |  |  |  |
| 471 | `AVQUALITYGROUP16CODE` | CHAR(3) |  |  |  |  |
| 472 | `LEVEL17MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 473 | `LEVEL17ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 474 | `LEVEL17ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 475 | `LEVEL17SUBCODE01` | CHAR(20) |  |  |  |  |
| 476 | `LEVEL17SUBCODE02` | CHAR(10) |  |  |  |  |
| 477 | `LEVEL17SUBCODE03` | CHAR(10) |  |  |  |  |
| 478 | `LEVEL17SUBCODE04` | CHAR(10) |  |  |  |  |
| 479 | `LEVEL17SUBCODE05` | CHAR(10) |  |  |  |  |
| 480 | `LEVEL17SUBCODE06` | CHAR(10) |  |  |  |  |
| 481 | `LEVEL17SUBCODE07` | CHAR(10) |  |  |  |  |
| 482 | `LEVEL17SUBCODE08` | CHAR(10) |  |  |  |  |
| 483 | `LEVEL17SUBCODE09` | CHAR(10) |  |  |  |  |
| 484 | `LEVEL17SUBCODE10` | CHAR(10) |  |  |  |  |
| 485 | `RULE17CODE` | CHAR(10) |  |  |  |  |
| 486 | `RULEPOLICY17CODE` | CHAR(20) |  |  |  |  |
| 487 | `ONETOONERELATION17` | SMALLINT | NOT NULL |  |  |  |
| 488 | `ADDNEWRESERVATIONSAFTERPO17` | SMALLINT | NOT NULL |  |  |  |
| 489 | `PLANNINGAVLFORMULA17CMYCODE` | CHAR(3) |  |  |  |  |
| 490 | `PLANNINGAVLFORMULA17CODE` | CHAR(3) |  |  |  |  |
| 491 | `AVAILABILITYCONDITION17` | CHAR(1) |  |  |  |  |
| 492 | `AVAILABILITYBYGROUP17` | SMALLINT | NOT NULL |  |  |  |
| 493 | `PERIODIZEDCALENDARTYPE17CODE` | CHAR(10) |  |  |  |  |
| 494 | `LOGICALWAREHOUSE17COMPANYCODE` | CHAR(3) |  |  |  |  |
| 495 | `LOGICALWAREHOUSE17CODE` | CHAR(8) |  |  |  |  |
| 496 | `AVLWHSGROUP17COMPANYCODE` | CHAR(3) |  |  |  |  |
| 497 | `AVLWAREHOUSEGROUP17CODE` | CHAR(3) |  |  |  |  |
| 498 | `TOLERANCEQTY17` | DECIMAL(15,5) |  |  |  |  |
| 499 | `FORCERECALCULATION17` | SMALLINT | NOT NULL |  |  |  |
| 500 | `AVQUALITYGROUP17CODE` | CHAR(3) |  |  |  |  |
| 501 | `LEVEL18MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 502 | `LEVEL18ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 503 | `LEVEL18ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 504 | `LEVEL18SUBCODE01` | CHAR(20) |  |  |  |  |
| 505 | `LEVEL18SUBCODE02` | CHAR(10) |  |  |  |  |
| 506 | `LEVEL18SUBCODE03` | CHAR(10) |  |  |  |  |
| 507 | `LEVEL18SUBCODE04` | CHAR(10) |  |  |  |  |
| 508 | `LEVEL18SUBCODE05` | CHAR(10) |  |  |  |  |
| 509 | `LEVEL18SUBCODE06` | CHAR(10) |  |  |  |  |
| 510 | `LEVEL18SUBCODE07` | CHAR(10) |  |  |  |  |
| 511 | `LEVEL18SUBCODE08` | CHAR(10) |  |  |  |  |
| 512 | `LEVEL18SUBCODE09` | CHAR(10) |  |  |  |  |
| 513 | `LEVEL18SUBCODE10` | CHAR(10) |  |  |  |  |
| 514 | `RULE18CODE` | CHAR(10) |  |  |  |  |
| 515 | `RULEPOLICY18CODE` | CHAR(20) |  |  |  |  |
| 516 | `ONETOONERELATION18` | SMALLINT | NOT NULL |  |  |  |
| 517 | `ADDNEWRESERVATIONSAFTERPO18` | SMALLINT | NOT NULL |  |  |  |
| 518 | `PLANNINGAVLFORMULA18CMYCODE` | CHAR(3) |  |  |  |  |
| 519 | `PLANNINGAVLFORMULA18CODE` | CHAR(3) |  |  |  |  |
| 520 | `AVAILABILITYCONDITION18` | CHAR(1) |  |  |  |  |
| 521 | `AVAILABILITYBYGROUP18` | SMALLINT | NOT NULL |  |  |  |
| 522 | `PERIODIZEDCALENDARTYPE18CODE` | CHAR(10) |  |  |  |  |
| 523 | `LOGICALWAREHOUSE18COMPANYCODE` | CHAR(3) |  |  |  |  |
| 524 | `LOGICALWAREHOUSE18CODE` | CHAR(8) |  |  |  |  |
| 525 | `AVLWHSGROUP18COMPANYCODE` | CHAR(3) |  |  |  |  |
| 526 | `AVLWAREHOUSEGROUP18CODE` | CHAR(3) |  |  |  |  |
| 527 | `TOLERANCEQTY18` | DECIMAL(15,5) |  |  |  |  |
| 528 | `FORCERECALCULATION18` | SMALLINT | NOT NULL |  |  |  |
| 529 | `AVQUALITYGROUP18CODE` | CHAR(3) |  |  |  |  |
| 530 | `LEVEL19MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 531 | `LEVEL19ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 532 | `LEVEL19ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 533 | `LEVEL19SUBCODE01` | CHAR(20) |  |  |  |  |
| 534 | `LEVEL19SUBCODE02` | CHAR(10) |  |  |  |  |
| 535 | `LEVEL19SUBCODE03` | CHAR(10) |  |  |  |  |
| 536 | `LEVEL19SUBCODE04` | CHAR(10) |  |  |  |  |
| 537 | `LEVEL19SUBCODE05` | CHAR(10) |  |  |  |  |
| 538 | `LEVEL19SUBCODE06` | CHAR(10) |  |  |  |  |
| 539 | `LEVEL19SUBCODE07` | CHAR(10) |  |  |  |  |
| 540 | `LEVEL19SUBCODE08` | CHAR(10) |  |  |  |  |
| 541 | `LEVEL19SUBCODE09` | CHAR(10) |  |  |  |  |
| 542 | `LEVEL19SUBCODE10` | CHAR(10) |  |  |  |  |
| 543 | `RULE19CODE` | CHAR(10) |  |  |  |  |
| 544 | `RULEPOLICY19CODE` | CHAR(20) |  |  |  |  |
| 545 | `ONETOONERELATION19` | SMALLINT | NOT NULL |  |  |  |
| 546 | `ADDNEWRESERVATIONSAFTERPO19` | SMALLINT | NOT NULL |  |  |  |
| 547 | `PLANNINGAVLFORMULA19CMYCODE` | CHAR(3) |  |  |  |  |
| 548 | `PLANNINGAVLFORMULA19CODE` | CHAR(3) |  |  |  |  |
| 549 | `AVAILABILITYCONDITION19` | CHAR(1) |  |  |  |  |
| 550 | `AVAILABILITYBYGROUP19` | SMALLINT | NOT NULL |  |  |  |
| 551 | `PERIODIZEDCALENDARTYPE19CODE` | CHAR(10) |  |  |  |  |
| 552 | `LOGICALWAREHOUSE19COMPANYCODE` | CHAR(3) |  |  |  |  |
| 553 | `LOGICALWAREHOUSE19CODE` | CHAR(8) |  |  |  |  |
| 554 | `AVLWHSGROUP19COMPANYCODE` | CHAR(3) |  |  |  |  |
| 555 | `AVLWAREHOUSEGROUP19CODE` | CHAR(3) |  |  |  |  |
| 556 | `TOLERANCEQTY19` | DECIMAL(15,5) |  |  |  |  |
| 557 | `FORCERECALCULATION19` | SMALLINT | NOT NULL |  |  |  |
| 558 | `AVQUALITYGROUP19CODE` | CHAR(3) |  |  |  |  |
| 559 | `LEVEL20MANAGED` | SMALLINT | NOT NULL |  |  |  |
| 560 | `LEVEL20ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 561 | `LEVEL20ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 562 | `LEVEL20SUBCODE01` | CHAR(20) |  |  |  |  |
| 563 | `LEVEL20SUBCODE02` | CHAR(10) |  |  |  |  |
| 564 | `LEVEL20SUBCODE03` | CHAR(10) |  |  |  |  |
| 565 | `LEVEL20SUBCODE04` | CHAR(10) |  |  |  |  |
| 566 | `LEVEL20SUBCODE05` | CHAR(10) |  |  |  |  |
| 567 | `LEVEL20SUBCODE06` | CHAR(10) |  |  |  |  |
| 568 | `LEVEL20SUBCODE07` | CHAR(10) |  |  |  |  |
| 569 | `LEVEL20SUBCODE08` | CHAR(10) |  |  |  |  |
| 570 | `LEVEL20SUBCODE09` | CHAR(10) |  |  |  |  |
| 571 | `LEVEL20SUBCODE10` | CHAR(10) |  |  |  |  |
| 572 | `RULE20CODE` | CHAR(10) |  |  |  |  |
| 573 | `RULEPOLICY20CODE` | CHAR(20) |  |  |  |  |
| 574 | `ONETOONERELATION20` | SMALLINT | NOT NULL |  |  |  |
| 575 | `ADDNEWRESERVATIONSAFTERPO20` | SMALLINT | NOT NULL |  |  |  |
| 576 | `PLANNINGAVLFORMULA20CMYCODE` | CHAR(3) |  |  |  |  |
| 577 | `PLANNINGAVLFORMULA20CODE` | CHAR(3) |  |  |  |  |
| 578 | `AVAILABILITYCONDITION20` | CHAR(1) |  |  |  |  |
| 579 | `AVAILABILITYBYGROUP20` | SMALLINT | NOT NULL |  |  |  |
| 580 | `PERIODIZEDCALENDARTYPE20CODE` | CHAR(10) |  |  |  |  |
| 581 | `LOGICALWAREHOUSE20COMPANYCODE` | CHAR(3) |  |  |  |  |
| 582 | `LOGICALWAREHOUSE20CODE` | CHAR(8) |  |  |  |  |
| 583 | `AVLWHSGROUP20COMPANYCODE` | CHAR(3) |  |  |  |  |
| 584 | `AVLWAREHOUSEGROUP20CODE` | CHAR(3) |  |  |  |  |
| 585 | `TOLERANCEQTY20` | DECIMAL(15,5) |  |  |  |  |
| 586 | `FORCERECALCULATION20` | SMALLINT | NOT NULL |  |  |  |
| 587 | `AVQUALITYGROUP20CODE` | CHAR(3) |  |  |  |  |
| 588 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 589 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 590 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 591 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 592 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 593 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 594 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPLANNINGTEMPLATE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.RULECODE,
       t.RULEPOLICYCODE,
       t.PLANNINGBY,
       t.MULTILINKSPLANNING,
       t.PROJECTMANAGEMENT,
       t.USEBASEQUANTITIES,
       t.USEORDERONLOWERLEVELRULE,
       t.USESPLITTEDPDFORORDER,
       t.FINITECAPACITYPLANNING,
       t.LEVEL1ITEMTYPECOMPANYCODE
FROM   DB2ADMIN.LOGPLANNINGTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
