# DB2ADMIN.FACTORY

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 53
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121919

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `COUNTRYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `ADDRESSLINE1` | VARCHAR(150) | NOT NULL |  |  |  |
| 8 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 9 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 10 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 11 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 12 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 13 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 14 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 15 | `TRANSPORTZONECODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 17 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 18 | `EMAILADDRESS` | CHAR(60) |  |  |  |  |
| 19 | `ISOCERTIFIED` | INTEGER | NOT NULL |  |  |  |
| 20 | `LSTNO` | CHAR(20) |  |  |  |  |
| 21 | `LSTDATE` | DATE |  |  |  |  |
| 22 | `CSTNO` | CHAR(20) |  |  |  |  |
| 23 | `CSTDATE` | DATE |  |  |  |  |
| 24 | `RANGECODE` | CHAR(15) |  |  |  |  |
| 25 | `RANGEDESCRIPTION` | CHAR(120) |  |  |  |  |
| 26 | `RANGEDIVISIONCODE` | CHAR(15) |  |  |  |  |
| 27 | `RANGEDIVISIONDESCRIPTION` | CHAR(120) |  |  |  |  |
| 28 | `COMMISIONERATE` | CHAR(30) |  |  |  |  |
| 29 | `ADDRCOMMRATE` | CHAR(100) |  |  |  |  |
| 30 | `REGISTRATIONNO` | CHAR(30) |  |  |  |  |
| 31 | `REGISTRATIONDATE` | DATE |  |  |  |  |
| 32 | `ECCNO` | CHAR(20) |  |  |  |  |
| 33 | `ECCDATE` | DATE |  |  |  |  |
| 34 | `STATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 35 | `NAMEANDDESOFEXOFF` | CHAR(100) |  |  |  |  |
| 36 | `NAMEANDDESOFEXSUP` | CHAR(100) |  |  |  |  |
| 37 | `RANGEII` | CHAR(120) |  |  |  |  |
| 38 | `PLAACCNO` | CHAR(30) |  |  |  |  |
| 39 | `SERVICERANGECODE` | CHAR(15) |  |  |  |  |
| 40 | `SERVICERANGEDESCRIPTION` | CHAR(120) |  |  |  |  |
| 41 | `SERVICERANGEDIVISIONCODE` | CHAR(15) |  |  |  |  |
| 42 | `SERVICERANGEDIVDESCRIPTION` | CHAR(120) |  |  |  |  |
| 43 | `SERVICECOMMISSIONERATE` | CHAR(30) |  |  |  |  |
| 44 | `SERVICECOMMISSINERATEADDRESS` | CHAR(120) |  |  |  |  |
| 45 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 46 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 47 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 48 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 49 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 50 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 51 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 52 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FACTORY.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FACTORY.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `COUNTRY_COUNTRY` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `FACTORY.COUNTRYCODE = COUNTRY.CODE` |
| `STATE_STATE` | `STATECODE` | [`STATE`](../HR/STATE.md) | `CODE` | RESTRICT | `FACTORY.STATECODE = STATE.CODE` |
| `TRANSPORTZONE_TRANSPORTZONE` | `COUNTRYCODE`, `TRANSPORTZONECODE` | [`TRANSPORTZONE`](../CORE_MASTER/TRANSPORTZONE.md) | `COUNTRYCODE`, `CODE` | RESTRICT | `FACTORY.COUNTRYCODE = TRANSPORTZONE.COUNTRYCODE AND FACTORY.TRANSPORTZONECODE = TRANSPORTZONE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FACTORY_FACTORY` | [`ESSEMPLOYEE`](../HR/ESSEMPLOYEE.md) | `FACTORYCOMPANYCODE`, `DIVISIONCODE`, `FACTORYCODE` | `ESSEMPLOYEE.FACTORYCOMPANYCODE = FACTORY.COMPANYCODE AND ESSEMPLOYEE.DIVISIONCODE = FACTORY.DIVISIONCODE AND ESSEMPLOYEE.FACTORYCODE = FACTORY.CODE` |

## Indexes

- `FACTORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COUNTRYCODE,
       t.ADDRESSLINE1,
       t.ADDRESSLINE2,
       t.ADDRESSLINE3,
       t.ADDRESSLINE4,
       t.ADDRESSLINE5
FROM   DB2ADMIN.FACTORY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
