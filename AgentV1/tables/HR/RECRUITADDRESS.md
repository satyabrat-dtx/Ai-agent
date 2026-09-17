# DB2ADMIN.RECRUITADDRESS

- **Module**: `HR` (high confidence — table name starts with 'RECRUIT')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `APPLNOCODE`, `ADDRESSTYPEICSTABLECODE`, `ADDRESSTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159293

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `APPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ADDRESSTYPEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ADDRESSTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ADDRESSLINE1` | VARCHAR(200) | NOT NULL |  |  |  |
| 5 | `ADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 6 | `ADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 7 | `ADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 8 | `COUNTRYICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 9 | `COUNTRYCODE` | CHAR(6) |  | FK | foreign_key |  |
| 10 | `STATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `DISTRICTDISTRICTCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `CITYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `PINCODE` | CHAR(10) | NOT NULL |  |  |  |
| 14 | `EMAILID` | CHAR(25) |  |  |  |  |
| 15 | `COUNTCODE` | CHAR(5) |  |  |  |  |
| 16 | `TELEPHONELANDLINE` | CHAR(12) |  |  |  |  |
| 17 | `TELEPHONEMOBILE` | CHAR(12) |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLNO` | `COMPANYCODE`, `APPLNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITADDRESS.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND RECRUITADDRESS.APPLNOCODE = APPLICANTSDETAILS.CODE` |
| `CITY_CITY` | `CITYCODE` | [`CITY`](../HR/CITY.md) | `CODE` | RESTRICT | `RECRUITADDRESS.CITYCODE = CITY.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECRUITADDRESS.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_ADDRESSTYPE` | `COMPANYCODE`, `ADDRESSTYPEICSTABLECODE`, `ADDRESSTYPECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `RECRUITADDRESS.COMPANYCODE = ICSENTITY.COMPANYCODE AND RECRUITADDRESS.ADDRESSTYPEICSTABLECODE = ICSENTITY.ICSTABLECODE AND RECRUITADDRESS.ADDRESSTYPECODE = ICSENTITY.CODE` |
| `ICSENTITY_COUNTRY` | `COMPANYCODE`, `COUNTRYICSTABLECODE`, `COUNTRYCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `RECRUITADDRESS.COMPANYCODE = ICSENTITY.COMPANYCODE AND RECRUITADDRESS.COUNTRYICSTABLECODE = ICSENTITY.ICSTABLECODE AND RECRUITADDRESS.COUNTRYCODE = ICSENTITY.CODE` |
| `STATEVSDISTRICT_DISTRICT` | `STATECODE`, `DISTRICTDISTRICTCODE` | [`STATEVSDISTRICT`](../HR/STATEVSDISTRICT.md) | `STATECODE`, `DISTRICTCODE` | RESTRICT | `RECRUITADDRESS.STATECODE = STATEVSDISTRICT.STATECODE AND RECRUITADDRESS.DISTRICTDISTRICTCODE = STATEVSDISTRICT.DISTRICTCODE` |
| `STATE_STATE` | `STATECODE` | [`STATE`](../HR/STATE.md) | `CODE` | RESTRICT | `RECRUITADDRESS.STATECODE = STATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECRUITADDRESSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.APPLNOCODE,
       t.ADDRESSTYPEICSTABLECODE,
       t.ADDRESSTYPECODE,
       t.ADDRESSLINE1,
       t.ADDRESSLINE2,
       t.ADDRESSLINE3,
       t.ADDRESSLINE4,
       t.COUNTRYICSTABLECODE,
       t.COUNTRYCODE,
       t.STATECODE,
       t.DISTRICTDISTRICTCODE
FROM   DB2ADMIN.RECRUITADDRESS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
