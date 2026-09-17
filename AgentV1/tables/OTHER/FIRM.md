# DB2ADMIN.FIRM

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 60
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 122003

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `BANKCODE` | CHAR(15) |  | FK | foreign_key |  |
| 7 | `BANKBRANCHCODE` | CHAR(6) |  | FK | foreign_key |  |
| 8 | `ESTABLISHMENTDATE` | DATE |  |  |  |  |
| 9 | `TEXTILECOMMITTEENO` | CHAR(30) |  |  |  |  |
| 10 | `TEXTILECOMMITTEENODATE` | DATE |  |  |  |  |
| 11 | `IECODE` | CHAR(20) |  |  |  |  |
| 12 | `IECODEISSUINGAUTHORITY` | CHAR(35) |  |  |  |  |
| 13 | `RBICODE` | CHAR(20) |  |  |  |  |
| 14 | `RBICODEISSUEDATE` | DATE |  |  |  |  |
| 15 | `PANNO` | CHAR(20) |  |  |  |  |
| 16 | `PANISSUINGAUTHORITY` | CHAR(35) |  |  |  |  |
| 17 | `PANISSUEDATE` | DATE |  |  |  |  |
| 18 | `TANNO` | CHAR(20) |  |  |  |  |
| 19 | `TANISSUINGAUTHORITY` | CHAR(35) |  |  |  |  |
| 20 | `TANISSUEDATE` | DATE |  |  |  |  |
| 21 | `SSIREGISTRATIONNO` | CHAR(20) |  |  |  |  |
| 22 | `SSIREGISTRATIONDATE` | DATE |  |  |  |  |
| 23 | `INDUSTRIALLICENSENO` | CHAR(25) |  |  |  |  |
| 24 | `ILICENSEISSUINGAUTHORITY` | CHAR(35) |  |  |  |  |
| 25 | `EXPORTHOUSETYPE` | CHAR(30) |  |  |  |  |
| 26 | `EXPORTERTYPE` | CHAR(30) |  |  |  |  |
| 27 | `CERTIFICATENO` | CHAR(30) |  |  |  |  |
| 28 | `CERTIFICATEVALIDITYDATE` | DATE |  |  |  |  |
| 29 | `NATUREOFAPPLICANTFIRM` | CHAR(30) |  |  |  |  |
| 30 | `DEPBENROLLMENTNO` | CHAR(20) |  |  |  |  |
| 31 | `LSTNO` | CHAR(20) |  |  |  |  |
| 32 | `LSTDATE` | DATE |  |  |  |  |
| 33 | `CSTNO` | CHAR(20) |  |  |  |  |
| 34 | `CSTDATE` | DATE |  |  |  |  |
| 35 | `NOWFIRMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 36 | `TINNO` | CHAR(30) |  |  |  |  |
| 37 | `MIDNO` | CHAR(35) |  |  |  |  |
| 38 | `COUNTRYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 39 | `ADDRESSLINE1` | VARCHAR(150) | NOT NULL |  |  |  |
| 40 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 41 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 42 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 43 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 44 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 45 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 46 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 47 | `TRANSPORTZONECODE` | CHAR(3) |  | FK | foreign_key |  |
| 48 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 49 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 50 | `EMAILADDRESS` | CHAR(60) |  |  |  |  |
| 51 | `PURCHASEVALUATION` | INTEGER | NOT NULL |  |  |  |
| 52 | `PERIODIZEDCALENDARTYPECODE` | CHAR(10) |  | FK | foreign_key |  |
| 53 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 54 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 55 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 56 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 57 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 58 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 59 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BANK_BANK` | `BANKBANKCOUNTRYCODE`, `BANKCODE`, `BANKBRANCHCODE` | [`BANK`](../CORE_MASTER/BANK.md) | `BANKCOUNTRYCODE`, `CODE`, `BRANCHCODE` | RESTRICT | `FIRM.BANKBANKCOUNTRYCODE = BANK.BANKCOUNTRYCODE AND FIRM.BANKCODE = BANK.CODE AND FIRM.BANKBRANCHCODE = BANK.BRANCHCODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FIRM.COMPANYCODE = COMPANY.CODE` |
| `COUNTRY_COUNTRY` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `FIRM.COUNTRYCODE = COUNTRY.CODE` |
| `DIVISION_NOWFIRM` | `COMPANYCODE`, `NOWFIRMCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FIRM.COMPANYCODE = DIVISION.COMPANYCODE AND FIRM.NOWFIRMCODE = DIVISION.CODE` |
| `PERIODIZEDCALENDARTYPE_PERIODIZEDCALENDARTYPE` | `PERIODIZEDCALENDARTYPECODE` | [`PERIODIZEDCALENDARTYPE`](../CORE_MASTER/PERIODIZEDCALENDARTYPE.md) | `CODE` | RESTRICT | `FIRM.PERIODIZEDCALENDARTYPECODE = PERIODIZEDCALENDARTYPE.CODE` |
| `TRANSPORTZONE_TRANSPORTZONE` | `COUNTRYCODE`, `TRANSPORTZONECODE` | [`TRANSPORTZONE`](../CORE_MASTER/TRANSPORTZONE.md) | `COUNTRYCODE`, `CODE` | RESTRICT | `FIRM.COUNTRYCODE = TRANSPORTZONE.COUNTRYCODE AND FIRM.TRANSPORTZONECODE = TRANSPORTZONE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FIRMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.BANKBANKCOUNTRYCODE,
       t.BANKCODE,
       t.BANKBRANCHCODE,
       t.ESTABLISHMENTDATE,
       t.TEXTILECOMMITTEENO,
       t.TEXTILECOMMITTEENODATE,
       t.IECODE
FROM   DB2ADMIN.FIRM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
