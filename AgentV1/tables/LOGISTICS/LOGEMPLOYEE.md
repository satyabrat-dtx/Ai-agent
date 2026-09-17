# DB2ADMIN.LOGEMPLOYEE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 210
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 151897

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `CATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 3 | `CATEGORYCODE` | CHAR(6) |  |  |  |  |
| 4 | `CATEGORYTYPE` | INTEGER | NOT NULL |  |  |  |
| 5 | `CODE` | CHAR(9) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `CARDNO` | CHAR(50) |  |  |  |  |
| 7 | `OLDEMPLOYEENOCODE` | CHAR(9) |  |  |  |  |
| 8 | `FIRSTNAME` | CHAR(160) |  |  |  |  |
| 9 | `LASTNAME` | CHAR(160) |  |  |  |  |
| 10 | `MIDDLENAME` | CHAR(25) |  |  |  |  |
| 11 | `SHORTNAME` | CHAR(25) |  |  |  |  |
| 12 | `FACTORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 14 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 15 | `SECTIONSECTIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 16 | `SECTIONSECTIONCODE` | CHAR(6) |  |  |  |  |
| 17 | `MATYPEMACHINETYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 18 | `MACHINETYPEMACHINETYPECODE` | CHAR(6) |  |  |  |  |
| 19 | `MACHINENOMACHINENOICSTABLECODE` | CHAR(4) |  |  |  |  |
| 20 | `MACHINENOMACHINENOCODE` | CHAR(6) |  |  |  |  |
| 21 | `GRADEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 22 | `GRADECODE` | CHAR(6) |  |  |  |  |
| 23 | `DESGDESIGNATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 24 | `DESGDESIGNATIONCODE` | CHAR(6) |  |  |  |  |
| 25 | `CADREICSTABLECODE` | CHAR(4) |  |  |  |  |
| 26 | `CADRECODE` | CHAR(6) |  |  |  |  |
| 27 | `EMPROLECODE` | CHAR(3) |  |  |  |  |
| 28 | `SUBCTGSUBCATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 29 | `SUBCATEGORYSUBCATEGORYCODE` | CHAR(6) |  |  |  |  |
| 30 | `REPORTINGTOCODE` | CHAR(9) |  |  |  |  |
| 31 | `HODCODE` | CHAR(9) |  |  |  |  |
| 32 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 33 | `NATIONALITYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 34 | `NATIONALITYCODE` | CHAR(6) |  |  |  |  |
| 35 | `RELIGIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 36 | `RELIGIONCODE` | CHAR(6) |  |  |  |  |
| 37 | `SUBCASTEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 38 | `SUBCASTECODE` | CHAR(6) |  |  |  |  |
| 39 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 40 | `GENDER` | INTEGER | NOT NULL |  |  |  |
| 41 | `CASTECASTEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 42 | `CASTECASTECODE` | CHAR(6) |  |  |  |  |
| 43 | `MARITALSTATUSICSTABLECODE` | CHAR(4) |  |  |  |  |
| 44 | `MARITALSTATUSCODE` | CHAR(6) |  |  |  |  |
| 45 | `BIRTHDATE` | DATE |  |  |  |  |
| 46 | `CONFIRMATIONDATE` | DATE |  |  |  |  |
| 47 | `REINSTATEMENTDATE` | DATE |  |  |  |  |
| 48 | `REASONFORLEAVINGICSTABLECODE` | CHAR(4) |  |  |  |  |
| 49 | `REASONFORLEAVINGCODE` | CHAR(6) |  |  |  |  |
| 50 | `RESIGNDATE` | DATE |  |  |  |  |
| 51 | `JOININGDATE` | DATE |  |  |  |  |
| 52 | `GROUPJOININGDATE` | DATE |  |  |  |  |
| 53 | `DISCONTINUEDDATE` | DATE |  |  |  |  |
| 54 | `EXITDATE` | DATE |  |  |  |  |
| 55 | `NOTICEPERIODDAYS` | DECIMAL(2,0) |  |  |  |  |
| 56 | `ELIGIBLEFORPF` | INTEGER | NOT NULL |  |  |  |
| 57 | `PFNUMBER` | CHAR(30) |  |  |  |  |
| 58 | `JOININGPFDATE` | DATE |  |  |  |  |
| 59 | `LEAVINGPFDATE` | DATE |  |  |  |  |
| 60 | `PFCEILINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 61 | `PENSIONFLAG` | INTEGER | NOT NULL |  |  |  |
| 62 | `UANNUMBER` | CHAR(20) |  |  |  |  |
| 63 | `UANACTIVATIONFLAG` | INTEGER | NOT NULL |  |  |  |
| 64 | `UANACTIVATIONDATE` | DATE |  |  |  |  |
| 65 | `ELIGIBLEFORESI` | INTEGER | NOT NULL |  |  |  |
| 66 | `ESINO` | CHAR(15) |  |  |  |  |
| 67 | `JOININGESIDATE` | DATE |  |  |  |  |
| 68 | `LEAVINGESIDATE` | DATE |  |  |  |  |
| 69 | `ESIDEDUCTEDFORTHECURRENT` | INTEGER | NOT NULL |  |  |  |
| 70 | `MEMEBERSHIPFLAG` | INTEGER | NOT NULL |  |  |  |
| 71 | `UNIONMEMBERSHIPNO` | CHAR(15) |  |  |  |  |
| 72 | `JOININGUNIONDATE` | DATE |  |  |  |  |
| 73 | `LEAVINGUNIONDATE` | DATE |  |  |  |  |
| 74 | `AADHAARNUMBER` | DECIMAL(12,0) |  |  |  |  |
| 75 | `PANNO` | CHAR(30) |  |  |  |  |
| 76 | `PASSPORT` | CHAR(25) |  |  |  |  |
| 77 | `PASSPORTDATE` | DATE |  |  |  |  |
| 78 | `PASSPORTEXPDATE` | DATE |  |  |  |  |
| 79 | `INSURED` | INTEGER | NOT NULL |  |  |  |
| 80 | `BLOODGROUPICSTABLECODE` | CHAR(4) |  |  |  |  |
| 81 | `BLOODGROUPCODE` | CHAR(6) |  |  |  |  |
| 82 | `WEIGHTINKG` | DECIMAL(3,0) |  |  |  |  |
| 83 | `CHESTININCHES` | DECIMAL(3,0) |  |  |  |  |
| 84 | `DISABILITY` | INTEGER | NOT NULL |  |  |  |
| 85 | `IDENTIFICATIONMARK1` | CHAR(25) |  |  |  |  |
| 86 | `DOMICILEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 87 | `DOMICILECODE` | CHAR(6) |  |  |  |  |
| 88 | `SMOKING` | INTEGER | NOT NULL |  |  |  |
| 89 | `HEIGHTINCMS` | DECIMAL(3,0) |  |  |  |  |
| 90 | `WAISTININCHES` | DECIMAL(3,0) |  |  |  |  |
| 91 | `DISABILITYDESCRIPTION` | CHAR(20) |  |  |  |  |
| 92 | `IDENTIFICATIONMARK2` | CHAR(25) |  |  |  |  |
| 93 | `BIRTHDAYGREETING` | SMALLINT | NOT NULL |  |  |  |
| 94 | `FATHERNAME` | VARCHAR(200) |  |  |  |  |
| 95 | `MOTHERNAME` | VARCHAR(200) |  |  |  |  |
| 96 | `EMAILID` | VARCHAR(200) |  |  |  |  |
| 97 | `MOBILE` | CHAR(12) |  |  |  |  |
| 98 | `DIRECTLINE` | CHAR(12) |  |  |  |  |
| 99 | `OFFICEEXTENSION` | CHAR(12) |  |  |  |  |
| 100 | `EMERGENCYCONTACTPERSON` | VARCHAR(200) |  |  |  |  |
| 101 | `EMERGENCYCONTACTRELATION` | CHAR(25) |  |  |  |  |
| 102 | `EMERGENCYCONTACTNO` | CHAR(12) |  |  |  |  |
| 103 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 104 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 105 | `TYPEOFEMPLOYMENTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 106 | `TYPEOFEMPLOYMENTCODE` | CHAR(6) |  |  |  |  |
| 107 | `NATUREOFEMPLOYMENTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 108 | `NATUREOFEMPLOYMENTCODE` | CHAR(6) |  |  |  |  |
| 109 | `TYPEOFACCOMODATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 110 | `TYPEOFACCOMODATIONCODE` | CHAR(6) |  |  |  |  |
| 111 | `TYPEOFVEHICLEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 112 | `TYPEOFVEHICLECODE` | CHAR(6) |  |  |  |  |
| 113 | `WORKLOCATIONCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 114 | `WORKLOCATIONSTATECODE` | CHAR(3) |  |  |  |  |
| 115 | `WORKMILLNOICSTABLECODE` | CHAR(4) |  |  |  |  |
| 116 | `WORKMILLNOCODE` | CHAR(6) |  |  |  |  |
| 117 | `WORKCOSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 118 | `WORKCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 119 | `WORKLOCDISTRICTDISTRICTCODE` | CHAR(3) |  |  |  |  |
| 120 | `WORKLOCATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 121 | `WORKLOCATIONCODE` | CHAR(6) |  |  |  |  |
| 122 | `WORKSHIFTNOCODE` | CHAR(3) |  |  |  |  |
| 123 | `MONTHPRESENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 124 | `MONTHPAYABLEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 125 | `MONTHLYLEAVEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 126 | `MONTHLYABSENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 127 | `TOTALPRESENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 128 | `TOTALPAYABLEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 129 | `TOTALLEAVEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 130 | `TOTALABSENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 131 | `RATEDFREQUENCYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 132 | `RATEDFREQUENCYCODE` | CHAR(6) |  |  |  |  |
| 133 | `PAYMENTFREQUENCY` | INTEGER | NOT NULL |  |  |  |
| 134 | `BASICPAY` | DECIMAL(11,2) |  |  |  |  |
| 135 | `UNITOFBASICPAY` | INTEGER | NOT NULL |  |  |  |
| 136 | `VOLUANTARYPF` | DECIMAL(5,2) |  |  |  |  |
| 137 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 138 | `PAYMENTTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 139 | `PAYMENTTYPECODE` | CHAR(6) |  |  |  |  |
| 140 | `SENIORALLOWANCE` | SMALLINT | NOT NULL |  |  |  |
| 141 | `BANKIDBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 142 | `BANKIDCODE` | CHAR(15) |  |  |  |  |
| 143 | `BANKIDBRANCHCODE` | CHAR(6) |  |  |  |  |
| 144 | `TYPEOFACCOUNTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 145 | `TYPEOFACCOUNTCODE` | CHAR(6) |  |  |  |  |
| 146 | `BANKREFNO` | CHAR(25) |  |  |  |  |
| 147 | `LEDGERID` | CHAR(12) |  |  |  |  |
| 148 | `ACCOUNTNUMBER` | CHAR(25) |  |  |  |  |
| 149 | `BANKIDSECBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 150 | `BANKIDSECCODE` | CHAR(15) |  |  |  |  |
| 151 | `BANKIDSECBRANCHCODE` | CHAR(6) |  |  |  |  |
| 152 | `TYPEOFACCOUNTSECICSTABLECODE` | CHAR(4) |  |  |  |  |
| 153 | `TYPEOFACCOUNTSECCODE` | CHAR(6) |  |  |  |  |
| 154 | `BANKREFNOSEC` | CHAR(25) |  |  |  |  |
| 155 | `LEDGERIDSEC` | CHAR(12) |  |  |  |  |
| 156 | `ACCOUNTNUMBERSEC` | CHAR(25) |  |  |  |  |
| 157 | `BONDTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 158 | `BONDTYPECODE` | CHAR(6) |  |  |  |  |
| 159 | `BONDFROMDATE` | DATE |  |  |  |  |
| 160 | `BONDAMOUNT` | DECIMAL(9,0) |  |  |  |  |
| 161 | `BONDTODATE` | DATE |  |  |  |  |
| 162 | `FINANCIALGROUPICSTABLECODE` | CHAR(4) |  |  |  |  |
| 163 | `FINANCIALGROUPCODE` | CHAR(6) |  |  |  |  |
| 164 | `REQUESTFLAG` | INTEGER | NOT NULL |  |  |  |
| 165 | `COLUMN1` | CHAR(30) |  |  |  |  |
| 166 | `COLUMN2` | CHAR(30) |  |  |  |  |
| 167 | `COLUMN3` | CHAR(30) |  |  |  |  |
| 168 | `COLUMN4` | CHAR(30) |  |  |  |  |
| 169 | `COLUMN5` | CHAR(30) |  |  |  |  |
| 170 | `COLUMN6` | CHAR(30) |  |  |  |  |
| 171 | `COLUMN7` | CHAR(30) |  |  |  |  |
| 172 | `COLUMN8` | CHAR(30) |  |  |  |  |
| 173 | `COLUMN9` | CHAR(30) |  |  |  |  |
| 174 | `COLUMN10` | CHAR(30) |  |  |  |  |
| 175 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 176 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 177 | `USER1USERID` | CHAR(50) |  |  |  |  |
| 178 | `USER2USERID` | CHAR(50) |  |  |  |  |
| 179 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 180 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 181 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 182 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 183 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 184 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 185 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 186 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 187 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 188 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 189 | `REMARK1` | VARCHAR(200) |  |  |  |  |
| 190 | `APPROVALDATE` | DATE |  |  |  |  |
| 191 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 192 | `REMARK2` | VARCHAR(200) |  |  |  |  |
| 193 | `RELEASEDATE` | DATE |  |  |  |  |
| 194 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 195 | `REMARK3` | VARCHAR(200) |  |  |  |  |
| 196 | `STEP` | CHAR(1) |  |  |  |  |
| 197 | `VALIDATORFLAG` | SMALLINT | NOT NULL |  |  |  |
| 198 | `SAPFLAG` | CHAR(15) |  |  |  |  |
| 199 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 200 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 201 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 202 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 203 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 204 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 205 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 206 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 207 | `OLDEMPLOYEECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 208 | `OLDEMPLOYEECODE` | CHAR(9) |  |  |  |  |
| 209 | `NATIONID` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEMPLOYEE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGEMPLOYEEPREFIX`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.CATEGORYTYPE,
       t.CODE,
       t.CARDNO,
       t.OLDEMPLOYEENOCODE,
       t.FIRSTNAME,
       t.LASTNAME,
       t.MIDDLENAME,
       t.SHORTNAME
FROM   DB2ADMIN.LOGEMPLOYEE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
