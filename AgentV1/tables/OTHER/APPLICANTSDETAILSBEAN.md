# DB2ADMIN.APPLICANTSDETAILSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 123
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 171370

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | BIGINT | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `APPFLAG` | INTEGER | NOT NULL |  |  |  |
| 4 | `REFERENCEID` | CHAR(9) |  |  |  |  |
| 5 | `ACCESSCARDNO` | CHAR(50) |  |  |  |  |
| 6 | `APPDATE` | DATE |  |  |  |  |
| 7 | `FLAGSWT` | INTEGER | NOT NULL |  |  |  |
| 8 | `FUNCTIONALAREAICSTABLECODE` | CHAR(4) |  |  |  |  |
| 9 | `FUNCTIONALAREACODE` | CHAR(6) |  |  |  |  |
| 10 | `FIRSTNAME` | CHAR(100) |  |  |  |  |
| 11 | `MIDDLENAME` | CHAR(100) |  |  |  |  |
| 12 | `LASTNAME` | CHAR(100) |  |  |  |  |
| 13 | `DOB` | DATE |  |  |  |  |
| 14 | `AGE` | DECIMAL(3,0) |  |  |  |  |
| 15 | `GENDER` | INTEGER | NOT NULL |  |  |  |
| 16 | `MARITALSTATUSICSTABLECODE` | CHAR(4) |  |  |  |  |
| 17 | `MARITALSTATUSCODE` | CHAR(6) |  |  |  |  |
| 18 | `COMMUNITYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 19 | `COMMUNITYCODE` | CHAR(6) |  |  |  |  |
| 20 | `SERVICESTATUS` | VARCHAR(100) |  |  |  |  |
| 21 | `QUALIFICATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 22 | `QUALIFICATIONCODE` | CHAR(6) |  |  |  |  |
| 23 | `PREEXPERIENCE` | INTEGER | NOT NULL |  |  |  |
| 24 | `APPLSRCICSTABLECODE` | CHAR(4) |  |  |  |  |
| 25 | `APPLSRCCODE` | CHAR(6) |  |  |  |  |
| 26 | `POSAPPLIEDICSTABLECODE` | CHAR(4) |  |  |  |  |
| 27 | `POSAPPLIEDCODE` | CHAR(6) |  |  |  |  |
| 28 | `HEIGHT` | DECIMAL(10,0) |  |  |  |  |
| 29 | `WEIGHT` | DECIMAL(10,0) |  |  |  |  |
| 30 | `BLOODGRPICSTABLECODE` | CHAR(4) |  |  |  |  |
| 31 | `BLOODGRPCODE` | CHAR(6) |  |  |  |  |
| 32 | `PHYDISABLED` | INTEGER | NOT NULL |  |  |  |
| 33 | `DISTFRMLOC` | DECIMAL(10,0) |  |  |  |  |
| 34 | `CITIZENSHIPICSTABLECODE` | CHAR(4) |  |  |  |  |
| 35 | `CITIZENSHIPCODE` | CHAR(6) |  |  |  |  |
| 36 | `PASSPORTNO` | CHAR(10) |  |  |  |  |
| 37 | `PASSPORTVAL` | DATE |  |  |  |  |
| 38 | `EMCONTACTNO` | DECIMAL(10,0) |  |  |  |  |
| 39 | `EMCONTACTNAME` | CHAR(100) |  |  |  |  |
| 40 | `FAMILYINCOME` | DECIMAL(10,0) |  |  |  |  |
| 41 | `APPLICANTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 42 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 43 | `LINKURL` | VARCHAR(250) |  |  |  |  |
| 44 | `SHORTNAME` | CHAR(10) |  |  |  |  |
| 45 | `CATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 46 | `CATEGORYCODE` | CHAR(6) |  |  |  |  |
| 47 | `SUBCTGSUBCATEGORYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 48 | `SUBCATEGORYSUBCATEGORYCODE` | CHAR(6) |  |  |  |  |
| 49 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 50 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 51 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 52 | `SECTIONSECTIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 53 | `SECTIONSECTIONCODE` | CHAR(6) |  |  |  |  |
| 54 | `GRADEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 55 | `GRADECODE` | CHAR(6) |  |  |  |  |
| 56 | `DESGDESIGNATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 57 | `DESGDESIGNATIONCODE` | CHAR(6) |  |  |  |  |
| 58 | `EMPROLECODE` | CHAR(3) |  |  |  |  |
| 59 | `REPORTINGTOCODE` | CHAR(9) |  |  |  |  |
| 60 | `HODCODE` | CHAR(9) |  |  |  |  |
| 61 | `ELIGIBLEFORPF` | INTEGER | NOT NULL |  |  |  |
| 62 | `ELIGIBLEFORESI` | INTEGER | NOT NULL |  |  |  |
| 63 | `JOININGDATE` | DATE |  |  |  |  |
| 64 | `GROUPJOININGDATE` | DATE |  |  |  |  |
| 65 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 66 | `NATIONALITYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 67 | `NATIONALITYCODE` | CHAR(6) |  |  |  |  |
| 68 | `RELIGIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 69 | `RELIGIONCODE` | CHAR(6) |  |  |  |  |
| 70 | `CASTECASTEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 71 | `CASTECASTECODE` | CHAR(6) |  |  |  |  |
| 72 | `SUBCASTEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 73 | `SUBCASTECODE` | CHAR(6) |  |  |  |  |
| 74 | `TYPEOFEMPLOYMENTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 75 | `TYPEOFEMPLOYMENTCODE` | CHAR(6) |  |  |  |  |
| 76 | `NATUREOFEMPLOYMENTICSTABLECODE` | CHAR(4) |  |  |  |  |
| 77 | `NATUREOFEMPLOYMENTCODE` | CHAR(6) |  |  |  |  |
| 78 | `TYPEOFACCOMODATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 79 | `TYPEOFACCOMODATIONCODE` | CHAR(6) |  |  |  |  |
| 80 | `TYPEOFVEHICLEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 81 | `TYPEOFVEHICLECODE` | CHAR(6) |  |  |  |  |
| 82 | `WORKLOCATIONSTATECODE` | CHAR(3) |  |  |  |  |
| 83 | `WORKLOCATIONCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 84 | `WORKMILLNOICSTABLECODE` | CHAR(4) |  |  |  |  |
| 85 | `WORKMILLNOCODE` | CHAR(6) |  |  |  |  |
| 86 | `WORKCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 87 | `WORKLOCDISTRICTDISTRICTCODE` | CHAR(3) |  |  |  |  |
| 88 | `WORKLOCATIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 89 | `WORKLOCATIONCODE` | CHAR(6) |  |  |  |  |
| 90 | `WORKSHIFTNOCODE` | CHAR(3) |  |  |  |  |
| 91 | `RATEDFREQUENCYICSTABLECODE` | CHAR(4) |  |  |  |  |
| 92 | `RATEDFREQUENCYCODE` | CHAR(6) |  |  |  |  |
| 93 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 94 | `PAYMENTTYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 95 | `PAYMENTTYPECODE` | CHAR(6) |  |  |  |  |
| 96 | `BANKIDBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 97 | `BANKIDCODE` | CHAR(15) |  |  |  |  |
| 98 | `BANKIDBRANCHCODE` | CHAR(6) |  |  |  |  |
| 99 | `ACCOUNTNUMBER` | CHAR(25) |  |  |  |  |
| 100 | `DISABILITY` | INTEGER | NOT NULL |  |  |  |
| 101 | `INSURED` | INTEGER | NOT NULL |  |  |  |
| 102 | `SMOKING` | INTEGER | NOT NULL |  |  |  |
| 103 | `BASICPAY` | DECIMAL(11,2) |  |  |  |  |
| 104 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 105 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 106 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 107 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 108 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 109 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 110 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 111 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 112 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 113 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 114 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 115 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 116 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 117 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 118 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 119 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 120 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 121 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 122 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPLICANTSDETAILSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.APPFLAG,
       t.REFERENCEID,
       t.ACCESSCARDNO,
       t.APPDATE,
       t.FLAGSWT,
       t.FUNCTIONALAREAICSTABLECODE,
       t.FUNCTIONALAREACODE,
       t.FIRSTNAME,
       t.MIDDLENAME
FROM   DB2ADMIN.APPLICANTSDETAILSBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
