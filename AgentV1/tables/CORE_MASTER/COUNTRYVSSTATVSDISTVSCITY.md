# DB2ADMIN.COUNTRYVSSTATVSDISTVSCITY

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'COUNTRY')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `COUNTRYCODE`, `STATECODE`, `DISTRICTCODE`, `CITYCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 150756

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COUNTRYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `STATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DISTRICTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CITYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CITY_CITY` | `CITYCODE` | [`CITY`](../HR/CITY.md) | `CODE` | RESTRICT | `COUNTRYVSSTATVSDISTVSCITY.CITYCODE = CITY.CODE` |
| `COUNTRY_COUNTRY` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `COUNTRYVSSTATVSDISTVSCITY.COUNTRYCODE = COUNTRY.CODE` |
| `NETDISTRICT_DISTRICT` | `DISTRICTCODE` | [`NETDISTRICT`](../LOCALIZATION/NETDISTRICT.md) | `CODE` | RESTRICT | `COUNTRYVSSTATVSDISTVSCITY.DISTRICTCODE = NETDISTRICT.CODE` |
| `STATE_STATE` | `STATECODE` | [`STATE`](../HR/STATE.md) | `CODE` | RESTRICT | `COUNTRYVSSTATVSDISTVSCITY.STATECODE = STATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COUNTRYVSSTATVSDISTVSCITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COUNTRYCODE,
       t.STATECODE,
       t.DISTRICTCODE,
       t.CITYCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.COUNTRYVSSTATVSDISTVSCITY t
FETCH FIRST 100 ROWS ONLY;
```
