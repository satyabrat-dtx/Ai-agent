# DB2ADMIN.ABSEQB

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ABSUIXMLPATH`, `ABSUIXMLNAME`, `CODE`
- **FK degree**: referenced by 4 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 28961

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(30) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `DESCRIPTION` | CHAR(50) | NOT NULL |  | description |  |
| 4 | `DATA` | CLOB(1000000) |  |  |  |  |
| 5 | `CONTEXT` | INTEGER | NOT NULL |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSEQB_AUTHORIZATIONS` | [`ABSEQBAUTH`](../PLATFORM/ABSEQBAUTH.md) | `ABSEQBABSUIXMLPATH`, `ABSEQBABSUIXMLNAME`, `ABSEQBCODE` | `ABSEQBAUTH.ABSEQBABSUIXMLPATH = ABSEQB.ABSUIXMLPATH AND ABSEQBAUTH.ABSEQBABSUIXMLNAME = ABSEQB.ABSUIXMLNAME AND ABSEQBAUTH.ABSEQBCODE = ABSEQB.CODE` |
| `ABSEQB_EQB` | [`ABSUIPROCESS`](../PLATFORM/ABSUIPROCESS.md) | `UIXMLPATH`, `UIXMLNAME`, `EQBCODE` | `ABSUIPROCESS.UIXMLPATH = ABSEQB.ABSUIXMLPATH AND ABSUIPROCESS.UIXMLNAME = ABSEQB.ABSUIXMLNAME AND ABSUIPROCESS.EQBCODE = ABSEQB.CODE` |
| `ABSEQB_COLLECTIONDEFAULTEQB` | [`ABSUIXMLAUTH`](../PLATFORM/ABSUIXMLAUTH.md) | `ABSUIXMLPATH`, `ABSUIXMLNAME`, `COLLECTIONDEFAULTEQBCODE` | `ABSUIXMLAUTH.ABSUIXMLPATH = ABSEQB.ABSUIXMLPATH AND ABSUIXMLAUTH.ABSUIXMLNAME = ABSEQB.ABSUIXMLNAME AND ABSUIXMLAUTH.COLLECTIONDEFAULTEQBCODE = ABSEQB.CODE` |
| `ABSEQB_LOOKUPDEFAULTEQB` | [`ABSUIXMLAUTH`](../PLATFORM/ABSUIXMLAUTH.md) | `ABSUIXMLPATH`, `ABSUIXMLNAME`, `LOOKUPDEFAULTEQBCODE` | `ABSUIXMLAUTH.ABSUIXMLPATH = ABSEQB.ABSUIXMLPATH AND ABSUIXMLAUTH.ABSUIXMLNAME = ABSEQB.ABSUIXMLNAME AND ABSUIXMLAUTH.LOOKUPDEFAULTEQBCODE = ABSEQB.CODE` |

## Indexes

- `ABSEQBUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.CODE,
       t.DESCRIPTION,
       t.DATA,
       t.CONTEXT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.ABSEQB t
FETCH FIRST 100 ROWS ONLY;
```
