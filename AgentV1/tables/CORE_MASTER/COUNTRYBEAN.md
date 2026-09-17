# DB2ADMIN.COUNTRYBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'COUNTRY')
- **Roles**: `staging_mirror`
- **Columns**: 53
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 115811

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `CODE` | CHAR(3) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `UEMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 6 | `EUROMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 7 | `IBANMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SEPAMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 9 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 10 | `BANKCONTROLLCHECK` | INTEGER | NOT NULL |  |  |  |
| 11 | `ISOCODE` | CHAR(2) |  |  |  |  |
| 12 | `INTERNATIONALNUMERICCODE` | DECIMAL(3,0) |  |  |  |  |
| 13 | `TAXCODELENGTH` | DECIMAL(2,0) |  |  |  |  |
| 14 | `CALENDARCODE` | CHAR(3) |  |  |  |  |
| 15 | `FIRSTADDRESSLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 16 | `SECONDADDRESSLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 17 | `THIRDADDRESSLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 18 | `FOURTHADDRESSLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 19 | `FIFTHADDRESSLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 20 | `POSTALCODEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 21 | `TOWNDESCRIPTION` | CHAR(30) |  |  |  |  |
| 22 | `DISTRICTDESCRIPTION` | CHAR(30) |  |  |  |  |
| 23 | `ADDRESSCUSTOMANDCHECKPLYREFCOD` | CHAR(20) |  |  |  |  |
| 24 | `VALIDATEIBAN` | SMALLINT | NOT NULL |  |  |  |
| 25 | `IBANCHECKRULE` | CHAR(1) |  |  |  |  |
| 26 | `BICCHECKRULE` | CHAR(1) |  |  |  |  |
| 27 | `VALIDATEBIC` | SMALLINT | NOT NULL |  |  |  |
| 28 | `IBANCOUNTRYMATCH` | SMALLINT | NOT NULL |  |  |  |
| 29 | `BICCOUNTRYMATCH` | SMALLINT | NOT NULL |  |  |  |
| 30 | `IBANISOOVERRIDECODE` | CHAR(3) |  |  |  |  |
| 31 | `BICISOOVERRIDECODE` | CHAR(3) |  |  |  |  |
| 32 | `ACCOUNTVALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 33 | `BICVALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 34 | `BANKDETAILVALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 35 | `LENGTHOFCLEARING` | INTEGER | NOT NULL |  |  |  |
| 36 | `BRANCHNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 37 | `STARTPOSITIONOFBRANCH` | INTEGER | NOT NULL |  |  |  |
| 38 | `LENGTHOFACCOUNT` | INTEGER | NOT NULL |  |  |  |
| 39 | `STARTOFACCOUNT` | INTEGER | NOT NULL |  |  |  |
| 40 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 41 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 42 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 43 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 44 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 45 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 46 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 47 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 48 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 49 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 50 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 51 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 52 | `TAXSTAMPEXCLUDED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COUNTRYBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.UEMEMBER,
       t.EUROMEMBER,
       t.IBANMEMBER,
       t.SEPAMEMBER,
       t.LANGUAGECODE,
       t.BANKCONTROLLCHECK,
       t.ISOCODE
FROM   DB2ADMIN.COUNTRYBEAN t
FETCH FIRST 100 ROWS ONLY;
```
