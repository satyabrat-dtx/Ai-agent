# DB2ADMIN.RECRUITEXPERIENCE

- **Module**: `HR` (high confidence — table name starts with 'RECRUIT')
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `APPLNOCODE`, `SERIALNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 8 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159607

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `APPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SERIALNUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYNAME` | CHAR(25) | NOT NULL |  |  |  |
| 4 | `COUNTRYICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 5 | `COUNTRYCODE` | CHAR(6) |  | FK | foreign_key |  |
| 6 | `STATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `DISTRICTDISTRICTCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `LOCATIONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `WORKEDFROM` | DATE | NOT NULL |  |  |  |
| 10 | `WORKEDUNTIL` | DATE | NOT NULL |  |  |  |
| 11 | `WORKEDASICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 12 | `WORKEDASCODE` | CHAR(6) |  | FK | foreign_key |  |
| 13 | `CTC` | DECIMAL(11,2) | NOT NULL |  |  |  |
| 14 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 8

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLNO` | `COMPANYCODE`, `APPLNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITEXPERIENCE.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND RECRUITEXPERIENCE.APPLNOCODE = APPLICANTSDETAILS.CODE` |
| `CITY_LOCATION` | `LOCATIONCODE` | [`CITY`](../HR/CITY.md) | `CODE` | RESTRICT | `RECRUITEXPERIENCE.LOCATIONCODE = CITY.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECRUITEXPERIENCE.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `RECRUITEXPERIENCE.CURRENCYCODE = CURRENCY.CODE` |
| `ICSENTITY_COUNTRY` | `COMPANYCODE`, `COUNTRYICSTABLECODE`, `COUNTRYCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `RECRUITEXPERIENCE.COMPANYCODE = ICSENTITY.COMPANYCODE AND RECRUITEXPERIENCE.COUNTRYICSTABLECODE = ICSENTITY.ICSTABLECODE AND RECRUITEXPERIENCE.COUNTRYCODE = ICSENTITY.CODE` |
| `ICSENTITY_WORKEDAS` | `COMPANYCODE`, `WORKEDASICSTABLECODE`, `WORKEDASCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `RECRUITEXPERIENCE.COMPANYCODE = ICSENTITY.COMPANYCODE AND RECRUITEXPERIENCE.WORKEDASICSTABLECODE = ICSENTITY.ICSTABLECODE AND RECRUITEXPERIENCE.WORKEDASCODE = ICSENTITY.CODE` |
| `STATEVSDISTRICT_DISTRICT` | `STATECODE`, `DISTRICTDISTRICTCODE` | [`STATEVSDISTRICT`](../HR/STATEVSDISTRICT.md) | `STATECODE`, `DISTRICTCODE` | RESTRICT | `RECRUITEXPERIENCE.STATECODE = STATEVSDISTRICT.STATECODE AND RECRUITEXPERIENCE.DISTRICTDISTRICTCODE = STATEVSDISTRICT.DISTRICTCODE` |
| `STATE_STATE` | `STATECODE` | [`STATE`](../HR/STATE.md) | `CODE` | RESTRICT | `RECRUITEXPERIENCE.STATECODE = STATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECRUITEXPERIENCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.APPLNOCODE,
       t.SERIALNUMBER,
       t.COMPANYNAME,
       t.COUNTRYICSTABLECODE,
       t.COUNTRYCODE,
       t.STATECODE,
       t.DISTRICTDISTRICTCODE,
       t.LOCATIONCODE,
       t.WORKEDFROM,
       t.WORKEDUNTIL,
       t.WORKEDASICSTABLECODE
FROM   DB2ADMIN.RECRUITEXPERIENCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
