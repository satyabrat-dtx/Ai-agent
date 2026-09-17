# DB2ADMIN.DIVISIONIE

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'DIVISION')
- **Roles**: `business_data`
- **Columns**: 46
- **Primary key**: `ABSCOMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 217579

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 3 | `BANKCODE` | CHAR(15) |  | FK | foreign_key |  |
| 4 | `BANKBRANCHCODE` | CHAR(6) |  | FK | foreign_key |  |
| 5 | `ESTABLISHMENTDATE` | DATE |  |  |  |  |
| 6 | `TEXTILECOMMITTEENO` | CHAR(30) |  |  |  |  |
| 7 | `TEXTILECOMMITTEENODATE` | DATE |  |  |  |  |
| 8 | `IECODE` | CHAR(20) |  |  |  |  |
| 9 | `IECODEISSUINGAUTHORITY` | CHAR(35) |  |  |  |  |
| 10 | `RBICODEISSUEDATE` | DATE |  |  |  |  |
| 11 | `PANNO` | CHAR(20) |  |  |  |  |
| 12 | `PANISSUINGAUTHORITY` | CHAR(35) |  |  |  |  |
| 13 | `PANISSUEDATE` | DATE |  |  |  |  |
| 14 | `TANNO` | CHAR(20) |  |  |  |  |
| 15 | `TANISSUINGAUTHORITY` | CHAR(35) |  |  |  |  |
| 16 | `TANISSUEDATE` | DATE |  |  |  |  |
| 17 | `SSIREGISTRATIONNO` | CHAR(20) |  |  |  |  |
| 18 | `SSIREGISTRATIONDATE` | DATE |  |  |  |  |
| 19 | `INDUSTRIALLICENSENO` | CHAR(25) |  |  |  |  |
| 20 | `ILICENSEISSUINGAUTHORITY` | CHAR(35) |  |  |  |  |
| 21 | `EXPORTHOUSETYPE` | CHAR(30) |  |  |  |  |
| 22 | `EXPORTERTYPE` | CHAR(30) |  |  |  |  |
| 23 | `CERTIFICATENO` | CHAR(30) |  |  |  |  |
| 24 | `CERTIFICATEVALIDITYDATE` | DATE |  |  |  |  |
| 25 | `NATUREOFAPPLICANTFIRM` | CHAR(30) |  |  |  |  |
| 26 | `DEPBENROLLMENTNO` | CHAR(20) |  |  |  |  |
| 27 | `TINNO` | CHAR(30) |  |  |  |  |
| 28 | `MIDNO` | CHAR(35) |  |  |  |  |
| 29 | `COUNTRYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 30 | `ADDRESSLINE1` | VARCHAR(150) | NOT NULL |  |  |  |
| 31 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 32 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 33 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 34 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 35 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 36 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 37 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 38 | `TRANSPORTZONECODE` | CHAR(3) |  | FK | foreign_key |  |
| 39 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 40 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 41 | `EMAILADDRESS` | CHAR(60) |  |  |  |  |
| 42 | `RBICODE` | CHAR(20) |  |  |  |  |
| 43 | `PURCHASEVALUATION` | INTEGER | NOT NULL |  |  |  |
| 44 | `PERIODIZEDCALENDARTYPECODE` | CHAR(10) |  | FK | foreign_key |  |
| 45 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BANK_BANK` | `BANKBANKCOUNTRYCODE`, `BANKCODE`, `BANKBRANCHCODE` | [`BANK`](../CORE_MASTER/BANK.md) | `BANKCOUNTRYCODE`, `CODE`, `BRANCHCODE` | RESTRICT | `DIVISIONIE.BANKBANKCOUNTRYCODE = BANK.BANKCOUNTRYCODE AND DIVISIONIE.BANKCODE = BANK.CODE AND DIVISIONIE.BANKBRANCHCODE = BANK.BRANCHCODE` |
| `COMPANY_ABSCOMPANY` | `ABSCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DIVISIONIE.ABSCOMPANYCODE = COMPANY.CODE` |
| `COUNTRY_COUNTRY` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `DIVISIONIE.COUNTRYCODE = COUNTRY.CODE` |
| `PERIODIZEDCALENDARTYPE_PERIODIZEDCALENDARTYPE` | `PERIODIZEDCALENDARTYPECODE` | [`PERIODIZEDCALENDARTYPE`](../CORE_MASTER/PERIODIZEDCALENDARTYPE.md) | `CODE` | RESTRICT | `DIVISIONIE.PERIODIZEDCALENDARTYPECODE = PERIODIZEDCALENDARTYPE.CODE` |
| `TRANSPORTZONE_TRANSPORTZONE` | `COUNTRYCODE`, `TRANSPORTZONECODE` | [`TRANSPORTZONE`](../CORE_MASTER/TRANSPORTZONE.md) | `COUNTRYCODE`, `CODE` | RESTRICT | `DIVISIONIE.COUNTRYCODE = TRANSPORTZONE.COUNTRYCODE AND DIVISIONIE.TRANSPORTZONECODE = TRANSPORTZONE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DIVISIONIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSCOMPANYCODE,
       t.CODE,
       t.BANKBANKCOUNTRYCODE,
       t.BANKCODE,
       t.BANKBRANCHCODE,
       t.ESTABLISHMENTDATE,
       t.TEXTILECOMMITTEENO,
       t.TEXTILECOMMITTEENODATE,
       t.IECODE,
       t.IECODEISSUINGAUTHORITY,
       t.RBICODEISSUEDATE,
       t.PANNO
FROM   DB2ADMIN.DIVISIONIE t
FETCH FIRST 100 ROWS ONLY;
```
