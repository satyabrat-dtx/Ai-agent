# DB2ADMIN.ABSUIXMLAUTH

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `ABSUIXMLPATH`, `ABSUIXMLNAME`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 69213

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `CREATEAUTH` | SMALLINT | NOT NULL |  |  |  |
| 5 | `READAUTH` | SMALLINT | NOT NULL |  |  |  |
| 6 | `UPDATEAUTH` | SMALLINT | NOT NULL |  |  |  |
| 7 | `DELETEAUTH` | SMALLINT | NOT NULL |  |  |  |
| 8 | `QUERYAUTH` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SUBMITAUTH` | SMALLINT | NOT NULL |  |  |  |
| 10 | `READASDEFAULT` | SMALLINT | NOT NULL |  |  |  |
| 11 | `CREATEEQBALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `COLLECTIONDEFAULTEQBCODE` | CHAR(30) |  | FK | foreign_key |  |
| 13 | `LOOKUPDEFAULTEQBCODE` | CHAR(30) |  | FK | foreign_key |  |
| 14 | `CREATEGBALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `DEFAULTGBCODE` | CHAR(30) |  | FK | foreign_key |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSEQB_COLLECTIONDEFAULTEQB` | `ABSUIXMLPATH`, `ABSUIXMLNAME`, `COLLECTIONDEFAULTEQBCODE` | [`ABSEQB`](../PLATFORM/ABSEQB.md) | `ABSUIXMLPATH`, `ABSUIXMLNAME`, `CODE` | RESTRICT | `ABSUIXMLAUTH.ABSUIXMLPATH = ABSEQB.ABSUIXMLPATH AND ABSUIXMLAUTH.ABSUIXMLNAME = ABSEQB.ABSUIXMLNAME AND ABSUIXMLAUTH.COLLECTIONDEFAULTEQBCODE = ABSEQB.CODE` |
| `ABSEQB_LOOKUPDEFAULTEQB` | `ABSUIXMLPATH`, `ABSUIXMLNAME`, `LOOKUPDEFAULTEQBCODE` | [`ABSEQB`](../PLATFORM/ABSEQB.md) | `ABSUIXMLPATH`, `ABSUIXMLNAME`, `CODE` | RESTRICT | `ABSUIXMLAUTH.ABSUIXMLPATH = ABSEQB.ABSUIXMLPATH AND ABSUIXMLAUTH.ABSUIXMLNAME = ABSEQB.ABSUIXMLNAME AND ABSUIXMLAUTH.LOOKUPDEFAULTEQBCODE = ABSEQB.CODE` |
| `ABSGB_DEFAULTGB` | `ABSUIXMLPATH`, `ABSUIXMLNAME`, `DEFAULTGBCODE` | [`ABSGB`](../PLATFORM/ABSGB.md) | `ABSUIXMLPATH`, `ABSUIXMLNAME`, `CODE` | RESTRICT | `ABSUIXMLAUTH.ABSUIXMLPATH = ABSGB.ABSUIXMLPATH AND ABSUIXMLAUTH.ABSUIXMLNAME = ABSGB.ABSUIXMLNAME AND ABSUIXMLAUTH.DEFAULTGBCODE = ABSGB.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- UNIQUE `ABSUIXMLAUTH01` (ABSUIXMLNAME, ABSUIXMLPATH, USERUSERID, COMPANYCODE)
- UNIQUE `ABSUIXMLAUTH02` (ABSUIXMLNAME, ABSUIXMLPATH, COMPANYCODE, USERUSERID)
- `ABSUIXMLAUTHUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.USERUSERID,
       t.COMPANYCODE,
       t.CREATEAUTH,
       t.READAUTH,
       t.UPDATEAUTH,
       t.DELETEAUTH,
       t.QUERYAUTH,
       t.SUBMITAUTH,
       t.READASDEFAULT,
       t.CREATEEQBALLOWED
FROM   DB2ADMIN.ABSUIXMLAUTH t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
