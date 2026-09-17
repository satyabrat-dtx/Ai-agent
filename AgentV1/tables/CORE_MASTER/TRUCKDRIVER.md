# DB2ADMIN.TRUCKDRIVER

- **Module**: `CORE_MASTER` (low confidence — referenced across 4 modules, so shared reference data)
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 7 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 27317

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `DRIVINGLICENCE` | CHAR(10) |  |  |  |  |
| 6 | `EXPIRATIONLICENCEDATE` | DATE |  |  |  |  |
| 7 | `COUNTRYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 9 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 10 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 11 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 12 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 13 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 14 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 15 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 16 | `TRANSPORTZONECODE` | CHAR(3) |  | FK | foreign_key |  |
| 17 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 18 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRUCKDRIVER.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRUCKDRIVER.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `COUNTRY_COUNTRY` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `TRUCKDRIVER.COUNTRYCODE = COUNTRY.CODE` |
| `TRANSPORTZONE_TRANSPORTZONE` | `COUNTRYCODE`, `TRANSPORTZONECODE` | [`TRANSPORTZONE`](../CORE_MASTER/TRANSPORTZONE.md) | `COUNTRYCODE`, `CODE` | RESTRICT | `TRUCKDRIVER.COUNTRYCODE = TRANSPORTZONE.COUNTRYCODE AND TRUCKDRIVER.TRANSPORTZONECODE = TRANSPORTZONE.CODE` |

## Referenced by (child → this table) — 7

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TRUCKDRIVER_TRUCKDRIVER` | [`EXTERNALRECEIVINGDOCUMENT`](../INVENTORY/EXTERNALRECEIVINGDOCUMENT.md) | `TRUCKDRIVERCOMPANYCODE`, `TRUCKDRIVERCODE` | `EXTERNALRECEIVINGDOCUMENT.TRUCKDRIVERCOMPANYCODE = TRUCKDRIVER.COMPANYCODE AND EXTERNALRECEIVINGDOCUMENT.TRUCKDRIVERCODE = TRUCKDRIVER.CODE` |
| `TRUCKDRIVER_TRUCKDRIVER` | [`INTERNALDOCUMENT`](../INTERNAL_ORDERS/INTERNALDOCUMENT.md) | `TRUCKDRIVERCOMPANYCODE`, `TRUCKDRIVERCODE` | `INTERNALDOCUMENT.TRUCKDRIVERCOMPANYCODE = TRUCKDRIVER.COMPANYCODE AND INTERNALDOCUMENT.TRUCKDRIVERCODE = TRUCKDRIVER.CODE` |
| `TRUCKDRIVER_TRUCKDRIVER` | [`EXTOPDOCUMENT`](../SUBCONTRACTING/EXTOPDOCUMENT.md) | `TRUCKDRIVERCOMPANYCODE`, `TRUCKDRIVERCODE` | `EXTOPDOCUMENT.TRUCKDRIVERCOMPANYCODE = TRUCKDRIVER.COMPANYCODE AND EXTOPDOCUMENT.TRUCKDRIVERCODE = TRUCKDRIVER.CODE` |
| `TRUCKDRIVER_TRUCKDRIVER` | [`SALESDOCUMENT`](../SALES/SALESDOCUMENT.md) | `TRUCKDRIVERCOMPANYCODE`, `TRUCKDRIVERCODE` | `SALESDOCUMENT.TRUCKDRIVERCOMPANYCODE = TRUCKDRIVER.COMPANYCODE AND SALESDOCUMENT.TRUCKDRIVERCODE = TRUCKDRIVER.CODE` |
| `TRUCKDRIVER_TRUCKDRIVER` | [`INTERNALRETURNDOCUMENT`](../INTERNAL_ORDERS/INTERNALRETURNDOCUMENT.md) | `TRUCKDRIVERCOMPANYCODE`, `TRUCKDRIVERCODE` | `INTERNALRETURNDOCUMENT.TRUCKDRIVERCOMPANYCODE = TRUCKDRIVER.COMPANYCODE AND INTERNALRETURNDOCUMENT.TRUCKDRIVERCODE = TRUCKDRIVER.CODE` |
| `TRUCKDRIVER_TRUCKDRIVER` | [`PURCHASERETURNDOCUMENT`](../PURCHASING/PURCHASERETURNDOCUMENT.md) | `TRUCKDRIVERCOMPANYCODE`, `TRUCKDRIVERCODE` | `PURCHASERETURNDOCUMENT.TRUCKDRIVERCOMPANYCODE = TRUCKDRIVER.COMPANYCODE AND PURCHASERETURNDOCUMENT.TRUCKDRIVERCODE = TRUCKDRIVER.CODE` |
| `TRUCKDRIVER_DRIVER` | [`FONSHIPGUIDEHEADER`](../OTHER/FONSHIPGUIDEHEADER.md) | `DRIVERCOMPANYCODE`, `DRIVERCODE` | `FONSHIPGUIDEHEADER.DRIVERCOMPANYCODE = TRUCKDRIVER.COMPANYCODE AND FONSHIPGUIDEHEADER.DRIVERCODE = TRUCKDRIVER.CODE` |

## Indexes

- `TRUCKDRIVERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DRIVINGLICENCE,
       t.EXPIRATIONLICENCEDATE,
       t.COUNTRYCODE,
       t.ADDRESSLINE1,
       t.ADDRESSLINE2,
       t.ADDRESSLINE3,
       t.ADDRESSLINE4
FROM   DB2ADMIN.TRUCKDRIVER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
