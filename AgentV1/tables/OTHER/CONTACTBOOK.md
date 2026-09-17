# DB2ADMIN.CONTACTBOOK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 35
- **Primary key**: `UNIQUEID`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 47694

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `CODE` | CHAR(8) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `PERSON` | VARCHAR(200) | NOT NULL |  |  |  |
| 3 | `ROLEINTHECOMPANY` | VARCHAR(200) |  |  |  |  |
| 4 | `PHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 5 | `FAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 6 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 7 | `BOOKLINE01` | VARCHAR(200) |  |  |  |  |
| 8 | `BOOKLINE02` | VARCHAR(200) |  |  |  |  |
| 9 | `BOOKLINE03` | VARCHAR(200) |  |  |  |  |
| 10 | `BOOKLINE04` | VARCHAR(200) |  |  |  |  |
| 11 | `BOOKLINE05` | VARCHAR(200) |  |  |  |  |
| 12 | `DOCUMENTTYPEFORMAIL` | CHAR(90) |  |  |  |  |
| 13 | `ADDRESSTYPE` | INTEGER | NOT NULL |  |  |  |
| 14 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL | FK | foreign_key |  |
| 15 | `DELIVERYPOINTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 16 | `COUNTRYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 17 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 18 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 19 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 20 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 21 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 22 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 23 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 24 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 25 | `TRANSPORTZONECODE` | CHAR(3) |  | FK | foreign_key |  |
| 26 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 27 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 28 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 29 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 30 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 31 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 33 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 34 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADDRESS_DELIVERYPOINT` | `DELIVERYPOINTUNIQUEID`, `DELIVERYPOINTCODE` | [`ADDRESS`](../CORE_MASTER/ADDRESS.md) | `UNIQUEID`, `CODE` | RESTRICT | `CONTACTBOOK.DELIVERYPOINTUNIQUEID = ADDRESS.UNIQUEID AND CONTACTBOOK.DELIVERYPOINTCODE = ADDRESS.CODE` |
| `COUNTRY_COUNTRY` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `CONTACTBOOK.COUNTRYCODE = COUNTRY.CODE` |
| `TRANSPORTZONE_TRANSPORTZONE` | `COUNTRYCODE`, `TRANSPORTZONECODE` | [`TRANSPORTZONE`](../CORE_MASTER/TRANSPORTZONE.md) | `COUNTRYCODE`, `CODE` | RESTRICT | `CONTACTBOOK.COUNTRYCODE = TRANSPORTZONE.COUNTRYCODE AND CONTACTBOOK.TRANSPORTZONECODE = TRANSPORTZONE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CONTACTBOOKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.CODE,
       t.PERSON,
       t.ROLEINTHECOMPANY,
       t.PHONENUMBER,
       t.FAXNUMBER,
       t.EMAILADDRESS,
       t.BOOKLINE01,
       t.BOOKLINE02,
       t.BOOKLINE03,
       t.BOOKLINE04,
       t.BOOKLINE05
FROM   DB2ADMIN.CONTACTBOOK t
FETCH FIRST 100 ROWS ONLY;
```
