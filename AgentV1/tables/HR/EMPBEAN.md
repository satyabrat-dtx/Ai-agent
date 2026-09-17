# DB2ADMIN.EMPBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `HR` (medium confidence — table name starts with 'EMP')
- **Roles**: `staging_mirror`
- **Columns**: 230
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 171525

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `CATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 4 | `CATEGORYCODE` | CHAR(6) |  |  |  |  |
| 5 | `PREFIX` | CHAR(3) |  |  |  |  |
| 6 | `CATEGORYTYPE` | INTEGER | NOT NULL |  |  |  |
| 7 | `EMPLOYEENUMBER` | CHAR(6) |  |  |  |  |
| 8 | `CODE` | CHAR(9) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `CARDNO` | CHAR(50) |  |  |  |  |
| 10 | `OLDEMPLOYEENOCODE` | CHAR(9) |  |  |  |  |
| 11 | `FIRSTNAME` | CHAR(160) |  |  |  |  |
| 12 | `LASTNAME` | CHAR(160) |  |  |  |  |
| 13 | `MIDDLENAME` | CHAR(25) |  |  |  |  |
| 14 | `SHORTNAME` | CHAR(25) |  |  |  |  |
| 15 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 16 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 17 | `SECTIONSECTIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 18 | `SECTIONSECTIONCODE` | CHAR(6) |  |  |  |  |
| 19 | `MATYPEMACHINETYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 20 | `MACHINETYPEMACHINETYPECODE` | CHAR(6) |  |  |  |  |
| 21 | `MACHINENOMACHINENOICSTABLECODE` | CHAR(4) |  |  |  |  |
| 22 | `MACHINENOMACHINENOCODE` | CHAR(6) |  |  |  |  |
| 23 | `GRADEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 24 | `GRADECODE` | CHAR(6) |  |  |  |  |
| 25 | `DESGDESIGNATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 26 | `DESGDESIGNATIONCODE` | CHAR(6) |  |  |  |  |
| 27 | `CADREICSTABLECODE` | CHAR(4) |  |  |  |  |
| 28 | `CADRECODE` | CHAR(6) |  |  |  |  |
| 29 | `EMPROLECODE` | CHAR(3) |  |  |  |  |
| 30 | `SUBCTGSUBCATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 31 | `SUBCATEGORYSUBCATEGORYCODE` | CHAR(6) |  |  |  |  |
| 32 | `REPORTINGTOCODE` | CHAR(9) |  |  |  |  |
| 33 | `HODCODE` | CHAR(9) |  |  |  |  |
| 34 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 35 | `NATIONALITYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 36 | `NATIONALITYCODE` | CHAR(6) |  |  |  |  |
| 37 | `RELIGIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 38 | `RELIGIONCODE` | CHAR(6) |  |  |  |  |
| 39 | `SUBCASTEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 40 | `SUBCASTECODE` | CHAR(6) |  |  |  |  |
| 41 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 42 | `GENDER` | INTEGER | NOT NULL |  |  |  |
| 43 | `CASTECASTEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 44 | `CASTECASTECODE` | CHAR(6) |  |  |  |  |
| 45 | `MARITALSTATUSICSTABLECODE` | CHAR(4) |  |  |  |  |
| 46 | `MARITALSTATUSCODE` | CHAR(6) |  |  |  |  |
| 47 | `BIRTHDATE` | DATE |  |  |  |  |
| 48 | `CONFIRMATIONDATE` | DATE |  |  |  |  |
| 49 | `REINSTATEMENTDATE` | DATE |  |  |  |  |
| 50 | `REASONFORLEAVINGICSTABLECODE` | CHAR(4) |  |  |  |  |
| 51 | `REASONFORLEAVINGCODE` | CHAR(6) |  |  |  |  |
| 52 | `RESIGNDATE` | DATE |  |  |  |  |
| 53 | `JOININGDATE` | DATE |  |  |  |  |
| 54 | `GROUPJOININGDATE` | DATE |  |  |  |  |
| 55 | `DISCONTINUEDDATE` | DATE |  |  |  |  |
| 56 | `EXITDATE` | DATE |  |  |  |  |
| 57 | `NOTICEPERIODDAYS` | DECIMAL(2,0) |  |  |  |  |
| 58 | `ELIGIBLEFORPF` | INTEGER | NOT NULL |  |  |  |
| 59 | `PFNUMBER` | CHAR(30) |  |  |  |  |
| 60 | `JOININGPFDATE` | DATE |  |  |  |  |
| 61 | `LEAVINGPFDATE` | DATE |  |  |  |  |
| 62 | `PFCEILINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 63 | `PENSIONFLAG` | INTEGER | NOT NULL |  |  |  |
| 64 | `UANNUMBER` | CHAR(20) |  |  |  |  |
| 65 | `UANACTIVATIONFLAG` | INTEGER | NOT NULL |  |  |  |
| 66 | `UANACTIVATIONDATE` | DATE |  |  |  |  |
| 67 | `ELIGIBLEFORESI` | INTEGER | NOT NULL |  |  |  |
| 68 | `ESINO` | CHAR(15) |  |  |  |  |
| 69 | `JOININGESIDATE` | DATE |  |  |  |  |
| 70 | `LEAVINGESIDATE` | DATE |  |  |  |  |
| 71 | `ESIDEDUCTEDFORTHECURRENT` | INTEGER | NOT NULL |  |  |  |
| 72 | `MEMEBERSHIPFLAG` | INTEGER | NOT NULL |  |  |  |
| 73 | `UNIONMEMBERSHIPNO` | CHAR(15) |  |  |  |  |
| 74 | `JOININGUNIONDATE` | DATE |  |  |  |  |
| 75 | `LEAVINGUNIONDATE` | DATE |  |  |  |  |
| 76 | `AADHAARNUMBER` | DECIMAL(12,0) |  |  |  |  |
| 77 | `PANNO` | CHAR(30) |  |  |  |  |
| 78 | `PASSPORT` | CHAR(25) |  |  |  |  |
| 79 | `PASSPORTDATE` | DATE |  |  |  |  |
| 80 | `PASSPORTEXPDATE` | DATE |  |  |  |  |
| 81 | `INSURED` | INTEGER | NOT NULL |  |  |  |
| 82 | `BLOODGROUPICSTABLECODE` | CHAR(4) |  |  |  |  |
| 83 | `BLOODGROUPCODE` | CHAR(6) |  |  |  |  |
| 84 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 85 | `WEIGHTINKG` | DECIMAL(3,0) |  |  |  |  |
| 86 | `CHESTININCHES` | DECIMAL(3,0) |  |  |  |  |
| 87 | `DISABILITY` | INTEGER | NOT NULL |  |  |  |
| 88 | `IDENTIFICATIONMARK1` | CHAR(25) |  |  |  |  |
| 89 | `DOMICILEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 90 | `DOMICILECODE` | CHAR(6) |  |  |  |  |
| 91 | `SMOKING` | INTEGER | NOT NULL |  |  |  |
| 92 | `HEIGHTINCMS` | DECIMAL(3,0) |  |  |  |  |
| 93 | `WAISTININCHES` | DECIMAL(3,0) |  |  |  |  |
| 94 | `DISABILITYDESCRIPTION` | CHAR(20) |  |  |  |  |
| 95 | `IDENTIFICATIONMARK2` | CHAR(25) |  |  |  |  |
| 96 | `BIRTHDAYGREETING` | SMALLINT | NOT NULL |  |  |  |
| 97 | `FATHERNAME` | VARCHAR(200) |  |  |  |  |
| 98 | `MOTHERNAME` | VARCHAR(200) |  |  |  |  |
| 99 | `EMAILID` | VARCHAR(200) |  |  |  |  |
| 100 | `MOBILE` | CHAR(12) |  |  |  |  |
| 101 | `DIRECTLINE` | CHAR(12) |  |  |  |  |
| 102 | `OFFICEEXTENSION` | CHAR(12) |  |  |  |  |
| 103 | `EMERGENCYCONTACTPERSON` | VARCHAR(200) |  |  |  |  |
| 104 | `EMERGENCYCONTACTRELATION` | CHAR(25) |  |  |  |  |
| 105 | `EMERGENCYCONTACTNO` | CHAR(12) |  |  |  |  |
| 106 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 107 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 108 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 109 | `TYPEOFEMPLOYMENTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 110 | `TYPEOFEMPLOYMENTCODE` | CHAR(6) |  |  |  |  |
| 111 | `NATUREOFEMPLOYMENTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 112 | `NATUREOFEMPLOYMENTCODE` | CHAR(6) |  |  |  |  |
| 113 | `TYPEOFACCOMODATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 114 | `TYPEOFACCOMODATIONCODE` | CHAR(6) |  |  |  |  |
| 115 | `TYPEOFVEHICLEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 116 | `TYPEOFVEHICLECODE` | CHAR(6) |  |  |  |  |
| 117 | `WORKLOCATIONCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 118 | `WORKLOCATIONSTATECODE` | CHAR(3) |  |  |  |  |
| 119 | `WORKMILLNOICSTABLECODE` | CHAR(4) |  |  |  |  |
| 120 | `WORKMILLNOCODE` | CHAR(6) |  |  |  |  |
| 121 | `WORKCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 122 | `WORKLOCDISTRICTDISTRICTCODE` | CHAR(3) |  |  |  |  |
| 123 | `WORKLOCATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 124 | `WORKLOCATIONCODE` | CHAR(6) |  |  |  |  |
| 125 | `WORKSHIFTNOCODE` | CHAR(3) |  |  |  |  |
| 126 | `MONTHPRESENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 127 | `MONTHPAYABLEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 128 | `MONTHLYLEAVEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 129 | `MONTHLYABSENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 130 | `TOTALPRESENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 131 | `TOTALPAYABLEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 132 | `TOTALLEAVEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 133 | `TOTALABSENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 134 | `RATEDFREQUENCYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 135 | `RATEDFREQUENCYCODE` | CHAR(6) |  |  |  |  |
| 136 | `PAYMENTFREQUENCY` | INTEGER | NOT NULL |  |  |  |
| 137 | `BASICPAY` | DECIMAL(11,2) |  |  |  |  |
| 138 | `UNITOFBASICPAY` | INTEGER | NOT NULL |  |  |  |
| 139 | `VOLUANTARYPF` | DECIMAL(5,2) |  |  |  |  |
| 140 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 141 | `PAYMENTTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 142 | `PAYMENTTYPECODE` | CHAR(6) |  |  |  |  |
| 143 | `SENIORALLOWANCE` | SMALLINT | NOT NULL |  |  |  |
| 144 | `BANKIDBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 145 | `BANKIDCODE` | CHAR(15) |  |  |  |  |
| 146 | `BANKIDBRANCHCODE` | CHAR(6) |  |  |  |  |
| 147 | `TYPEOFACCOUNTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 148 | `TYPEOFACCOUNTCODE` | CHAR(6) |  |  |  |  |
| 149 | `BANKREFNO` | CHAR(25) |  |  |  |  |
| 150 | `LEDGERID` | CHAR(12) |  |  |  |  |
| 151 | `ACCOUNTNUMBER` | CHAR(25) |  |  |  |  |
| 152 | `BANKIDSECBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 153 | `BANKIDSECCODE` | CHAR(15) |  |  |  |  |
| 154 | `BANKIDSECBRANCHCODE` | CHAR(6) |  |  |  |  |
| 155 | `TYPEOFACCOUNTSECICSTABLECODE` | CHAR(4) |  |  |  |  |
| 156 | `TYPEOFACCOUNTSECCODE` | CHAR(6) |  |  |  |  |
| 157 | `BANKREFNOSEC` | CHAR(25) |  |  |  |  |
| 158 | `LEDGERIDSEC` | CHAR(12) |  |  |  |  |
| 159 | `ACCOUNTNUMBERSEC` | CHAR(25) |  |  |  |  |
| 160 | `BONDTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 161 | `BONDTYPECODE` | CHAR(6) |  |  |  |  |
| 162 | `BONDFROMDATE` | DATE |  |  |  |  |
| 163 | `BONDAMOUNT` | DECIMAL(9,0) |  |  |  |  |
| 164 | `BONDTODATE` | DATE |  |  |  |  |
| 165 | `FINANCIALGROUPICSTABLECODE` | CHAR(4) |  |  |  |  |
| 166 | `FINANCIALGROUPCODE` | CHAR(6) |  |  |  |  |
| 167 | `REQUESTFLAG` | INTEGER | NOT NULL |  |  |  |
| 168 | `COLUMN1` | CHAR(30) |  |  |  |  |
| 169 | `COLUMN2` | CHAR(30) |  |  |  |  |
| 170 | `COLUMN3` | CHAR(30) |  |  |  |  |
| 171 | `COLUMN4` | CHAR(30) |  |  |  |  |
| 172 | `COLUMN5` | CHAR(30) |  |  |  |  |
| 173 | `COLUMN6` | CHAR(30) |  |  |  |  |
| 174 | `COLUMN7` | CHAR(30) |  |  |  |  |
| 175 | `COLUMN8` | CHAR(30) |  |  |  |  |
| 176 | `COLUMN9` | CHAR(30) |  |  |  |  |
| 177 | `COLUMN10` | CHAR(30) |  |  |  |  |
| 178 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 179 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 180 | `USER1USERID` | CHAR(50) |  |  |  |  |
| 181 | `USER2USERID` | CHAR(50) |  |  |  |  |
| 182 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 183 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 184 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 185 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 186 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 187 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 188 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 189 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 190 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 191 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 192 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 193 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 194 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 195 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 196 | `STATUS` | CHAR(1) |  |  |  |  |
| 197 | `RELEASEFORCHECKING` | SMALLINT | NOT NULL |  |  |  |
| 198 | `REMARK1` | VARCHAR(200) |  |  |  |  |
| 199 | `RUNAPPROVE` | SMALLINT | NOT NULL |  |  |  |
| 200 | `RUNAPPROVEREJECT` | SMALLINT | NOT NULL |  |  |  |
| 201 | `APPROVALDATE` | DATE |  |  |  |  |
| 202 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 203 | `REMARK2` | VARCHAR(200) |  |  |  |  |
| 204 | `RUNACTIVATE` | SMALLINT | NOT NULL |  |  |  |
| 205 | `RUNACTIVATEREJECT` | SMALLINT | NOT NULL |  |  |  |
| 206 | `RELEASEDATE` | DATE |  |  |  |  |
| 207 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 208 | `REMARK3` | VARCHAR(200) |  |  |  |  |
| 209 | `STEP` | CHAR(1) |  |  |  |  |
| 210 | `VALIDATORFLAG` | SMALLINT | NOT NULL |  |  |  |
| 211 | `SAPFLAG` | CHAR(15) |  |  |  |  |
| 212 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 213 | `UPDATEFLAG` | SMALLINT | NOT NULL |  |  |  |
| 214 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 215 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 216 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 217 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 218 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 219 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 220 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 221 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 222 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 223 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 224 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 225 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 226 | `ABSUNIQUEIDOLD` | BIGINT | NOT NULL |  |  |  |
| 227 | `OLDEMPLOYEECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 228 | `OLDEMPLOYEECODE` | CHAR(9) |  |  |  |  |
| 229 | `NATIONID` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.PREFIX,
       t.CATEGORYTYPE,
       t.EMPLOYEENUMBER,
       t.CODE,
       t.CARDNO,
       t.OLDEMPLOYEENOCODE,
       t.FIRSTNAME
FROM   DB2ADMIN.EMPBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
