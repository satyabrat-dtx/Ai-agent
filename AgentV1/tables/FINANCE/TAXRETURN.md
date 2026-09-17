# DB2ADMIN.TAXRETURN

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `CODE`
- **FK degree**: referenced by 2 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103224

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `COUNTRYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ADDRESSLINE1` | VARCHAR(100) |  |  |  |  |
| 6 | `ADDRESSLINE2` | VARCHAR(100) |  |  |  |  |
| 7 | `ADDRESSLINE3` | VARCHAR(100) |  |  |  |  |
| 8 | `ADDRESSLINE4` | VARCHAR(100) |  |  |  |  |
| 9 | `ADDRESSLINE5` | VARCHAR(100) |  |  |  |  |
| 10 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 11 | `TOWN` | VARCHAR(100) |  |  |  |  |
| 12 | `DISTRICT` | VARCHAR(100) |  |  |  |  |
| 13 | `TRANSPORTZONECODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `ADDRESSPHONENUMBER` | VARCHAR(40) |  |  |  |  |
| 15 | `ADDRESSFAXNUMBER` | VARCHAR(40) |  |  |  |  |
| 16 | `RESPONSIBLE` | CHAR(50) |  |  |  |  |
| 17 | `TEXT` | CHAR(50) |  |  |  |  |
| 18 | `POSTING` | SMALLINT | NOT NULL |  |  |  |
| 19 | `LEADINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_LEADINGCOMPANY` | `LEADINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TAXRETURN.LEADINGCOMPANYCODE = COMPANY.CODE` |
| `COUNTRY_COUNTRY` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `TAXRETURN.COUNTRYCODE = COUNTRY.CODE` |
| `TRANSPORTZONE_TRANSPORTZONE` | `COUNTRYCODE`, `TRANSPORTZONECODE` | [`TRANSPORTZONE`](../CORE_MASTER/TRANSPORTZONE.md) | `COUNTRYCODE`, `CODE` | RESTRICT | `TAXRETURN.COUNTRYCODE = TRANSPORTZONE.COUNTRYCODE AND TAXRETURN.TRANSPORTZONECODE = TRANSPORTZONE.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TAXRETURN_TAXRETURN` | [`TAXDECLARATION`](../FINANCE/TAXDECLARATION.md) | `TAXRETURNCODE` | `TAXDECLARATION.TAXRETURNCODE = TAXRETURN.CODE` |
| `TAXRETURN_TAXRETURNCOMPANY` | [`TAXRETURNCOMPANY`](../FINANCE/TAXRETURNCOMPANY.md) | `TAXRETURNCODE` | `TAXRETURNCOMPANY.TAXRETURNCODE = TAXRETURN.CODE` |

## Indexes

- `TAXRETURNUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COUNTRYCODE,
       t.ADDRESSLINE1,
       t.ADDRESSLINE2,
       t.ADDRESSLINE3,
       t.ADDRESSLINE4,
       t.ADDRESSLINE5,
       t.POSTALCODE,
       t.TOWN
FROM   DB2ADMIN.TAXRETURN t
FETCH FIRST 100 ROWS ONLY;
```
