# DB2ADMIN.EMPLOYEEHISTORYBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `HR` (high confidence — table name starts with 'EMPLOYEE')
- **Roles**: `staging_mirror`
- **Columns**: 211
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 172310

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `CATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 4 | `CATEGORYCODE` | CHAR(6) |  |  |  |  |
| 5 | `CATEGORYTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `CODE` | CHAR(9) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `CARDNO` | CHAR(50) |  |  |  |  |
| 8 | `OLDEMPLOYEENOCODE` | CHAR(9) |  |  |  |  |
| 9 | `FIRSTNAME` | CHAR(160) |  |  |  |  |
| 10 | `MIDDLENAME` | CHAR(25) |  |  |  |  |
| 11 | `LASTNAME` | CHAR(160) |  |  |  |  |
| 12 | `SHORTNAME` | CHAR(25) |  |  |  |  |
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
| 32 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
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
| 77 | `INSURED` | INTEGER | NOT NULL |  |  |  |
| 78 | `PASSPORTDATE` | DATE |  |  |  |  |
| 79 | `PASSPORTEXPDATE` | DATE |  |  |  |  |
| 80 | `BLOODGROUPICSTABLECODE` | CHAR(4) |  |  |  |  |
| 81 | `BLOODGROUPCODE` | CHAR(6) |  |  |  |  |
| 82 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 83 | `WEIGHTINKG` | DECIMAL(3,0) |  |  |  |  |
| 84 | `CHESTININCHES` | DECIMAL(3,0) |  |  |  |  |
| 85 | `DISABILITY` | INTEGER | NOT NULL |  |  |  |
| 86 | `IDENTIFICATIONMARK1` | CHAR(25) |  |  |  |  |
| 87 | `DOMICILEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 88 | `DOMICILECODE` | CHAR(6) |  |  |  |  |
| 89 | `SMOKING` | INTEGER | NOT NULL |  |  |  |
| 90 | `HEIGHTINCMS` | DECIMAL(3,0) |  |  |  |  |
| 91 | `WAISTININCHES` | DECIMAL(3,0) |  |  |  |  |
| 92 | `DISABILITYDESCRIPTION` | CHAR(20) |  |  |  |  |
| 93 | `IDENTIFICATIONMARK2` | CHAR(25) |  |  |  |  |
| 94 | `BIRTHDAYGREETING` | SMALLINT | NOT NULL |  |  |  |
| 95 | `FATHERNAME` | VARCHAR(200) |  |  |  |  |
| 96 | `MOTHERNAME` | VARCHAR(200) |  |  |  |  |
| 97 | `EMAILID` | VARCHAR(200) |  |  |  |  |
| 98 | `MOBILE` | CHAR(12) |  |  |  |  |
| 99 | `DIRECTLINE` | CHAR(12) |  |  |  |  |
| 100 | `OFFICEEXTENSION` | CHAR(12) |  |  |  |  |
| 101 | `EMERGENCYCONTACTPERSON` | VARCHAR(200) |  |  |  |  |
| 102 | `EMERGENCYCONTACTRELATION` | CHAR(25) |  |  |  |  |
| 103 | `EMERGENCYCONTACTNO` | CHAR(12) |  |  |  |  |
| 104 | `TYPEOFEMPLOYMENTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 105 | `TYPEOFEMPLOYMENTCODE` | CHAR(6) |  |  |  |  |
| 106 | `NATUREOFEMPLOYMENTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 107 | `NATUREOFEMPLOYMENTCODE` | CHAR(6) |  |  |  |  |
| 108 | `TYPEOFACCOMODATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 109 | `TYPEOFACCOMODATIONCODE` | CHAR(6) |  |  |  |  |
| 110 | `TYPEOFVEHICLEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 111 | `TYPEOFVEHICLECODE` | CHAR(6) |  |  |  |  |
| 112 | `WORKLOCATIONCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 113 | `WORKLOCATIONSTATECODE` | CHAR(3) |  |  |  |  |
| 114 | `WORKMILLNOICSTABLECODE` | CHAR(4) |  |  |  |  |
| 115 | `WORKMILLNOCODE` | CHAR(6) |  |  |  |  |
| 116 | `WORKCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 117 | `WORKLOCDISTRICTDISTRICTCODE` | CHAR(3) |  |  |  |  |
| 118 | `WORKLOCATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 119 | `WORKLOCATIONCODE` | CHAR(6) |  |  |  |  |
| 120 | `WORKSHIFTNOCODE` | CHAR(3) |  |  |  |  |
| 121 | `MONTHPRESENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 122 | `MONTHPAYABLEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 123 | `MONTHLYLEAVEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 124 | `MONTHLYABSENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 125 | `TOTALPRESENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 126 | `TOTALPAYABLEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 127 | `TOTALLEAVEDAYS` | DECIMAL(9,0) |  |  |  |  |
| 128 | `TOTALABSENTDAYS` | DECIMAL(9,0) |  |  |  |  |
| 129 | `EMPLOYEESTATUS` | CHAR(8) |  |  |  |  |
| 130 | `RATEDFREQUENCYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 131 | `RATEDFREQUENCYCODE` | CHAR(6) |  |  |  |  |
| 132 | `PAYMENTFREQUENCY` | INTEGER | NOT NULL |  |  |  |
| 133 | `BASICPAY` | DECIMAL(11,2) |  |  |  |  |
| 134 | `UNITOFBASICPAY` | INTEGER | NOT NULL |  |  |  |
| 135 | `VOLUANTARYPF` | DECIMAL(5,2) |  |  |  |  |
| 136 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 137 | `PAYMENTTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 138 | `PAYMENTTYPECODE` | CHAR(6) |  |  |  |  |
| 139 | `BANKIDBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 140 | `BANKIDCODE` | CHAR(15) |  |  |  |  |
| 141 | `BANKIDBRANCHCODE` | CHAR(6) |  |  |  |  |
| 142 | `TYPEOFACCOUNTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 143 | `TYPEOFACCOUNTCODE` | CHAR(6) |  |  |  |  |
| 144 | `BANKREFNO` | CHAR(15) |  |  |  |  |
| 145 | `LEDGERID` | CHAR(12) |  |  |  |  |
| 146 | `ACCOUNTNUMBER` | CHAR(25) |  |  |  |  |
| 147 | `BANKIDSECBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 148 | `BANKIDSECCODE` | CHAR(15) |  |  |  |  |
| 149 | `BANKIDSECBRANCHCODE` | CHAR(6) |  |  |  |  |
| 150 | `TYPEOFACCOUNTSECICSTABLECODE` | CHAR(4) |  |  |  |  |
| 151 | `TYPEOFACCOUNTSECCODE` | CHAR(6) |  |  |  |  |
| 152 | `BANKREFNOSEC` | CHAR(25) |  |  |  |  |
| 153 | `LEDGERIDSEC` | CHAR(12) |  |  |  |  |
| 154 | `ACCOUNTNUMBERSEC` | CHAR(25) |  |  |  |  |
| 155 | `BONDTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 156 | `BONDTYPECODE` | CHAR(6) |  |  |  |  |
| 157 | `BONDFROMDATE` | DATE |  |  |  |  |
| 158 | `BONDAMOUNT` | DECIMAL(9,0) |  |  |  |  |
| 159 | `BONDTODATE` | DATE |  |  |  |  |
| 160 | `FINANCIALGROUPICSTABLECODE` | CHAR(4) |  |  |  |  |
| 161 | `FINANCIALGROUPCODE` | CHAR(6) |  |  |  |  |
| 162 | `REQUESTFLAG` | INTEGER | NOT NULL |  |  |  |
| 163 | `COLUMN1` | CHAR(30) |  |  |  |  |
| 164 | `COLUMN2` | CHAR(30) |  |  |  |  |
| 165 | `COLUMN3` | CHAR(30) |  |  |  |  |
| 166 | `COLUMN4` | CHAR(30) |  |  |  |  |
| 167 | `COLUMN5` | CHAR(30) |  |  |  |  |
| 168 | `COLUMN6` | CHAR(30) |  |  |  |  |
| 169 | `COLUMN7` | CHAR(30) |  |  |  |  |
| 170 | `COLUMN8` | CHAR(30) |  |  |  |  |
| 171 | `COLUMN9` | CHAR(30) |  |  |  |  |
| 172 | `COLUMN10` | CHAR(30) |  |  |  |  |
| 173 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 174 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 175 | `REMARK1` | VARCHAR(200) |  |  |  |  |
| 176 | `REMARK2` | VARCHAR(200) |  |  |  |  |
| 177 | `REMARK3` | VARCHAR(200) |  |  |  |  |
| 178 | `USER1USERID` | CHAR(50) |  |  |  |  |
| 179 | `USER2USERID` | CHAR(50) |  |  |  |  |
| 180 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 181 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 182 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 183 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 184 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 185 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 186 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 187 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 188 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 189 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 190 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 191 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 192 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 193 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 194 | `STEP` | CHAR(1) |  |  |  |  |
| 195 | `VALIDATORFLAG` | SMALLINT | NOT NULL |  |  |  |
| 196 | `SAPFLAG` | CHAR(15) |  |  |  |  |
| 197 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 198 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 199 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 200 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 201 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 202 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 203 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 204 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 205 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 206 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 207 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 208 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 209 | `OLDEMPLOYEECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 210 | `OLDEMPLOYEECODE` | CHAR(9) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPLOYEEHISTORYBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.CATEGORYTYPE,
       t.CODE,
       t.CARDNO,
       t.OLDEMPLOYEENOCODE,
       t.FIRSTNAME,
       t.MIDDLENAME,
       t.LASTNAME
FROM   DB2ADMIN.EMPLOYEEHISTORYBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
