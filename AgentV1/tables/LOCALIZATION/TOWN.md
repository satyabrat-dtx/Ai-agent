# DB2ADMIN.TOWN

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `DISTRICTCOUNTRYCODE`, `DISTRICTCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 86215

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DISTRICTCOUNTRYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DISTRICTCODE` | CHAR(100) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(100) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DISTRICT_TOWN` | `DISTRICTCOUNTRYCODE`, `DISTRICTCODE` | [`DISTRICT`](../LOCALIZATION/DISTRICT.md) | `COUNTRYCODE`, `CODE` | RESTRICT | `TOWN.DISTRICTCOUNTRYCODE = DISTRICT.COUNTRYCODE AND TOWN.DISTRICTCODE = DISTRICT.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TOWN_DSTTOWN` | [`USASALESTAXDEFINITIONS`](../LOCALIZATION/USASALESTAXDEFINITIONS.md) | `DSTCOUNTRYCODE`, `DSTDISTRICTCODE`, `DSTTOWNCODE` | `USASALESTAXDEFINITIONS.DSTCOUNTRYCODE = TOWN.DISTRICTCOUNTRYCODE AND USASALESTAXDEFINITIONS.DSTDISTRICTCODE = TOWN.DISTRICTCODE AND USASALESTAXDEFINITIONS.DSTTOWNCODE = TOWN.CODE` |
| `TOWN_ORIGINTOWN` | [`USASALESTAXDEFINITIONS`](../LOCALIZATION/USASALESTAXDEFINITIONS.md) | `ORIGINCOUNTRYCODE`, `ORIGINDISTRICTCODE`, `ORIGINTOWNCODE` | `USASALESTAXDEFINITIONS.ORIGINCOUNTRYCODE = TOWN.DISTRICTCOUNTRYCODE AND USASALESTAXDEFINITIONS.ORIGINDISTRICTCODE = TOWN.DISTRICTCODE AND USASALESTAXDEFINITIONS.ORIGINTOWNCODE = TOWN.CODE` |

## Indexes

- `TOWNUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DISTRICTCOUNTRYCODE,
       t.DISTRICTCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.TOWN t
FETCH FIRST 100 ROWS ONLY;
```
