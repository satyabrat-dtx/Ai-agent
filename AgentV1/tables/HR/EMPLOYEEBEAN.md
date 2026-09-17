# DB2ADMIN.EMPLOYEEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `HR` (high confidence — table name starts with 'EMPLOYEE')
- **Roles**: `staging_mirror`
- **Columns**: 192
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 171849

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `CATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 4 | `CATEGORYCODE` | CHAR(6) |  |  |  |  |
| 5 | `CATEGORYTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `EMPLOYEENUMBER` | CHAR(6) |  |  |  |  |
| 7 | `CODE` | CHAR(9) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `CARDNO` | CHAR(50) |  |  |  |  |
| 9 | `OLDEMPLOYEENOCODE` | CHAR(9) |  |  |  |  |
| 10 | `FIRSTNAME` | CHAR(160) |  |  |  |  |
| 11 | `LASTNAME` | CHAR(160) |  |  |  |  |
| 12 | `MIDDLENAME` | CHAR(25) |  |  |  |  |
| 13 | `SHORTNAME` | CHAR(25) |  |  |  |  |
| 14 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 15 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 16 | `SECTIONSECTIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 17 | `SECTIONSECTIONCODE` | CHAR(6) |  |  |  |  |
| 18 | `MATYPEMACHINETYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 19 | `MACHINETYPEMACHINETYPECODE` | CHAR(6) |  |  |  |  |
| 20 | `MACHINENOMACHINENOICSTABLECODE` | CHAR(4) |  |  |  |  |
| 21 | `MACHINENOMACHINENOCODE` | CHAR(6) |  |  |  |  |
| 22 | `GRADEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 23 | `GRADECODE` | CHAR(6) |  |  |  |  |
| 24 | `DESGDESIGNATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 25 | `DESGDESIGNATIONCODE` | CHAR(6) |  |  |  |  |
| 26 | `CADREICSTABLECODE` | CHAR(4) |  |  |  |  |
| 27 | `CADRECODE` | CHAR(6) |  |  |  |  |
| 28 | `EMPROLECODE` | CHAR(3) |  |  |  |  |
| 29 | `SUBCTGSUBCATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 30 | `SUBCATEGORYSUBCATEGORYCODE` | CHAR(6) |  |  |  |  |
| 31 | `REPORTINGTOCODE` | CHAR(9) |  |  |  |  |
| 32 | `HODCODE` | CHAR(9) |  |  |  |  |
| 33 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 34 | `NATIONALITYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 35 | `NATIONALITYCODE` | CHAR(6) |  |  |  |  |
| 36 | `RELIGIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 37 | `RELIGIONCODE` | CHAR(6) |  |  |  |  |
| 38 | `SUBCASTEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 39 | `SUBCASTECODE` | CHAR(6) |  |  |  |  |
| 40 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 41 | `GENDER` | INTEGER | NOT NULL |  |  |  |
| 42 | `CASTECASTEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 43 | `CASTECASTECODE` | CHAR(6) |  |  |  |  |
| 44 | `MARITALSTATUSICSTABLECODE` | CHAR(4) |  |  |  |  |
| 45 | `MARITALSTATUSCODE` | CHAR(6) |  |  |  |  |
| 46 | `BIRTHDATE` | DATE |  |  |  |  |
| 47 | `CONFIRMATIONDATE` | DATE |  |  |  |  |
| 48 | `REINSTATEMENTDATE` | DATE |  |  |  |  |
| 49 | `REASONFORLEAVINGICSTABLECODE` | CHAR(4) |  |  |  |  |
| 50 | `REASONFORLEAVINGCODE` | CHAR(6) |  |  |  |  |
| 51 | `RESIGNDATE` | DATE |  |  |  |  |
| 52 | `JOININGDATE` | DATE |  |  |  |  |
| 53 | `GROUPJOININGDATE` | DATE |  |  |  |  |
| 54 | `DISCONTINUEDDATE` | DATE |  |  |  |  |
| 55 | `EXITDATE` | DATE |  |  |  |  |
| 56 | `NOTICEPERIODDAYS` | DECIMAL(2,0) |  |  |  |  |
| 57 | `ELIGIBLEFORPF` | INTEGER | NOT NULL |  |  |  |
| 58 | `PFNUMBER` | CHAR(30) |  |  |  |  |
| 59 | `JOININGPFDATE` | DATE |  |  |  |  |
| 60 | `LEAVINGPFDATE` | DATE |  |  |  |  |
| 61 | `PFCEILINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 62 | `PENSIONFLAG` | INTEGER | NOT NULL |  |  |  |
| 63 | `UANNUMBER` | CHAR(20) |  |  |  |  |
| 64 | `UANACTIVATIONFLAG` | INTEGER | NOT NULL |  |  |  |
| 65 | `UANACTIVATIONDATE` | DATE |  |  |  |  |
| 66 | `ELIGIBLEFORESI` | INTEGER | NOT NULL |  |  |  |
| 67 | `ESINO` | CHAR(15) |  |  |  |  |
| 68 | `JOININGESIDATE` | DATE |  |  |  |  |
| 69 | `LEAVINGESIDATE` | DATE |  |  |  |  |
| 70 | `ESIDEDUCTEDFORTHECURRENT` | INTEGER | NOT NULL |  |  |  |
| 71 | `MEMEBERSHIPFLAG` | INTEGER | NOT NULL |  |  |  |
| 72 | `UNIONMEMBERSHIPNO` | CHAR(15) |  |  |  |  |
| 73 | `JOININGUNIONDATE` | DATE |  |  |  |  |
| 74 | `LEAVINGUNIONDATE` | DATE |  |  |  |  |
| 75 | `AADHAARNUMBER` | DECIMAL(12,0) |  |  |  |  |
| 76 | `PANNO` | CHAR(30) |  |  |  |  |
| 77 | `PASSPORT` | CHAR(25) |  |  |  |  |
| 78 | `PASSPORTDATE` | DATE |  |  |  |  |
| 79 | `PASSPORTEXPDATE` | DATE |  |  |  |  |
| 80 | `INSURED` | INTEGER | NOT NULL |  |  |  |
| 81 | `BLOODGROUPICSTABLECODE` | CHAR(4) |  |  |  |  |
| 82 | `BLOODGROUPCODE` | CHAR(6) |  |  |  |  |
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
| 104 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
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
| 117 | `WORKCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 118 | `WORKLOCDISTRICTDISTRICTCODE` | CHAR(3) |  |  |  |  |
| 119 | `WORKLOCATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 120 | `WORKLOCATIONCODE` | CHAR(6) |  |  |  |  |
| 121 | `WORKSHIFTNOCODE` | CHAR(3) |  |  |  |  |
| 122 | `RATEDFREQUENCYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 123 | `RATEDFREQUENCYCODE` | CHAR(6) |  |  |  |  |
| 124 | `PAYMENTFREQUENCY` | INTEGER | NOT NULL |  |  |  |
| 125 | `BASICPAY` | DECIMAL(11,2) |  |  |  |  |
| 126 | `UNITOFBASICPAY` | INTEGER | NOT NULL |  |  |  |
| 127 | `VOLUANTARYPF` | DECIMAL(5,2) |  |  |  |  |
| 128 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 129 | `PAYMENTTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 130 | `PAYMENTTYPECODE` | CHAR(6) |  |  |  |  |
| 131 | `SENIORALLOWANCE` | SMALLINT | NOT NULL |  |  |  |
| 132 | `BANKIDBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 133 | `BANKIDCODE` | CHAR(15) |  |  |  |  |
| 134 | `BANKIDBRANCHCODE` | CHAR(6) |  |  |  |  |
| 135 | `TYPEOFACCOUNTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 136 | `TYPEOFACCOUNTCODE` | CHAR(6) |  |  |  |  |
| 137 | `BANKREFNO` | CHAR(25) |  |  |  |  |
| 138 | `LEDGERID` | CHAR(12) |  |  |  |  |
| 139 | `ACCOUNTNUMBER` | CHAR(25) |  |  |  |  |
| 140 | `BANKIDSECBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 141 | `BANKIDSECCODE` | CHAR(15) |  |  |  |  |
| 142 | `BANKIDSECBRANCHCODE` | CHAR(6) |  |  |  |  |
| 143 | `TYPEOFACCOUNTSECICSTABLECODE` | CHAR(4) |  |  |  |  |
| 144 | `TYPEOFACCOUNTSECCODE` | CHAR(6) |  |  |  |  |
| 145 | `BANKREFNOSEC` | CHAR(25) |  |  |  |  |
| 146 | `LEDGERIDSEC` | CHAR(12) |  |  |  |  |
| 147 | `ACCOUNTNUMBERSEC` | CHAR(25) |  |  |  |  |
| 148 | `BONDTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 149 | `BONDTYPECODE` | CHAR(6) |  |  |  |  |
| 150 | `BONDFROMDATE` | DATE |  |  |  |  |
| 151 | `BONDAMOUNT` | DECIMAL(9,0) |  |  |  |  |
| 152 | `BONDTODATE` | DATE |  |  |  |  |
| 153 | `FINANCIALGROUPICSTABLECODE` | CHAR(4) |  |  |  |  |
| 154 | `FINANCIALGROUPCODE` | CHAR(6) |  |  |  |  |
| 155 | `REQUESTFLAG` | INTEGER | NOT NULL |  |  |  |
| 156 | `USER1USERID` | CHAR(50) |  |  |  |  |
| 157 | `USER2USERID` | CHAR(50) |  |  |  |  |
| 158 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 159 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 160 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 161 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 162 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 163 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 164 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 165 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 166 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 167 | `STATUS` | CHAR(1) |  |  |  |  |
| 168 | `REMARK1` | VARCHAR(200) |  |  |  |  |
| 169 | `APPROVALDATE` | DATE |  |  |  |  |
| 170 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 171 | `REMARK2` | VARCHAR(200) |  |  |  |  |
| 172 | `RELEASEDATE` | DATE |  |  |  |  |
| 173 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 174 | `REMARK3` | VARCHAR(200) |  |  |  |  |
| 175 | `VALIDATORFLAG` | SMALLINT | NOT NULL |  |  |  |
| 176 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 177 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 178 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 179 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 180 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 181 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 182 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 183 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 184 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 185 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 186 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 187 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 188 | `ABSUNIQUEIDOLD` | BIGINT | NOT NULL |  |  |  |
| 189 | `OLDEMPLOYEECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 190 | `OLDEMPLOYEECODE` | CHAR(9) |  |  |  |  |
| 191 | `NATIONID` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPLOYEEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.CATEGORYTYPE,
       t.EMPLOYEENUMBER,
       t.CODE,
       t.CARDNO,
       t.OLDEMPLOYEENOCODE,
       t.FIRSTNAME,
       t.LASTNAME
FROM   DB2ADMIN.EMPLOYEEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
