# DB2ADMIN.WRKMONTHLYARSREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 244
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `EMPLOYEECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 162963

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `PAYROLLCODE` | CHAR(3) |  |  |  |  |
| 4 | `ATTENDANCETYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `PRLPRPERIODNOPROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 6 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 7 | `FIRSTNAME` | CHAR(25) |  |  |  |  |
| 8 | `MIDDLENAME` | CHAR(25) |  |  |  |  |
| 9 | `LASTNAME` | CHAR(25) |  |  |  |  |
| 10 | `CATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 11 | `CATEGORYCODE` | CHAR(6) |  |  |  |  |
| 12 | `SUBCTGSUBCATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 13 | `SUBCATEGORYSUBCATEGORYCODE` | CHAR(6) |  |  |  |  |
| 14 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 15 | `FACTORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 17 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 18 | `SECTIONSECTIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 19 | `SECTIONSECTIONCODE` | CHAR(6) |  |  |  |  |
| 20 | `MATYPEMACHINETYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 21 | `MACHINETYPEMACHINETYPECODE` | CHAR(6) |  |  |  |  |
| 22 | `DESGDESIGNATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 23 | `DESGDESIGNATIONCODE` | CHAR(6) |  |  |  |  |
| 24 | `ORDERBY` | INTEGER | NOT NULL |  |  |  |
| 25 | `FORMAT` | INTEGER | NOT NULL |  |  |  |
| 26 | `INTIME1` | TIME |  |  |  |  |
| 27 | `INTIME2` | TIME |  |  |  |  |
| 28 | `INTIME3` | TIME |  |  |  |  |
| 29 | `INTIME4` | TIME |  |  |  |  |
| 30 | `INTIME5` | TIME |  |  |  |  |
| 31 | `INTIME6` | TIME |  |  |  |  |
| 32 | `INTIME7` | TIME |  |  |  |  |
| 33 | `INTIME8` | TIME |  |  |  |  |
| 34 | `INTIME9` | TIME |  |  |  |  |
| 35 | `INTIME10` | TIME |  |  |  |  |
| 36 | `INTIME11` | TIME |  |  |  |  |
| 37 | `INTIME12` | TIME |  |  |  |  |
| 38 | `INTIME13` | TIME |  |  |  |  |
| 39 | `INTIME14` | TIME |  |  |  |  |
| 40 | `INTIME15` | TIME |  |  |  |  |
| 41 | `INTIME16` | TIME |  |  |  |  |
| 42 | `INTIME17` | TIME |  |  |  |  |
| 43 | `INTIME18` | TIME |  |  |  |  |
| 44 | `INTIME19` | TIME |  |  |  |  |
| 45 | `INTIME20` | TIME |  |  |  |  |
| 46 | `INTIME21` | TIME |  |  |  |  |
| 47 | `INTIME22` | TIME |  |  |  |  |
| 48 | `INTIME23` | TIME |  |  |  |  |
| 49 | `INTIME24` | TIME |  |  |  |  |
| 50 | `INTIME25` | TIME |  |  |  |  |
| 51 | `INTIME26` | TIME |  |  |  |  |
| 52 | `INTIME27` | TIME |  |  |  |  |
| 53 | `INTIME28` | TIME |  |  |  |  |
| 54 | `INTIME29` | TIME |  |  |  |  |
| 55 | `INTIME30` | TIME |  |  |  |  |
| 56 | `INTIME31` | TIME |  |  |  |  |
| 57 | `OUTTIME1` | TIME |  |  |  |  |
| 58 | `OUTTIME2` | TIME |  |  |  |  |
| 59 | `OUTTIME3` | TIME |  |  |  |  |
| 60 | `OUTTIME4` | TIME |  |  |  |  |
| 61 | `OUTTIME5` | TIME |  |  |  |  |
| 62 | `OUTTIME6` | TIME |  |  |  |  |
| 63 | `OUTTIME7` | TIME |  |  |  |  |
| 64 | `OUTTIME8` | TIME |  |  |  |  |
| 65 | `OUTTIME9` | TIME |  |  |  |  |
| 66 | `OUTTIME10` | TIME |  |  |  |  |
| 67 | `OUTTIME11` | TIME |  |  |  |  |
| 68 | `OUTTIME12` | TIME |  |  |  |  |
| 69 | `OUTTIME13` | TIME |  |  |  |  |
| 70 | `OUTTIME14` | TIME |  |  |  |  |
| 71 | `OUTTIME15` | TIME |  |  |  |  |
| 72 | `OUTTIME16` | TIME |  |  |  |  |
| 73 | `OUTTIME17` | TIME |  |  |  |  |
| 74 | `OUTTIME18` | TIME |  |  |  |  |
| 75 | `OUTTIME19` | TIME |  |  |  |  |
| 76 | `OUTTIME20` | TIME |  |  |  |  |
| 77 | `OUTTIME21` | TIME |  |  |  |  |
| 78 | `OUTTIME22` | TIME |  |  |  |  |
| 79 | `OUTTIME23` | TIME |  |  |  |  |
| 80 | `OUTTIME24` | TIME |  |  |  |  |
| 81 | `OUTTIME25` | TIME |  |  |  |  |
| 82 | `OUTTIME26` | TIME |  |  |  |  |
| 83 | `OUTTIME27` | TIME |  |  |  |  |
| 84 | `OUTTIME28` | TIME |  |  |  |  |
| 85 | `OUTTIME29` | TIME |  |  |  |  |
| 86 | `OUTTIME30` | TIME |  |  |  |  |
| 87 | `OUTTIME31` | TIME |  |  |  |  |
| 88 | `COSTCENTERBADLICODE1` | CHAR(10) |  |  |  |  |
| 89 | `COSTCENTERBADLICODE2` | CHAR(10) |  |  |  |  |
| 90 | `COSTCENTERBADLICODE3` | CHAR(10) |  |  |  |  |
| 91 | `COSTCENTERBADLICODE4` | CHAR(10) |  |  |  |  |
| 92 | `COSTCENTERBADLICODE5` | CHAR(10) |  |  |  |  |
| 93 | `COSTCENTERBADLICODE6` | CHAR(10) |  |  |  |  |
| 94 | `COSTCENTERBADLICODE7` | CHAR(10) |  |  |  |  |
| 95 | `COSTCENTERBADLICODE8` | CHAR(10) |  |  |  |  |
| 96 | `COSTCENTERBADLICODE9` | CHAR(10) |  |  |  |  |
| 97 | `COSTCENTERBADLICODE10` | CHAR(10) |  |  |  |  |
| 98 | `COSTCENTERBADLICODE11` | CHAR(10) |  |  |  |  |
| 99 | `COSTCENTERBADLICODE12` | CHAR(10) |  |  |  |  |
| 100 | `COSTCENTERBADLICODE13` | CHAR(10) |  |  |  |  |
| 101 | `COSTCENTERBADLICODE14` | CHAR(10) |  |  |  |  |
| 102 | `COSTCENTERBADLICODE15` | CHAR(10) |  |  |  |  |
| 103 | `COSTCENTERBADLICODE16` | CHAR(10) |  |  |  |  |
| 104 | `COSTCENTERBADLICODE17` | CHAR(10) |  |  |  |  |
| 105 | `COSTCENTERBADLICODE18` | CHAR(10) |  |  |  |  |
| 106 | `COSTCENTERBADLICODE19` | CHAR(10) |  |  |  |  |
| 107 | `COSTCENTERBADLICODE20` | CHAR(10) |  |  |  |  |
| 108 | `COSTCENTERBADLICODE21` | CHAR(10) |  |  |  |  |
| 109 | `COSTCENTERBADLICODE22` | CHAR(10) |  |  |  |  |
| 110 | `COSTCENTERBADLICODE23` | CHAR(10) |  |  |  |  |
| 111 | `COSTCENTERBADLICODE24` | CHAR(10) |  |  |  |  |
| 112 | `COSTCENTERBADLICODE25` | CHAR(10) |  |  |  |  |
| 113 | `COSTCENTERBADLICODE26` | CHAR(10) |  |  |  |  |
| 114 | `COSTCENTERBADLICODE27` | CHAR(10) |  |  |  |  |
| 115 | `COSTCENTERBADLICODE28` | CHAR(10) |  |  |  |  |
| 116 | `COSTCENTERBADLICODE29` | CHAR(10) |  |  |  |  |
| 117 | `COSTCENTERBADLICODE30` | CHAR(10) |  |  |  |  |
| 118 | `COSTCENTERBADLICODE31` | CHAR(10) |  |  |  |  |
| 119 | `NUMBEROFHRS1` | DECIMAL(5,2) |  |  |  |  |
| 120 | `NUMBEROFHRS2` | DECIMAL(5,2) |  |  |  |  |
| 121 | `NUMBEROFHRS3` | DECIMAL(5,2) |  |  |  |  |
| 122 | `NUMBEROFHRS4` | DECIMAL(5,2) |  |  |  |  |
| 123 | `NUMBEROFHRS5` | DECIMAL(5,2) |  |  |  |  |
| 124 | `NUMBEROFHRS6` | DECIMAL(5,2) |  |  |  |  |
| 125 | `NUMBEROFHRS7` | DECIMAL(5,2) |  |  |  |  |
| 126 | `NUMBEROFHRS8` | DECIMAL(5,2) |  |  |  |  |
| 127 | `NUMBEROFHRS9` | DECIMAL(5,2) |  |  |  |  |
| 128 | `NUMBEROFHRS10` | DECIMAL(5,2) |  |  |  |  |
| 129 | `NUMBEROFHRS11` | DECIMAL(5,2) |  |  |  |  |
| 130 | `NUMBEROFHRS12` | DECIMAL(5,2) |  |  |  |  |
| 131 | `NUMBEROFHRS13` | DECIMAL(5,2) |  |  |  |  |
| 132 | `NUMBEROFHRS14` | DECIMAL(5,2) |  |  |  |  |
| 133 | `NUMBEROFHRS15` | DECIMAL(5,2) |  |  |  |  |
| 134 | `NUMBEROFHRS16` | DECIMAL(5,2) |  |  |  |  |
| 135 | `NUMBEROFHRS17` | DECIMAL(5,2) |  |  |  |  |
| 136 | `NUMBEROFHRS18` | DECIMAL(5,2) |  |  |  |  |
| 137 | `NUMBEROFHRS19` | DECIMAL(5,2) |  |  |  |  |
| 138 | `NUMBEROFHRS20` | DECIMAL(5,2) |  |  |  |  |
| 139 | `NUMBEROFHRS21` | DECIMAL(5,2) |  |  |  |  |
| 140 | `NUMBEROFHRS22` | DECIMAL(5,2) |  |  |  |  |
| 141 | `NUMBEROFHRS23` | DECIMAL(5,2) |  |  |  |  |
| 142 | `NUMBEROFHRS24` | DECIMAL(5,2) |  |  |  |  |
| 143 | `NUMBEROFHRS25` | DECIMAL(5,2) |  |  |  |  |
| 144 | `NUMBEROFHRS26` | DECIMAL(5,2) |  |  |  |  |
| 145 | `NUMBEROFHRS27` | DECIMAL(5,2) |  |  |  |  |
| 146 | `NUMBEROFHRS28` | DECIMAL(5,2) |  |  |  |  |
| 147 | `NUMBEROFHRS29` | DECIMAL(5,2) |  |  |  |  |
| 148 | `NUMBEROFHRS30` | DECIMAL(5,2) |  |  |  |  |
| 149 | `NUMBEROFHRS31` | DECIMAL(5,2) |  |  |  |  |
| 150 | `SHIFTCODE1` | CHAR(3) |  |  |  |  |
| 151 | `SHIFTCODE2` | CHAR(3) |  |  |  |  |
| 152 | `SHIFTCODE3` | CHAR(3) |  |  |  |  |
| 153 | `SHIFTCODE4` | CHAR(3) |  |  |  |  |
| 154 | `SHIFTCODE5` | CHAR(3) |  |  |  |  |
| 155 | `SHIFTCODE6` | CHAR(3) |  |  |  |  |
| 156 | `SHIFTCODE7` | CHAR(3) |  |  |  |  |
| 157 | `SHIFTCODE8` | CHAR(3) |  |  |  |  |
| 158 | `SHIFTCODE9` | CHAR(3) |  |  |  |  |
| 159 | `SHIFTCODE10` | CHAR(3) |  |  |  |  |
| 160 | `SHIFTCODE11` | CHAR(3) |  |  |  |  |
| 161 | `SHIFTCODE12` | CHAR(3) |  |  |  |  |
| 162 | `SHIFTCODE13` | CHAR(3) |  |  |  |  |
| 163 | `SHIFTCODE14` | CHAR(3) |  |  |  |  |
| 164 | `SHIFTCODE15` | CHAR(3) |  |  |  |  |
| 165 | `SHIFTCODE16` | CHAR(3) |  |  |  |  |
| 166 | `SHIFTCODE17` | CHAR(3) |  |  |  |  |
| 167 | `SHIFTCODE18` | CHAR(3) |  |  |  |  |
| 168 | `SHIFTCODE19` | CHAR(3) |  |  |  |  |
| 169 | `SHIFTCODE20` | CHAR(3) |  |  |  |  |
| 170 | `SHIFTCODE21` | CHAR(3) |  |  |  |  |
| 171 | `SHIFTCODE22` | CHAR(3) |  |  |  |  |
| 172 | `SHIFTCODE23` | CHAR(3) |  |  |  |  |
| 173 | `SHIFTCODE24` | CHAR(3) |  |  |  |  |
| 174 | `SHIFTCODE25` | CHAR(3) |  |  |  |  |
| 175 | `SHIFTCODE26` | CHAR(3) |  |  |  |  |
| 176 | `SHIFTCODE27` | CHAR(3) |  |  |  |  |
| 177 | `SHIFTCODE28` | CHAR(3) |  |  |  |  |
| 178 | `SHIFTCODE29` | CHAR(3) |  |  |  |  |
| 179 | `SHIFTCODE30` | CHAR(3) |  |  |  |  |
| 180 | `SHIFTCODE31` | CHAR(3) |  |  |  |  |
| 181 | `ATTENDANCECODE1` | CHAR(3) |  |  |  |  |
| 182 | `ATTENDANCECODE2` | CHAR(3) |  |  |  |  |
| 183 | `ATTENDANCECODE3` | CHAR(3) |  |  |  |  |
| 184 | `ATTENDANCECODE4` | CHAR(3) |  |  |  |  |
| 185 | `ATTENDANCECODE5` | CHAR(3) |  |  |  |  |
| 186 | `ATTENDANCECODE6` | CHAR(3) |  |  |  |  |
| 187 | `ATTENDANCECODE7` | CHAR(3) |  |  |  |  |
| 188 | `ATTENDANCECODE8` | CHAR(3) |  |  |  |  |
| 189 | `ATTENDANCECODE9` | CHAR(3) |  |  |  |  |
| 190 | `ATTENDANCECODE10` | CHAR(3) |  |  |  |  |
| 191 | `ATTENDANCECODE11` | CHAR(3) |  |  |  |  |
| 192 | `ATTENDANCECODE12` | CHAR(3) |  |  |  |  |
| 193 | `ATTENDANCECODE13` | CHAR(3) |  |  |  |  |
| 194 | `ATTENDANCECODE14` | CHAR(3) |  |  |  |  |
| 195 | `ATTENDANCECODE15` | CHAR(3) |  |  |  |  |
| 196 | `ATTENDANCECODE16` | CHAR(3) |  |  |  |  |
| 197 | `ATTENDANCECODE17` | CHAR(3) |  |  |  |  |
| 198 | `ATTENDANCECODE18` | CHAR(3) |  |  |  |  |
| 199 | `ATTENDANCECODE19` | CHAR(3) |  |  |  |  |
| 200 | `ATTENDANCECODE20` | CHAR(3) |  |  |  |  |
| 201 | `ATTENDANCECODE21` | CHAR(3) |  |  |  |  |
| 202 | `ATTENDANCECODE22` | CHAR(3) |  |  |  |  |
| 203 | `ATTENDANCECODE23` | CHAR(3) |  |  |  |  |
| 204 | `ATTENDANCECODE24` | CHAR(3) |  |  |  |  |
| 205 | `ATTENDANCECODE25` | CHAR(3) |  |  |  |  |
| 206 | `ATTENDANCECODE26` | CHAR(3) |  |  |  |  |
| 207 | `ATTENDANCECODE27` | CHAR(3) |  |  |  |  |
| 208 | `ATTENDANCECODE28` | CHAR(3) |  |  |  |  |
| 209 | `ATTENDANCECODE29` | CHAR(3) |  |  |  |  |
| 210 | `ATTENDANCECODE30` | CHAR(3) |  |  |  |  |
| 211 | `ATTENDANCECODE31` | CHAR(3) |  |  |  |  |
| 212 | `LEAVECODE1` | CHAR(3) |  |  |  |  |
| 213 | `LEAVECODE2` | CHAR(3) |  |  |  |  |
| 214 | `LEAVECODE3` | CHAR(3) |  |  |  |  |
| 215 | `LEAVECODE4` | CHAR(3) |  |  |  |  |
| 216 | `LEAVECODE5` | CHAR(3) |  |  |  |  |
| 217 | `LEAVECODE6` | CHAR(3) |  |  |  |  |
| 218 | `LEAVECODE7` | CHAR(3) |  |  |  |  |
| 219 | `LEAVECODE8` | CHAR(3) |  |  |  |  |
| 220 | `LEAVECODE9` | CHAR(3) |  |  |  |  |
| 221 | `LEAVECODE10` | CHAR(3) |  |  |  |  |
| 222 | `LEAVECODE11` | CHAR(3) |  |  |  |  |
| 223 | `LEAVECODE12` | CHAR(3) |  |  |  |  |
| 224 | `LEAVECODE13` | CHAR(3) |  |  |  |  |
| 225 | `LEAVECODE14` | CHAR(3) |  |  |  |  |
| 226 | `LEAVECODE15` | CHAR(3) |  |  |  |  |
| 227 | `LEAVECODE16` | CHAR(3) |  |  |  |  |
| 228 | `LEAVECODE17` | CHAR(3) |  |  |  |  |
| 229 | `LEAVECODE18` | CHAR(3) |  |  |  |  |
| 230 | `LEAVECODE19` | CHAR(3) |  |  |  |  |
| 231 | `LEAVECODE20` | CHAR(3) |  |  |  |  |
| 232 | `LEAVECODE21` | CHAR(3) |  |  |  |  |
| 233 | `LEAVECODE22` | CHAR(3) |  |  |  |  |
| 234 | `LEAVECODE23` | CHAR(3) |  |  |  |  |
| 235 | `LEAVECODE24` | CHAR(3) |  |  |  |  |
| 236 | `LEAVECODE25` | CHAR(3) |  |  |  |  |
| 237 | `LEAVECODE26` | CHAR(3) |  |  |  |  |
| 238 | `LEAVECODE27` | CHAR(3) |  |  |  |  |
| 239 | `LEAVECODE28` | CHAR(3) |  |  |  |  |
| 240 | `LEAVECODE29` | CHAR(3) |  |  |  |  |
| 241 | `LEAVECODE30` | CHAR(3) |  |  |  |  |
| 242 | `LEAVECODE31` | CHAR(3) |  |  |  |  |
| 243 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKMONTHLYARSREPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYDESCRIPTION,
       t.COMPANYCODE,
       t.PAYROLLCODE,
       t.ATTENDANCETYPECODE,
       t.PRLPRPERIODNOPROCESSPERIOD,
       t.EMPLOYEECODE,
       t.FIRSTNAME,
       t.MIDDLENAME,
       t.LASTNAME,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE
FROM   DB2ADMIN.WRKMONTHLYARSREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
