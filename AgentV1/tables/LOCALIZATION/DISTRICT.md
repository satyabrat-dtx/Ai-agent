# DB2ADMIN.DISTRICT

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COUNTRYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 86173

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COUNTRYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CODE` | CHAR(100) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COUNTRY_DISTRICT` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `DISTRICT.COUNTRYCODE = COUNTRY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `DISTRICT_TOWN` | [`TOWN`](../LOCALIZATION/TOWN.md) | `DISTRICTCOUNTRYCODE`, `DISTRICTCODE` | `TOWN.DISTRICTCOUNTRYCODE = DISTRICT.COUNTRYCODE AND TOWN.DISTRICTCODE = DISTRICT.CODE` |
| `DISTRICT_DSTDISTRICT` | [`USASALESTAXDEFINITIONS`](../LOCALIZATION/USASALESTAXDEFINITIONS.md) | `DSTCOUNTRYCODE`, `DSTDISTRICTCODE` | `USASALESTAXDEFINITIONS.DSTCOUNTRYCODE = DISTRICT.COUNTRYCODE AND USASALESTAXDEFINITIONS.DSTDISTRICTCODE = DISTRICT.CODE` |
| `DISTRICT_ORIGINDISTRICT` | [`USASALESTAXDEFINITIONS`](../LOCALIZATION/USASALESTAXDEFINITIONS.md) | `ORIGINCOUNTRYCODE`, `ORIGINDISTRICTCODE` | `USASALESTAXDEFINITIONS.ORIGINCOUNTRYCODE = DISTRICT.COUNTRYCODE AND USASALESTAXDEFINITIONS.ORIGINDISTRICTCODE = DISTRICT.CODE` |

## Indexes

- `DISTRICTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COUNTRYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.DISTRICT t
FETCH FIRST 100 ROWS ONLY;
```
