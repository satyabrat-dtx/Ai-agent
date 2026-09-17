# DB2ADMIN.ISOCOUNTRY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `CODE`
- **FK degree**: referenced by 3 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 102590

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(2) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(100) |  |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `ISO3A` | CHAR(3) |  |  |  |  |
| 5 | `ISO3N` | DECIMAL(3,0) |  |  |  |  |
| 6 | `EUMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 7 | `EUROMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 8 | `IBANMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SEPAMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 10 | `IBANCHECKRULE` | CHAR(1) |  |  |  |  |
| 11 | `BICCHECKRULE` | CHAR(1) |  |  |  |  |
| 12 | `CLEARINGCHECKRULE` | CHAR(1) |  |  |  |  |
| 13 | `VALIDATEIBAN` | SMALLINT | NOT NULL |  |  |  |
| 14 | `VALIDATEBIC` | SMALLINT | NOT NULL |  |  |  |
| 15 | `VALIDATEBANKMASTER` | SMALLINT | NOT NULL |  |  |  |
| 16 | `IBANCOUNTRYMATCH` | SMALLINT | NOT NULL |  |  |  |
| 17 | `BICCOUNTRYMATCH` | SMALLINT | NOT NULL |  |  |  |
| 18 | `IBANISOOVERRIDECODE` | CHAR(2) |  | FK | foreign_key |  |
| 19 | `BICISOOVERRIDECODE` | CHAR(2) |  | FK | foreign_key |  |
| 20 | `ACCOUNTVALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 21 | `CLEARINGVALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 22 | `BICVALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 23 | `BANKDETAILVALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 24 | `LENGTHOFCLEARING` | INTEGER | NOT NULL |  |  |  |
| 25 | `LENGTHOFACCOUNT` | INTEGER | NOT NULL |  |  |  |
| 26 | `STARTOFACCOUNT` | INTEGER | NOT NULL |  |  |  |
| 27 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 28 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 29 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 30 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ISOCOUNTRY_BICISOOVERRIDE` | `BICISOOVERRIDECODE` | [`ISOCOUNTRY`](../OTHER/ISOCOUNTRY.md) | `CODE` | RESTRICT | `ISOCOUNTRY.BICISOOVERRIDECODE = ISOCOUNTRY.CODE` |
| `ISOCOUNTRY_IBANISOOVERRIDE` | `IBANISOOVERRIDECODE` | [`ISOCOUNTRY`](../OTHER/ISOCOUNTRY.md) | `CODE` | RESTRICT | `ISOCOUNTRY.IBANISOOVERRIDECODE = ISOCOUNTRY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ISOCOUNTRY_BICISOOVERRIDE` | [`ISOCOUNTRY`](../OTHER/ISOCOUNTRY.md) | `BICISOOVERRIDECODE` | `ISOCOUNTRY.BICISOOVERRIDECODE = ISOCOUNTRY.CODE` |
| `ISOCOUNTRY_IBANISOOVERRIDE` | [`ISOCOUNTRY`](../OTHER/ISOCOUNTRY.md) | `IBANISOOVERRIDECODE` | `ISOCOUNTRY.IBANISOOVERRIDECODE = ISOCOUNTRY.CODE` |
| `ISOCOUNTRY_COUNTRYISO` | [`BANKMASTER`](../OTHER/BANKMASTER.md) | `COUNTRYISOCODE` | `BANKMASTER.COUNTRYISOCODE = ISOCOUNTRY.CODE` |

## Indexes

- `ISOCOUNTRYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ISO3A,
       t.ISO3N,
       t.EUMEMBER,
       t.EUROMEMBER,
       t.IBANMEMBER,
       t.SEPAMEMBER,
       t.IBANCHECKRULE,
       t.BICCHECKRULE
FROM   DB2ADMIN.ISOCOUNTRY t
FETCH FIRST 100 ROWS ONLY;
```
